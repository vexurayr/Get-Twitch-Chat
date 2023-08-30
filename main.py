# Code written by Austin Foulks, 8/29/2023

import getchat
from pynput.keyboard import Key
import pynput.keyboard
from pynput.mouse import Button
import pynput.mouse
import time
import random

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

loop = True
# Messages have a 1 in x chance of activating
message_success = 1

# Set custom commands
forward_key = "w"
backwards_key = "s"
left_key = "a"
right_key = "d"
jump_key = "space"
drop_item_key = "q"
open_inventory_key = "e"
left_click_key = "left click"
right_click_key = "right click"
scroll_wheel_up_key = "scroll up"
scroll_wheel_down_key = "scroll down"
mouse_up_key = "mouse up"
mouse_down_key = "mouse down"
mouse_left_key = "mouse left"
mouse_right_key = "mouse right"

def RunProgram():
    try:
        getchat.StartConnection()
        
        while(loop):
            msg = getchat.GetMessage()
            WaitTime(10)
            CheckMessage(msg)
        
    # Runs when program exits
    finally:
        print("Closing App")
        getchat.CloseSocket()
        
def CheckMessage(msg):
    if msg == forward_key:
        LongPressKey('w', 3)
    elif msg == backwards_key:
        LongPressKey('s', 3)
    elif msg == left_key:
        LongPressKey('a', 3)
    elif msg == right_key:
        LongPressKey('d', 3)
    elif msg == jump_key:
        QuickPressKey(Key.space)
    elif msg == drop_item_key:
        QuickPressKey('q')
    elif msg == open_inventory_key:
        QuickPressKey('e')
    elif msg == scroll_wheel_down_key:
        MouseScroll(-1)
    elif msg == scroll_wheel_up_key:
        MouseScroll(1)
    elif msg == left_click_key:
        LongMouseClick(Button.left, 5)
    elif msg == right_click_key:
        QuickMouseClick(Button.right)
    elif msg == mouse_up_key:
        MoveMouse(0, -500)
    elif msg == mouse_down_key:
        MoveMouse(0, 500)
    elif msg == mouse_left_key:
        MoveMouse(-500, 0)
    elif msg == mouse_right_key:
        MoveMouse(500, 0)
        
# For keyboard
def QuickPressKey(key):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Quick Press Key: " + str(key))
    keyboard.press(key)
    keyboard.release(key)
    
# For keyboard
def LongPressKey(key, seconds):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Long Press Key: " + str(key))
    keyboard.press(key)
    WaitTime(seconds)
    keyboard.release(key)
        
# For mouse
def MoveMouse(coord_x, coord_y):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print(mouse.position)
    mouse.move(coord_x, coord_y)
    print(mouse.position)
    
# For mouse
def QuickMouseClick(key):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Quick Press Mouse Key: " + str(key))
    mouse.press(key)
    mouse.release(key)

# For mouse
def LongMouseClick(key, seconds):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Long Press Mouse Key: " + str(key))
    mouse.press(key)
    WaitTime(seconds)
    mouse.release(key)

# For mouse
def MultiMouseClick(key, amount):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Multi Press Mouse Key: " + str(key))
    mouse.click(key, amount)

# For mouse
def MouseScroll(key):
    if RollDice() != 0:
        print("Unlucky roll.")
        return
    
    print("Mouse Scroll: " + str(key))
    mouse.scroll(0, key)
        
# Helper functions
def RollDice():
    return random.randrange(0, message_success)
        
def WaitTime(seconds):
    time.sleep(seconds)
    
if __name__ == "__main__":
    RunProgram()