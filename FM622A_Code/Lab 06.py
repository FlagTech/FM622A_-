from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
import utime

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
sonar = HCSR04(trigger_pin=14, echo_pin=12)

while True:
    
    distance = sonar.distance_cm()
    
    oled.fill(0)
    oled.text("Distance:", 0, 0)
    oled.text(str(distance) + " cm", 0, 16)
    oled.show()
    print("偵測距離: " + str(distance) + " 公分")
    
    utime.sleep_ms(25)