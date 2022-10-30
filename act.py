from pynput.keyboard import Key, Controller
from time import sleep
import webbrowser
import pyautogui
import time
import os
##any instance of time.sleep(x) is for 
##pausing the Pi before doing the next action
keyboard = Controller()
pyautogui.FAILSAFE = False
wh = pyautogui.size()
wide = wh.width
high = wh.height
wide1 = wide % 16

def search():
##opens browser/fullscreen
	time.sleep(2)
	webbrowser.open_new("chrome://newtab") #opens buffer window
	time.sleep(5)
	pyautogui.hotkey('ctrl','shift','n') #opens main window 
	time.sleep(2)
	pyautogui.hotkey('alt','\t')
	time.sleep(1)
	pyautogui.hotkey('alt','f4')
	time.sleep(2)
	pyautogui.write("https://ccx1.dhrhs.com:8444/cuicui/permalink/?viewId=D89EC20E10000175000274F00A7F0838&linkType=dashboard") #edit link to specific website
	time.sleep(4)
	pyautogui.press('enter')
	time.sleep(3)
	pyautogui.press('f11')

def keyb():
##moves using keyboard strokes
##initial bootup navigation
	pyautogui.write('21943') #inputs username
	for i in range(1):
		pyautogui.press('\t')
		time.sleep(3)
	pyautogui.press('enter')
	time.sleep(8)
	pyautogui.write('21943') #inputs password
	for i in range(1):
		time.sleep(3)
		pyautogui.press('\t')
		time.sleep(2)
	pyautogui.press('enter')
	time.sleep(30)
	for i in range(2):
		pyautogui.press('\t')
		time.sleep(2)	
	pyautogui.press('space')

def zoom():
#for specific displays, it needs to zoom out
	time.sleep(3)
	if wide == 1366:
		time.sleep(5)
		for i in range(4):
			pyautogui.hotkey('ctrl','-') #zooms the screen out for weird resolution screen
			time.sleep(2)

time.sleep(5)
search()
time.sleep(30)
keyb()
time.sleep(6)
zoom()

##moves mouse to edge of screen
if wide1 == 0:
	hl = high / 2
	pyautogui.moveTo(wide, hl)
else:
	hl = high / 2
	pyautogui.moveTo(wide, hl)

##keeps mouse moving up and down
while True:
	now = time.strftime("%H:%M:%S", time.localtime())
	time.sleep(4)
	pyautogui.moveTo(wide, hl-10, duration=1)
	time.sleep(4)
	pyautogui.moveTo(wide, hl+10, duration=1)
	if (now == "04:00:00"):			#at 4am, hits the refresh button
		pyautogui.press('f5')
