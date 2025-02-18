# moslashuvchan funkiya funkiyamiz bir nechta argumentlar qabulsayu biz argumentlar sonini bilmasak bizda istalgancha argument qabul qiladigan funksiya yaratishimiz mumkin

# *args usuli biz funkiyamizda argumentlar soni noaniq bolsa yu va bizni argument yagona qiyamat uzatilsa funkiya ichidagi argumentga * qoymamiz

# def summa(*sonlar):
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
#
# ikki=summa(1,50,3,200)
# print(ikki)
#


# def summa(*sonlar):
#     """"Sonlar yigindisini qaytarar ekan"""
#     return sum(sonlar)
#
# uch=summa(3,45,5,1,5,47,1,)
# print(uch)

# ager funkiya bir nechta argument qabul qilsa biz kvargizni oxirida qollashimiz kerak

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# tor=summa(5,54,5,5)
# print(tor)
#

# yoqoridagi funkiyamiz kamida ikkita argument qabul qilishi kerak


""""
*kwargs usuli bu yerda kaliq so'z qiymat juftlgi shaklida keldi biz uni nechta parametr ekanligini bilmasak shu usuldan foydalanamiz

"""
"""
**kwargs usuli key word value arguments
"""
def avto_info(kompanya,model,**malumotlar):
    malumotlar['kompanya']=kompanya
    malumotlar['model']=model
    return malumotlar

avto1=avto_info("GM","Malibu",rang='oq',yil=2021)
avto2=avto_info('kia','k5',rang='qora',yil=2020)

print(avto1)
print(avto2)

"""
agar biz qoshimcha qiymatlarni qoshmoqchi boldak key='value' deb yozish kerak

"""





























