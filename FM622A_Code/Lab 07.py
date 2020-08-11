from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
import utime

alarm_distance = 10 # 觸發警報距離

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
sonar = HCSR04(trigger_pin=14, echo_pin=12)

buzzer = PWM(Pin(15, Pin.OUT), freq=880, duty=0)

while True:
    
    distance = sonar.distance_cm()
    
    oled.fill(0)
    oled.text("Distance:", 0, 0)
    oled.text(str(distance) + " cm", 0, 16)
    
    if 2 <= distance <= alarm_distance:
        buzzer.duty(512)
        oled.text("!!! ALARM !!!", 0, 40)
        print("!!! 觸發警報 !!!")
    else:
        buzzer.duty(0)
        print("無警報")
    
    oled.show()
    
    utime.sleep_ms(25)