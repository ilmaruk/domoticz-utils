# -*- coding: utf-8 -*-
import subprocess

from domoticz_utils.presence import DEVICE_FOUND, DEVICE_NOT_FOUND


class IpFinder(object):
    def find(self, device_ip):
        command = 'ping -q -c1 -W 1 {device_ip:s} > /dev/null'.format(device_ip=device_ip)
        return DEVICE_FOUND if subprocess.call(command, shell=True) == 0 else DEVICE_NOT_FOUND
