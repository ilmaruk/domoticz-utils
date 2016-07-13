# -*- coding: utf-8 -*-

from domoticz_utils.alertme.webapi import WebAPIClient
from domoticz_utils.json_api_client import JsonApiClient, IA_STATUS_DISARMED, IA_STATUS_ARMED_AWAY, IA_STATUS_ARMED_HOME

STATES_MAP = {
    "Home": IA_STATUS_DISARMED,
    "Away": IA_STATUS_ARMED_AWAY,
    "Night": IA_STATUS_ARMED_HOME,
}


def main():
    alertme_web_api_client = WebAPIClient()
    domoticz_client = JsonApiClient("http://192.168.0.91:8080")

    alertme_web_api_client.login("thechaseely", "Z0Eusti08", "domoticz-utils")
    ia_state = alertme_web_api_client.get_behaviour()
    print ia_state
    ia_state = domoticz_client.set_ia_status(STATES_MAP[ia_state])
    print ia_state


if "__main__" == __name__:
    main()
