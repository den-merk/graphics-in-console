from math import *
import os

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
ratio = width / height
ratio_of_letter = 0.5
a = ""


for i in range(height):
    for j in range(width):
        x = (j - width/2)/(width/2) * ratio * ratio_of_letter
        y = (i - height/2)/(height/2)
        if  (sin(x*10)/10<sin(y*10)/10+0.02) and (sin(x*10)/10>sin(y*10)/10-0.02):
            a+="█"
        else:
            a+=" "

    a+="\n"


print(a)

input()
