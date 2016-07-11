# -*- coding: utf-8 -*-
import importlib
import logging
import sys
import signal

from domoticz_utils.presence.detector import PresenceDetector, PresenceDetectorConfig

workers = list()


def signal_handler(signal, frame):
    for worker in workers:
        worker.join()
        worker.stop()

    sys.exit(0)


def populate_finders_registry(finders):
    module = importlib.import_module('domoticz_utils.presence.finders')
    finders_registry = dict()
    for label, settings in finders.items():
        class_name = settings.get('class')
        class_ = getattr(module, class_name)
        del settings['class']
        finders_registry[label] = class_(**settings)

    return finders_registry


def main(config_file):
    config = PresenceDetectorConfig(config_file)
    finders_registry = populate_finders_registry(config.get_finders())
    detectors = list()
    for device_id, device_config in config.get_devices().items():
        detector = PresenceDetector(finders_registry.get(device_config.get_finder()), device_id, device_config)
        detectors.append(detector)
        detector.start()

if __name__ == '__main__':
    for i in [x for x in dir(signal) if x.startswith("SIG")]:
        try:
            signum = getattr(signal, i)
            if signum > 0:
                signal.signal(signum, signal_handler)
        except RuntimeError:
            print "Skipping %s" % i
        except ValueError as error:
            logging.error(error)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    main(sys.argv[1])
