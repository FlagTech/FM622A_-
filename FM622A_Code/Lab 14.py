from machine import Pin
import utime, urandom

r = Pin(14, Pin.OUT)
g = Pin(12, Pin.OUT)
b = Pin(13, Pin.OUT)

while True:
    
    r.value(urandom.getrandbits(1))
    g.value(urandom.getrandbits(1))
    b.value(1 if r.value() == 0 and g.value() == 0 else urandom.getrandbits(1))
    
    utime.sleep_ms(500)