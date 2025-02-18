 # moduldan foydalanish codeni chiroyli yozish tartibli chiqarish uchun modul yaratish zarur

# modul yaratamiz

def avto_info(kompanya,model,rangi,korobka,yili,narhi=None):
    """Avtomobil haqidagi malumotlarni lug'at ko'rinishda qaytaruvchi funksiya"""
    avto={
        'kompanya':kompanya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yili':yili,
        'narhi':narhi
    }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funkiyasi yordamida bir nechta avtolar haqida"""
    avtolar=[]
    while True:
        print("Quyidagi malumotlarni kiriting")
        kompanya=input('Ishlab chiqaruvchi>>>')
        model=input('Modeli')
        rangi=input('rangi')
        korobka=input('korobka')
        yili=input('yili')
        narhi=input('narhi')
        avtolar.append(avto_info(kompanya,model,rangi,korobka,yili,narhi))
        javob=input("Yana avto qoshasizmi (yes/no)")
        if javob=='no':
            break

    return avtolar

def info_print(avto_info):
    """Avtomobilar haqida malumotlar saqlangan konsulga chiqarish"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompanya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobkada, "
          f"{avto_info['yili']}-yil ${avto_info['narhi']}")



sonlar=list(range(10,100))

# yuqoridagi funkiyalarni bir nechta usul orqali boshqa filda chaqirishimiz mumkin



























