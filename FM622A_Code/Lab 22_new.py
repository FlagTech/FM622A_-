import network, urequests, utime, sys
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
iss_url = "http://api.open-notify.org/iss-now.json"
key = '你的金鑰'
geo_url = 'http://api.geodatasource.com/v2/city'

print("連接 WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)
while not wifi.isconnected():
    pass
print("已連上")

response = urequests.get(iss_url)

if response.status_code != 200:
    oled.text("Location fail", 0, 0)
    oled.show()
    print('國際太空站現在位置查詢失敗')
    sys.exit(0)

parsed = response.json()
response.close()
print("國際太空站現在位置:")
longitude = parsed['iss_position']['longitude']
latitude = parsed['iss_position']['latitude']
print('經度：' + longitude)
print('緯度：' + latitude)
oled.text("Lat: " + latitude, 0, 0)
oled.text("Lng: " + longitude, 0, 16)
oled.show()

response = urequests.get(geo_url +
                         '?lat=' + latitude +
                         '&lng=' + longitude +
                         '&key=' + key)
if response.status_code != 200:
    oled.text("City fail", 0, 32)
    oled.show()
    print('最靠近城市查詢失敗')
    sys.exit(0)

parsed = response.json()
response.close()
print('最靠近城市：')
country = parsed['country']
city = parsed['city']
print('國家：' + country)
print('城市：' + city)
oled.text(city, 0, 32)
oled.text(country, 0, 48)
oled.show()
