from __future__ import division
import numpy as np
import math
__author__ = 'junzi'

bitisx=474
bitisy=360

baslangicy=20
baslangicx=30


data_type_kordinatlar = np.dtype([('x', np.float64),('y', np.float64)])

data_type_mesafeler = np.dtype([('mes_son', np.float),('mes_baslangic', np.float)])


kordinatlar = np.empty( 5, dtype=data_type_kordinatlar)

mesafeler=np.empty( 5, dtype=data_type_mesafeler)


#mesafeler['mes_son']= math.sqrt(math.pow((kordinatlar['x']-bitisx),2)+math.pow((kordinatlar['x']-bitisy),2))


kordinatlar[:]=12,13
kordinatlar[0]=1,2
x=3
y=5


def nokta_ekle(kordinatlar,x,y):
    array=kordinatlar.copy()
    kordinatlar = np.empty( kordinatlar.shape[0]+1, dtype=array.dtype)
    print kordinatlar.shape[0]

    kordinatlar[0:kordinatlar.shape[0]-1]=array.copy()
    kordinatlar[kordinatlar.shape[0]-1]['x']=x
    kordinatlar[kordinatlar.shape[0]-1]['y']=y
    return kordinatlar

mesafe_yaz(mesafeler,kordinatlar)