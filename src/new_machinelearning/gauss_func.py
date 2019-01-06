#-*- coding:UTF-8 -*-
'''
Created on 2019/01/06

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt

#ガウス関数
def gauss(x,mu,s):
    return np.exp(-(x - mu)**2 / (2 * s**2))

#y(x,W) = w0φ0(x) + w1φ1(x) + w2φ2(x) + w3φ3(x) + w4
#をM=4の線形基底関数モデルという

#線形基底関数モデル
def gauss_func(w,x):
    m = len(w) - 1
    mu = np.linspace(5, 30, m)
    s = mu[1] - mu[0]
    y = np.zeros_like(x)
    for j in range(m):
        y = y + w[j] * gauss(x, mu[j], s)
    y = y + w[m]
    return y

#線形基底関数モデルMSE
def mse_gauss_func(x,t,w):
    y = gauss_func(w,x)
    mse = np.mean((y-t)**2)
    return mse

#線形基底関数モデル 厳密解
def fit_gauss_func(x,t,m):
    mu = np.linspace(5, 30, m)
    s = mu[1] - mu[0]
    n = x.shape[0]
    psi = np.ones((n,m+1))
    for j in range(m):
        psi[:,j] = gauss(x, mu[j], s)
    psi_T = np.transpose(psi)

    b = np.linalg.inv(psi_T.dot(psi))
    c = b.dot(psi_T)
    w = c.dot(t)
    return w


#ガウス基底関数表示
def show_gauss_func(w,X_min,X_max):
    xb = np.linspace(X_min, X_max, 100)
    y = gauss_func(w, xb)
    plt.plot(xb,y,c=[.5,.5,.5], lw=4)
