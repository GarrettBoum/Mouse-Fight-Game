import random
from turtle import left, right
import pyautogui
import time

f=0
time.sleep(0.5)
while True:
    i=random.randint(-10,10)
    leftrand=random.randint(-500,-50)
    rightrand=random.randint(50,500)
    if i<<0:
        pyautogui.move(leftrand, 0, _pause=False, duration=0.25)
    if i >> 0:
        pyautogui.move(rightrand, 0, _pause=False, duration=0.25)
    if i == 0:
        continue
    if f == 10000:
        break
    f=f+1