from machine import Pin, I2C, PWM
from hcsr04 import HCSR04
import bh1750fvi, utime

sonar = HCSR04(trigger_pin=0, echo_pin=16)

r = PWM(Pin(14, Pin.OUT), freq=1000, duty=0)
g = PWM(Pin(12, Pin.OUT), freq=1000, duty=0)
b = PWM(Pin(13, Pin.OUT), freq=1000, duty=0)

while True:
    
    distance = sonar.distance_cm()
    light_level = bh1750fvi.sample(I2C(scl=Pin(5), sda=Pin(4)), mode=0x23)
    
    if 2 <= distance <= 30:
        led_light_value = 1023
        
    else:
        if light_level > 256:
            light_level = 256
        led_light_value = (256 - light_level) * 4 - 1
    
    r.duty(led_light_value)
    g.duty(led_light_value)
    b.duty(led_light_value)
        
    utime.sleep_ms(50)