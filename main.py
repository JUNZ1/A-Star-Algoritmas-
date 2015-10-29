#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from cells import *

global rakam
rakam=0
def nothing(x):
    global rakam
    rakam=x
    print "rakam===>",rakam
    pass

cv2.namedWindow('image')
cv2.createTrackbar('sayi1', 'image',1,255,nothing)

#baslangic 30,20


if __name__ == "__main__":
    print "Merhaba"
    maze=cv2.imread('maze.png')
    maze=cv2.resize(maze,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

    imgray = cv2.cvtColor(maze,cv2.COLOR_BGR2GRAY)

    zeros=np.zeros((maze.shape[0],maze.shape[1]),np.uint8)

    cv2.threshold(imgray,rakam,255,cv2.THRESH_BINARY,zeros)

    zeros[20,30]=0


    while(True):
        cv2.imshow('image',zeros)

        k = cv2.waitKey(33)
        if k==1048689:    # 'q' tusu cikmak icin
            break