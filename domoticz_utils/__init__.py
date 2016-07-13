# -*- coding: utf-8 -*-
import logging
import os

import yaml

IA_STATUS_DISARMED = 0
IA_STATUS_ARMED_HOME = 1
IA_STATUS_ARMED_AWAY = 2


def set_up_logging(level):
    logging.basicConfig(level=level, format="[%(asctime)s|%(levelname)s] %(message)s")
    logging.getLogger("requests").setLevel(logging.ERROR)


def load_credentials(path, source="etc/credentials.yaml"):
    with open(os.path.join(path, source)) as stream:
        credentials = yaml.load(stream)
    return credentials
