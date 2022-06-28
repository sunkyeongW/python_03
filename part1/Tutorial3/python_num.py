
print('---'* 5)
print('int형')
print(type(-1))
print(0)
print(1) 
print('---'* 5)
print('float형')
print(type(-3.14))
print(1.1)
print('---'* 5)
print('사칙연산')
print('덧셈:', 1 + 1)
print('뺄셈:', 4 - 2)
print('곱셈:', 5 * 5)
print('나눗셈:', 4 / 2)
print('---'* 5)
print('모듈(math) 사용')

import math

print('math.sqrt:', math.sqrt(4))
print('math.pow:', math.pow(4,3))

print('---'* 5)
print('모듈(random) 사용')

import random

print('random:', random.random())