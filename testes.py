import pyautogui
import random
import time

time.sleep(5)

mensagens = ['1', '2', '3', '4', '5']

for i in range(50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("enter")