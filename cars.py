class Car:
    def __init__(self,make,model,year,km=0,price=None):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.__km=km

    def set_price(self,price):
        self.price=price

    def add_km(self,km):
        """Mashinani km ga yana km qoshish"""
        if km>0:
            self.__km+=km
        else:
            raise ValueError('km manfiy bolishi mumkin emas')


    def get_info(self):
        info=(f"{self.make.upper()} {self.model.title()}, "
              f"{self.year}-yil, {self.__km}km yurgan.")
        if self.price:
            info+=f"Narhi: {self.price}"
        return info

    def get_km(self):
        return self.__km



# avto1=Car('gm','malibu',2020)
#
# print(avto1.get_info())
# avto1.set_price(2000)
# print(avto1.get_info())
# avto1.add_km(50)
# print(avto1.get_info())
# avto1.add_km(100)
# print(avto1.get_info())
# avto1.add_km(800)
# print(avto1.get_info())
#











