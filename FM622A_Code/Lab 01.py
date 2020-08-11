from machine import Pin
import time

led = Pin(2, Pin.OUT)

led.value(0)
time.sleep(3)
led.value(1)