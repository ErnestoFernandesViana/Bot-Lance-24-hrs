import pyautogui as rpa
import time


def box(x,y,z,w):
    width = z - x
    hight = w - y
    return (x, y , width, hight)

def box_frame(x_tuple):
    x, y , width, hight = x_tuple
    z = width + x
    w = hight + y
    x1 = x - 50
    y1 = y - 50
    z1 = z + 50
    w1 = w + 50
    return box(x1, y1, z1, w1)
