from math import sin
import os

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
ratio = width / height
ratio_of_letter = 0.5
k = 0
a = ""

while True:
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    k += 1
    for i in range(height):
        for j in range(width):
            x = (j - width/2)/(width/2) * ratio * ratio_of_letter
            y = (i - height/2)/(height/2)
            if (sin(x*5-(k/10))/5 < y+0.025) and (sin(x*5-(k/10))/5 > y-0.025):
                a+="█"
            else:
                a+=" "

        a+="\n"
    

    print(a)
    a = ''
