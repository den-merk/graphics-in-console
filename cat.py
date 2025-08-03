from math import *

width = 157
height = 60
ratio = width / height
ratio_of_letter = 0.5
k = 0
a = ""
letters = ['к', 'о', 'ш', 'к', 'а']

letters.append(" ")
letters.append(" ")

while True:
    k += 1
    for i in range(height):
        for j in range(width):
            x = (j - width/2)/(width/2) * ratio * ratio_of_letter
            y = (i - height/2)/(height/2)
            if x*x + y*y + x*sin(k/10) < 0.5 :
                a+=letters[j % len(letters)]
            else:
                a+=" "

        a+="\n"
    

    print(a)
    a = ''
