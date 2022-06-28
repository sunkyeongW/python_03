import pandas
house = pandas.read_csv('100BT.csv')
print(house)
print(house.head) #앞쪽에만 있는 데이터만 출력
print(house.head(2)) #앞쪽에만 있는 데이터 2개만 출력
print(house.describe()) #통계 데이터