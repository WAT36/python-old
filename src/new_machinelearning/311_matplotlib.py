'''
Created on 2018/09/18

@author: watarutsukagoshi
'''

import numpy as np
import matplotlib.pyplot as plt

#data create
np.random.seed(1)
x = np.arange(100)
y = np.random.rand(100)

#graph display
plt.plot(x,y)
plt.show()
