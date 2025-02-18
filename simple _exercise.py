# i=1
# while i<=10:
#     print(i)
#     i+=1
# print("Dastur tugadi")

# i=1
# while i<=1:
#     print(i)
#     i+=1
#     print("Dastur tugadi")
#     j=1
#     while j<=2:
#
#         print(j)
#         j+=1
#         print("Dastur tugadi")
#         a=1
#         while a<=3:
#             print(a)
#             a+=1
#             b=1
#             while b<=4:
#                 print(b)
#                 b+=1
#                 c=1
#                 while c<=5:
#                     print(c)
#                     c+=1
# print("Dastur tugadi")


# print('Hello world')
# print('Hayrli tong')
# print(41/35)
# print(41*20)

# print('Mening ismim "asror" men hozir it sohasini o\'rganmoqdaman    \nmen har doim o\'zimga ishonaman')

# arifmatik amalar 4 ta qo'shish ,ayirish, bo\'lish , ko\'paytirish
# print(5+6)
# print(5-8)
# print(5*6)
# print(25/5)  # har doim biz bilamiz bunday bo\'lishda butun qismi bilan keladi agar bizga kerak bo\'lsa shu usulardan foydalanamiz


# bo\'lish va butun qismini olish // va bo\'linmani qoldiq  qismini olish % va darajaga oshirish bizga malumki ** ikkita ko\'paytirish

# print(40/2)
# print(40//2)
# print(40%3)
# print(40**40)

#print('"Nexia", "Tiko","Damasni" ko\'rganlar qilar havas')
# ** shu usul harqaday sonni kvadratini topish
#print(5**4)
# %  bo\'lganda qoldiqni topish shu usul bilan topiladi
#print(22%4)
# 125 ga teng kv p=4*a  va s=a**2
# a=125
# s=a**2
# print(s)
# p=4*a
# print(p)

# d=12 ga teng doiraning yuzi
# pi=3.14
# d=12
# r=d/2
# s=pi*r**2
# print(s)
#
# to\'rt burchakni gepatenuzasini  topish a**2+b**2=c**2
# agar biz darajani ildizni topmoqchi bo\'lsak **0.5 yoki **1/2 ham o\'rinli bo\'ladi
# a=6
# b=7
# c=(a**2+b**2)**(1/2)
# print(c)

# a="Hello world"
# print(a)
#
# xabar='seni isming nima'
# print(xabar)
#
# xabar='men yurishni yoqtiraman'
# print(xabar)
#

# clas='how are you'
# print(clas)

# radius=5
# pi=3.14159
# aylana_yuzi=radius*pi**2
# print(aylana_yuzi)

# ism='Asror'
# familiya="Abdurazoqov"
# print("Mening ismim " + ism)
# print(ism+" "+ familiya)

# f-string ikki va undan ko\'p matinlarni birlashtirish uchun ishlatiladi
#print(f"Mening ismim {ism} , va familiyam {familiya}")

# matinga bo\'sh joy yani bo\'sh joy qolishi uchun \t va keyingi qatordan yozish \n belgisidan foydalanamiz

# print("My name is Asror")
# print("My name is \tAsror")
# print("My name is \nAsror")

# .upper() va .lower() qanday qilib ishlaydi .upper() berilgan har bir matinni katta harflarga o\'zgartiradi .lower() metodi esa aksincha har birini kichik harfga aylatiradi

# ism_fam="Asror Abdurazoqov"
# print(ism_fam.upper())
# print(ism_fam.lower())

# .title() va . capitalize()  bu ikki metodni farqi birichisini farqi har so\'zni katta harf bilan boshlanadi ikkinchisi faqt umumiy matndan birinchisini katta bilan boshlanadi

# ism="asror abdurazoqov"
# print(ism.title())
# print(ism.capitalize())
# meva="   olma   "
# print(f"Men {meva}ni yaxshi ko'raman")
# print(f"Men {meva.strip()}ni yaxshi ko'raman")
# print(f"Men {meva.rstrip()}ni yaxshi ko'raman")
# print(f"Men {meva.lstrip()}ni yaxshi ko'raman")

# input() endi bizga foydalanuvchi bilan muloqtni beradi

# ism=input("Ismingizni kiriting>>>")
# print(f"Assalomu aleykum {ism.title()} qaleysiz "

# integer yani int() bu butun son hisoblanadi uni biz (/,*,+,-) ishlarinini olib boradi bunga naturlar sonlar va unga qaramaqarshi va nol bilan solar kiradi
# kv_to=20
# kv_yuz=kv_to**2
# print(kv_yuz)

# floats float() bu o\'nlik sonlar butun bilan yoziladi 54.5 biz butun sonlarni vergul bilan yozar edik edi biz buyerda butunni nuqta bilan yozmiz

# PI=3.14159
# r=20
# per=2*PI*r
# print(per)

# butun sonlardan o\'nlikka o\'tish o\'nlikni butunga (+,-,/,*) keyin un butunga aylanadi

