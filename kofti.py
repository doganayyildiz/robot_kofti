from machine import Pin, I2C,PWM
from ssd1306 import SSD1306_I2C
from servo import Servo
import framebuf
import time

pin = 22
motor = Servo(pin)



button = Pin(18,Pin.IN,Pin.PULL_DOWN)
sayac = 0
last_press_time = time.ticks_ms()

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)
oled.rotate(False)
#-------HAPPY-----
# oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
# oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
# oled.fill_rect(45,55,5,5,framebuf.MONO_HLSB)
# oled.fill_rect(85,55,5,5,framebuf.MONO_HLSB)
# oled.fill_rect(50,60,35,5,framebuf.MONO_HLSB)
# oled.show()

#------SAD--------
# oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
# oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
# oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
# oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
# oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
# oled.show()

#------CRY--------
# for i in range(20,50,5):
#     oled.fill_rect(10,15,25,5,framebuf.MONO_HLSB)
#     oled.fill_rect(92,15,25,5,framebuf.MONO_HLSB)
#     oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
#     oled.fill_rect(20,i,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(100,i,5,5,framebuf.MONO_HLSB)
#     oled.show()
#     time.sleep(0.1)
#     oled.fill(0)
#-----BLINK--------
#     oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
#     oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
#     oled.fill_rect(50 ,55,35,5,framebuf.MONO_HLSB)
#     oled.show()
#     time.sleep(1.5)
#     oled.fill(0)
#     oled.fill_rect(4,15,30,5,framebuf.MONO_HLSB)
#     oled.fill_rect(98,15,30,5,framebuf.MONO_HLSB)
#     oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
#     oled.show()
#     time.sleep(0.3)
#     oled.fill(0)
#while True:
#     for i in range(1,3):
#         oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
#         oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
#         oled.fill_rect(50 ,55,35,5,framebuf.MONO_HLSB)
#         oled.show()
#         time.sleep(1)
#         oled.fill(0)
#         oled.fill_rect(4,15,30,5,framebuf.MONO_HLSB)
#         oled.fill_rect(98,15,30,5,framebuf.MONO_HLSB)
#         oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
#         oled.show()
#         time.sleep(0.3)
#         oled.fill(0)
#     
#     oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
#     oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
#     oled.fill_rect(45,55,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(85,55,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(50,60,35,5,framebuf.MONO_HLSB)
#     oled.show()
#     time.sleep(1.5)
#     oled.fill(0)
#     #------SAD--------
#     oled.fill_rect(10,5,25,25,framebuf.MONO_HLSB)
#     oled.fill_rect(98,5,25,25,framebuf.MONO_HLSB)
#     oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
#     oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
#     oled.show()
#     time.sleep(1.5)
#     oled.fill(0)
#     #------CRY--------
#     for i in range(1,5):
#         
#         for i in range(20,50,5):
#             oled.fill_rect(10,15,25,5,framebuf.MONO_HLSB)
#             oled.fill_rect(98,15,25,5,framebuf.MONO_HLSB)
#             oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
#             oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
#             oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
#             oled.fill_rect(20,i,5,5,framebuf.MONO_HLSB)
#             oled.fill_rect(108,i,5,5,framebuf.MONO_HLSB)
#             oled.show()
#             time.sleep(0.1)
#             oled.fill(0)
motor.move(30)     
while True:
    
    #-------BLINK-------
    oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
    oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
    oled.fill_rect(50 ,55,35,5,framebuf.MONO_HLSB)
    oled.show()
    time.sleep(1.5)
    oled.fill(0)
    oled.fill_rect(4,15,30,5,framebuf.MONO_HLSB)
    oled.fill_rect(98,15,30,5,framebuf.MONO_HLSB)
    oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
    oled.show()
    time.sleep(0.3)
    oled.fill(0)
    
    if button.value() == 1:
        motor.move(30)
        last_press_time = time.ticks_ms()
        time.sleep(0.1)
        oled.fill_rect(4,0,30,30,framebuf.MONO_HLSB)
        oled.fill_rect(98,0,30,30,framebuf.MONO_HLSB)
        oled.fill_rect(45,55,5,5,framebuf.MONO_HLSB)
        oled.fill_rect(85,55,5,5,framebuf.MONO_HLSB)
        oled.fill_rect(50,60,35,5,framebuf.MONO_HLSB)
        oled.show()
        time.sleep(1.5)
        oled.fill(0)
        sayac=0
        
    elif time.ticks_diff(time.ticks_ms(), last_press_time) >= 5000:
        #-----SAD--------
        oled.fill(0)
        oled.fill_rect(10,5,25,25,framebuf.MONO_HLSB)
        oled.fill_rect(98,5,25,25,framebuf.MONO_HLSB)
        oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
        oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
        oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
        oled.show()
        time.sleep(1)
        oled.fill(0)
        #------CRY--------
        while(button.value()==0):    
            for i in range(20,50,5):
                oled.fill_rect(10,15,25,5,framebuf.MONO_HLSB)
                oled.fill_rect(98,15,25,5,framebuf.MONO_HLSB)
                oled.fill_rect(45,60,5,5,framebuf.MONO_HLSB)
                oled.fill_rect(85,60,5,5,framebuf.MONO_HLSB)
                oled.fill_rect(50,55,35,5,framebuf.MONO_HLSB)
                oled.fill_rect(20,i,5,5,framebuf.MONO_HLSB)
                oled.fill_rect(108,i,5,5,framebuf.MONO_HLSB)
                oled.show()
                #time.sleep(0.1)
                oled.fill(0)
                
            motor.move(0)
            
            
            
        last_press_time = time.ticks_ms()
        time.sleep(0.1)
        

         

