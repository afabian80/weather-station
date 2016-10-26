#!/bin/bash -ex
date
/usr/bin/python /home/pi/Documents/Python/nokia5110/wunderground-weather.py
echo "weather station updated" > /tmp/weather-health.log