# print(10+20.3)
# print(10-20.3)
# print(10/20.3)
# print(10*20.3)

# uzun sonlarni kiritishda (_) belgidan foydalanamiz

# son=54_254_632_654
# print(f"O\'zbekistonda {son}ta odam yashaydi")

# costant o\'zdarmas sonlar har bir dasturlash olamida kelishib olingan bo'ladi misol PI=3.14 bu constantlar katta harflar bilan yoziladi

# PI=3.14
# E=2.7

# bir nechta o\'zgaruvchiga qiymat berish
# x,y,z=10,20,30
# print(x*y*z)

# o'zgaruvchi turini almashtirish
# ism="Asror"
# yosh=24
# xabar=f"Mening ismim {ism} va men {yosh} daman"
# print(xabar)

# x=20.3
# y=20
# print(int(x))
# print(float(y))

# o\'zgaruvchi turini tekshirish uchun type() deb yozish kerak
# a=10
# b=32.5
# c='asror'
# print(type(a))
# print(type(b))
# print(type(c))

# input va sonlar inputga qabul qilingan qiymat matn ko\'rinishda bo\'ladi va natija matn ko\'rinishida chiqadi

# yosh=input("Yoshingiz nechida>>>")
# t_yil=2024-int(yosh)
# print(f"Siz {t_yil}-yilda tug\'ulgansiz")

# list yani ro\'yxat bilan tanishamiz biz avval o\'zgarvchiga  bitta qiymatni yuklagan edik endi list ichiga istalgancha o\'zgaruvchini yuklashimiz mumkin (str() ,int(),float()) yuklash mumkin
# mevalar=['olma','o\'rik','shaftoli','olcha'] # matin
# mashinalar=['malibu','nexia3','damas','tiko','jentra']  # matin
#narhlar=[12000,14000,16000,18000,20000]  # sonlar
# sonlar=['bir','uch',5,4,7] # matin va sonlar
# ismlar=[]

# list elemetlari tartib bilan jolashgani sababli unga biz list elementlarga index orqali murojat qilishimiz mumkin dasturlashda kelishib olingan birinchi index oldan boshlandi

# mashinalar=['malibu','nexia3','damas','tiko','jentra']
# print(f"Birinchi mashina {mashinalar[0].upper()}")
# print(f"Ikkinchi mashina {mashinalar[2].lower()}")

# append() bu listni ichiga elemet qo'shadi  .append() metodi listni oxiriga elemet qo'shadi

# mevalar=['olma','o\'rik','shaftoli','olcha']
# mevalar.append("tarvuz")
# print(mevalar)

# .append() metodi bo\'sh ro'yxatni to\'ldirish uchun ham ishlatiladi

# phone=[]
# phone.append('iphone')
# phone.append('samsung')
# phone.append('read mi')
# phone.append('vivo')
# phone.append('appo')
# print(phone)


# .insert() metodi bu usul islatgan joyga biz aytgan elementni kiritadi va biz uni indexni bilan yozishimiz kerak

#mashinalar=['malibu','nexia3','damas','tiko','jentra']
# mashinalar.insert(1,'jetavo')
# mashinalar.insert(0,'BYD')
# print(mashinalar)
# print(narhlar[2]+narhlar[3])
# print(narhlar[2])
# print(narhlar[3])

# elenmetni o\'zgartirish elementni o\'zgartirish uchun indexni berib keyin o\'sha element yoziladi

# mashinalar=['malibu','nexia3','damas','tiko','jentra']
# mashinalar[1]='lacetti'
# mashinalar[3]='spark'
# print(mashinalar)

# del va .remove()(remove() metodi ro\'yxtda ikki bir xil elemetdan birinchi kelganini o'chiradi) biz elemetni o\'chirish uchun listni index yoki qiymatni bilishimiz lozim agar index bo\'yicha 'del' operatori qiymat bo'yicha .remove()ni metodidan foydalamiz

#mevalar=['olma','o\'rik','shaftoli','olcha']
# del mevalar[2]
# del mevalar[0]
#print(mevalar)

# mevalar.remove('o\'rik')
# mevalar.remove('olcha')
# print(mevalar)

# .pop() agar bizdan biror elemetni sug\'urib olish talab qilinsa o\'chirish emas .pop() metodidan foydalanamiz agar index berilmasa oxiridan o\'chirishni boshlaydi


# hayvonlar=['ayiq','bo\'ri','tulki','it','quyon','mol']
# hayvon=hayvonlar.pop(2)
# hayvon=hayvonlar.pop()

# # Indeks orqali
# my_list = [10, 20, 30, 40]
# print(my_list[0])  # 10 (birinchi element)
# print(my_list[-1])  # 40 (oxirgi element)
# Bir nechta elementlar
# print(my_list[1:3])  # [20, 30]
# print("Hello world")

# my_list = [3, 1, 4, 1, 5]
# my_list.sort()  # Asl ro'yxatni o'zgartiradi
# print(my_list)  # [1, 1, 3, 4, 5]

