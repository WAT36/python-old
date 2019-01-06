#-*- coding:UTF-8 -*-
'''
Created on 2019/01/06

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt
from new_machinelearning.gauss_func import fit_gauss_func, mse_gauss_func

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

#リスト 5-2-(11)
plt.figure(figsize=(5,4))
M = range(2,10)
mse_train = np.zeros(len(M))
mse_test = np.zeros(len(M))
for i in range(len(M)):
    W = fit_gauss_func(X_train,T_train,M[i])
    mse_train[i] = np.sqrt(mse_gauss_func(X_train,T_train,W))
    mse_test[i] = np.sqrt(mse_gauss_func(X_test,T_test,W))

plt.plot(M,mse_train,marker='o',linestyle='-',markerfacecolor='white',markeredgecolor='black',color='black',label='training')
plt.plot(M,mse_test,marker='o',linestyle='-',markerfacecolor='blue',markeredgecolor='black',color='black',label='test')
plt.legend(loc='upper left',fontsize=10)
plt.ylim(0,12)
plt.grid(True)
plt.show()