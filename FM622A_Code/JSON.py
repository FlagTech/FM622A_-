import network, urequests, utime

ssid = "FlagoWiFi"
pw = "0233110330"
url = "http://api.icndb.com/jokes/random"

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
    print(parsed)
    
    print("")
    print(parsed["value"]["joke"])