from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import utime

sw520d = Pin(13, Pin.IN, Pin.PULL_UP)
oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
buzzer = PWM(Pin(15, Pin.OUT), freq=392, duty=0)

oled.text("Step counter", 0, 8)
oled.show()
print("計步器已啟動")

count = 0

while True:
    
    if sw520d.value() == 1:
    
        start_time = utime.ticks_ms()
    
        while sw520d.value() == 1:
            pass
        
        if utime.ticks_ms() - start_time > 50:
        
            count += 1
            print("步數: " + str(count))
        
            buzzer.duty(512)
    
            oled.fill(0)
            oled.text("Count:", 0, 0)
            oled.text(str(count) + " step(s)", 0, 16)
            oled.show()
        
            buzzer.duty(0)