# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:21:08 2024

@author: Asilbek
"""

# Bizga malumki dictionary sozi bilamiz kalit sozvaunga tarif qaysiki bu qiymat deb nomlanadi
#talaba_0={
#    "ism":"alijon",
 #   "familiya":"shamshiyev",
 #   "yosh":22,
  #  "fakultet":"matematika",
  #  "kurs":4
#    }
#  biz hech qachon bilmaymiz ichida nechta metod borligini va qaysi birini chiqarishni shunda biz bir nechta metodan foydalanamiz ulardan biri 
# items() metodi ingliz tilidan elementlar deb tarjima qilinadi 
#print(talaba_0.items())
# qarang bu juda ham chioyli emas shu da biz for tsikli dan foydalanamiz shunda u chiroyli chiqishi mumkun
#for key, value in talaba_0.items(): 
 #   print(f"Kalit  {key}")
  #  print(f"Qiymat  {value}")
#telefonlar={
#    "ali":"iphone x",
#    "vali":"galaxy s9",
#    "olim":"mi 10 pro",
#    "orif":"nokia 3311",
#    "hamida":"galaxy s9",
#    "mariyam":"huawei p30",
#    "tohir":"iphone x",
#   "umar":"iphone x"
#    }
#for k, q in telefonlar.items():
# .Keys()metodi bu yerda faqat kalitlarni olish uchun foydalaniladi bizga malumku
#mahsulotlar={
#    "olma":10000,
#    "anor":20000,
#    "uzum":40000,
#   "anjir":25000,
#    "shaftali":30000
#   (mahsulotlar.keys())   
#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot.title())
#print("Do'kondagi mahsulotlar:")
#for mahsulot in mahsulotlar:
  #  print(mahsulot.title())
#bozorlik=["anor","uzum","non","baliq"]
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, dokonizga {buyum} ham olib keling ")
# biz bu yerda bilamiz keys() metodidan foydalanamiz va bunda har doim ular har xil bo'lib chiqadi biz shu yerda sorted() metodidan foydalanamiz har doim bu metod yordam beradi tartblashga 
#print("Do'knimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())
# values()  metodi bizga malumki bizdan so'ralishi mumkun endi qiymatni chiqarish biz 
#print(telefonlar.values())
#print("foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
#for tel in telefonlar.values():
#    print(tel)
# set() set funksiyasi har doim takrorlangan so'zlarni takrorlamaslikka huquq beradi
#print("foydalanuvchilar quyidagi telifonni ishlatishadi: ")
#for tel in set(telefonlar.values()):
#    print(tel)
# set bu  yerda bir malumot turi hisoblanadi
#toys={"ball","car","lamp","ball","bear","car","car"}
# agar biz har doim {} so'zi ishlatsak si ichdan saralaboladi
 
      
#hiyobonlar={
#    "amir temir":"skver",
#    "g'ofur g'ulom":"bog'i",
#    "yunsobod":"ashqabot",
#    "alisher navoiy":"toshkent sity",
#     "milliy bog'":"majik",
#     "chosu":"muzey",
#     "uzgaradok":"taklaba savdo",
#     "yo'l":"g'alaba bog'i",
#     "tdau":"telivishka",
#    "g'azalkent":"chortoq"
#     }
#print(hiyobonlar.keys())
#for hiyobon in sorted(hiyobonlar.keys()):
 #   print(hiyobon.title())
#print(hiyobonlar.values())
#for hiyobon in sorted(hiyobonlar.values()):
 #   print(hiyobon.title())    
#print(hiyobonlar.items())
#for key, value in sorted(hiyobonlar.items()):
#    print(f"Key {key}")
#    print(f"Value {value}")
#davlatlar={
#    "uzbekistion":"toshkent",
#    "rassia":"moskua",
#    "amerika":"vashington",
#    "buyuk biritania":"londom",
#    "argentia":"benus airs",
#    "yaponia":"tokio",
#    "xitoy":"pekin"}    

#print("Mamlakatlarning nomi:")   
#for country in sorted(countries.keys()):
#    print(country.title())
#print(input("Mamlakatlar nomi:>>>"))
#for country in sorted(countries.values()):
#    print(country.title())
#country=input("istalgan mamlakatni kiriting:>>>")
#if country in countries:
#    print(countries[country])
#else:
#    print("Bunday mamlakat mavjud emas")
#print(countries.get(country,"Bunday mamlakat mavjud emas"))

#davlat=input("Qaysi davlatni poytaxtini bilishni istaysiz?:>>.")
#if davlat in davlatlar:
 #   print(davlatlar[davlat])
#else:
#    print("Bunday mamlakat mavjud emas")    
#davlat=input("Qaysi davlatni poytaxtini bilishni hohlaysiz?:")
#print(davlatlar.get(davlat,"Bunday davlat mavjud emas"))
   
#menu={
#    "choy":10000,
#    "salat":20000,
#    "non":5000,
#    "osh":7000,
#    "sho'rva":30000,
#    "norin":40000,
#    "qozon kabo":50000,
#    "english food":60000,
#    "italian food":70000,
#    "makaron":100000
#    }
#print("3 ta taomga buyurtma bering: ")
#buyurtmalar=[]
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-taom:").lower())


#for buyurtma in menu:
#    print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#else:
#    print(f"kechirasiz, bizda {buyurtma} yo'q")
#print("Do'kondagi mahsulotlar:")
#for taom in taomlar.keys():
#    print(taom)
#print("Do'kondagi taomlar:")
#for taom in taomlar.values():
#    print(taom)
#food=["osh","polov","sumalak","chuchvara","lovya"]
#for taom in taomlar:
#  if taom in food:
 #     print(f"{taomlar.title()}  {taomlar[taom]} so'm")
     
menu={
      "osh":20000,
      "lag'mon":22000,
      "choy":5000,
      "shashlik":12000,
       "non":4000,
       "somsa":6000,
        "tabaka":15000}
print("3 ta taom buyurtma bering")
buyurtmalar=[]
for n  in range(3) :
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
 
for buyurtma in buyurtmalar:
    if buyurtma in menu:    
        print(f"{buyurtma.title()}  {menu[buyurtma]} so'm")
else:
    print(f"Kechirasiz, bizda {buyurtma} yo'q")









