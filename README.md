# weather-station
Display online weather info on an SSD1306 OLED display. 
Based on https://ssd1306.readthedocs.io/en/latest/intro.html.
Small usage example in https://ssd1306.readthedocs.io/en/latest/_modules/oled/device.html

# Harware configuration:
Used OLED display: http://www.banggood.com/0_96-Inch-4Pin-White-IIC-I2C-OLED-Display-Module-12864-LED-For-Arduino-p-958196.html
Wiring: Connect Ground and 3.3V to the display from the Raspberry PI. The connect SCL to SCL pin on the PI and SDA to the SDA pin on the PI.

# Start 
```
python wunderground-weather.py
```

# Autostart
Add these lines to /etc/cron.d/weather
```
*/10 * * * * pi /home/pi/weather-station/init-update.sh
@reboot pi /home/pi/weather-station/wrapper.sh
``` 
