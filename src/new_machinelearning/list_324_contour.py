# -*- coding: utf-8 -*-
'''
Created on 2018/09/19

@author: T.Wakasugi
'''
import numpy as np
import matplotlib.pyplot as plt

#関数f3を定義　
def f3(x,y):
    r = 2 * x**2 + y**2
    ans = r * np.exp(-r)
    return ans


xn = 50
x0 = np.linspace(-2, 2, xn)
x1 = np.linspace(-2, 2, xn)

y = np.zeros((len(x0),len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        y[i1,i0] = f3(x0[i0],x1[i1])

print(y)

xx0,xx1 = np.meshgrid(x0,x1)

plt.figure(1,figsize=(4,4))
cont=plt.contour(xx0,xx1,y,5,colors='black')
plt.xlabel('$x_0$',fontsize=14)
plt.ylabel('$x_1$',fontsize=14)
plt.show()