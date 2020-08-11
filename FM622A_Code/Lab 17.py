from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import utime

sw520d = Pin(13, Pin.IN, Pin.PULL_UP)
oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
buzzer = PWM(Pin(15, Pin.OUT), freq=880, duty=0)

while True:
    
    oled.fill(0)
    oled.text("Shake status:", 0, 0)
    
    if sw520d.value() == 1:
        buzzer.duty(512)
        oled.text("!!! TIPPED !!!", 0, 16)
        print("!!! 感測器傾倒 !!!")
        
    else:
        buzzer.duty(0)
        oled.text("- Standby -", 0, 16)
        print("感測器狀態正常")
        
    oled.show()
    utime.sleep_ms(100)