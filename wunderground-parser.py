import json
from pprint import pprint

with open('wunderground-conditions-data.json') as conditions_data_file:    
    conditions_data = json.load(conditions_data_file)

with open('wunderground-forecast-data.json') as forecast_data_file:    
    forecast_data = json.load(forecast_data_file)

print("temp:  " +   str(conditions_data[u'current_observation'][u'temp_c']))
print("feels: " +   str(conditions_data[u'current_observation'][u'feelslike_c']))
print("weather: " + str(conditions_data[u'current_observation'][u'weather']))
#print("epoch: " +   str(conditions_data[u'current_observation'][u'observation_epoch']))

#print("today: " +   str(forecast_data[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'title']))
print("today: " +   str(forecast_data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'conditions']))

