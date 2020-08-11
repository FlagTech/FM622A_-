from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
import utime

note_min = 220 # 最小頻率(Hz)
note_max = 880 # 最大頻率(Hz)
dist_min = 40 # 測距最小距離(公厘)
dist_max = dist_min + (note_max - note_min) # 測距最大距離(公厘)

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
sonar = HCSR04(trigger_pin=14, echo_pin=12)
buzzer = PWM(Pin(15, Pin.OUT), freq=0, duty=0)

while True:
    
    distance = sonar.distance_mm()
    
    if dist_min <= distance <= dist_max:
        key = note_min + (distance - dist_min)
        buzzer.freq(key)
        buzzer.duty(512)
    else:
        key = 0
        buzzer.duty(0)
        
    oled.fill(0)
    oled.text("Dist: " + str(distance) + " mm", 0, 0)
    oled.text("Note: " + str(key) + " Hz", 0, 16)
    oled.show()
    print("偵測距離: " + str(distance) + " 公厘, 播放頻率: " + str(key) + " 赫茲")

    utime.sleep_ms(10)
