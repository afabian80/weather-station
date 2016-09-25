#!/bin/bash -ex

BASEDIR=$(dirname "$0")
KEY=`cat $BASEDIR/wunderground-api.key`
COORD=zmw:00000.6.12838 # Budapest

curl -s -G \
	-o ${BASEDIR}/wunderground-conditions-data.json \
	http://api.wunderground.com/api/${KEY}/conditions/q/${COORD}.json

sleep 1

curl -s -G \
	-o ${BASEDIR}/wunderground-forecast-data.json \
	http://api.wunderground.com/api/${KEY}/forecast/q/${COORD}.json
