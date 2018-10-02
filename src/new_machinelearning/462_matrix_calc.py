# -*- coding: utf-8 -*-
'''
Created on 2018/10/02

@author: watarutsukagoshi
'''
import numpy as np

#リスト4-3
A=np.array([[1,2,3],[4,5,6]])
print('A:')
print(A)

B=np.array([[7,8,9],[10,11,12]])
print('B:')
print(B)

#行列の足し引き
print('A+B:')
print(A+B)
print('A-B:')
print(A-B)

#行列のスカラー倍
print('2*A:')
print(2*A)

#行列の積
print('B^T(Bの転置)')
print(B.T)

print('A(B^T):')
print(A.dot(B.T))

#次は行列の要素どうしを掛け算、割り算
print('A*B:')
print(A*B)
print('A/B:')
print(A/B)

#単位行列
print('I:')
print(np.identity(3))

#逆行列
C=np.array([[1,2],[3,4]])
print('C:')
print(C)
print('C^-1:')
print(np.linalg.inv(C))

#転置行列
print('A:')
print(A)
print('A^T:')
print(A.T)