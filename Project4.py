__author__ = 'henrynguyen'
import pygame, sys
from pygame.locals import *
from sys import exit
import time
import math
import linecache

pygame.init()
w = 640
h = 480
size = (w,h)
white = (255, 255, 255)
blue = (0,0,255)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption('Ant Movement')
Ant = pygame.image.load('ant.jpg').convert()
ant_rect = Ant.get_rect()
clock = pygame.time.Clock()
line = 1

#opening .btf files
antId = open("id.btf" , "r").read().splitlines()
#timestamp = open("timestamp.btf" , "r").read().splitlines()
#timage = open("timage.btf" , "r").read().splitlines()
#antX = open("ximage.btf" , "r").read().splitlines()
#antY= open("yimage.btf" , "r").read().splitlines()
"""
for i in range(0, len(antId)):
    antId[i] = int(antId[i])
    antX[i] = float(antX[i])
    antY[i] = float(antY[i])
    #timestamp[i] = int(timestamp[i])
    timage[i] = float(timage[i])
"""
def rad2deg(radians):
    degrees = 180 * radians / math.pi
    return degrees

def rotate(i):
    rad = float(linecache.getline('timage.btf', i))
    deg = rad2deg(rad)
    return deg

def antPos(i):
    x = float(linecache.getline('ximage.btf', i))
    y = float(linecache.getline('yimage.btf', i))
    antPos = (x, y)
    return antPos

#screen.blit(Ant, (antPos(line)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

#ant movement

    timestamp = int(linecache.getline('timestamp.btf', line))
    while timestamp == int(linecache.getline('timestamp.btf', line)):
        rotatedAnt = pygame.transform.rotate(Ant, rotate(line))
        position = ant_rect.move(antPos(line+1))
        pygame.draw.line(rotatedAnt, blue, antPos(line+1), antPos(line))
        screen.blit(rotatedAnt, position)
        line += 1
        break
    clock.tick(33.33)
    pygame.display.update()


