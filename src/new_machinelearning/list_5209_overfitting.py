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

"リスト 5-2-(9)"
plt.figure(figsize=(5,4))
M = range(2,10)
mse2 = np.zeros(len(M))
for i in range(len(M)):
    W = fit_gauss_func(X,T,M[i])
    mse2[i] = np.sqrt(mse_gauss_func(X,T,W))

plt.plot(M,mse2,marker='o',color='cornflowerblue',markeredgecolor='black')
plt.grid(True)
plt.show()
