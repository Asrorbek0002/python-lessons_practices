# from uuid import uuid4
# class Avto:
#     """Avtomobil classi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narh=narh
#         self.__km=km
#         self.__id=uuid4()
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self,km):
#         """Mashinani kmga yana km qoshish"""
#         if km>10:
#             self.__km+=km
#         else:
#             print("Mashinani kmga km qoshib bolmaydi")
#
#
# avto1=Avto('GM','Malaibu','Qora',2020,40000,1000)
#
#
# avto1.add_km(2000)
# avto1.add_km(4000)
# avto1.add_km(-6000)
# print(avto1.get_km())
# print(avto1.get_km())
# print(avto1.get_id())
# print(avto1.rang)
# print(avto1.model)
# print(avto1.km)


"""
we give class some appropriates and methods
this method is asked @classmethod cls instead of self

"""
from uuid import uuid4

class Avto:
    """Avtomobil classi"""
    __num_avto=0
    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        """Mashinani kmga yana km qoshish"""
        if km>10:
            self.__km+=km
        else:
            print("Mashinani kmga km qoshib bolmaydi")


avto1=Avto('GM','Malaibu','Qora',2020,40000,1000)
avto2=Avto('GM','Laceti','Oq',2020,20000,5000)
avto3=Avto('Toyota','Carolla','Silver',2021,60000,3000)
avto1=Avto('GM','Malaibu','Qora',2020,40000,1000)
avto2=Avto('GM','Laceti','Oq',2020,20000,5000)
avto3=Avto('Toyota','Carolla','Silver',2021,60000,3000)



# print(avto1.get_num_avto())
# print(Avto.get_num_avto())


class Bus:
    pass

class Train:
    pass












































