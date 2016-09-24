#!/bin/bash -ex

BASEDIR=$(dirname "$0")
KEY=`cat $BASEDIR/api.key`
COORD=47.55,19.0434 # Budapest
#COORD=53.5259,-7.3381 # Ireland, raining now

curl -s -G \
	-o ${BASEDIR}/data.json \
	-d units=si \
	-d exclude=minutely,hourly,daily,flags \
	https://api.darksky.net/forecast/${KEY}/${COORD}


