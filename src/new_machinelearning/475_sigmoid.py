# -*- coding: UTF-8 -*-
'''
Created on 2018/10/09

@author: T.Wakasugi
'''

import numpy as np
import matplotlib.pyplot as plt

#シグモイド関数
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(4,4))
plt.plot(x,y,'black',linewidth=3)


plt.ylim(-1,2)
plt.xlim(-10,10)
plt.grid(True)
plt.show()