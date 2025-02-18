# class yaratish

class Shaxs:
    """Shaxs haqida malumot"""
    def __init__(self,ism,familya,password,tyil):
        self.ism=ism
        self.familya=familya
        self.password=password
        self.tyil=tyil

    def get_info(self):
        """Shaxs haqida malumot"""
        info=f"{self.ism} {self.familya}.Password:{self.password}, {self.tyil}-yilda tug'ulgan"
        return info

    def get_age(self,yil):
        """Shaxsning tugulgan kuni"""
        return yil-self.tyil

inson=Shaxs('Anvar','Aliyev','UH4499999444',2000)

# print(inson.get_info())
# print(inson.get_age(2025))
# print(f"{inson.get_info()} {inson.get_age(2025)} yoshda")


#voris klass yaratish

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familya,password,tyil):
#         """Talabaning husiyati"""
#         super().__init__(ism,familya,password,tyil)
#
#
# talaba=Talaba('Hasan','Aliyev',"PP0099444222",2000)

# print(talaba.get_info())
# print(talaba.get_age(2025))


# voris klassga hos husudiyatlar va methodlar
# palimarfizm

class Talaba(Shaxs):
    """Talaba klass"""
    def __init__(self,ism,familya,password,tyil,idraqam,manzil):
        """Talaba hususiyatlari"""
        super().__init__(ism,familya,password,tyil)
        self.idraqam=idraqam
        self.manzil=manzil
        self.bosqich=1

    def get_id(self):
        """Talabani id raqami"""
        return self.idraqam

    def get_manzil(self):
        """Talaba manzili"""
        return self.manzil

    def get_bosqich(self):
        """Talabani bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida malumot"""
        info=(f"{self.ism} {self.familya} "
              f"{self.bosqich}-bosqich. ID raqam:{self.idraqam}")
        return info
#talaba=Talaba('Hasan','Aliyev',"PP0099444222",2000,'7774443333l',manzil)

#print(f"{talaba.get_info} {talaba.get_age(2025)} yoshda. ID {talaba.get_id} va {talaba.get_bosqich}-bosqich talabasi ")
#print(talaba.get_info())

# obyekt ichida obyekt


class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil husiyatlari"""
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil=(f"{self.viloyat} viloyati, {self.tuman} tumani,"
                f" {self.kocha} kocha , {self.uy}-uyi")

        return manzil

talaba1_manzil=Manzil(45,'Shodlik','Dangara','Fargana')
talaba1=Talaba('Asror','Abdurazoqov','JH7474848',2000,'AD%%^4899',talaba1_manzil)

print(talaba1.manzil)
print(talaba1.manzil.get_manzil())
