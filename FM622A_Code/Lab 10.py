from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import bh1750fvi, utime

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    
    light_level = bh1750fvi.sample(i2c, mode=0x23)
    
    oled.fill(0)
    oled.text("Light level:", 0, 0)
    oled.text(str(light_level) + " lux", 0, 16)
    oled.show()
    print("偵測亮度: " + str(light_level) + " lux")