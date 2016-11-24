from oled.device import ssd1306
from oled.render import canvas
from PIL import Image, ImageFont, ImageDraw, ImageOps
import time
import datetime
import subprocess
import json
import os

device = ssd1306(port=1, address=0x3c)
ttf = '/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf'
bigFont   = ImageFont.truetype(ttf, 64)
smallFont = ImageFont.truetype(ttf, 42)
littleFont = ImageFont.truetype(ttf, 20)
tinyFont = ImageFont.truetype(ttf, 12)
delay = 1.5

def main():
    print("Weather station started")

    while True:
        basedir = os.path.dirname(os.path.realpath(__file__))
        updateFile = os.path.join(basedir, 'update_tick')
        try:
            if os.path.isfile(updateFile):
                print "Update file found, calling weather-update"
                with canvas(device) as drawUpdate:
                    drawUpdate.text((0,0), "Updating...", font=littleFont, fill=255)
                subprocess.call([os.path.join(basedir, 'wunderground-update.sh')])
                print "Deleting update file"
                os.unlink(updateFile)

            with open(os.path.join(basedir, 'wunderground-conditions-data.json')) as conditions_data_file:
                conditions_data = json.load(conditions_data_file)

            with open(os.path.join(basedir, 'wunderground-forecast-data.json')) as forecast_data_file:
                forecast_data = json.load(forecast_data_file)

            temp_num = float(conditions_data[u'current_observation'][u'temp_c'])
            temp_cur = "%2.0f" % temp_num
            feelslike_num = float(conditions_data[u'current_observation'][u'feelslike_c'])
            feelslike_str = "= %2.0f" % feelslike_num
            icon = str(conditions_data[u'current_observation'][u'icon'])
            humidity = conditions_data[u'current_observation'][u'relative_humidity']
            wind = str(conditions_data[u'current_observation'][u'wind_kph'])
            icon_today = str(forecast_data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'icon'])
            high_today = str(forecast_data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'high'][u'celsius'])
            low_today = str(forecast_data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'low'][u'celsius'])
            epoch = int(conditions_data[u'current_observation'][u'local_epoch'])
            utime = time.strftime('%H:%M', time.localtime(epoch))

            logo = Image.open("icons/" + icon + ".bmp")
            logoToday = Image.open("icons/" + icon_today + ".bmp")

            print(temp_cur)
            print(feelslike_str)
            print(icon)
            print(icon_today)
            print(high_today)

            with canvas(device) as drawTemp:
                drawTemp.text((20,0), temp_cur + u"\u00B0", font=bigFont, fill=255)
                drawTemp.text((0,0), "" + utime, font=tinyFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawFeelslike:
                drawFeelslike.text((10,8), feelslike_str + u"\u00B0", font=smallFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawHumidity:
                drawHumidity.text((20,8), humidity, font=smallFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawHigh:
                drawHigh.text((10,8), u"\u2191  " + high_today + u"\u00B0", font=smallFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawLow:
                drawLow.text((10,8), u"\u2193  " + low_today + u"\u00B0", font=smallFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawWind:
                drawWind.text((30,0), wind, font=smallFont, fill=255)
                drawWind.text((60,40), u" km/h", font=littleFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawLogo:
                drawLogo.bitmap((32,0), logo, fill=1)
                drawLogo.text((0,0), "Now:", font=tinyFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawForecastLogo:
                drawForecastLogo.bitmap((32,0), logoToday, fill=1)
                drawForecastLogo.text((0,0), "Today:", font=tinyFont, fill=255)
            time.sleep(delay)
            with canvas(device) as drawTime:
                now = datetime.datetime.now()
                drawTime.text((10,8), "%02d" % now.hour + ":" + "%02d" % now.minute, font=smallFont, fill=255)
            time.sleep(delay)
        except:
            with canvas(device) as drawError:
                drawError.text((0,0), "Error!", font=littleFont, fill=255)
                drawError.text((0,40), time.strftime('%H:%M', time.localtime(epoch)), font=littleFont, fill=255)
            time.sleep(60)

if __name__ == "__main__":
    main()
