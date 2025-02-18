
# for takrorlash operatori haqida gaplashamiz dasturlash davomida bir kodni takrorlash uchun ishlatiladi
# bu yerda for tsikl (loop) deb nomlanadi

# mehmonlar=['Ali','Hasan','Vali','Husan','Jalol']
# for mehmon in mehmonlar:
#     print(mehmon)

# for so'zi 'uchun' deb tarjima qilinadi

# mehmonlar=['Ali','Hasan','Vali','Husan','Jalol']
# for mehmon in mehmonlar:
#     print(f"Hurmatli ,{mehmon} sizni 20-dekabr kuni nohorgi oshga taklif qilamiz")
#     print("Hurmat bilan ,Qo'chqorovlar oilasi")

# Bu yerda 2 ta print() tsikl badani deyiladi

# mehmonlar = ['Ali', 'Hasan', 'Vali', 'Husan', 'Jalol']
# for mehmon in mehmonlar:
#     print(f"Hurmatli ,{mehmon} sizni 20-dekabr kuni nohorgi oshga taklif qilamiz")
#
# print("Hurmat bilan ,Qo'chqorovlar oilasi")

# mehmonlar=['Ali','Hasan','Vali','Husan','Jalol']
# for mehmon in mehmonlar:
#     print(mehmon)
#     print(mehmonlar)

# for yordamida sonli ro\'yhatlar bilan ishlash

# sonlar=list(range(1,10+1))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# for yordamida yangi yangi ro\'yhat yaratish mumkin

# sonlar=list(range(1,10+1))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar_kvadrati)
# print(sonlar)

# for va input orasidagi bog\'liqlik
# sonlar=[]
# print("5 ta yaqin do\'stingizni kiriting")
# for n in range(5):
#     sonlar.append(input(f"Sizni {n+1} do\'stingizni kiriting>>>"))
#     print(sonlar)
#

# if-else operatorlar shart operatorlar hisoblanadi tarmoqlanish hisoblanadi

# if operatori if ingliz tilida agar deb tarjima qilinadi

# avtolar=['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto=='bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# agar shartning ikki tarafi to\'g\'ri bo\'lasa 'True' yoki aksincha ikki tarafi ham noto\'g\'ri bo\'lsa 'False' qiymatni qaytaradi

# ism='Ali'
# print(ism=='Ali')
# print(ism=='Vali')

# Demak if ning badani True bo\'lganda else badani esa False bo\'lganda ishlaydi

# qiymatni teng emasligini tekshirish '==' tengmi deb tarjima qilinadi '!=' bu belgi esa teng emas deb o\'qiladi

# car=input('Mashina namini kiriting>>>')
# if car.title()=='Bmw':
#     print(f"Men seni kutaytovdim {car.lower()}")
# else:
#     print(f"Men bu mashinani hohlamayman")
#
# ism=input("Ismingizni kiriting>>>")
# if ism.lower() != "ali":
#     print(f"Uzir, {ism.title()} biz Ali kutmoqdamiz")
# else:
#     print("Salom ,Ali")

# sonlarni solishtirish bu yerda 'a>b' a katta b 'a>=b' a katta yoki teng b 'a<b' a kichkina b 'a<=b' a katta yoki teng b

# javob=float(input("12*6 nechiga teng>>>"))
# if javob!=72:
#     print("Javon xato")
# else:
#     print("Javob turi")

# yosh=int(input("Yoshingiz nechida>>>"))
# if yosh>=18:
#     print("Xush kelibsiz")
# else:
#     print("Sizga kirish mumkin emas")
#

# login=input("yangi login tanlang >>>")
# if len(login)<=5:
#     print("Login 5 tadan kam bolmasligi kerak")

# yil=int(input("Tugulgan yilingizni kiriting>>>"))
# if 2024-yil<=18:
#     print(f"Sizni yoshingiz {2024-yil} da ekan")
#

# yosh=int(input("Yoshingiz nechda>>>"))
# if yosh>=65: print("Siz COVID-19 riskida ekansiz")

# x,y=25,50
# print("x>y") if x>y else print("y<x")

