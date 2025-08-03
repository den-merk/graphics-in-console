import math

width = 157
height = 60
ratio = width / height
ratio_of_letter = 0.5
k = 0
a = ""

while True:
    k += 1
    for i in range(height):
        for j in range(width):
            x = (j - width/2)/(width/2) * ratio * ratio_of_letter
            y = (i - height/2)/(height/2)
            if y <math.tan((k/100+x)*5)/10<(y+0.1):
                a+="█"
            else:
                a+=" "

        a+="\n"
    

    print(a)
    a = ''
