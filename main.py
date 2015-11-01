#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy_dtype import *
from matplotlib import pyplot as plt
global rakam
rakam=0
def nothing(x):
    global rakam
    rakam=x
    print "rakam===>",rakam
    pass

cv2.namedWindow('image')
cv2.createTrackbar('sayi1', 'image',1,255,nothing)

baslangicy=5
baslangicx=3


kordinatlar = np.empty( 1, dtype=data_type_kordinatlar)

mesafeler=np.empty( 12, dtype=data_type_mesafeler)

path = np.empty( 1, dtype=data_type_kordinatlar)

tum_kordinatlar = np.empty( 1, dtype=data_type_kordinatlar)
tum_kordinatlar[0]=baslangicx,baslangicy

if __name__ == "__main__":
    print "Merhaba"
    maze=cv2.imread('maze.png')
    maze=cv2.resize(maze,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)

    imgray = cv2.cvtColor(maze,cv2.COLOR_BGR2GRAY)

    binary_image=np.zeros((maze.shape[0],maze.shape[1]),np.uint8)

    cv2.threshold(imgray,rakam,255,cv2.THRESH_BINARY,binary_image)
    demo=binary_image.copy()
    binary_image[20,30]=0
    path['x']=baslangicx
    path['y']=baslangicy


    while(1):

        cv2.imshow('image',binary_image)
        k = cv2.waitKey(33)
        if k==1048689:    # 'q' tusu cikmak icin
            break

        kordinatlar= komsular(path[path.shape[0]-1])

        kordinatlar=path_eleme(kordinatlar,path)

        kordinatlar=pixel_eleme(kordinatlar,binary_image)


        for a in range(0,kordinatlar.shape[0]):
            tum_kordinatlar=nokta_ekle3(tum_kordinatlar,kordinatlar[a])

        tum_kordinatlar=path_eleme(tum_kordinatlar,path)



        mesafeler=mesafe_yaz(mesafeler,tum_kordinatlar)



        index= np.where((mesafeler[:]['toplam']==mesafeler[:]['toplam'].min())==True)



        path=nokta_ekle3(path,tum_kordinatlar[index[0][0]])



        binary_image[tum_kordinatlar[index[0][0]]['y'],tum_kordinatlar[index[0][0]]['x']]=0