# -*- coding: utf-8 -*-
'''
Created on 2018/10/02

@author: watarutsukagoshi
'''

import numpy as np
import matplotlib.pyplot as plt

#指数関数 y = 2^x , 3^x , 0.5^x
x = np.linspace(-4, 4, 100)
y = 2**x
y2= 3**x
y3= 0.5**x

#対数関数　y = log(2)x, log(3)x, log(0.5)x
y4= np.log(x) / np.log(2)
y5= np.log(x) / np.log(3)
y6= np.log(x) / np.log(0.5)

#指数関数の微分
dy = y * np.log(2)

#プロットの画面サイズ
plt.figure(figsize=(5,5))
#y,y2,y3をプロット
plt.plot(x,y,'black',linewidth=3,label='$y=2^x$')
plt.plot(x,y2,'cornflowerblue',linewidth=3,label='$y=3^x$')
plt.plot(x,y3,'gray',linewidth=3,label='$y=0.5^x$')
plt.plot(x,y4,'black',linewidth=3,label='$y=log2x$')
plt.plot(x,y5,'cornflowerblue',linewidth=3,label='$y=log3x$')
plt.plot(x,y6,'gray',linewidth=3,label='$y=log(0.5)x$')
#dyを点線でプロット
plt.plot(x,dy,'black',linestyle='--',linewidth=3,label='$y=(2^x)log2$')
#プロットのy軸、x軸の範囲
plt.ylim(-4,4)
plt.xlim(-4,4)
#プロットのグリッド線
plt.grid(True)
#プロットの凡例の位置
plt.legend(loc='lower right')
#プロット表示
plt.show()

