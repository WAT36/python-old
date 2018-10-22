# -*- coding: UTF-8 -*-
'''
Created on 2018/10/13

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#データ生成(ここは5.1.1と同じ)-------------
np.random.seed(seed=1)  #乱数を固定
X_min = 4               #Xの下限
X_max = 30              #Xの上限
X_n = 16                #データの個数
X = 5 + 25 * np.random.rand(X_n)
print(X)
Prm_c = [170,108,0.2]
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)

#２次元データ生成
X0 = X
X0_min = 5
X0_max = 30
np.random.seed(seed=1)
X1 = 23*(T/100)**2 + 2 * np.random.randn(X_n)
X1_min = 40
X1_max = 75

#データ表示
print(np.round(X0,2))
print(np.round(X1,2))
print(np.round(T,2))

#２次元データの表示
def show_data2(ax,x0,x1,t):
    for i in range(len(x0)):
        ax.plot([x0[i],x0[i]],[x1[i],x1[i]],[120,t[i]],color='gray')
    ax.plot(x0,x1,t,'o',color='cornflowerblue',markeredgecolor='black',markersize=6,markeredgewidth=0.5)
    ax.view_init(elev=35,azim=75)

#メイン
plt.figure(figsize=(6,5))
ax = plt.subplot(1,1,1,projection='3d')
show_data2(ax, X0, X1, T)
plt.show()

