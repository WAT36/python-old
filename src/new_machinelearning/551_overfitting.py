#-*- coding:UTF-8 -*-
'''
Created on 2019/01/06

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt
import gauss_func as gf

outfile = np.load('ch5_data.npz')
X = outfile['X']
X_min = outfile['X_min']
X_max = outfile['X_max']
X_n = outfile['X_n']
T = outfile['T']

#リスト5-2-(8)
plt.figure(figsize=(10,2.5))
plt.subplots_adjust(wspace=0.3)
M=[2,4,7,9]
for i in range(len(M)):
    plt.subplot(1,len(M),i+1)
    W = gf.fit_gauss_func(X,T,M[i])
    gf.show_gauss_func(W,X_min,X_max)
    plt.plot(X,T,marker='o',linestyle='None',
             color='cornflowerblue',markeredgecolor='black')
    plt.xlim(X_min,X_max)
    plt.grid(True)
    plt.ylim(130,180)
    mse = gf.mse_gauss_func(X,T,W)

    plt.title("M=[0:d],SD=[1:.1f]".format(M[i], np.sqrt(mse)))
plt.show()