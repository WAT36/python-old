# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

#関数fの定義
def f(w0,w1):
    return w0**2 + 2*w0*w1 + 3

#fのw0に対する偏微分
def df_dw0(w0,w1):
    return 2*w0 + 2*w1

#fのw1に対する偏微分
def df_dw1(w0,w1):
    return 2*w0 + 0*w1

w_range = 2
dw = 0.25
w0 = np.arange(-w_range,w_range+dw,dw)  #-2から2まで0.25間隔、終点で指定した数字は含まれないので2.25までとしている
w1 = np.arange(-w_range,w_range+dw,dw)
wn = w0.shape[0]                        #w0の長さ。正確には(長さ,)という形で返るため、[0]を参照して返す

ww0,ww1 = np.meshgrid(w0,w1)

ff = np.zeros((len(w0),len(w1)))
diff_dw0 = np.zeros((len(w0),len(w1)))  #ゼロ行列。行列の初期化。
diff_dw1 = np.zeros((len(w0),len(w1)))
for i0 in range(wn):
    for i1 in range(wn):
        ff[i1,i0] = f(w0[i0],w1[i1])
        diff_dw0[i1,i0] = df_dw0(w0[i0],w1[i1])
        diff_dw1[i1,i0] = df_dw1(w0[i0],w1[i1])

plt.figure(figsize=(9,4))
plt.subplots_adjust(wspace=0.3)
plt.subplot(1,2,1)
cont = plt.contour(ww0,ww1,ff,10,colors='k')
cont.clabel(fmt='%2.0f',fontsize=8)
plt.xticks(range(-w_range,w_range+1,1))
plt.yticks(range(-w_range,w_range+1,1))
plt.xlim(-w_range-0.5,w_range+.5)
plt.ylim(-w_range-.5,w_range+.5)
plt.xlabel('$w_0$',fontsize=14)
plt.ylabel('$w_1$',fontsize=14)

plt.subplot(1,2,2)
plt.quiver(ww0,ww1,diff_dw0,diff_dw1)
plt.xlabel('$w_0$',fontsize=14)
plt.ylabel('$w_1$',fontsize=14)
plt.xticks(range(-w_range,w_range+1,1))
plt.yticks(range(-w_range,w_range+1,1))
plt.xlim(-w_range-0.5,w_range+.5)
plt.ylim(-w_range-.5,w_range+.5)
plt.show()