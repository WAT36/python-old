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

#リスト 5-2-(12)
#K分割交差検証
def kfold_gauss_func(x,t,m,k):
    n = x.shape[0]
    mse_train = np.zeros(k)
    mse_test = np.zeros(k)
    for i in range(0,k):
        x_train = x[np.fmod(range(n),k) != i] #(A)
        t_train = t[np.fmod(range(n),k) != i] #(A)
        x_test = x[np.fmod(range(n),k) == i] #(A)
        t_test = t[np.fmod(range(n),k) == i] #(A)
        wm = fit_gauss_func(x_train,t_train,m)
        mse_train[i] = mse_gauss_func(x_train,t_train,wm)
        mse_test[i] = mse_gauss_func(x_test,t_test,wm)
    return mse_train,mse_test

#リスト 5-2-(13)
#np.fmodとは？ →第１引数を第２引数で割ったときのあまり
np.fmod(range(10),5)

#リスト 5-2-(14)
#kfold_gauss_func実行、
#上段がそれぞれの分割における平均二乗誤差、下段がテストデータでの平均二乗誤差
M = 4
K = 4
kfold_gauss_func(X, T, M, K)


#リスト 5-2-(15)
M = range(2,8)
K = 16
Cv_Gauss_train = np.zeros((K,len(M)))
Cv_Gauss_test = np.zeros((K,len(M)))
for i in range(0,len(M)):
    Cv_Gauss_train[:,i], Cv_Gauss_test[:,i] = kfold_gauss_func(X, T, M[i], K)
mean_Gauss_train = np.sqrt(np.mean(Cv_Gauss_train,axis=0))
mean_Gauss_test = np.sqrt(np.mean(Cv_Gauss_test,axis=0))

plt.figure(figsize=(4,3))
plt.plot(M,mean_Gauss_train,marker='o',linestyle='-',color='k',markerfacecolor='w',label='training')
plt.plot(M,mean_Gauss_test,marker='o',linestyle='-',color='cornflowerblue',markeredgecolor='black',label='test')
plt.legend(loc='upper left',fontsize=10)
plt.ylim(0,20)
plt.grid(True)
plt.show()