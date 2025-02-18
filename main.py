# modulni chaqirib olish modul ichidagi istalgan funkiyada murjat qilishi uchun import file nomi
"""
import file_name
file_name.functoin_name()

"""

# import avto_info_mod
#
# avto=avto_info_mod.avto_info('GM','Malibu','qora','avtomat',2020,40000)
# avto_info_mod.info_print(avto)


# import modul nomi bir marta yoziladi

# modulga qisqa nom berish bu as yordamida yoziladi va siz modulga qisqa nom berganizda shunga oxshash funksiya va ozgaruvchi bolishiga amin boling

# import avto_info_mod as aim
#
# avto=aim.avto_info('GM','Malibu','qora','avtomat',2020,40000)
# aim.info_print(avto)


# modul ichidan malum funksiyalarmi ko'chirib olish

""""
from avto_info_mod import avto_info, info_print, avto_kirit
bu yerda biz endi modul nomini kiritishimiz  mumkin  emas togridan togri murojat qilishimiz mumkin
"""

# from avto_info_mod import avto_info, info_print
#
# avto=avto_info('GM','Malibu','qora','avtomat',2020,40000)
# info_print(avto)
#

"""
funksiyalarga qisqa nom berish 
"""
# from avto_info_mod import avto_info as ainfo, info_print as iprint
#
# avto1=ainfo('Kia','K 5','oq','avtomat',2024,50000)
# iprint(avto1)
#

"""
modulni ichida hamma funkiyani chaqirish * shu belgi bilan chaqiriladi 
agar siz bu belgi bilan yozsangiz modul chida 100 lab funksiyalar bolishi mumkin shu paytda bir biriga halaqt berishi mumkin
"""

#from avto_info_mod import *

"""
modulda ozgaruvchi saqlash funsiyani qanday qilib chaqirsangiz ozgaruvchini ham shunday chaqirishingiz mumkin
"""

# from avto_info_mod import sonlar
#
# for son in sonlar:
#     print(son,end=' ')
#


# python modular

# math moduli matematik hisob kitoblarni qiladi
import math

# sqrt(x) bu funkiya sonni ildizini hisoblaydi

# x=400
# print(math.sqrt(x))

# pow(x,y) sonni darajasini hisoblaydi

#print(math.pow(2,20))

# from math import pi
# print(pi)

# logarifm log2() va log20()

# print(math.log2(20))
# print(math.log10(100))

# random moduli bu tasodifiy sonlar bilan ishlash uchun boy

import random as r

#  randint(x,y) bu model shu oraliqdagi soni qaytaradi

# son=r.randint(10,20)
# print(son)

# choice bu x ning ichidan tasodifiy qiymatlarni qaytarivchi modul bu yerda x list matn bolishi kerak

# ismlar=['ali','hasan','botir','vali','anvar']
# ism=r.choice(ismlar)
# print(ism)
# print(r.choice(ism))


# sonlar=list(range(1,50,5))
# son=r.choice(sonlar)
# print(son)


 # shuffle(x) funkisyasi har doim x elementidagi sonlar har hil tartibda tartiblaydi

# x=list(range(110))
# print(x)
# r.shuffle(x)
# print(x)
#


