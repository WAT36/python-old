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

#リスト 5-2-(16)
M = 3
plt.figure(figsize=(4,4))
W = fit_gauss_func(X,T,M)
show_gauss_func(W,X_min,X_max)
plt.plot(X,T,marker='o',linestyle='None',color='cornflowerblue',markeredgecolor='black')
plt.xlim([X_min,X_max])
plt.grid(True)
mse = mse_gauss_func(X,T,W)
print("SD={0:.2f} cm".format(np.sqrt(mse)))
plt.show()