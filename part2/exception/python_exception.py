#SyntaxError : 문법 오류

#print('error)
#print('error'))


#NameError : 참조 없음

#a = 10
#b = 15
#print(c)


#ZeroDivisionError : 0으로 값이 정해지지 않을 때

#print(100 / 0)


#IndexError

#x = [10, 30, 50]
#print(x[4])
#print(x.pop()) -> 더이상 .pop할 값이 없을 때 오류 발생.



#AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용할 때

#import mdo
#print(mdo.time)


#KeyError

#dic = {'name': 'Won', 'Age': 26, 'City': 'Seoul'}
#print(dic['hoppy'])
#print(dic.get('hobby')) -> None으로 표시.


#ValuesError

#x = [10, 30, 50]
#x.remove(70)
#print(x)



#FileNotError

#f= open('text.txt') -> 파일이 지정 위치에 존재하지 않을 때


#TypeError : 자료형에 맞지 않은 연산을 수행 할 때
#x = [1, 2]
#y = (1, 2)
#z = 'test'

#print(x + y)
#print(x + z)
#print(y + z)


#예외 처리 예제

name = ['Kim', 'Won','Yoon']

#예제1
#try:
#    z = 'x'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
#except ValueError:
#    print('Not Found it! - Occurred ValueError!')
#else:
#    print('OK! else')

#print()

#예제2
#try:
#    z = 'x'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
#except Exception:    #예외는 잡지만 구체적인 예외는 잡아주지 못함.
#    print('Not Found it! - Occurred ValueError!')
#else:
#    print('OK! else')

#print()


#예제3
#try:
#    z = 'x'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
#except Exception as e:    #예외는 잡지만 구체적인 예외는 잡아주지 못함.
#    print(e)
#    print('Not Found it! - Occurred ValueError!')
#else:
#    print('OK! else')
#finally:
#    print('OK! finally') #예외가 발생하든 안하든 명령이 실행.
#print()


#예제4
#예외 발생 : raise
#raise 키워드로 예외 직접 발생
try:
    a = 'd'
    if a == 'Won':
        print('Found it!')
    else:
        raise ValueError
except ValueError:
    print('catch')
else:
    print('ok')
print()