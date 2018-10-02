# -*- coding: utf-8 -*-
'''
Created on 2018/09/19

@author: watarutsukagoshi
'''
import numpy as np

#ベクトルa
a=np.array([2,1])
print(a)

#ベクトルaの型
print(type(a))

#縦ベクトル
c=np.array([[1,2],[3,4],[5,6]])
print(c)

#転置行列
print(c.T)

#行列の演算
d=np.array([2,1])
e=np.array([4,3])

print(d)
print(e)
##行列の足し算
print(d+e)
##行列の引き算
print(d-e)
##行列の（スカラー）掛け算
print(3*d)
##行列（ベクトル）の内積
print(d.dot(e))
##行列（ベクトル）の大きさ（ノルム）
print(np.linalg.norm(d))

#4.2.2
#Σn(1000,k=1)を内積を使って計算する
f=np.ones(1000)     #[1 1 1... 1]
g=np.arange(1,1001) #[1 2 3... 1000]
print(f.dot(g))
