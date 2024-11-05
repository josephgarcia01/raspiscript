##Opens an RDP session and checks if the window is still active.
##Author: jg
##Date: 2/2023

import time
import os
import pyautogui
import subprocess

pyautogui.FAILSAFE = False
wh = pyautogui.size()
wide = wh.width
high = wh.height
wide1 = wide % 16

#tells user what pi is opening
#runs rdesktop
def open():
    time.sleep(10)
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(5)
    pyautogui.write("stty -echo ##Starting Bedtracker")
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.write("rdesktop ACCOUNT_NAME -d DOMAIN -u USER -p 'PASS'")
    time.sleep(4)
    pyautogui.press('enter')
    time.sleep(7)

#runs shell command to return true/false if window is active
def check_window_open(window_title):
    cmd = ['xdotool', 'search', '--onlyvisible', '--name', window_title]
    try:
        subprocess.check_output(cmd)
        return True
    except subprocess.CalledProcessError:
        return False

def restart_linux():
    subprocess.call(['sudo', 'reboot'])

#assigns window that needs to be open to variable
window_title = "nameofWindow"

open()
time.sleep(3)
for x in range(2):
    pyautogui.press('tab')
pyautogui.press('enter')

if wide1 == 0:
    h1 = high / 2
    pyautogui.moveTo(wide, h1)
else:
    h1 = high / 2
    pyautogui.moveTo(wide, h1)

#loops continuously; if window expectedly shuts down
#due to disconnect, restart.
while True:
    time.sleep(3)
    pyautogui.moveTo(wide, h1-10, duration = 1)
    time.sleep(5)
    pyautogui.moveTo(wide, h1+10, duration = 1)
    if not check_window_open(window_title):
        print("The window is not open. Restarting Linux...")
        restart_linux()
