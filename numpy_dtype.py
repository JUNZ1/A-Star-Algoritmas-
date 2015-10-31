from __future__ import division
import numpy as np
import math
__author__ = 'junzi'

bitisx=474
bitisy=360

baslangicy=20
baslangicx=30


data_type_kordinatlar = np.dtype([('x', np.float64),('y', np.float64)])

data_type_mesafeler = np.dtype([('mes_son', np.float),('mes_baslangic', np.float),('toplam', np.float)])


kordinatlar = np.empty( 5, dtype=data_type_kordinatlar)

mesafeler=np.empty( 12, dtype=data_type_mesafeler)

kordinatlar[:]=474,360



def nokta_ekle(kordinatlar,x,y):
    array=kordinatlar.copy()
    kordinatlar = np.empty( kordinatlar.shape[0]+1, dtype=array.dtype)
    kordinatlar[0:kordinatlar.shape[0]-1]=array.copy()
    kordinatlar[kordinatlar.shape[0]-1]['x']=x
    kordinatlar[kordinatlar.shape[0]-1]['y']=y
    return kordinatlar


def mesafe_yaz(mesafe,kordinat):
    if mesafe.shape[0]!=kordinat.shape[0]:
        mesafe=np.empty( kordinat.shape[0], dtype=mesafe.dtype)

    for a in range(0,mesafe.shape[0]):
        mesafe[a]['mes_son']= math.sqrt(math.pow((kordinat[a]['x']-bitisx), 2)+math.pow((kordinat[a]['y']-bitisy), 2))
        mesafe[a]['mes_baslangic']= math.sqrt(math.pow((kordinat[a]['x']-baslangicx), 2)+math.pow((kordinat[a]['y']-baslangicy), 2))
        mesafe[a]['toplam']=mesafe[a]['mes_son']+mesafe[a]['mes_baslangic']
    return mesafe