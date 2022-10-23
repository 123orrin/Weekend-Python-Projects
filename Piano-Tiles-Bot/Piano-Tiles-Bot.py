"""
Piano Tiles Bot
Created by Orrin Dahanaggamaarachchi

This is a Piano tiles bot designed to play the hit game, Piano Tiles. Whenever the program detects a pixel of a specific colour (namely, value 17) it clicks the screen or a button on the screen (depending on the mode selected). It is designed to play with the following version of Piano Tiles: http://tanksw.com/piano-tiles/.

If you are using MouseCLick mode, the program must be calibrated to your specific screen coordinates. The following code can be run to find the values of the 4 clickable areas:

# Getting Mouse Position Coords
#def Test():
#    pyautogui.displayMousePosition()
#while 1:
#    Test()

Input these into the MouseClick function at the clicking location and the program will be good to go!
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def Click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.07)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def MouseControl():
    while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(1212, 1000)[0] == 17:
            Click(1212, 1000)
        if pyautogui.pixel(1460, 1000)[0] == 17:
            Click(1460, 1000)
        if pyautogui.pixel(1712, 1000)[0] == 17:
            Click(1712, 1000)
        if pyautogui.pixel(1946, 1000)[0] == 17:
            Click(1946, 1000)


def ClickKeyboard(x):
    keyboard.press(x)
    time.sleep(0.05)
    keyboard.release(x)
    time.sleep(0.05)


def KeyboardControl():
    while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(1212, 1000)[0] == 17:
            ClickKeyboard('a')
        if pyautogui.pixel(1460, 1000)[0] == 17:
            ClickKeyboard('s')
        if pyautogui.pixel(1712, 1000)[0] == 17:
            ClickKeyboard('d')
        if pyautogui.pixel(1946, 1000)[0] == 17:
            ClickKeyboard('f')


time.sleep(5)

# Select Either Mouse Control or Keyboard Control

#MouseControl()
KeyboardControl()
