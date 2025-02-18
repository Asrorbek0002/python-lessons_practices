class Talaba:
    """Talaba nomli klass yarartamiz"""
    def __init__(self,ism,familya,tyil):
        """Talabaning hususiyatlari"""
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
        self.bosqich=1

    def get_info(self):
        """Talaba haqida malumot"""
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi"

    def get_name(self):
        """Talabaning isminni qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning famiyasini qaytaradi"""
        return self.familya

    def get_tyil(self):
        """Talabaning tugulgan yili"""
        return self.tyil

    def get_fullname(self):
        """Talabaning toliq ism familyansi qaytaradi"""
        return f"{self.ism} {self.familya}"

    def set_bosqich(self,yangi_bosqich):
        """Talabani kursini yangilovchi method"""
        self.bosqich=yangi_bosqich

    def update_bosqich(self):
        """Talabani bosqichini 1 taga oshiradigan method hisoblanadi"""
        self.bosqich+=1

    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith('__')]


class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni+=1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]

        # talabalar=[]
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_fullname())
        # return talabalar


talaba1=Talaba('Alijon','Valiyev',1995)
# Dunder methods (double under score) dir() i except all of methods such as properties and methods
#print(dir(Talaba))

# we  see only my methods the through this formula if i give class and we see only my methods and properties the through this formula if i give obyect
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
print(see_methods(Talaba))
print(see_methods(talaba1))




matematika=Fan("Oliy matematika")

#talaba1=Talaba('Alijon','Valiyev',1995)
# talaba2=Talaba('Hasan','Qodirov',2000)
# talaba3=Talaba('Olimjon','Hasanov',1996)

# __dict__ methods this method may give obyect which keys and values
talaba1.__dict__
print(talaba1.__dict__)

# i need keys
talaba1.__dict__.keys()
print(talaba1.__dict__.keys())

# i need values
talaba1.__dict__.values()
print(talaba1.__dict__.values())

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
#
# print(matematika.get_students())

# talaba1=Talaba('Alijon','Valiyev',1995)
#
# matem.add_student(talaba1)
# print(matematika.talabalar_soni)
#
# talaba2=Talaba('Hasan','Qodirov',2000)
#
# matematika.add_student(talaba2)
# print(matematika.talabalar_soni)
#
# print(matematika.nomi)
#
# print(matematika.talabalar)
#


# matematika.talabalar
# print(matematika.talabalar)
# matematika.talabalar_soni
# print(matematika.talabalar_soni)



# talaba1.update_bosqich()
# print(talaba1.get_info())
#
# talaba1.update_bosqich()
# print(talaba1.get_info())
#
# talaba1.update_bosqich()
# print(talaba1.get_info())
# talaba1.set_bosqich(5)
# print(talaba1.get_info())
# talaba1.bosqich
# talaba1.bosqich=2
# print(talaba1.bosqich)
#print(talaba1.get_lastname())
#This method does not recommond for everyone
# print(talaba1.bosqich)
# print(talaba1.ism)
# print(talaba1.tyil)
#every time we use with methods









