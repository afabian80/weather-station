import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

import Image
import ImageDraw
import ImageFont
import subprocess
import json
from pprint import pprint
import os

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

basedir = os.path.dirname(os.path.realpath(__file__))

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

disp.begin(contrast=40)

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

big_font   = ImageFont.truetype(os.path.join('/usr/share/fonts/truetype/freefont/', 'FreeSansBold.ttf'), 14)
small_font = ImageFont.load_default()

#subprocess.call([os.path.join(basedir, 'update.sh')])

with open(os.path.join(basedir, 'data.json')) as data_file:
    data = json.load(data_file)

temp_num = float(data[u'currently'][u'temperature'])
temp_cur = "%3.1f C" % temp_num
summary = str(data[u'currently'][u'summary'])
#humidity_num = float(data[u'currently'][u'humidity']) * 100
#humidity = "%2.0f %%" % humidity_num
precip_prob_num = int(data[u'currently'][u'precipProbability'])
precip_prob = "%d %% rain" % precip_prob_num
cloud_num = int(data[u'currently'][u'cloudCover'])
cloud = "%d %% cloud" % cloud_num
epoch = int(data[u'currently'][u'time'])
utime = time.strftime('%H:%M', time.localtime(epoch))

draw.text((0,0), temp_cur, font=big_font)
#draw.text((0,20), humidity, font=big_font)
#draw.text((0,20), summary, font=big_font)
draw.text((0,13), cloud, font=big_font)
draw.text((0,26), precip_prob, font=big_font)
draw.text((0,39), '      at ' + utime, font=small_font)

disp.image(image)
disp.display()

