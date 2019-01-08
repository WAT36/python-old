# -*- coding: UTF-8 -*-
'''
Created on 2018/10/13

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#データ生成-------------
np.random.seed(seed=1)  #乱数を固定
X_min = 4               #Xの下限
X_max = 30              #Xの上限
X_n = 16                #データの個数
X = 5 + 25 * np.random.rand(X_n)
print(X)
Prm_c = [170,108,0.2]
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)
np.savez('ch5_data.npz',X=X,X_min=X_min,X_max=X_max,X_n=X_n,T=T)

#データグラフ表示
plt.figure(figsize=(4,4))
plt.plot(X,T,marker='o',linestyle='None',markeredgecolor='black',color='cornflowerblue')
plt.xlim(X_min,X_max)
plt.grid(True)
plt.show()

#平均誤差関数
def mse_line(x,t,w):
    y = w[0] * x + w[1]     #直線モデル、近似式
    mse = np.mean((y-t)**2) #平均二乗誤差、(予測データ(y) - 実データ(t))(=誤差) の平均
    return mse

#計算
xn = 100                #等高線表示の解像度
w0_range = [-25,25]     #w0の範囲
w1_range = [120,170]    #w1の範囲
x0 = np.linspace(w0_range[0],w0_range[1],xn)
x1 = np.linspace(w1_range[0],w1_range[1],xn)
xx0,xx1 = np.meshgrid(x0,x1)
J =np.zeros((len(x0),len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        J[i1,i0] = mse_line(X, T, (x0[i0],x1[i1]))

#表示
plt.figure(figsize=(9.5,4))
plt.subplots_adjust(wspace=0.5)

ax = plt.subplot(1,2,1,projection='3d')
ax.plot_surface(xx0,xx1,J,rstride=10,cstride=10,alpha=0.3,color='blue',edgecolor='black')
ax.set_xticks([-20,0,20])
ax.set_yticks([120,140,160])
ax.view_init(20,-60)

plt.subplot(1,2,2)
cont = plt.contour(xx0,xx1,J,30,colors='black',levels=[100,1000,10000,100000])
cont.clabel(fmt='%1.0f',fontsize=8)
plt.grid(True)
plt.show()

#平均二乗誤差の勾配
def dmse_line(x,t,w):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y-t) * x)   #Jをw0で偏微分したもの
    d_w1 = 2 * np.mean((y-t))       #Jをw1で偏微分したもの
    return d_w0, d_w1

#試しにw=[10,165]での勾配を求める
d_w=dmse_line(X, T, [10,165])
print(np.round(d_w,1))      #小数点１桁で丸め


#勾配法
def fit_line_num(x,t):
    w_init = [10.0,165.0]   #wの初期値
    alpha = 0.001           #学習率
    i_max = 100000          #繰り返しの最大数
    eps = 0.1               #繰り返しを止める勾配の絶対値の閾値
    w_i = np.zeros([i_max,2])
    w_i[0,:] = w_init
    for i in range(1,i_max):
        dmse = dmse_line(x, t, w_i[i-1])
        w_i[i,0] = w_i[i-1,0] - alpha * dmse[0]
        w_i[i,1] = w_i[i-1,1] - alpha * dmse[1]
        if max(np.absolute(dmse)) < eps:    #終了判定、np.absoluteは絶対値
            break
    w0 = w_i[i,0]
    w1 = w_i[i,1]
    w_i = w_i[:i,:]
    return w0,w1,dmse,w_i

#メイン
plt.figure(figsize=(4,4))

#MSEの等高線表示
xn = 100        #等高線表示
w0_range = [-25,25]
w1_range = [120,170]
x0 = np.linspace(w0_range[0],w0_range[1],xn)
x1 = np.linspace(w1_range[0],w1_range[1],xn)
xx0,xx1 = np.meshgrid(x0,x1)
J = np.zeros((len(x0),len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        J[i1,i0] = mse_line(X,T,(x0[i0],x1[i1]))
cont = plt.contour(xx0,xx1,J,30,colors='black',levels=(100,1000,10000,100000))
cont.clabel(fmt='%1.0f',fontsize=8)
plt.grid(True)

#勾配法呼び出し
W0,W1,dMSE,W_history = fit_line_num(X, T)

#結果表示
print('繰り返し回数 {0}'.format(W_history.shape[0]))
print('W=[{0:.6f},{1:.6f}]'.format(W0,W1))
print('dMSE=[{0:.6f},{1:.6f}]'.format(dMSE[0],dMSE[1])) #勾配法ループで求めた最後の勾配
print('MSE={0:.6f}'.format(mse_line(X, T, [W0,W1])))    #求めたW0,W1での平均二乗誤差
plt.plot(W_history[:,0],W_history[:,1],'-',color='gray',markersize=10,markeredgecolor='cornflowerblue')
plt.show()


#ここで求めたw0とw1が平均二乗誤差Jがもっとも小さくなる値
#本当なのか実際にプロットして検証

#線の表示
def show_line(w):
    xb = np.linspace(X_min, X_max, 100)
    y = w[0] * xb + w[1]
    plt.plot(xb,y,color=(.5,.5,.5),linewidth=4)

#メイン
plt.figure(figsize=(4,4))
W=np.array([W0,W1])
mse = mse_line(X, T, W)
print("w0={0:.3f},w1={1:.3f}".format(W0,W1))
print("SD={0:.3f}cm".format(np.sqrt(mse)))      #平均二乗誤差の平方根＝標準偏差
show_line(W)
plt.plot(X,T,marker='o',linestyle='None',color='cornflowerblue',markeredgecolor='black')
plt.xlim(X_min,X_max)
plt.grid(True)
plt.show()


#解析解で求める
def fit_line(x,t):
    mx = np.mean(x)
    mt = np.mean(t)
    mtx = np.mean(t * x)
    mxx = np.mean(x * x)
    w0 = (mtx - mt * mx)/(mxx - mx**2)
    w1 = mt - w0 * mx
    return np.array([w0,w1])

#メイン
W = fit_line(X, T)
print("w0={0:.3f},w1={1:.3f}".format(W[0],W[1]))
mse = mse_line(X, T, W)
print("SD={0:.3f} cm".format(np.sqrt(mse)))
plt.figure(figsize=(4,4))
show_line(W)
plt.plot(X,T,marker='o',linestyle='None',color='cornflowerblue',markeredgecolor='black')
plt.xlim(X_min,X_max)
plt.grid(True)
plt.show()