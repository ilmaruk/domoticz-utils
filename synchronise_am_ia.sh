#!/usr/bin/env bash
pushd $(dirname $0) > /dev/null
. ~/.venv/domoticz-utils/bin/activate
python synchronise_am_ia.py
deactivate
popd > /dev/null
