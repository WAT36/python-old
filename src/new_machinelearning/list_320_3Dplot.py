# -*- coding: utf-8 -*-
'''
Created on 2018/09/18

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

#関数f3を定義　
def f3(x,y):
    r = 2 * x**2 + y**2
    ans = r * np.exp(-r)
    return ans

#各x0,x1でf3を計算
xn = 9
#-2から2まで9個の要素
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)
#9*9行列を作成
y = np.zeros((len(x0),len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        y[i1,i0] = f3(x0[i0],x1[i1])

#行列yを出力
print(y)

#行列yを小数点n桁に四捨五入して表示
print(np.round(y,1))

#数値を色で表現する
plot.figure(figsize=(3.5,3))
#グラデーションパターン。他にも.jet(),.pink(),.bone()などある
plot.pink()
#色による行列の表示
plot.pcolor(y)
#カラーバー表示
plot.colorbar()
#plot.show()


xx0,xx1 = np.meshgrid(x0,x1)
plot.figure(figsize=(5,3.5))
ax = plot.subplot(1,1,1,projection='3d')
ax.plot_surface(xx0,xx1,y,rstride=1,cstride=1,alpha=0.3,color='blue',edgecolor='black')
ax.set_zticks((0,0.2))
ax.view_init(75,-95)
plot.show()