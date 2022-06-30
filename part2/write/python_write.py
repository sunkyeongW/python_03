print('---' * 10)
#파일 읽기(Read)

f = open('C://PYTHON_03//part2//write//resource//it_news.txt', 'r', encoding= 'UTF-8')
f = open('.//resource//it_news.txt', 'r', encoding= 'UTF-8')


#속성 확인
print('속성 확인')
print(dir(f))

print('---' * 10)

#인코딩 확인
print('인코딩 확인')
print(f.encoding)

print('---' * 10)


#파일 이름
print('파일 이름')
print(f.name)

print('---' * 10)

#모드 확인
print('모드 확인')
print(f.mode)
print()
cts = f.read()
print(cts)

print('---' * 10)

#반드시 close
f.close()

#with문
with open('./resource/it_news.txt', 'r', encoding= 'UTF-8') as A:
    c = A.read()
    print(c)
    print(iter(c))
    print(list(c))

print()
print('---' * 10)

#예제3
with open('./resource/it_news.txt', 'r', encoding= 'UTF-8') as A:
    c = A.read(20)
    print(c)
    c = A.read(20)
    print(c)
    c = A.read(20)
    print(c)
    A.seek(0,0)
    c = A.read(20)
    print(c)

print()
print('---' * 10)

#예제4(readline)
with open('./resource/it_news.txt', 'r', encoding= 'UTF-8') as A:
    line = A.readline()
    print(line)
    line = A.readline()
    print(line)
    line = A.readline()
    print(line)
print()
print('---' * 10)

#예제5(readlines)
#readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding= 'UTF-8') as A:
    lines = A.readlines()
    print(lines)
    print('---' * 10)
    for c in lines:
        print(c, end='')

print()
print('---' * 10)

# 파일 쓰기(write)

with open('./resource/contents1.txt', 'w') as B:
    B.write('I love you\n')

with open('./resource/contents1.txt', 'a') as B:
    B.write('I love Star\n')

#writelines : 리스트 -> 파일

with open('./resource/contents2.txt', 'w') as B:
    list = ['Orange\n', 'Apple\n', 'Banana\n']
    B.writelines(list)

#예제4 파일로 출력

with open('./resource/contents3.txt', 'w') as B:
    print('test 1', file= B)
    print('test 2', file= B)
    print('test 3', file= B)
   