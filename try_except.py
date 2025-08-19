"""
try and except opetrator
i can use try only a mistake line
i can use except how to request
"""

# yosh=input("Yoshingizni kiriting>>>")
# try:
#     yosh=int(yosh)
# except ValueError:
#     print('Siz butun son kiritmadingiz')
# else:
#     print(f"Siz {2025-yosh} yilda tug'ulgansiz")
# print('Dastur davom etmoqda')
# print('Dastur tugadi')


# ZeroDivisionError

# x,y=20,10
# try:
#     y/(x-20)
# except ZeroDivisionError:
#     print('0 ga bo\'lishish mumkin emas')
#
# print('Dastur tugadi')

#IndexError

# memalar=['olma','anor','anjir','uzim','anjir',]
# try:
#     print(memalar[5])
# except IndexError:
#     print(f"Royhatda {len(memalar)} ta meva bor xolos")

# # KeyError
# user={
#     'username':'sariqdev',
#     'status':'admin',
#     'email':'admin@sariq.dev',
#     'phone':'998971234739'
# }
# key='tell'
# key2='phone'
# try:
#     print(f'foydalanuvchi: {user[key]}')
# except KeyError:
#     print('Bunday kalit mavjud emas')
#
# print(user[key2])
#

# #FileNotFoundError
#
# filename='datalar.txt'
# try:
#     with open(filename) as file:
#         text=file.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas")

#import json
# talaba1={'ism':'hasan olimov'}
# talaba2={'ism':'alijon jalilov'}
# talaba3={'ism':'vali alijonov'}
# talaba4={'ism':'raim husanov'}
#
# with open('talaba1.json','w') as f1:
#     json.dump(talaba1,f1)
#
# with open('talaba2.json','w') as f2:
#     json.dump(talaba1,f2)
#
# with open('talaba4.json','w') as f4:
#     json.dump(talaba1,f4)

# files=['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for file in files:
#     try:
#         with open(file) as fi:
#             talaba=json.load(fi)
#     except FileNotFoundError:
#         pass   #print(f"{file} mavjud emas")
#     else:
#         print(talaba['ism'])
#


# n=input("Butun son kiriting>>>")
# try:
#     n=int(n)
#     x=20/n
# except ValueError:
#     print('Butun son kiritmadingiz')
# except ZeroDivisionError:
#     print("0 ga bolish mumkin emas")
# else:
#     print(f"x={x}")

while True:
    yosh=input("Yoshinzini kiriting>>>")
    if yosh.isdigit():
        yosh=int(yosh)
        break

        

print(f"Siz {2025-yosh} yilda tug'ulgan ekansiz")













