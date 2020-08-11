from machine import Pin, I2C, PWM
import bh1750fvi, utime

score = 0
buzzer = PWM(Pin(15, Pin.OUT), freq=784, duty=0)
while score < 10:

    light_level = bh1750fvi.sample(I2C(scl=Pin(5), sda=Pin(4)), mode=0x23)
    print("偵測亮度: " + str(light_level) + " lux, 得分: " + str(score))
    
    if light_level > 10000:
        
        print("==== 命中! ====")
        score += 1
        
        buzzer.freq(784)
        buzzer.duty(512)
        utime.sleep_ms(100)
        buzzer.freq(988)
        utime.sleep_ms(300)
        buzzer.duty(0)
    
    utime.sleep_ms(10)
    
print("=== 遊戲結束! ===")

buzzer.freq(784)
buzzer.duty(512)
utime.sleep_ms(100)
buzzer.freq(659)
utime.sleep_ms(100)
buzzer.freq(523)
utime.sleep_ms(300)
buzzer.duty(0)