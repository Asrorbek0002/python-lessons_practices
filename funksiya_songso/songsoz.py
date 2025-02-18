"""
lambda yohud nomsiz funksiya
nomsiz funksiya quydagicha yaratiladi
lambda argument:infoda
bu lambda funksiyasi istalgancha argument qabul qilishi mumkin lekin funksiya badanida bitta infoda boladi
"""
from colorsys import yiq_to_rgb

# import math
# uzunlik=lambda pi,r:2*pi*r
# print(uzunlik(math.pi,10))

# product=lambda x,y:x*y
# print(product(4,6))


# def daraja(n):
#     return lambda x:x**n
#
# kvadrat=daraja(2)
# kub=daraja(3)
#
# print(f"3-ning darajasi {kvadrat(3)} ga, {kub(3)} ga teng")
#


"""
map() funksiyasi argument sifatida funksiya , ikkinchisiga itreble typdagi argumentni hisobida boldadi

"""
# from math import sqrt
#
# sonlar=list(range(11))
# ildizlar=list(map(sqrt,sonlar))
#
# print(ildizlar)

# sonlar=list(range(10))
# def kvadrat(x):
#     """Berilgan soni darajasini hisoblaydigan dastur"""
#     return x*x
#
# print(list(map(kvadrat,sonlar)))
#
# sonlar=list(range(10))
# print(list(map(lambda x:x*x,sonlar)))

# kvadrat=[]
# for son in list(range(11)):
#     kvadrat.append(son**2)
#
# print(kvadrat)
#
# a=[2,5,4]
# b=[2,5,8]
# a_plus_b=list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)
#

# ismlar=['asror','ahmad','ali','ayubxon','olim']
# print(list(map(lambda matn:matn.upper(),ismlar)))


"""
filter() funksiyasi ikki argument qabul qiladi funksiya va iterable type qabul qiladi

"""
#import random as r

# sonlar=r.sample(range(100),10)
#
# def juftmi(x):
#     """"x juft bolsa true , aks holda false qaytaradi"""
#     return x%2==0
#
# juft_son=list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_son)
#

# sonlar=r.sample(range(100),10)
#
# juft_son=list(filter(lambda x:x%2==0,sonlar))
#
# print(juft_son)
# print(sonlar)

# mevalar=['olma','anor','olcha','gilos','behi','o\'rik','tarvuz','qovun','banan','shaftoli']
#
# print(list(filter(lambda meva:meva.startswith('o'),mevalar)))
#
# print(list(filter(lambda meva:len(meva)>=5,mevalar)))
#
# print(list(filter(lambda meva:meva.startswith('o') and meva.endswith('a'),mevalar)))

"""
reduce funksiyasi ham ikki argument qabul qiladi funksiya iterable type qabul qiladi 
"""

from functools import reduce

# numbers = [1, 2, 3, 4, 5]
#
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  # Natija: 15
#

# sonlar=list(range(1,5))
# qosh=reduce(lambda x,y:x*y,sonlar)
# print(qosh)
#
#










