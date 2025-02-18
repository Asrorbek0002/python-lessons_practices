# yigindi=[]
# n=int(input("1 dan n gacha bo\'lgan sonlar yig\'indisini kiriting>>>"))
# for son in range(1,n):
#     yigindi.append(son)
# print(sum(yigindi))
#
#
# n=int(input("1 dan n gacha bo\'lgan sonlar yig\'indisini kiriting>>>"))
# sum = 0
# for i in range(1,n):
#     sum = sum + i
# print(sum)
#
#
# n=int(input("1 dan n gacha son kiriting>>>"))
# kop=1
# for i in range(1,n):
#     kop*=i
# print(kop)
#
# n=int(input('Istlagan sonni kiriting>>>'))
# for son in range(1,n):
#     if son%2==0:
#         print(son,end=' ')
#
#
# n=int(input("Istalgan sonni kiriting>>>"))
# for son in range(1,n):
#     if son%2==1:
#         print(son,end=" ")
#

# word = input("enter a word")
#
# for i in word[::-1]:
#     print(i,end=" ")


# row=10
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" " ,end='')
#     for k in range(2*i-1):
#         print("M",end='')
#     print()


# def name():
#     print('hello world')
#
# name()

# def calculate(x,y):
#      #print(x+y)
#      return x+y
# print(calculate(10,20))

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


# print('5 ta eng yaqin dostingizni kiriting')
# dostlar=[]
# for i in range(5):
#     dostlar.append(input(f"{i+1}- dostingizni kiriting>>>"))
#
# print(dostlar)
#

# while tsikili haqida malumot


# ism=input("Ismingiz nima>>>")
# print(f"Salom,  {ism.title()}")

# ism=input('Ismingiz nima>>>')
# savol=f"Salom, {ism.title()}.Yoshingiz nechida"
# yosh=int(input(savol))
# height=input("Boyiz nechi sanimeter>>>")
# height=float(height)


 #  while tskil bir shart togri bolsa dastur dastur takrorlanaveradi

# son=1
# while son<=5:
#     print(son,end=" ")
#     son+=1
#

# pythonda +=,-=,*=,/= operatori bor bu yerda ong tomoni chap tonga qo'shish ,ayrish, bo'lish va ko\'paytirish kabi amalarni bajaradi

# savol="Kiritilgan sonni kvadratini chiqaruvchi dastur. Istlagan sonni kiriting va agar toxtatishni istasangiz 'exit' deb yozing>>>"
# qiymat=''
# while qiymat!='exit':
#     qiymat=float(input(savol))
#     if qiymat!='exit':
#         print(f"{qiymat} ning kvadrati {qiymat**2} ga teng")

# ishora ni vazifasi malum bir shartni toxtatish uchun ishlatiladi

# savol="Istalgan sonni kiriting, bu son kvadrat qaytaradi,tugashi ushun 'stop'>>> "
# ishora=True
# while ishora:
#     qiymat=float(input(savol))
#     if qiymat=='stop':
#         ishora=False
#     else:
#         print(f"{qiymat} ning kvadrati {qiymat**2} ga teng")

# break operatori dasturni toxtatish uchun ishlatiladi

# savol="Istalgan sonni kiriting, bu dastur kvadrat qaytaradi,tugashi ushun 'stop' bosing>>> "
# while True:
#     son=float(input(savol))
#     if son=='stop':
#         break
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")
#
# for uchun break operatorini ishlatish

# savol = "Istalgan sonni kiriting, bu dastur kvadrat qaytaradi,tugashi ushun 'stop' bosing>>> "
#
# sonlar=list(range(10))
# for son in sonlar:
#     if son==5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")
#

# continue operatori davom etishni taminlaydi

# sonlar=list(range(10))
# for son in sonlar:
#     if son==5:
#         print("----")
#         continue
#         print('hiiii')
#     else:
#         print(f"{son} kvadrati {son**2} ga teng")
#         print("helooo")
#

# continue while bilan birga

# son=0
# while son<=10:
#     son+=1
#     if son%2==0:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")

# abadiy tsikl tuzog'i bu umumiy hatolardan kelib chiqadi

# son=0
# while son<=10:
#     son+=1  # bu yerda son+=1 qolib ketibdi
#     if son%2!=0:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")


# son=0
# while son<=10:
#      if son%2!=0:
#         continue
#      else:
#         print(f"{son} ning kvadrati {son**2} ga teng")
#      son+=1 # bu yerda hato eng pasiga yozganimiz


# son=1
# while son<0:
#     son+=1
#     if son%2==0:
#         continue
#     else:
#         print(f"{son} kvadrati {son**2} ga teng")
#

# ismlar=[]
# print("Yaqin do'stlarnigiz ro'yhatini tuzamiz")
# n=1
# while True:
#     ism=input(f"{n}-dostingizni kiriting>>>")
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasizmi (ha/yoq)>>>")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
#
# for ism in ismlar:
#     print(ism.title())

# print('Dostlariz yoshini saqlaymiz')
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Dostingizni ismini kiriting>>>")
#     yosh=int(input(f"{ism.title()} ning yoshini kiriting>>>"))
#     dostlar[ism]=yosh
#     javob=input('Yana malumot qo\'shasizmi? (ha/yoq)')
#     if javob=='yoq':
#         ishora=False
#
#
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da")
#

# royhat elemetlarini ochirish

# cars=['malibu','lacetti','kobolt','audi','nexia','bmw','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
#
# print(cars)

# roytdan royhatga element ko'chirish

talabalar=['hasan','husan','olim','botir','ali']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting>>>")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba]=baho

for key, value in baholangan_talabalar.items():
    print(f"{key}ning bahosi {value}")














