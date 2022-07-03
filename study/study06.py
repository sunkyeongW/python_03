#집합 자료형(순서x, 중복x, 수정o, 삭제o)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 3, 5, 6])
d = set([1, 3, 'cute','pretty'])
e = {'foo', 'doo', 'er', 'fox'} #키값이 없을 땐 set
f ={42, 12, 3.134, ('cute', 'pretty')}

#형 변환
t = tuple(b)

print(t)

print(t[0], t[1:3])

li = list(c)

print(li)

#집합 자료형 활용
s1 = set([4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('집합')
print('교집합',s1 & s2)
print('교집합',s1.intersection(s2))
print()
print('합집합',s1 | s2)
print('합집합',s1.union(s2))
print()
print('차집합',s1 - s2)
print('차집합',s1.difference(s2))
print()
#중복 원소 확인
print(s1.isdisjoint(s2)) #교집합 확인

#부분 집합 확인
print(s1.issubset(s2)) #부분집합
print(s2.issuperset(s1)) #부분집합을 포함하는 집합
print()

#추가 & 제거

set_01 = set([1, 2, 3, 4])
set_01.add(87)
print(set_01)

set_01.remove(87)
print(set_01)

set_01.discard(8) #에러 발생 x
print(set_01)

