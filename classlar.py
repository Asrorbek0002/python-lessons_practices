"""
classlar biz bilamiz object orientedni programmingni asosiy ustunlarnidan biridir va u bizni real hayotda obyektlar qanday qilib yondashishini orgatadi
classni ishlashini tushingan dasturchi dunyo qorashda ham kuchli boladi va komples muamolarga ham yechim topishda juda yordam beradi

"""


# x=100
# print(x)
# print(type(x))
#
# matn='salom'
# print(matn)
# print(type(matn))
#

# def salom_ber():
#     print("Assalomu aleykum")
#
# print(type(salom_ber))
# salom_ber()

# methodlar
# matn='asror'
# print(matn.upper())
#
# x=10
# print(x.upper())

"""
class bu obyekt yaratish uchun shablon holos 

"""

# class Talaba:
#     """Talaba nomli class yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """Talabaning husiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil

# classdan obyect yaratamiz bu yerda Talaba classiga murojat qilamiz

#talaba1=Talaba('ali'.title(),'hasanov'.title(),2000)

# obyekning hususiyatlarini koramiz

# print(talaba1.ism)
# print(talaba1.familya)
# print(talaba1.tyil)


# class dan bir nechta obyektlar yaratish

# talaba2=Talaba('abror','abdurazoqov',2005)
# talaba2=Talaba('ayubxon','valiyev',2026)
# talaba3=Talaba('jack','whatson',1987)


# print(talaba3.tyil)
# print(talaba2.familya)


# class Talaba:
#     """Talaba nomli class yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """Talabaning husiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#
#     def tanishtir(self):
#         print(f"{self.ism.title()} {self.familya.title()} {self.tyil}-yilda tug'ulgan ")

# obyektning metodiga murojat qilamiz obyekt va nuqta va funksiya nomi

# talaba1=Talaba('asror','abdurazoqov',2000)
#
# print(talaba1.ism)
#
# talaba1.tanishtir()
#
# class simiz istalgancha methodlardan iborat bolishi mumkin


class inson:
    """Talaba nomli class yaratamiz"""
    kim = "Tirik"
    def __init__(self,ism,familya):
        """Talabaning husiyatlari"""
        self.ism=ism
        self.familya=familya
        self.tyil = 50

    def get_name(self):
        """Talabani ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabani familyasini qaytara"""
        return self.familya

    def get_tyil(self):
        """Talabani tog'lgan yilini qaytaradi"""
        return self.tyil

    def get_fullname(self):
        """Talabani ism familyasini qaytardi"""
        return f"{self.ism} {self.familya}"

    def tanishtir(self):
        print(f"{self.ism.title()} {self.familya.title()} {self.tyil}-yilda tug'ulgan ")


talaba1=inson('asror','abdurazoqov')
talaba2=inson('abror','abdurazoqov')
print(talaba1.get_fullname())
print(talaba2)


# argument qabul qiluvchi methodlar



# class Talaba:
#     """Talaba nomli class yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """Talabaning husiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#
#     def get_name(self):
#         """Talabani ismini qaytaradi"""
#         return self.ism
#
#     def get_lastname(self):
#         """Talabani familyasini qaytara"""
#         return self.familya
#
#     def get_tyil(self,yil):
#         """Talabani tog'lgan yilini qaytaradi"""
#         return yil-self.tyil
#
#     def get_fullname(self):
#         """Talabani ism familyasini qaytardi"""
#         return f"{self.ism} {self.familya}"
#
#     def tanishtir(self):
#         print(f"{self.ism.title()} {self.familya.title()} {self.tyil}-yilda tug'ulgan ")
#
#
# talaba1=Talaba('asror','abdurazoqov',2000)
#
# print(talaba1.get_tyil(2025))
#


"""

pass operatori pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud

pass operatorini biz if-else,while,for larda ishlatamiz

"""

class User:
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email

    def describe(self):
        pass

    def get_email(self):
        pass









