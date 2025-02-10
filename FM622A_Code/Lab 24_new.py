from machine import Pin, I2C, RTC
from ssd1306 import SSD1306_I2C
import network, urequests, utime

ssid = "無線網路名稱"
pw =   "無線網路密碼"
url = "https://timeapi.io/api/time/current/zone?timeZone=Asia/Taipei"
web_query_delay = 600000

weekday_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
rtc = RTC()

print("連接 WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)
while not wifi.isconnected():
    pass
print("已連上")

update_time = utime.ticks_ms() - web_query_delay

while True:
    
    if utime.ticks_ms() - update_time >= web_query_delay:
        
        response = urequests.get(url)
    
        if response.status_code == 200:
            
            parsed = response.json()
            print("JSON 資料查詢成功")
            
            year = parsed["year"]
            month = parsed["month"]
            day = parsed["day"]
            hour = parsed["hour"]
            minute = parsed["minute"]
            second = parsed["seconds"]
            subsecond = parsed["milliSeconds"]
            weekday = weekday_names.index(parsed["dayOfWeek"])
        
            rtc.datetime((year, month, day, weekday, hour, minute, second, subsecond))
            print("系統時間已更新:")
            print(rtc.datetime())
            
            update_time = utime.ticks_ms()
            
        else:
            print("JSON 資料查詢失敗")
    
    weekday_str = " " + weekday_names[rtc.datetime()[3]]
    date_str = " {:02}/{:02}/{:4}".format(rtc.datetime()[1], rtc.datetime()[2], rtc.datetime()[0])
    time_str = " {:02}:{:02}:{:02}".format(rtc.datetime()[4], rtc.datetime()[5], rtc.datetime()[6])
    oled.fill(0)
    oled.text(weekday_str, 0, 8)
    oled.text(date_str, 0, 24)
    oled.text(time_str, 0, 40)
    oled.show()
    
    utime.sleep(0.1)