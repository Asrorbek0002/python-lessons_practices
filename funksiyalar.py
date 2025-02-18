# funksiyalar haqida toliq malumot
# fuksiya yaratishdan maqsad bir kodni qayta qayta yozmaslik funkiya def operatori bilan yaratiladi

# def salom_ber(): # eng sodda funksiya
#     """Salom beruvchi funsiya"""
#     print("Assalomu aleykum!!!")
#
# salom_ber()
#


# funksiyaga qiymat uzatish biz har doim funsiya qiymat uzatganimizda unga harakat nomi sozlarni berishimiz kerak

# def salom_ber(ism):
#     """Foydalanuvchiga salom beradi va ism qaytaradigan dastur"""
#     print(f"Assalomu aleykum : {ism.title()}")
#
# salom_ber('asror')
# salom_ber('abror')

# docstring haqida malumot har doim bu fuksiyada tarif berib keladi yani qanday ishlashi haqida funsiya nomi nuqta __doc__

#print(salom_ber.__doc__)

# print(salom_ber.__doc__)
# print(print.__doc__)
# print(str.__doc__)
#

# funkiyaga parametri va argumenti

# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ism va familiyasini qaytaruvchi dastur"""
#     print(f"Assalomu aleykum foydalanuvchi ismi {ism.title()} \n"
#           f"Assalomu aleykum foydalanuvchi familiyasi {familiya.title()}")
#
#
# toliq_ism('asror','abdurazoqov')
#

# buni oldini olish uchun parametrda argumetni berib ketish kerak

# def toliq_data(ism,familiya):
#     """Foydalanuvchi toliq datasi"""
#     print(f"Foydalanuvchi ismi : {ism.title()}\n"
#           f"Foydalanuvchi famiyasi : {familiya.title()}" )
#
# toliq_data(familiya='abdurazoqov',ism='asror')
#

# standart qiymat har doim qiymatlargan beriladi agar dasturchini esidan chiqib qolsa ishlatiladi

# def yoshni_kor(ism,t_yil,joriy_yil=2024):
#     """Foydalanuvchini yoshini ko'rsatuvchi dastur"""
#     print(f"{ism.title()}ning yoshi {joriy_yil-t_yil}")
#
# yoshni_kor('asror',2000,2010)
#
#
# standart qiymatni oxiriga yozish kerak bolmasa hatolik beradi


# bu yerda biz malumot qaytarishda return operatoridan foydalanamiz

# def toq_ism_yasa(ism,familya):
#     """Toliq ism qaytaruvchi funksiya """
#     toq_ism=f"{ism.title()} {familya.title()}"
#     return toq_ism
#
# talaba1=toq_ism_yasa('olimjon','oripov')
# talaba2=toq_ism_yasa('ali','valiyev')
#
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")
#

# ixtiyoriy argumentlarni berib

# def toliq_ism_yasa(ism,familya,ota_ismi=''):
#     """Toliq ismni qaytaruvchi dastur"""
#     if ota_ismi:
#         toliq_ism=f"{ism.title()} {familya.title()} {ota_ismi.title()}"
#     else:
#         toliq_ism=f"{ism.title()} {familya.title()}"
#     return toliq_ism
#
# talaba3=toliq_ism_yasa('hamidillo','olimov','hasanivich')
# talaba4=toliq_ism_yasa('asadbek','marjonov')
#
# print(talaba3)
# print(talaba4)


 # funksiyadan lugat qaytaramiz

# def avto_info(kompaniya,model,rang,korobka,yil,narh=None):
#      """Mashina haqida toliq malumot qaytarish"""
#      avto={'kompaniya':kompaniya,
#            'model':model,
#            'rang':rang,
#            'korobka':korobka,
#            'yil':yil,
#            'narh':narh
#          }
#      return avto
#
# avto1=avto_info("GM",'Malibu','Qora','Avtomat','2020')
# avto2=avto_info('GM','Jenta','Oq','Mehanika',2022,54000)
#
# print(avto1)
# print(avto2)
#
# avtolar=[avto1,avto2]
# print("Online bozordagi mashinalar ro\'yhati")
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Nomalum'
#     print(f"{avto['rang']} {avto['model']} . Narhi {narh}")
#

# to'rtburchak yuzi

# def tor_yuz(a,b):
#     """Tortburchak yuzini hisoblash"""
#     tort_yuz=a*b
#     return tort_yuz
# s=tor_yuz(10,20)
# print(s)


# doir yuzi

# def doir_yuz(Pi,r):
#     """Doiraing yuzini hisoblash"""
#     doira_yuzi=Pi*r**2
#     return doira_yuzi
#
# d=doir_yuz(3.14,10)
# print(d)


# def uchbur_yuzi(a,b,c):
#     """Uchburchak yuzini topish dasturi"""
#     uchb_yuz=a*b/2
#     return uchb_yuz
# u=uchbur_yuzi(4,10,30)
# print(u)



# def son_yig(so,sonlar):
#     """"Sonni yigindisini hisoblash"""
#     sonlar=int(input('Istalgan sonni kiriting'))
#     yigidi=so+sonlar
#     return yigidi
#
# yi=son_yig(10,20)
# print(yi)
#

# for i in range(1,11):
#     for j in range(1,11):
#         print(j,end=" ")
#     print(i)

# def fibonachi(n):
#
#     x,y=0,1
#     z=1
#     for i in range(n):
#         z=x+y
#         x=y # 0 + 1
#         y=z
#         print("z: ",z)
#
# fibonachi(20)

# arr=[2,4,5,7,9]
# count=0
# while True:
#     print(f"in our list we have the {len(arr)}")
#     qiy=int(input(arr))
#     if qiy in arr:
#         print(f"Nice, you find the {count}")
#         arr.remove(qiy)
#         if len(arr)==0:
#             print("You win: ")
#             break
#     else:
#         print("Try again: D")
#         continue










































