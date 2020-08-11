import network, urequests, utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
url = "http://api.open-notify.org/iss-pass.json?lat=25.066667&lon=121.516667"

print("連接 WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)
while not wifi.isconnected():
    pass
print("已連上")

response = urequests.get(url)

if response.status_code == 200:

    parsed = response.json()
    print("JSON 資料查詢成功:")
    print("")
    
    print("國際太空站下次掠過時間:")
    
    data = parsed["response"][0]
    
    pass_time = int(data["risetime"]) - 946684800 + 28800
    pass_localtime = utime.localtime(pass_time)
    year = str(pass_localtime[0])
    month = str(pass_localtime[1])
    day = str(pass_localtime[2])
    hour = str(pass_localtime[3])
    minute = str(pass_localtime[4])
    second = str(pass_localtime[5])
    duration = str(data["duration"])
    
    date = str(year) + "/" + str(month) + "/" + str(day)
    time = str(hour) + ":" + str(minute) + ":" + str(second)
    
    print(date + " " + time + " (為時 " + duration + " 秒)")
    
    oled.fill(0)
    oled.text("ISS next flyby", 0, 0)
    oled.text("Date: " + str(year) + "/" + str(month) + "/" + str(day), 0, 24)
    oled.text("Time: " + str(hour) + ":" + str(minute) + ":" + str(second), 0, 40)
    oled.text("Duration: " + str(duration) + "s", 0, 56)
    oled.show()