#!/bin/bash -ex

BASEDIR=$(dirname "$0")
KEY=c26a1b3b3045e18845d765446a523e73
COORD=47.55,19.0434 # Budapest
#COORD=51.5074,0.1278 # London
#COORD=53.5259,-7.3381 # Ireland, raining now

curl -s -G -o ${BASEDIR}/data.json -d units=si -d exclude=minutely,hourly,daily,flags https://api.darksky.net/forecast/${KEY}/${COORD}


