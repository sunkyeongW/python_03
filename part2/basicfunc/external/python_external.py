#sys

import imp
import sys
print(sys.argv)
print('--' * 4)
#sys 강제종료

#sys.exit()

#파이썬 패키지 위치
print(sys.path)
print('--' * 4)

#pickle : 객체 파일 쓰기
import pickle

f = open("test.obj", 'wb')

obj = {1: 'python', 2:'study', 3: 'basic'}

pickle.dump(obj, f)
f.close


#객체 파일 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close

#os
import os
print(os.environ)
print(os.environ["USERNAME"])

print(os.getcwd()) #현재 경로

print('--' * 4)
#time

import time

print(time.time)
print(time.localtime(time.time()))

print(time.ctime()) #간단시계

#time(형식 표현)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print('--' * 4)

#시간 간격발생
#for i in range(5):
#    print(i)
#    time.sleep(2)  #초간 멈추는 기능

#random
import random

print(random.random())
print(random.randint(1, 56))  #1~56
print(random.randrange(1, 56)) #1~55

#shuffle

d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

#choice(선택)
c= random.choice(d)
print(c)


#webbrowser

import webbrowser

webbrowser.open("http://naver.com")
webbrowser.open_new("http://naver.com") #새 창으로 열림
