# -*- coding: utf-8 -*-

DEVICE_FOUND = 0
DEVICE_NOT_FOUND = 1

DEVICE_STATUS_MAP = {
    DEVICE_FOUND: 'Found',
    DEVICE_NOT_FOUND: 'Not found',
}

DEVICE_PRESENCE_UNKNOWN = -1
DEVICE_PRESENCE_PRESENT = 0
DEVICE_PRESENCE_IN_LIMBO = 1
DEVICE_PRESENCE_MISSING = 2

DEVICE_PRESENCE_STATUS_MAP = {
    DEVICE_PRESENCE_UNKNOWN: 'Unknown',
    DEVICE_PRESENCE_PRESENT: 'Present',
    DEVICE_PRESENCE_IN_LIMBO: 'In Limbo',
    DEVICE_PRESENCE_MISSING: 'Missing'
}


def device_status_as_string(status):
    return DEVICE_STATUS_MAP.get(status)


def device_presence_status_as_string(status):
    return DEVICE_PRESENCE_STATUS_MAP.get(status)
