#!/bin/bash -ex

date

/usr/bin/python /home/pi/Documents/Python/nokia5110/weather.py

logger "weather.py executed"

