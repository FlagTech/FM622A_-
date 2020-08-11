from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))

pic_list = [0x1e, 0x3f, 0x7e, 0xfc, 0x7e, 0x3f, 0x1e, 0x00]

pic_buffer = bytearray(pic_list)
pic = framebuf.FrameBuffer(pic_buffer, 8, 8,
                           framebuf.MONO_VLSB)
oled.text("I", 8, 8)
oled.blit(pic, 20, 8)
oled.text("PYTHON", 32, 8)
oled.rect(4, 4, 80, 16, 1) # 畫方框
oled.show()