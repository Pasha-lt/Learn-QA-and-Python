#HOMEWORK №3

# №1
# def prnt():
#     str = input('Введите строку: ')
#     print (f'{str[2]}', str[-2], str[:5], str[:-2],
#         str[: : 2], str[: : 1],str[1: : 2],
#         str[ : : -1],str[ : : -2],str[-2:1:-1],
#        len(str),
#         sep='\n')
# res = prnt()
# print (res)

# №2
def strdiv():
    import math
    str = input('Введите строку: ')
    n = math.ceil(len(str)/2)
    str1 = str[:n]
    print(str1)
    str2 = str[n:]
    print(str2)
    res = str2+str1
    print(res)
    return res
#strdiv()

#3

#3.1
def loop():
    n = 0
    while n <= 10:
        print(n)
        n += 1
#loop()

#3.2
def loop(n):
    #n = 20
    while n > 0:
        print(n, end=' ')
        n -= 1
#loop(20)

#3.3
def loopdiv(n):
    count = 0
    while n >= 1:
        if (n%2==0):
            count += 1
        n = n / 2
    return count
# res = loopdiv(16)
# print(res)

#4

#4.1

def dels(mas):
    i = 0;
    count = len(mas)
    while (i < count):
        print(mas[0])
        mas.pop(0)
        i+=1
    return(mas)
# mas = [1,2,3,4,5,6,7,8,9]
# r = dels([1,2,3,4,5,6,7,8,9])
# print(r)

#4.2

def delstr(str):
    i = 0;
    count = len(str)
    while (i < count):
        print(str[i])
        newstr = str[i:-1]
        # print(newstr)
        i+=1
    return(newstr)
# r = delstr('123456')
# print(r)

#4.3

def del_min(mas):
    while len(mas)>0:
        min = mas[0]
        for i in range(len(mas)):
            if(min>mas[i]):
                min = mas[i]
        print('Мінімальне:',min)
        mas.remove(min)
        print ('Перше',mas[0])
        print(mas)
# mas = [1,5,2,3,4,8,6,7,10,9]
# del_min(mas)

#4.4

def hw_4_4(str):

    str = str + ' '
    dict = {}

    counter = 1
    iter = len(str)

    #dict[str[0]] = counter

    for i in range(iter-1):
        if (str[i] == str[i+1]):
            counter +=1
        elif(str[i] != str[i+1]) or (i==iter-1):
            dict[str[i]] = counter
            counter = 1

    val = []

    for key in dict:
        val.append(dict[key])

    print(dict)
    print(val)

    res = val[0]
    for key in val:
        if res < key:
            res = key

    print(res)
    return res

# str ='122334555555'
# hw_4_4(str)

#5
def strl(str):
    counter = 1
    str1 = str.split(' ')

    newstr =[]
    for key in str1:
         newstr.append(key.strip(')(.,!'))

    print(newstr)
    print (len(newstr))
    b= newstr.sort()
    print(newstr)

# str = "we! are ()not. what, we should be! .,a!!!!!"
# strl(str)

#5_2

def count_word(str):

    dict={}
    str1 = str.split(' ')
    newstr =[]
    for key in str1:
        newstr.append(key.strip(')(.,!').lower())
    print(newstr)
    count = 1
    for i in range(len(newstr)):
        dict[newstr[i]] = newstr.count(newstr[i])
    print(dict)

str = "we! are ()not. AGHG what, we should be! .,a!!!!! a a"
count_word(str)