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

#面の表示
def show_plane(ax,w):
    px0 = np.linspace(X0_min, X0_max, 5)
    px1 = np.linspace(X1_min, X1_max, 5)
    px0,px1 = np.meshgrid(px0,px1)
    y = w[0]*px0 + w[1]*px1 + w[2]
    ax.plot_surface(px0,px1,y,rstride=1,cstride=1,alpha=0.3,color='blue',edgecolor='black')


#面のMSE
def mse_plane(x0,x1,t,w):
    y = w[0]*x0 + w[1]*x1 + w[2]
    mse = np.mean((y - t)**2)
    return mse

#メイン
plt.figure(figsize=(6,5))
ax = plt.subplot(1,1,1,projection='3d')
W = [1.5,1,90]
show_plane(ax,W)
show_data2(ax, X0, X1, T)
mse = mse_plane(X0, X1, T, W)
print("SD={0:.3f} cm".format(np.sqrt(mse)))
plt.show()

#リスト 5-1-(16)
#解析解
def fit_plane(x0,x1,t):
    c_tx0 = np.mean(t*x0) - np.mean(t) * np.mean(x0)
    c_tx1 = np.mean(t*x1) - np.mean(t) * np.mean(x1)
    c_x0x1 = np.mean(x0 * x1) - np.mean(x0) * np.mean(x1)
    v_x0 = np.var(x0)   #varは分散
    v_x1 = np.var(x1)
    w0 = (c_tx1 * c_x0x1 - v_x1 * c_tx0) / (c_x0x1**2 - v_x0 * v_x1)
    w1 = (c_tx0 * c_x0x1 - v_x0 * c_tx1) / (c_x0x1**2 - v_x0 * v_x1)
    w2 = -w0 * np.mean(x0) - w1 * np.mean(x1) + np.mean(t)
    return np.array([w0,w1,w2])

#メイン
plt.figure(figsize=(6,5))
ax = plt.subplot(1,1,1,projection='3d')
W = fit_plane(X0, X1, T)
print("w0={0:.1f}, w1={1:.1f}, w2={2:.1f}".format(W[0],W[1],W[2]))
show_plane(ax, W)
show_data2(ax, X0, X1, T)
mse = mse_plane(X0, X1, T, W)
print("SD={0:.3f} cm".format(np.sqrt(mse)))
plt.show()