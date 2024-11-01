# -*- coding: UTF-8 -*-
from __future__ import division, unicode_literals

def v(T,Cv,x,y,m,t,s,Kv=1):
    """Повертає швидкість різання, м/хв"""
    return Cv*Kv/(T**m * t**x * s**y)

#чистові подачі, мм/об
s0={"Ra":{0.63:{0.4:0.07, 0.8:0.1, 1.2:0.12},
          1.25:{0.4:0.1, 0.8:0.13, 1.2:0.165},
          2.5:{0.4:0.144, 0.8:0.2, 1.2:0.246}}}

CvXYm={"Конструкційна вуглецева сталь":
       {"Зовнішнє поздовжнє точіння":{"Т15К6":{"s<=0.3":(350,0.15,0.2,0.2),
                                               "0.3<s and s<=0.7":(290,0.15,0.35,0.2),
                                               "s>0.7":(280,0.15,0.45,0.2)}}},
       "Сірий чавун":
       {"Зовнішнє поздовжнє точіння":{"ВК6":{"s<=0.4":(292,0.15,0.2,0.2),
                                             "s>0.4":(243,0.15,0.4,0.2)}}}}

T=60 # стійкість, хв
d=50 # діаметр деталі, мм
L=80 # довжина обробки
t=0.1 # глибина різання, мм
Ra=0.63 # шорсткість, мкм
r=0.8 # радіус при вершині різця, мм
s=s0["Ra"][Ra][r] # подача, мм/об
print s, "мм/об"
mat=CvXYm["Конструкційна вуглецева сталь"]["Зовнішнє поздовжнє точіння"]["Т15К6"]
for k in mat.keys():
    if eval(k):
        Cv,x,y,m=mat[k] # коефіцієнти
Kmv=1
Kpv=1
Kiv=1
Kv=Kmv*Kpv*Kiv
vel=v(T,Cv,x,y,m,t,s,Kv) # швидкість різання
print vel, "м/хв"
n=1000*vel/(3.14*d) # частота обертання шпинделя
print n, "об/хв"
T0=L/(n*s) # основний час
print T0, "хв"
