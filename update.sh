#!/bin/bash -e

BASEDIR=$(dirname "$0")
COORD=47.55,19.0434

curl -s -G -o ${BASEDIR}/data.json -d units=si -d exclude=minutely,hourly,daily,flags https://api.darksky.net/forecast/a4aa7a5cdb1f7fd0b6251179bd9ca7f5/${COORD}


