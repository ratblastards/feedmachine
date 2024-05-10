#!/usr/bin/env bash
set -e
cd /home/pi/Scripts/feedmachine
source "/home/pi/Scripts/feedmachine/bin/activate"
source "/etc/environment"
export FEEDMACHINE_TOKEN=${FEEDMACHINE_TOKEN}
export FEEDMACHINE_USERID=${FEEDMACHINE_USERID}
python3 feedmachine.py
