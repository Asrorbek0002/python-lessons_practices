# ->1

#import datetime as dt

#hozir=dt.datetime.now()
# print(hozir.date())
# print(hozir.time())

# print(hozir)
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)

# date()

# bugun=dt.date.today()
# print(f"Bugungi sana: {bugun}")

#ertaga = dt.date(2025, 2, 28)
# print(f"Ertangi sana: {ertaga}")

# time()

# hozir=dt.datetime.now()
# vaqtHozir=hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin=dt.time(23,45,30)
# print(vaqtKeyin)


# bugun=dt.date.today()
# ramazon=dt.date(2025,3,30)
# farq=ramazon-bugun
# print(f"Ramazon {farq.days} kun davom etadi")

# hozir=dt.datetime.now()
# football=dt.datetime(2025,3,2,23,30,00)
# farq=football-hozir
# sekondlar=farq.seconds
# minutlar=int(sekondlar/60)
# soatlar=int(minutlar/60)
# print(f"Football boshlanishiga {farq.days} kun {soatlar} soat qoldi")

#->2
#import math

#PI=math.pi
# print(f"PIning qiymati {PI} ga teng")
# E=math.e
# print(f"Ening qiymati {E} ga teng")

# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# print(math.degrees(math.pi/2))
# print(math.radians(90))

# print(math.log(5))
# print(math.log10(100))

# x=4.6
#
# print(math.ceil(x))
# print(math.floor(x))
#

# sqrt()
# x=81
# print(math.sqrt(x))
# print(math.sqrt(100))

# pow

# x=100
# y=90
# print(math.pow(x,2))
# print(math.pow(y,3))



# from pprint import pprint
# import json
#

# bemor={
#     'ism':'Alijon Valiyev',
#     'yosh':30,
#     'oila':True,
#     'farzandlar':('Ahmad,Bonue'),
#     'allergiya':None,
#     'dorilar':[
#         {'nomi':'analgin', 'miqdori':0.5},
#         {'nomi':'Pandol', 'miqdor':1.2}
# ]
# }
#
#

# with open('bemor_json.txt','w') as fi:
#      json.dump(bemor,fi)
#
#
#
# filename='bemor_json.txt'
# with open(filename) as file:
#     bemor=json.load(file)
#
# print(bemor)
# pprint(bemor)

# import requests
# r=requests.get('https://api.github.com')
# print(r.json())
#
# pprint(r.json())

import re
from words_list import words


word1='asror'
word2='ahror'
word3='akborali'

# andoza="^a...r$"
#
# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

# andoza="^t...r$"
#
# matches=[]
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)
#
# print(matches)

# matn="""
# Maqolalar 2025-yilning 20-martiga qadar rtkmonfernsiya2025@mail.ru elektron pochtasida yuboring
# """
#
# andoza='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email=re.findall(andoza,matn)
# print(email)

andoza='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg="Yangi parol kiriting"
msg+='(kamida 8 belgidan iborat ,kamida 1 ta lotin bosh harifi, 1 ta kichik harf),'
msg+='1 ta son va 1 ta maxsus belgi bolishi kerak'

while True:
    password=input(msg)
    if re.match(andoza,password):
        print('Maxfiy soz qabul qilindi')
        break
    else:
        print("Maxfiy so'z qabul qilinmadi")






















