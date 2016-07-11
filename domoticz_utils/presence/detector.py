# -*- coding: utf-8 -*-
import os
import threading
import time

import re

import datetime
import yaml
import logging

from domoticz_utils.presence import device_status_as_string, DEVICE_PRESENCE_UNKNOWN, DEVICE_FOUND, \
    DEVICE_PRESENCE_PRESENT, DEVICE_PRESENCE_IN_LIMBO, DEVICE_PRESENCE_MISSING, device_presence_status_as_string


class InvalidConfigFileError(Exception):
    pass


class DeviceConfig(object):
    def __init__(self, parameters):
        self._parameters = parameters

    def __getattr__(self, name):
        pattern = re.compile(r'^get_(\s+)')
        match = pattern.match(name)
        if match is not None:
            return self._parameters.get(match.group(1), None)
        raise NotImplementedError(name)

    def get_finder(self):
        return self._parameters.get('finder')

    def get_polling_interval(self, default=30.0):
        return float(self._parameters.get('polling_interval', default))

    def get_missing_threshold(self, default=300.0):
        return float(self._parameters.get('missing_threshold', default))


class PresenceDetectorConfig(object):
    def __init__(self, config_file):
        self._config = {}
        _, type = os.path.splitext(config_file)
        if type.lower() == '.yaml':
            self._config = self.read_from_yaml(config_file)
        elif type.lower() == '.json':
            self._config = self.read_from_json(config_file)
        else:
            raise InvalidConfigFileError('Config files of type "{type:s}" are not supported'.
                                         format(type=type.lstrip('.')))

    def read_from_yaml(self, config_file):
        try:
            with open(config_file) as stream:
                return yaml.load(stream)
        except IOError as error:
            raise InvalidConfigFileError(error.message)

    def read_from_json(self, config_file):
        raise InvalidConfigFileError('"json" config file type is not yet supported')

    def get_finders(self):
        return self._config.get('finders', {})

    def get_devices(self):
        return {key: DeviceConfig(value) for (key, value) in self._config.get('devices', {}).items()}


class PresenceDetector(threading.Thread):
    def __init__(self, finder, device_id, config, group=None, target=None, name=None, args=(), kwargs=None,
                 verbose=None):
        super(PresenceDetector, self).__init__(group, target, name, args, kwargs, verbose)
        self._finder = finder
        self._device_id = device_id
        self._config = config
        self._presence_status = DEVICE_PRESENCE_UNKNOWN
        self._last_presence = datetime.datetime.now()
        self._stop_me = threading.Event()

    def stop(self):
        self._stop_me.set()

    def run(self):
        while True:
            if self._stop_me.is_set():
                return

            status = self._finder.find(self._device_id)
            logging.info('Device {device_id:s} status: {status:s}'.format(device_id=self._device_id,
                                                                          status=device_status_as_string(status)))

            if status == DEVICE_FOUND:
                self._last_presence = datetime.datetime.now()
                if self._presence_status != DEVICE_PRESENCE_PRESENT:
                    self._presence_status = DEVICE_PRESENCE_PRESENT
                    # Tell Domoticz

            elif self._presence_status == DEVICE_PRESENCE_PRESENT:
                self._presence_status = DEVICE_PRESENCE_IN_LIMBO

            elif self._presence_status == DEVICE_PRESENCE_IN_LIMBO:
                missing_seconds = (datetime.datetime.now() - self._last_presence).seconds
                if missing_seconds >= self._config.get_missing_threshold():
                    self._presence_status = DEVICE_PRESENCE_MISSING
                    # Tell Domoticz

            logging.info('Device {device_id:s} presence status: {status:s}'.
                         format(device_id=self._device_id,
                                status=device_presence_status_as_string(self._presence_status)))

            time.sleep(self._config.get_polling_interval())
