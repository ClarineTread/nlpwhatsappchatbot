import os
import sys
import subprocess
import time
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from chat import feed_data

class WhatsApp:

    def __init__(self, speed = 0.5, click_speed = 0.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        
    def msgnoti(self):
        try:
            position = pt.locateOnScreen('noti.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.doubleClick(interval = self.click_speed)
        except Exception as e:
            print('Exceptions caught for noti', e)
    def msgbox(self):
        try:
            position = pt.locateOnScreen('pin.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(100, 10, duration = self.speed)
            pt.click()
        except Exception as e:
            print('Exceptions caught for msgbox', e)
    def write_msg(self):
        try:
            position = pt.locateOnScreen('write.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(10, -50, duration = self.speed)
            pt.doubleClick(interval = self.click_speed)
        except Exception as e:
            print('Exceptions caught for write_msg', e)
    def copy_msg(self):
        try:
            pt.moveRel(-150, -80, duration = self.speed)
            pt.tripleClick()
            sleep(self.speed)
            pt.hotkey('ctrl', 'c') 
            sleep(self.speed)
            self.message = pc.paste()
            print('Message: ', self.message)
        except Exception as e:
            print('Exceptions caught for write_msg ', e)
    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = feed_data(self.message)
                print(bot_response)
                pt.typewrite(bot_response, interval= 0.1)
                pt.typewrite('\n')

                self.last_message = self.message
            else:
                print('No message received')
        except Exception as e:
            print('Exceptions caught for send_message', e)
    def navscode(self):
        try:
            position = pt.locateOnScreen('x.png', confidence = 0.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(50, 50, duration = self.speed)
            pt.doubleClick(interval = self.click_speed)
        except Exception as e:
            print('Exceptions caught for navx', e)
            

wa_bot = WhatsApp(speed=0.5, click_speed=0.4)
sleep(10)

wa_bot.msgnoti()
wa_bot.msgbox()
wa_bot.copy_msg()
wa_bot.msgbox()
wa_bot.send_message()
wa_bot.navscode()

# os.execv(sys.argv[0], sys.argv)
# wa_bot.msgnoti()
# wa_bot.msgbox()
# wa_bot.write_msg()
# wa_bot.copy_msg()
# wa_bot.send_message()


print('Restarting')
time.sleep(2)
subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])   