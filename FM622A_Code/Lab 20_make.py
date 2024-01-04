import network, urequests, utime, bh1750fvi
from machine import Pin, I2C

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
url = "輸入你的 MAKE 網址"

print("連接 WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

while not wifi.isconnected():
    pass
print("已連上")

print("亮度記錄器已啟動")

while True:
    
    light_level = bh1750fvi.sample(I2C(scl=Pin(5), sda=Pin(4)), mode=0x23)

    response = urequests.get(url + "?value1=" + str(light_level))
    
    if response.status_code == 200:
        print("MAKE 呼叫成功: 傳送亮度 " + str(light_level) + " lux")

    else:
        print("MAKE 呼叫失敗")
        
    utime.sleep(5)
