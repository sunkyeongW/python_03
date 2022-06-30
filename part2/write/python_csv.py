import csv
import resource

#예제1
with open('./resource/test1.csv', 'r', encoding= 'UTF-8') as a:
    reader = csv.reader(a)
    next(reader)   #header skip
 
    print(reader)
    print(type(reader))
    print(dir(reader))

    print()
    
    for c in reader:
        #print(c)
        print('-'.join(c))
    print()

print('----' * 10)
#예제2
with open('./resource/test2.csv', 'r', encoding= 'UTF-8') as a:
    reader = csv.reader(a, delimiter='|')

    for c in reader:
        print(c)

print('----' * 10)
#예제3
with open('./resource/test1.csv', 'r', encoding= 'UTF-8') as a:
    reader = csv.DictReader(a)

    for i in reader:
        for k,v in i.items():
            print(k,v)
        print('------' * 6)

#예제4
w = [[1, 2, 3], [4, 5,6], [7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18],[19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8') as b:
    print(dir(b))
    wt = csv.writer(b)
    print(dir(wt))

    for v in w:
        wt.writerow(v)


#예제5
with open('./resource/write2.csv', 'w', encoding='UTF-8') as b:
    fields = ['One', 'Two', 'Three']
    wt = csv.DictWriter(b,fieldnames=fields)
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})