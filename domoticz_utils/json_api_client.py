# -*- coding: utf-8 -*-
import hashlib
import requests

ENDPOINT = 'json.htm'

TYPE_DEVICES = 'devices'

DEVICE_STATUS_ON = 'On'
DEVICE_STATUS_OFF = 'Off'


class JsonApiError(Exception):
    pass


class JsonApiClient(object):
    def __init__(self, host):
        self._host = host
        self._endpoint_url = '/'.join([host.rstrip('/'), ENDPOINT])

    def _send_request(self, **kwargs):
        try:
            params = {key: value for key, value in kwargs.items() if value is not None}
            response = requests.get(self._endpoint_url, params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as error:
            raise JsonApiError(error.message)

    def get_device_info(self, device_idx):
        return self._send_request(type=TYPE_DEVICES, rid=device_idx)

    def get_device_status(self, device_idx):
        results = self.get_device_info(device_idx).get('result', [])
        return None if len(results) == 0 else results[0]['Status']

    def get_ia_status(self):
        return self._send_request(type="command", param="getsecstatus")['secstatus']

    def set_ia_status(self, status, sec_code):
        return self._send_request(type="command", param="setsecstatus", secstatus=status,
                                  seccode=hashlib.md5(sec_code).hexdigest())
