import pygame
import os
import math
import time

import numpy as np
from scipy.interpolate import griddata

from colour import Color

#low range of the sensor (this will be blue on the screen)
MINTEMP = 20

#high range of the sensor (this will be red on the screen)
MAXTEMP = 26

#how many color values we can have
COLORDEPTH = 1024

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()


points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

#sensor is an 8x8 grid so lets do a square
height = 480
width = 480

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

lcd = pygame.display.set_mode((width, height))

lcd.fill((255,0,0))

pygame.display.update()
pygame.mouse.set_visible(False)

lcd.fill((0,0,0))
pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)

f = open("data14.txt", "r")
pixels_str = f.read().splitlines()
#x_list = []
#y_list = []
pixels = []
for line in pixels_str:
    #x_list.append(line.split(" ")[0])
    #y_list.append(line.split(" ")[1])
    pixels.append(float(line.split(" ")[2])-273.15)
#pixels = [float(item) for item in pixels_str]
#print(pixels)
new_pixels = []

for y in range(0,480):
    for x in range(0,480):
        #print(pixels[480*x+y])
        #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        pygame.draw.rect(lcd, [int(pixels[480*x+y]*5),int(pixels[480*x+y]*5),int(pixels[480*x+y]*5)],[x,y,1,1])
        new_pixels.append(str(x-60)+" "+str(y)+" "+str(pixels[480*x+y])+"\n")

'''
f2 = open("1_BottleFLIR.txt","w")
f2.writelines(new_pixels)
f2.close()'''

pygame.display.update()

