import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

import Image
import ImageDraw
import ImageFont
import subprocess
import json
import os

bigfontsize = 22

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

basedir = os.path.dirname(os.path.realpath(__file__))
subprocess.call([os.path.join(basedir, 'wunderground-update.sh')])

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

disp.begin(contrast=40)

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

big_font   = ImageFont.truetype(os.path.join('/usr/share/fonts/truetype/freefont/', 'FreeSansBold.ttf'), bigfontsize)
small_font = ImageFont.load_default()

with open(os.path.join(basedir, 'wunderground-conditions-data.json')) as conditions_data_file:
    conditions_data = json.load(conditions_data_file)

with open(os.path.join(basedir, 'wunderground-forecast-data.json')) as forecast_data_file:
    forecast_data = json.load(forecast_data_file)

temp_num = float(conditions_data[u'current_observation'][u'temp_c'])
temp_cur = "%2.0f" % temp_num
feelslike_num = float(conditions_data[u'current_observation'][u'feelslike_c'])
feelslike_str = "/ %2.0f" % feelslike_num
condition_now = str(conditions_data[u'current_observation'][u'weather']) 
condition_today = str(forecast_data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'conditions']) 
epoch = int(conditions_data[u'current_observation'][u'observation_epoch'])
utime = time.strftime('%H:%M', time.localtime(epoch))

print(temp_cur)
print(feelslike_str)
print(condition_now)
print(condition_today)

draw.text((0,0), temp_cur, font=big_font)
draw.text((36,0), feelslike_str, font=big_font)
draw.text((0,20), condition_now, font=small_font)
draw.text((0,30), condition_today, font=small_font)
draw.text((45,39), utime, font=small_font)

disp.image(image)
disp.display()

print("Done.")

