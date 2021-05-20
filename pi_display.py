# !/usr/bin/python
# sudo pip install RPLCD
import RPi.GPIO as GPIO
from RPLCD import CharLCD
from RPLCD import cursor


def send_msg(str):
    lcd = CharLCD(pin_rs=12, pin_rw=17, pin_e=16, pins_data=[6, 13, 19, 26], numbering_mode=GPIO.BCM, cols=16, rows=2,
                  auto_linebreaks=False)    
    lcd.clear()
    lcd.cursor_pos = 0, 0
    lcd.write_string(str[:32])
    lcd.close()
    GPIO.cleanup()
    return True
