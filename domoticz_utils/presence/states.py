# -*- coding: utf-8 -*-
import logging
import datetime
import time

class StateMachine(object):
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.run()


class PresenceStateMachine(StateMachine):
    def __init__(self, config):
        super(PresenceStateMachine, self).__init__(StateUnknown(config))

    def run(self, device_found):
        self.current_state = self.current_state.next(device_found)
        self.current_state.run()


class State(object):
    def __init__(self, config):
        self._config = config

    def run(self):
        raise NotImplementedError

    def next(self, input):
        raise NotImplementedError


class StateUnknown(State):
    def __init__(self, config):
        super(StateUnknown, self).__init__(config)

    def run(self):
        logging.debug("State Unknown")

    def next(self, device_found):
        return StatePresent(self._config) if device_found else StateInLimbo(self._config)


class StatePresent(State):
    def __init__(self, config):
        super(StatePresent, self).__init__(config)

    def run(self):
        logging.debug("State Present")

    def next(self, device_found):
        return self if device_found else StateInLimbo(self._config)


class StateInLimbo(State):
    def __init__(self, config):
        super(StateInLimbo, self).__init__(config)
        self._start = datetime.datetime.now()

    def run(self):
        logging.debug("State In Limbo")

    def next(self, device_found):
        if device_found:
            return StatePresent(self._config)

        duration = (datetime.datetime.now() - self._start).seconds
        return StateMissing(self._config) if duration >= self._config['missing_threshold'] else self


class StateMissing(State):
    def __init__(self, config):
        super(StateMissing, self).__init__(config)

    def run(self):
        logging.debug("State Missing")

    def next(self, device_found):
        return StatePresent(self._config) if device_found else self


logging.basicConfig(level=logging.DEBUG)
presence_sm = PresenceStateMachine({'missing_threshold': 10})
presence_sm.run(True)
presence_sm.run(True)
presence_sm.run(False)
presence_sm.run(False)
time.sleep(10)
presence_sm.run(False)
presence_sm.run(True)
presence_sm.run(False)
