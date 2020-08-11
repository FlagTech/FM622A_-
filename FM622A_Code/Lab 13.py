from machine import Pin, I2C, PWM
import bh1750fvi, utime

def getLightLevel():
    data = bh1750fvi.sample(I2C(scl=Pin(5), sda=Pin(4)), mode=0x23)
    return data

buzzer = PWM(Pin(15, Pin.OUT), freq=768, duty=0)

count = 0
print("系統校準中, 請讓雷射持續照射在亮度感測器5秒鐘...")

while count < 5:
    
    light_level = getLightLevel()
    
    if light_level > 10000:
        count += 1
        print("已校準 " + str(count) + " 秒...")
    else:
        count = 0
    
    utime.sleep_ms(1000)

while True:

    light_level = getLightLevel()
    
    if light_level < 10000:
        print("!! 警報觸發 !!")
        buzzer.duty(512)
    
    else:
        buzzer.duty(0)
        print("-- 待命中 --")