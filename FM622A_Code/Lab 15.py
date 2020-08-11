from machine import Pin, PWM
import utime, urandom

while True:
    
    #隨機指定每個燈號是否要亮起
    r_switch = urandom.getrandbits(1)
    g_switch = urandom.getrandbits(1)
    b_switch = 1 if r_switch == 0 and g_switch == 0 else urandom.getrandbits(1)
    
    #指定的燈號要亮起時再建立該 PWM 物件
    if r_switch == 1:
        r = PWM(Pin(14, Pin.OUT), freq=1000, duty=0)
    if g_switch == 1:
        g = PWM(Pin(12, Pin.OUT), freq=1000, duty=0)
    if b_switch == 1:
        b = PWM(Pin(13, Pin.OUT), freq=1000, duty=0)

    for i in range(1024):
        if r_switch == 1:
            r.duty(i)
        if g_switch == 1:
            g.duty(i)
        if b_switch == 1:
            b.duty(i)
        utime.sleep_ms(1)
    
    for i in reversed(range(1024)):
        if r_switch == 1:
            r.duty(i)
        if g_switch == 1:
            g.duty(i)
        if b_switch == 1:
            b.duty(i)
        utime.sleep_ms(1)

    #每次燈滅掉後都關閉所有的 PWM 物件
    if r_switch == 1:
        r.deinit()
    if g_switch == 1:
        g.deinit()
    if b_switch == 1:
        b.deinit()
