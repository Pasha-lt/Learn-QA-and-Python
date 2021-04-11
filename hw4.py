#HOMEWORK 4

#1
# num = input('Введите значение №1: ')
# num2 = input('Введите значение №2: ')
#
# if (num.isalpha() or num2.isalpha()):
#     print(num + num2)
# else:
#     print(int(num) + int(num2))


#2.1

def is_year_leap(year):
    if not (year % 4) and not (year % 100) and not (year % 400):
            return True
    else:
            return (False)

# a = is_year_leap(800)
# print(a)

#2.2

def triangle(a,b,c):
    if (a+b>c and a+c>b and b+c>a):
       return (True)
    else:
        return (False)
#s = triangle(4,2,3)
# print(s)

#2.3

def triangle(a,b,c):
    if (a+b>c and a+c>b and b+c>a):
        if(a==b and b==c):
            return ('Equilateral triangle ')
        elif(a==b or b==c or a==c):
            return ('Isosceles triangle ')
        else:
            return ('Versatile triangle')
    else:
        return ('Not a triangle')

# b = triangle(4,4,4)
# print(b)

#2.4
# x1 = int(input('Введите координату X1:'))
# y1 = int(input('Введите координату Y1:'))
# x2 = int(input('Введите координату X2:'))
# y2 = int(input('Введите координату Y2:'))

def distanse(x1,x2,y1,y2):

    if((x1 == x2) and (y1>y2)):
        return (y1-y2)
    if ((x1 == x2) and (y1 < y2)):
        return (y2 - y1)
    if((y1 == y2) and (x1 > x2)):
        return (x1 - x2)
    if ((y1 == y2) and (x1 < x2)):
        return (x2 - x1)
    else:
        d= (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
        return d


# res = distanse(x1,x2,y1,y2)
# print(res)

#3.1
def digit():
    while True:
        a = input('Введите число:')
        if(a.isdigit()):
            break
# digit()

#3.2
def word_space():
    while True:
        a = input('Введите слово без пробелов внутри:')
        res = a.strip()
        if(res.find(' ')  == -1 ):
            break
    return a

# word_space()

#4.0
def la (ns, s, f = 0):
    s = int(s)
    ns = int(ns)
    for i in range(ns):
        if (i==ns-1):
            if(f == 0):
                print('la' + '-la' * (s - 1), end = '.')
            elif (f == 1):
                print('la' + '-la' * (s - 1), end='!')
        else:
            print ('la' + '-la'*(s-1))
# la(3,4,1)





