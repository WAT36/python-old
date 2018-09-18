'''
Created on 2017/09/29

@author: watarutsukagoshi
'''
print('hello world')

for num in range(1,100):
    if num % 15 == 0:
        print(str(num)+':Fizz Buzz')
    elif num % 3 == 0:
        print(str(num)+':Fizz')
    elif num % 5 == 0:
        print(str(num)+':Buzz')

a = 7
b = 8.0

c = a + b
print(c)

