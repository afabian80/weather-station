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

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

disp.begin(contrast=40)

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

big_font   = ImageFont.truetype(os.path.join('/usr/share/fonts/truetype/freefont/', 'FreeSansBold.ttf'), bigfontsize)
small_font = ImageFont.load_default()

subprocess.call([os.path.join(basedir, 'update.sh')])

with open(os.path.join(basedir, 'data.json')) as data_file:
    data = json.load(data_file)

temp_num = float(data[u'currently'][u'temperature'])
temp_cur = "%2.0f" % temp_num
apparent_temp_num = float(data[u'currently'][u'apparentTemperature'])
apparent_temp_str = "/ %2.0f" % apparent_temp_num
summary = str(data[u'currently'][u'summary'])
#humidity_num = float(data[u'currently'][u'humidity']) * 100
#humidity = "%2.0f %%" % humidity_num
precip_prob_num = float(data[u'currently'][u'precipProbability']) * 100.0
precip_prob = "%3.0f %% csapad." % precip_prob_num
cloud_num = float(data[u'currently'][u'cloudCover']) * 100.0
cloud = "%3.0f %% felho" % cloud_num
epoch = int(data[u'currently'][u'time'])
utime = time.strftime('%H:%M', time.localtime(epoch))

print(temp_cur)
print(cloud)
print(precip_prob)

draw.text((0,0), temp_cur, font=big_font)
draw.text((36,0), apparent_temp_str, font=big_font)
#draw.text((0,20), humidity, font=big_font)
#draw.text((0,20), summary, font=big_font)
draw.text((0,20), cloud, font=small_font)
draw.text((0,30), precip_prob, font=small_font)
draw.text((15,39), 'ekkor ' + utime, font=small_font)

disp.image(image)
disp.display()

