#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script is executed when the Domoticz IA is armed.
# It sets the AlertMe IA accordingly and flashes lights.
#
import os

import domoticz_utils.alertme as am
import logging

from domoticz_utils import set_up_logging, load_credentials
from domoticz_utils.json_api_client import JsonApiClient
from domoticz_utils.alertme.webapi import WebAPIClient


def main(credentials):
    # Read the parameters from the config file
    dz_host = credentials.get("domoticz").get("host")
    am_host = credentials.get("alertme").get("v2_api")
    am_user = credentials.get("alertme").get("user")
    am_pass = credentials.get("alertme").get("pass")
    am_skip_grace_period = False

    dz_client = JsonApiClient(dz_host)
    am_client = WebAPIClient(am_host)
    am_client.login(am_user, am_pass, "Domoticz Utils Ruggero")

    dz_ia_state = dz_client.get_ia_status()
    new_am_ia_state = am.map_dz_ia_state_to_am(dz_ia_state)
    logging.info("Current Domoticz IA state is {state:s}".format(state=new_am_ia_state))
    am_ia_state = am_client.get_current_service_state(am.SERVICE_INTRUDER_ALARM)
    logging.info("Current AlertMe IA state is {state:s}".format(state=am_ia_state))
    if new_am_ia_state != am_ia_state:
        am_command = am.map_dz_ia_state_to_am_command(dz_ia_state)
        if am_command is None:
            logging.error("No AlertMe command for Domoticz IA state {state:s}".format(state=dz_ia_state))
        else:
            logging.info("Setting AlertMe IA state to {state:s}".format(state=new_am_ia_state))
            am_client.set_intruder_alarm(am_command, am_skip_grace_period)
            # TODO: Flash lights
    else:
        logging.info("AlertMe IA state is already in sync")


if "__main__" == __name__:
    set_up_logging(logging.INFO)
    credentials = load_credentials(os.path.dirname(os.path.realpath(__file__)))
    main(credentials)
