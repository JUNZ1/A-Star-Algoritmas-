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

def nokta_ekle2(kordinatlar,sayilar):
    x=sayilar[0]
    y=sayilar[1]
    array=kordinatlar.copy()
    kordinatlar = np.empty( kordinatlar.shape[0]+1, dtype=array.dtype)
    kordinatlar[0:kordinatlar.shape[0]-1]=array.copy()
    kordinatlar[kordinatlar.shape[0]-1]['x']=x
    kordinatlar[kordinatlar.shape[0]-1]['y']=y
    return kordinatlar

def komsular(a):
    x=a[0]
    y=a[1]
    kordinatlar = np.empty( 8, dtype=data_type_kordinatlar)
    kordinatlar[0]['x']=x-1
    kordinatlar[0]['y']=y

    kordinatlar[1]['x']=x-1
    kordinatlar[1]['y']=y-1

    kordinatlar[2]['x']=x
    kordinatlar[2]['y']=y-1

    kordinatlar[3]['x']=x+1
    kordinatlar[3]['y']=y-1

    kordinatlar[4]['x']=x+1
    kordinatlar[4]['y']=y

    kordinatlar[5]['x']=x+1
    kordinatlar[5]['y']=y+1

    kordinatlar[6]['x']=x
    kordinatlar[6]['y']=y+1

    kordinatlar[7]['x']=x-1
    kordinatlar[7]['y']=y+1
    return kordinatlar

def mesafe_yaz(mesafe,kordinat):
    if mesafe.shape[0]!=kordinat.shape[0]:
        mesafe=np.empty( kordinat.shape[0], dtype=mesafe.dtype)

    for a in range(0,mesafe.shape[0]):
        mesafe[a]['mes_son']= math.sqrt(math.pow((kordinat[a]['x']-bitisx), 2)+math.pow((kordinat[a]['y']-bitisy), 2))
        mesafe[a]['mes_baslangic']= math.sqrt(math.pow((kordinat[a]['x']-baslangicx), 2)+math.pow((kordinat[a]['y']-baslangicy), 2))
        mesafe[a]['toplam']=mesafe[a]['mes_son']+mesafe[a]['mes_baslangic']
    return mesafe


