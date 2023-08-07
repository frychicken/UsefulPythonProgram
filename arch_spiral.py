###############################################################################
# Author: Duong Dinh
# Date: March 20, 2021
# Description: program to draw arch spiral or archimedeam spiral
###############################################################################

#import math and turtla to draw
from turtle import *
from math import *


#main stuff here
def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    # -------------------------------------------------------------------------
    #loop to draw i guess random number

    for i in range(4, 2161):
        t = i / 180 * pi
        # do math luen hthey want to
        x = (1/10 * i) * cos(t)
        y = (1/10 * i) * sin(t)
        goto(x, y)

    # Write your mainline logic here ------------------------------------------


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
