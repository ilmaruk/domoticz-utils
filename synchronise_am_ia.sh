#!/usr/bin/env bash
pushd $(dirname $0) > /dev/null
#SCRIPTPATH=$(pwd)
. ~/.venv/domoticz-utils/bin/activate
synchronise_am_ia.py
popd > /dev/null