# Ro'yhatni tartiblash .sort() metodidan foydalanamiz bu ro'yhatni tartiblaydi

# cars=['bmw','mercedes besz','general motor','volvo','tesla','audi']
# cars.sort()
# print(cars)

#bu yerda bosh harf har doim birinchi keladi
# cars=['Bmw','mercedes benz','general motor','volvo','tesla','audi']
# cars.sort()
# print(cars)

# teskarisiga saqlash uchun .sort() reverse=True ni shu .sort()metosdiga kiritamiz

# cars=['Bmw','mercedes benz','general motor','volvo','tesla','audi']
# cars.sort(reverse=True)
# print(cars)


# sorted() funksiyasi bu yerda listni tartiblash uchun ishlatiladi va bu asl ro'yhatga tegmaydi
#
# mehmonlar=['Odil','Hamid','Temir','Avazbek','Farrux','SHamsiddin']
# print(f"sorted() qaytargan ro'yhat, {sorted(mehmonlar)}")
# print("Asil ro'yhat o'zgarmas qoldi", mehmonlar)

# shu metodni qarshi teskarisiga aylantirish

#print(sorted(mehmonlar,reverse=True))

# ro'yhatni aylantirish biz shunday ro'yhatni aylantiramiz bu yerda .revverse() metodidan foydalanamiz

# fruits=['lemon','watermelon','banana','apple','pear']
# fruits.reverse()
# print(fruits)

# ro'yhatni uzunligini bilish len() funksiyasi orqali bajariladi

# a=len(fruits)
# print(f"Elementlar soni: {a} ta")

# range() funksiyasi malum bir oraliqdagi solar ketma-ketliga shakilantiradi

# sonlar=list(range(0,100))
# for son in sonlar:
#     print(son)
# print(sonlar)
# sonlar=list(range(0,100+1,2))
# print(sonlar)
# sonlar=list(range(1,100+1,2))
# print(sonlar)
# sonlar=list(range(0,100+1,5))
# print(sonlar)
# sonlar1=list(range(20))
# print(sonlar1)

# sonli ro'yhat ustida turli amalar min() va max() va sum()

# narhlar=[10000,20000,30000,40000,50000,60000]
# print(min(narhlar))
# print(max(narhlar))
# print(sum(narhlar))

# ro'yhatni kesish buyerda [index1:index2]
#cars=['malibu','nexia','kobolt','tiko','tesla','mersades benz','trekker']
# my_car=cars[0:3]
# print(my_car)
# my_car1=cars[2:5]
# print(my_car1)

# agar index kiritmasak boshiga u holda 0 dan boshlab kesadi agar index bermasak oxiriga bersak u oxirigacha kesadi

# car=cars[:5]
# print(car)
# car1=cars[4:]
# print(car1)


# ro'yhatdan nusha ilish bu yerda [:] usul bilan olinadi

# sonlar=[1,2,3,4,5]
# sonlar2=sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print(f"Bu sonlar ro'yhati: {sonlar}")
# print(f"Bu sonlar2 ro'yhati: {sonlar2}")


#tuple() metodi bu yerda biz ro'yhatni o'zgartirmaslik talab qilinishi mumkin bo'ladi shunda tuple() metodidan foydalanamiz tuple metodida  [] qavus o'rniga () shuni qo'yishimiz kerak list elementlarga murojat qilgandek biz tuple elemetlarga ham murojat qilishimiz mumkin

# tomonlar=(20,3,48,79,27)
# tomonlar1=tomonlar[1:4]
# tomonlar2=tomonlar[0:3]
# tomonlar3=tomonlar[0:]
# tomonlar4=tomonlar[:4]
# print(tomonlar1)
# print(tomonlar2)
# print(tomonlar3)
# print(tomonlar4)

# shu kabi ro'yhatdan element qo'shib ham olib tashlab ham bo'lmaydi

# tomonlar[2]='69'
# print(tomonlar)

# o'zgarmas tuple() ni o'zgartirish talab qilinsa biz uni listga o'tkazamiz va keyin yana tuplega aylantiramiz

# toys=('dinasour','snake','bear','rabbit','bird')
# toys=list(toys)
#
# toys.append('phone')
# toys.append('wolf')
# toys.append('house')
# print(toys)
# toys[3]='tv'
# print(toys)
#
# toys=tuple(toys)
# print(toys)


# for operatori

# mehmonlar=['ali','vali','hasan','husan','umid','bobur']
# for i in mehmonlar:
#     print(i.title())
#
# mehmonlar=['ali','vali','hasan','husan','umid','bobur']
# for i in mehmonlar:
#     print(f"Hurmatli, {i.title()} sizni 20-Dekabr kuni nohorgi oshga taklif qilamiz")
#     print("Hurmat bilan Polonchilar oilasi")

# sonlar=list(range(1,10))
# for i in sonlar:
#     print(f"{i} ni kvatrati {i**2} ga teng")

# sonlar=list(range(10,200))
# son_k=[]
# for i in sonlar:
#     son_k.append(i**2)
# print(sonlar)
# print(son_k)









