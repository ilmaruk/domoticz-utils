# -*- coding: utf-8 -*-
import domoticz_utils as dzu

SERVICE_INTRUDER_ALARM = "IntruderAlarm"

IA_STATE_HOME = "disarmed"
IA_STATE_AWAY = "away"
IA_STATE_NIGHT = "night"

IA_STATE_HOME_COMMAND = "disarm"
IA_STATE_AWAY_COMMAND = "arm"
IA_STATE_NIGHT_COMMAND = "nightArm"

DZ_TO_AM_IA_STATES_MAPPING = {
    dzu.IA_STATUS_DISARMED: {
        "state": IA_STATE_HOME,
        "command": IA_STATE_HOME_COMMAND
    },
    dzu.IA_STATUS_ARMED_AWAY: {
        "state": IA_STATE_AWAY,
        "command": IA_STATE_AWAY_COMMAND
    },
    dzu.IA_STATUS_ARMED_HOME: {
        "state": IA_STATE_NIGHT,
        "command": IA_STATE_NIGHT_COMMAND
    },
}


def map_dz_ia_state_to_am(dz_ia_state):
    return DZ_TO_AM_IA_STATES_MAPPING.get(dz_ia_state, {}).get("state", None)


def map_dz_ia_state_to_am_command(dz_ia_state):
    return DZ_TO_AM_IA_STATES_MAPPING.get(dz_ia_state, {}).get("command", None)
