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
#my_family={"otam":"abdurazoq","t_yil":1950,"shahar":"Farg'ona viloyatida tug'ulgan"}
#print(f"Mening otam {my_family['otam'].title()},\
#      {my_family['t_yil']} da ,\
 #         {my_family['shahar']}")
#print(f"Mening buvim {my_family_2['buvim'].title()},\
#      {my_family_2['t_yil']},\
#       {my_family_2['shahar']}")       

#my_life={"ism":"Asror","t_yil":2000,"shahar":"Kokond shaharida tug'ulganman"}
#print(f"Mening ism {my_life['ism'].title()},\
 #     {my_life['t_yil']},\
 #      {my_life['shahar']}")      
#lovely_food={"my father":"osh",
 #            "my mother":"norin",
 #            "my older brother":"qozon kabob",
 #            "my younger brother":"seafood",
 #            "I":"english food"}
#print(f"Mening dadamning sevimli taomi {lovely_food['my father'].title()},\
 #     mening onamning sevimli taomi {lovely_food['my mother']},\
  #        mening kichik katta ukaming sevimli taomi {lovely_food['my older brother']},\
   #           mening kichik ukamning sevimli taomi {lovely_food['my younger brother']},\
   #               mening sevimli taomim {lovely_food['I']}")          
my_knowlege={"string":"matin",
             "integer":"butun son",             
             "title()":"bosh harif katta bilan",
             "if":"agar","else":"aks holda",
             "elif":"agar,aks holda",
             "float":"o'nli sonlar",
             "upper":"hammasi kata bilan",
             "lower":"hammasi kichik bilan",
             "list":"ro'yhat",
            "del":"o'chirish "}   
print(f"I know {my_knowlege['string']},\
      {my_knowlege['integer']},\
      {my_knowlege['float']},\
      {my_knowlege['title()']},\
      {my_knowlege['if']},\
       {my_knowlege['elif']}'\
         { my_knowlege['upper']},\
          {my_knowlege['lower']},\
              {my_knowlege['list']},\
                  {my_knowlege['del']} ,Bunday so'z mavjud emas " )             
      
royhat=my_knowlege.get("float" ,"Bu soz mavjud emas ")      
print(royhat)      
royhat=my_knowlege.get("book","Bu mavjud emas")     
print(royhat)      
moon=my_knowlege.get("look", "Bu soz mavjud emas")
if my_knowlege==None:
    print("Bunday soz mavjud emas")
else:
    print(f"{my_knowlege['string'].title()} sozi deb tarjima qilinadi ")    
 

    

    












