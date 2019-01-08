#-*- coding:UTF-8 -*-
'''
Created on 2019/01/08

@author: T.Wakasugi
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

outfile = np.load('ch5_data.npz')
X = outfile['X']
X_min = outfile['X_min']
X_max = outfile['X_max']
X_n = outfile['X_n']
T = outfile['T']

#リスト 5-2-(17)
#モデルA
def model_A(x,w):
    y = w[0] - w[1] * np.exp(-w[2] * x)
    return y

#モデルA表示
def show_model_A(w):
    xb = np.linspace(X_min, X_max, 100)
    y = model_A(xb,w)
    plt.plot(xb,y,c=[.5,.5,.5],lw=4)

#モデルAのMSE
def mse_model_A(w,x,t):
    y = model_A(x, w)
    mse = np.mean((y-t)**2)
    return mse

#リスト 5-2-(18)
#モデルAのパラメータ最適化
def fit_model_A(w_init,x,t):
    res1 = minimize(mse_model_A,w_init,args=(x,t),method="powell")
    return res1.x

#リスト 5-2-(19)
#メイン
plt.figure(figsize=(4,4))
W_init=[100,0,0]
W = fit_model_A(W_init, X, T)
print("w0={0:.1f},w1={1:.1f},w2={2:.1f}".format(W[0], W[1],W[2]))
show_model_A(W)
plt.plot(X,T,marker='o',linestyle='None',color='cornflowerblue',markeredgecolor='black')
plt.xlim(X_min,X_max)
plt.grid(True)
mse = mse_model_A(W, X, T)
print("SD={0:.2f} cm".format(np.sqrt(mse)))
plt.show()