import network, urequests

ssid = "你的WiFi名稱"
pw =   "你的WiFi密碼"
url = "https://www.flag.com.tw/"

print("連接 WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

while not wifi.isconnected():
    pass
print("已連上")

print("IP: " + str(wifi.ifconfig()[0]))

print("取得網頁...")
response = urequests.get(url)
    
if response.status_code == 200:
    print("網頁請求成功:")
    print(response.text)

else:
    print("網頁請求失敗")