from __future__ import division
import math
import numpy as np
__author__ = 'junzi'

#yazida once Y sonra X

bitisx=474
bitisy=360

baslangicy=20
baslangicx=30



class cells:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dis_init=0
        self.dis_end=0
        self.find_dis_end()
        self.find_dis_init()
    def find_dis_end(self):
        self.dis_end= math.sqrt(math.pow((self.x-bitisx),2)+math.pow((self.y-bitisy),2))
        print "mesafe son ==>",self.dis_end

    def find_dis_init(self):
        self.dis_init= math.sqrt(math.pow((self.x-baslangicx),2)+math.pow((self.y-baslangicy),2))
        print "mesafe baslangic==>",self.dis_init