#-*- coding:UTF-8 -*-
'''
Created on 2019/01/08

@author: T.Wakasugi
'''
import numpy as np
import matplotlib.pyplot as plt
from new_machinelearning.list_5217_mse_model import fit_model_A, mse_model_A
from new_machinelearning.list_5212_k_hold_cross_validation import mean_Gauss_test

outfile = np.load('ch5_data.npz')
X = outfile['X']
X_min = outfile['X_min']
X_max = outfile['X_max']
X_n = outfile['X_n']
T = outfile['T']

#リスト 5-2-(20)
#交差検定 model_A
def kfold_model_A(x,t,k):
    n = len(x)
    mse_train = np.zeros(k)
    mse_test = np.zeros(k)
    for i in range(0,k):
        x_train = x[np.fmod(range(n),k)]
        t_train = t[np.fmod(range(n),k)]
        x_test = x[np.fmod(range(n),k)]
        t_test = t[np.fmod(range(n),k)]
        wm = fit_model_A(np.array([169,113,0.2]),x_train,t_train)
        mse_train[i] = mse_model_A(wm,x_train,t_train)
        mse_test[i] = mse_model_A(wm,x_test,t_test)
    return mse_train,mse_test

#メイン
K = 16
Cv_A_train,Cv_A_test = kfold_model_A(X, T, K)
mean_A_test = np.sqrt(np.mean(Cv_A_test))
print("Gauss(M=3) SD={0:.2f}cm".format(mean_Gauss_test[1]))
print("Model A SD={0:.2f}cm".format(mean_A_test))
SD = np.append(mean_Gauss_test[0:5], mean_A_test)
M = range(6)
label =["M=2","M=3","M=4","M=5","M=6","Model A"]
plt.figure(figsize=(5,3))
plt.bar(M,SD,tick_label=label,align="center",facecolor="cornflowerblue")
plt.show()