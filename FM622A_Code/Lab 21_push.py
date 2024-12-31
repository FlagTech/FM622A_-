import network, urequests, utime
from machine import Pin, I2C
from hcsr04 import HCSR04
import line

sonar = HCSR04(trigger_pin=14, echo_pin=12)

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
line_access_token = '你的 LINE 通道存取令牌'
lineUserID = '你的 LINE user/group id'

line.line_token(line_access_token)

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
        line.line_token(line_access_token)
        status_code = line.line_notify(
            lineUserID,
            '防盜器已觸發')
    
        if status_code == 200:
            print("呼叫成功: 傳送 Line 通知")

        else:
            print("呼叫失敗")
            
        utime.sleep(5)
        
    else:
        
        utime.sleep(0.1)