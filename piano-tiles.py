from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# Tile 1: X:803  Y:661
# Tile 2: X:904  Y:661
# Tile 3: X:999  Y:661
# Tile 4: X:1098 Y:661
# RGB (0, 0, 0)
# Width: X: 759 - 1144

TILE_X1 = 803
TILE_X2 = 904
TILE_X3 = 999
TILE_X4 = 1098
TILES_Y = 661

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
    while keyboard.is_pressed('q') == False:
        if(pyautogui.pixel(TILE_X1, TILES_Y)[0] == 0):
            click(TILE_X1, TILES_Y+100)

        if(pyautogui.pixel(TILE_X2, TILES_Y)[0] == 0):
            click(TILE_X2, TILES_Y+100)

        if(pyautogui.pixel(TILE_X3, TILES_Y)[0] == 0):
            click(TILE_X3, TILES_Y+100)

        if(pyautogui.pixel(TILE_X4, TILES_Y)[0] == 0):
            click(TILE_X4, TILES_Y+100)
        

if __name__ == '__main__':
    main()