# if elif else haqida  qo'shimcha shart operatorlar haqida malumot]


# age=int(input("How old are you>>>"))
# if age<=4:
#     print("it is free for you")
# elif age<=12:
#     print("it is about 5000 sum for you")
# else:
#     print("it is about 10000 sum for you")

# yosh=int(input("Yoshingiz nechida>>>"))
# if yosh<=4:
#     narh=0
# elif yosh<=12:
#     narh=5000
# elif yosh<=65:
#     narh=10000
# elif yosh>=65:
#     narh=8000
# print(f"Siz kirish {narh} so'm ")

# if-elif-else zanjirida biz else tashlab ketishimiz mumkin bu juda katta  ro'l o'ynamaydi

# or ingliz tilida yoki deb yuritiladi operatori ikki shartni birini bajaradi bu yerda or opertori shartlardan birini bajarsa True qiymatni qaytaradi
#
# day=input("What is the day today>>>")
# if day.lower()=='saturday' or day.lower()=='sunday':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# day=input("What is the day today>>>")
# temprature=int(input("What is the temprature>>>"))
# if day.lower()=='sunday' and temprature>=30:
#     print("Bugun cho\'milgani boramiz")
# elif day.lower()=='sunday' and temprature<=30:
#     print("Bugun cho\'milgani bormaymiz")
#


# avtolar=['audi','bmw','volvo','kia','hyundai']
#
# for i in avtolar:
#     if i=='bmw':
#         print(i.upper())
#     else:
#         print(i.title())


# ism='ALI'
# print(ism=='ALI')
# print(ism=='Vali')

# ism=input("Ismingizni kiriting>>>")
# if ism.lower()!='ali':
#     print(f"Salom, {ism.title()} biz ,Alini kutyabmiz")
# else:
#     print("Salom ,Ali")
#

# yosh = float(input("Yoshingizni kiriting>>>"))
# if yosh>=19:
#     print("Siz kirishingiz mumkin")
# else:
#     print("Sizga kirish mumkin emas")

# login=input("Login kiriting>>>")
# if len(login)<=5:
#     print("5 ta harfdan ko\'p bolishi kerak")


# t_yil=int(input('Yoshingizni kiriting>>>'))
# if 2024-t_yil<=18:
#     print(f"Sizning yoshingiz {2024-t_yil} da ekan kirish mumkin emas")
# else:
#     print("Xush kelibsiz")
#

# yosh=int(input("Yoshingizni kiriting>>>"))
# if yosh<=4:
#     print("Sizga kirish bupul")
# elif yosh<=12:
#     print("Sizga kirish 5000 so\'m")
# else:
#     print("Sizga kirish 10000 so\'m")
#

# yosh=int(input('Yoshingizni kiriting>>>'))
# if yosh<=4:
#     narh=0
# elif yosh<=12:
#     narh=5000
# else:
#     narh=10000
# print(f'Siz uchun {narh} so\'m')
#
# kun=input('Bugun kun nima>>>')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olamiz')
# else:
#     print('Bunun ish kuni')

# kun=input("Bugun kun nima>>>")
# harorat=float(input('Havo harorati qanday>>>'))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Bugun cho\'milgani boramiz")
# else:
#     print("Bugun dam olamiz")
#

# kun=input("Bugun kun nima>>>")
# harorat=float(input('Harorat nechi>>>'))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>30:
#     print('Bugun cho\'milishga chiqamiz')
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print('Bugun cho\'milishga chiqmaymiz')
#
#
# narh=15000
# non=True
# choy=True
# asarti=False
# salat=False
# kompot=True
#
# if choy:
#     print("Mijoz choy oldi")
#     narh=narh+2000
# if non:
#     print('Mijoz non oldi')
#     narh=narh+3000
# if asarti:
#     print('Mijoz asarti oldi')
#     narh=narh+5000
# if salat:
#     print('Mijoz salat oldi')
#     narh=narh+5000
# if kompot:
#     print('Mijoz kompot oldi')
#     narh=narh+10000
# print(f'Mijozning umumiy summasi: {narh}')
#

























