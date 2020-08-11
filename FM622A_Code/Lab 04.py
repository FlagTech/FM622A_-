from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

i2c = I2C(scl=Pin(5), sda=Pin(4))

oled = SSD1306_I2C(128, 64, i2c)

while True:
    
    system_time = utime.ticks_ms()
    
    oled.fill(0)
    oled.text("System time: ", 0, 0)
    oled.text(str(system_time), 0, 16)
    oled.show()
    
    utime.sleep_ms(100)