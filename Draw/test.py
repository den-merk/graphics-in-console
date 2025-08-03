from PIL import Image
from PIL import *
from rich.console import Console
from rich.text import Text

import math

from time import sleep

import os

import tkinter as tk
from tkinter import filedialog as fd 


def get_average_color(img, x, y, w, h):
    rr=0
    rg=0
    rb=0

    for i in range(h):
        for j in range(w):
            rr+=pix[x+j, y+i][0]
            rg+=pix[x+j, y+i][1]
            rb+=pix[x+j, y+i][2]
    
    return ((rr//(w*h)), (rg//(w*h)), (rb//(w*h)))

name= fd.askopenfilename() 


image = Image.open(name)  # Открываем изображение
image_width = image.size[0]  # Определяем ширину
image_height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей


# while True:

console_width = os.get_terminal_size().columns
console_height = os.get_terminal_size().lines

k = max([image_width/console_width*2, image_height/console_height])

console_image_width = math.floor(image_width/k)
console_image_height = math.floor(image_height/k)

console = Console()
a = Text()

n_y = 0

for y in range(console_image_height):
    for x in range(console_image_width-1):


        rgb_color = get_average_color(image, math.floor(x*k), math.floor(y*k), math.floor(k), math.floor(k))

        a.append("██", style=f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")
    a.append("\n")
    n_y = y
for i in range(console_height-n_y):
    a.append("\n")
console.print(a,end="")

sleep(0.1)
input()
# os.system('cls||clear')
