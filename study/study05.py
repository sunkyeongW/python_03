#사전 자료형(순서x, 키 중복x, 수정o, 삭제o)

a = {}
b = {'Name':"Won", 'Birth':'971109'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name':'Star',
    'City' : 'Seoul',
    'Age' : 17,
    'Grade' : 'S'
}

e = dict(
    Name = 'Star',
    City = 'Seoul',
    Age = 17,
    Grade = 'S'
)



print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)

print(b['Name'])
print(b.get('Name'))
print(b.keys())
print(b.values())
print(b.items())

#추가
a['adress'] = 'Seoul'
b['Goodboy'] = 'Cute'
print(a)
print(b)

print(b.pop('Name'))
print(b)

print(e.pop('Name'))
print(e)

#in
print('Birth' in b)
print('Birth' in a)

#수정
b['Birth']= '060705'
print(b)

b.update(Birth='971109')
print(b)

temp = {'Favorite' : 'Candy'}

c.update(temp)
print(c)