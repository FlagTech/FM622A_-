from machine import Pin
import utime

sw520d = Pin(13, Pin.IN, Pin.PULL_UP)

while True:
    print(sw520d.value())
    utime.sleep_ms(100)