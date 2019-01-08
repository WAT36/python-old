#-*- coding:UTF-8 -*-
'''
Created on 2019/01/06

@author: T.Wakasugi
'''

import numpy as np

#ch5_data.npzのロード
def ch5_data_load():
    outfile = np.load('ch5_data.npz')
    X = outfile['X']
    X_min = outfile['X_min']
    X_max = outfile['X_max']
    X_n = outfile['X_n']
    T = outfile['T']

