from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import bh1750fvi, utime

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

buzzer = PWM(Pin(15, Pin.OUT), freq=110, duty=0)

while True:
    
    light_level = bh1750fvi.sample(i2c, mode=0x23)
    print("偵測亮度: " + str(light_level) + " lux")
    
    oled.fill(0)
    oled.text("Light level:", 0, 0)
    oled.text(str(light_level) + " lux", 0, 16)
    
    if 20 < light_level < 300:
        oled.text("!! Warning !!", 0, 32)
        oled.text("TOO DARK", 0, 48)
        print("警告 !! 亮度不足 !!")
        buzzer.freq(110)
        buzzer.duty(512)
    
    else:
        buzzer.duty(0)
    
    oled.show()
    