#!/usr/bin/env bash
PI_HOME="/home/pi"
pushd $(dirname $0) > /dev/null
. "${PI_HOME}/.venv/domoticz-utils/bin/activate"
python synchronise_am_ia.py
deactivate
popd > /dev/null
