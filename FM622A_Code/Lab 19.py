from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import utime, urandom

sw520d = Pin(13, Pin.IN, Pin.PULL_UP)
oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
buzzer = PWM(Pin(15, Pin.OUT), freq=440, duty=0)
laser = Pin(16, Pin.OUT)
laser.off()

oled.fill(0)
oled.text("Reaction test", 0, 0)
oled.text("SHAKE to start", 0, 16)
oled.show()
print("反應大考驗 - 搖晃震動開關來啟動測試")

while True:

    if sw520d.value() == 1:
        
        laser.off()

        for i in reversed(range(3)):
            oled.fill(0)
            oled.text("Reaction test", 0, 0)
            oled.text("Ready in " + str(i + 1) + " secs", 0, 16)
            oled.show()
            print("倒數 " + str(i + 1) + " 秒...")
            buzzer.freq(440)
            buzzer.duty(512)
            utime.sleep(0.1)
            buzzer.duty(0)
            utime.sleep(0.9)

        buzzer.freq(880)
        buzzer.duty(512)
        oled.fill(0)
        oled.text("Started!", 0, 0)
        oled.text("SHAKE when laser", 0, 16)
        oled.text("turns on:", 0, 32)
        oled.show()
        print("測試開始! 在雷射光一點亮時搖晃震動開關")
        utime.sleep(0.3)
        buzzer.duty(0)
        utime.sleep(0.7)

        utime.sleep(3 + urandom.getrandbits(3))
        print("測試開始! 在雷射光一點亮時搖晃震動開關")
        laser.on()
        start_time = utime.ticks_ms()

        while sw520d.value() == 0:
            pass

        reaction_time = (utime.ticks_ms() - start_time) / 1000

        oled.fill(0)
        oled.text("Reaction time:", 0, 0)
        oled.text(str(reaction_time) + " secs", 0, 16)
        oled.text("SHAKE to start", 0, 40)
        oled.text("again", 0, 54)
        oled.show()
        print("反應時間: " + str(reaction_time) + " 秒")
        print("測試結束 - 搖晃震動開關以再次測試")
        buzzer.freq(440)
        buzzer.duty(512)
        utime.sleep(0.1)
        buzzer.freq(880)
        utime.sleep(0.3)
        buzzer.duty(0)
        utime.sleep(1.6)