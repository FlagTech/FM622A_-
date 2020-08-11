import network, urequests, utime
from machine import Pin, I2C
from hcsr04 import HCSR04

sonar = HCSR04(trigger_pin=14, echo_pin=12)

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
key =  "你的金鑰"

url = "https://maker.ifttt.com/trigger/sonar_detected/with/key/" + key

print("連接 WiFi: " + ssid + "...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)
while not wifi.isconnected():
    pass
print("已連上")

print("防盜器已啟動")

while True:
    
    distance = sonar.distance_cm()
    
    if 2 <= distance <= 10:

        print("偵測到不明物 !!!")
        response = urequests.get(url)
    
        if response.status_code == 200:
            print("IFTTT 呼叫成功: 傳送 Line 通知")

        else:
            print("IFTTT 呼叫失敗")
            
        utime.sleep(5)
        
    else:
        
        utime.sleep(0.1)