#among us controls

import keyboard
import time

time.sleep(1)
def up():
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.release('w')
    time.sleep(0.1)

def down():
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    time.sleep(0.5)

def right():
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    time.sleep(0.5)

def left():
    keyboard.press('a')
    time.sleep(0.5)
    keyboard.release('a')
    time.sleep(0.5)

def action():
    keyboard.press(' ')
    time.sleep(0.5)
    keyboard.release(' ')
    time.sleep(0.5)

up()
up()