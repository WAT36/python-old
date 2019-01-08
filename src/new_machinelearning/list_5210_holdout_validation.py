#-*- coding:UTF-8 -*-
'''
Created on 2019/01/06

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt
from new_machinelearning.gauss_func import fit_gauss_func, show_gauss_func, mse_gauss_func

outfile = np.load('ch5_data.npz')
X = outfile['X']
X_min = outfile['X_min']
X_max = outfile['X_max']
X_n = outfile['X_n']
T = outfile['T']

#リスト5-2-(10)
#訓練データとテストデータ
X_test = X[:int(X_n / 4)]
T_test = T[:int(X_n / 4)]
X_train = X[int(X_n / 4):]
T_train = T[int(X_n / 4):]

#メイン
plt.figure(figsize=(10,2.5))
M = [2,4,7,9]
for i in range(len(M)):
    plt.subplot(1,len(M),i+1)
    W = fit_gauss_func(X_train,T_train,M[i])
    show_gauss_func(W,X_min,X_max)
    plt.plot(X_train,T_train,marker='o',linestyle='None',color='white',markeredgecolor='black',label='training')
    plt.plot(X_test,T_test,marker='o',linestyle='None',color='cornflowerblue',markeredgecolor='black',label='test')
    plt.legend(loc='lower right',fontsize=10,numpoints=1)
    plt.xlim(X_min,X_max)
    plt.ylim(120,180)
    plt.grid(True)
    mse = mse_gauss_func(X_test,T_test,W)
    plt.title("M={0:d},SD={1:.1f}".format(M[i], np.sqrt(mse)))

plt.show()