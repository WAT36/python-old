# -*- coding: utf-8 -*-
'''
Created on 2018/09/18

@author: watarutsukagoshi
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#関数定義 f(x) = x^3
def f(x):
    return x**3

#関数定義 g(x) = (x-2)x(x+2)
def g(x):
    return (x-2)*x*(x+2)

#-5以上5未満0.1間隔
x = np.arange(-5,5,0.1)
y = f(x)

#-5以上5未満1間隔
v = np.arange(-5,5,1)
w = g(v)

#グラフに使用できる色の名前をコンソール出力
def useablecolors():
    print(matplotlib.colors.cnames)
    return

#グラフに変数x,y,色、ラベル名　を表示して描画　（まだ表示はしない）
plt.plot(x,y,color='black',label='$x^3,0.1$')
plt.plot(v,w,color='cornflowerblue',label='$(x-2)x(x+2),1$')
useablecolors()

#グラフの凡例の位置
plt.legend(loc="upper left")
#y軸の表示範囲
plt.ylim(-15,15)
#グラフのタイトル
plt.title("$f_2(x)$")
#x軸のラベル
plt.xlabel("$x$")
#y軸のラベル
plt.ylabel("$y$")
#グラフにグリッド線を表示
plt.grid(True)

#グラフを表示
plt.show()
