print('---'* 5)
print('list형')
Name = ['Star', 'Sun', 'Da'] #문자열 리스트
Age = [17 , 26, 30] #숫자형 리스트
print('Name :', Name)
print('Age :', Age)
print('Age 순서 :', Age[0]) #0부터 순서 시작
print('len :', len(Name)) #갯수는 1부터 시작
print('---'* 5)
print('모듈 사용')
print('minimalist :',min(Age))
print('maximalist :',max(Age))
print('합계 :',sum(Age))
print('---'* 5)
print('통계(statistics) 사용')

import statistics

print('평균값 :', statistics.mean(Age))
print('높은 중앙값 :', statistics.median_high(Age))
print('---'* 5)
print('random 사용')

import random

print('추첨 -', random.choice(Name))
