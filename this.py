# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:21:03 2024

author: Asilbek
"""

# 14-lesson dictionary (lug'at)
#Har bir malumot ikki qismdan iborat bizga malumki birinchisi KALIT SOZ IKKINCHISI kalit so'zga tog'ri keluvchi qiymat bu kalit so'z juftligi deb ataladi ingliz tilida bu Key-value pair deb ataladi
# For example=>1
#car_0={"model":"ferrary","rang":"qizil"}# bu yerda kalit so'z rang va qiymati qiz bo'ladi
#print(car_0["model"])
#print(car_0["rang"])

# For example =>2
#en_uz = {"apple":"olma","apricot":"o'rik","banana":"bana"}
#mevalar={"olma":10000,"tarvuz":8000,"qovun":10000}#kalit mevani nomi va qiymat mevani uning narhida 
#print(f"Olma narhi {mevalar['olma']} so'm")
#talaba_0={"ism":"asror abdurazoqv","yosh":20,"t_yil":2000}
#print(f"{talaba_0['ism'].title()},\
    # {talaba_0['t_yil']}-yilda tug'ilgan,\
    #  {talaba_0['yosh']} yoshda")

#talaba_0={"ism":"asrorxon abdurazoqov","t_yil":2000,"yosh":20}
#print(f"{talaba_0['ism'].title()},\
  #    {talaba_0['t_yil']}-yilda tug'ulgan,\
 #     {talaba_0['yosh']} yoshda")
#  Yangi kalit so'z va qiymat qo'shish
#talaba_0["kurs"]=4
#talaba_0["fakultet"]="informatika"
#talaba_0["ism"]="abdulloh"# bizga agar kalit nomini o'zgartirish kerak bo'lsa biz shu yerdan o'zgartiramiz
# Bo'sh lugat bizga bo'sh lug'at berilgan bo'lsa biz uni to'ldiramiz 
#talaba_1={}
#talaba_1['ism']="qobil rasulov"
#talaba_1['kurs']=3
#talaba_1['yosh']=20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# Qiymatni yangilash 
#talaba_1['kurs']=4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# Kalit so'z-qiymatni o'chirib tashlash
# del bilan tanishganmiz
#talaba_0={"ism":"murod olimov","yosh":20,"t_yil":2000}
#del talaba_0["yosh"]
#print(talaba_0)

# Lug'atlarni bir nechta qatorda yozish
#telefonlar={
   # "ali":"iphone x",
  #  "vali":"galaxy s9",
 #   "olim":"mi 10 pro",
 #   "orif":"nokia 3310",
#    "asror":"pixel 3xl"
   # }
# get() metodi KeyErrorni oldini olish uchun biz get metodidan foydalanamzm
#phone=telefonlar.get("hasan" ,"Bunday ism mavjud emas")
#print(phone) 
#meva=en_uz.get("pineapple", "Bunday meva mavjud emas")
#print(meva)
#phone=telefonlar.get("hasan", "Bunday ism mavjud emas")
#print(phone)




 

    

    












