# car_0={'model':'ferrari',
#        'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
#

# talaba_0={
#     'ism':'olim hakimov',
#     'yosh':20,
#     't_yil':2000
# }
# print(f"{talaba_0['ism'].title()},"
#       f"{talaba_0['t_yil']}-yilda tugulgan,"
#       f"{talaba_0['yosh']} yoshda")
#
#
# talaba_0['kurs']=4
# talaba_0['falulted']='engineering'
# print(talaba_0)
#

# bosh lug'at
# talaba_1={}
#
# talaba_1['ism']='oripov hasan'
# talaba_1['kurs']=4
# talaba_1['yosh']=25
# print(f"Talaba, {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# print(talaba_1)
#
# # qo'shish
#
# talaba_1['kurs']=2
# talaba_1['ism']='jasur halilov'
# print(talaba_1)

# ochirish

# del talaba_1['ism']
#
# print(talaba_1)


# talabalar={
#     'ali':'i phone',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nilka 3310'
# }
#
# phone=talabalar['ali']
# print(f"Alini telifoni {phone}")
#
# phone2=talabalar['orif']
# print(f"Hasanni telifoni {phone}")
#
# # shu yerda keyerror get metodi hammasini hal qiladi
#
# phone3=talabalar.get('javlon','Bunday ism mavjud emas')
# print(phone3)
# print('hello world')

# .items() methods bu yerda biz lugatdagi kalit va qiymatlarni bilmasak shu metodan foydalaniladi

# talaba_0={
#     'ism':'Olimjon',
#     'familya':'Hasanov',
#     'yosh':24,
#     'fakulted':'informatika',
#     'kurs':4
# }
#
# print(talaba_0.items())
#
# for key,val in talaba_0.items():
#     print(f"Bu yerda kalit so'zlar>>> {key}")
#     print(f"Bu yerda val so\'zlar>>>{val}")


# telefonlar={
#     'ali':'Iphone',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
# }

# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telifoni {q}")


# .keys() metodi lugatdagi faqat keyslar uchun ishlatiladi
# mahsulotlar={
#     'olma':1000,
#     'olcha':2000,
#     'nok':3000,
#     'hurmo':4000
# }
# #print(mahsulotlar.keys())
#
# # for i in mahsulotlar.keys():
# #     print(i.title())
#
# bozorlik=['olma','anor','olcha','nok','xurmo']
#
#
# for i in mahsulotlar.keys():
#     if i in bozorlik:
#         print(f"{i.title()} {mahsulotlar[i]} so\'m ")
#
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do\'konga {buyum.title()} ham olib keling ")
#

# .values() methodi lug\'at ichidagi qiymatlarni chiqaradi

# print(telefonlar.values())
#
#
# print("Foydalanuvchilar quyidagi telifonlarni ishlatadi")
# for tel in telefonlar.values():
#     print(tel)




# telefonlar={
#     'ali':'Iphone',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'Nkia 3310',
#     'hamida':'galaxy s9',
#     'mariam':'huawei p30',
#     'toxir':'iphone x',
#     'umar':'iphone x'
# }
#
# print("Foydalanuvchilar quyidagi telni ishlatadi>>>")
# for i in telefonlar.values():
#     print(i)
#
# # biz set yordamida bir xil elemetlarni olib tashlashni o\'rganiash
#
#
# print("Ajratilgan yani hammasidan bitta olinadi")
# for i in set(telefonlar.values()):
#     print(i)

# car0={
#     'model':'Lacetty',
#     'rang':'oq',
#     'yil':2018,
#     'narh':13000,
#     'km':50000,
#     'korobka':'avtomat'
#
# }
#
# car1={
#     'model':'nexia3',
#     'rang':'qora',
#     'yil':2015,
#     'narh':9000,
#     'km':89000,
#     'korobka':'mehanika'
#
# }
#
#
# car2={
#     'model':'gentra',
#     'rang':'qizil',
#     'yil':2019,
#     'narh':15000,
#     'km':20000,
#     'korobka':'mehanika'
# }

# car=car0
# print(f"{car['model'].title()},"
#       f"{car['rang']} rang, {car['yil']}-yil, ${car['narh']} narhda "
#       f"{car['km']} km yurgan va {car['korobka']} korobka")
#
# car=car1
# print(f"{car['model'].title()},"
#       f"{car['rang']} rang, {car['yil']}-yil, ${car['narh']} narhda "
#       f"{car['km']} km yurgan va {car['korobka']} korobka")
#
#
# car=car2
# print(f"{car['model'].title()},"
#       f"{car['rang']} rang, {car['yil']}-yil, ${car['narh']} narhda "
#       f"{car['km']} km yurgan va {car['korobka']} korobka")

#cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang']} rang, {car['yil']}-yil, ${car['narh']} narhda "
#           f"{car['km']} km yurgan va {car['korobka']} korobka")
#

# print(cars[0]['model'])
# print(cars[1])
# print(cars[2])

#print(f"{cars[2]['model']} {cars[2]['rang']}")


# malibus=[]
# for i in range(10):
#     new_car={
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'korobka':'avto'
#     }
#
#     malibus.append(new_car)
# #print(malibus)
#
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
#     print(malibu)
# for malibu in malibus[3:6]:
#     malibu['rang']='oq'
#     print(malibu)
# for malibu in malibus[6:]:
#      malibu['rang']='qora'
#      malibu['korobka']='mehanika'
#      print(malibu)
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#         print(malibu)
#     else:
#         malibu['narh']=35000
#
#         print(malibu)
#

# dasturchilar={
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','hph'],
#     'mariam':['c++','c#']
# }
#
#
# for key , values in dasturchilar.items():
#     print(f"{key.title()} quyidagi dasturlash tillarni biladi {values}" , end='  ')
#     for value in values:
#         print(value.upper(),end='  ')


hamkasblar={
     'ali':{'familya':'valiyev',
            'yil':1995,
            'malumoti':'oliy',
            'tillar':['python','c++']},


     'vali':{'familya':'aliyev',
             'yil':2001,
             'malumoti':'orta-mahsus',
             'tillar':['html','css','js']},

     'husan':{'familya':'husanov',
              'yil':1999,
              'malumoti':'mahsus',
              'tillar':['python','php']}
                                        }
for key , values in hamkasblar.items():
    print(f"{key.title()} {values['familya'].title()} "
          f"{values['yil']}-yil tug\'ulgan va malumoti {values['malumoti']} "
          f"Quyidagi dasturlash tillarni bildi",end=' ')
    for til in values['tillar']:
        print(til.upper(),end=' ')




















