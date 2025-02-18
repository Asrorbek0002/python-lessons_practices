# -> build in datatypes

# string matn
#a='asror'


# numeric
#s=4
#d=2.3
#f=log10

# sequence

# a=[1,2,3,3,3,]
# d=(1,6,2,8,2)
# c=range(10,100)

# mapping

#dict={'ism':'ali',
#      'yil':1999}

# set

#set={1,5,6}
# frozenset
#a=frozenset({'phone','watch'})
# bool true and false

#ism='ali'
#if ism=='vali':
#    print(ism)


# Nonetype

# sonlar=[1,2,5,8,6,5]
#
#a=None

# bites ,bytearray

#a=b'asror'

#b=bytearray(10)




# ->1 control flow

# sonlar=list(range(1,5+1))
# for son in sonlar:
#     print(son,end=' ')

# ->2 decorators

# decorator bu funkiya hisoblanadi va ni vazifasi funkiya qabul qiladi va har xil opiratsiyalar bajarish mumkin
# decorator odatda @ yordamida ishlatiladi va u nested funkiya bilan ishlaydi


# def decorator(funktsiya):
#     def sonlar(*args):
#       return funktsiya(*args)
#
# son=decorator(14,14,54,54)

# import decorator
# @decorator
# def salom_ber(ism):
#     print(f"Salom, {ism}!")
#
# salom_ber("Asror")
# @decorator
# def my_function():
#     print("Hello!")


# -> 3 varibles and datatypes

# varible bu o'zgaruvchi ichida datatypeslarni qabul qoiladi list ,dict...
# ikki xil datatypeslar bor o'zgaradigan va o'zgarmaydigan
# o'zgaradigan , list ,dict, set
# o'zgarmaydigan  , string  , float , integer , tuple, complex, bool

# -> operators and expressions

# operator malum bir vazifani bajaradi operatsiya bajaradi for , while , in ,if va
# ikkovini farqi shunda expression bu biror qiymat hisoblaydigan va  qaytaradigan kod hisoblanadi va Expressionlar operatorlar, qiymatlar, qaytaradi
#

#->5 strings

#ism='asror'
#print(f"{ism} ")


# ->6 lists

# sonlar=[1,2,3,4,5,6]
#
# sonlar.append(10)
# print(sonlar)
#
# sonlar.remove(5)
# print(sonlar)

# -> tuples
"""
listni ichiga argumet qoshamiz , olib tashlaymiz, keamiz"""
#ismlar=['ali','vali','asror']

"""
tuple da ozgartira olmaymiz elemetlarni boshqa hamma amalni bajara olamiz list kabi
qochonki ozgatirish kiritmasak shunda foydalanamiz"""
#ismlar_tuple=tuple(ismlar)


# -> 8 dictionary

# talaba={
#     'ism':'asror',
#     'fami':'abdurazoqov'
# }
# talaba['kurs']=4



#-> 9 sets
"""
set separet qiladi birxillarini olib tashlaydi"""

#set_sonlar=[1,3,5,78,41,8,58414,85481,241,16,1,2,3,5,4,79,4,2,1]
#set_op=set(set_sonlar)


# -> 10 list comprehention

# phones=[]
#
# phones.append('sumsang a 56')
# print(phones)
#

# ->11 break and continue

# for son in range(1,10):
#     if son==5:
#         continue
#     elif son==8:
#         break


# -> function
"""
mahsus vazifani bajaradi va codi yozishda yengillik olib keladi"""

# def toliq_ism(ism,familya):
#     toliq=f"{ism} {familya}"
#     return toliq
# print(toliq_ism('asror','abdurazoqov'))

# ->13 modul import

#from lesson_4 import son_top

# ->14 map(),filter(), reduce()


# map(functio,iterable)
#filter(argumet)  # true ,false
#reduce(argumet) # songa oxiri qo'shadi



























