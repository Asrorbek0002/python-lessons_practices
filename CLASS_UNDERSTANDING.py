class Car:
    """Car attribute"""
    Wheels=4
    def __init__(self,brand,colour,price):
        """Attribute of class is these"""
        self.brand = brand
        self.colour = colour
        self.price=price

    def show_info(self):
        """the method of class is this"""
        return f"Brand:{self.brand}, Colour:{self.colour}, Price:{self.price}"



car1=Car("BMW",'black',70000)
# print(car1.show_info())
# car1.brand='GM'
# print(car1.show_info())
# print(car1.colour)
# print(Car.Wheels)



#inheritance

class Animal:
    """Animal class"""
    def __init__(self,name,age):
        """Animal attributes"""
        self.name=name
        self.age=age

    def get_make_sound(self):
        return "Some genetic animal sound"

    def get_show_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Animal):
    def __init__(self,name,age,run,height):
        super().__init__(name,age)
        self.run=run
        self.height=height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_run(self):
        return self.run

    def get_show_info(self):
        return f"People call my dog called {self.name} its age is {self.age} and my dog runs about {self.run} as well as its {self.height}sm"


dog1=Dog('Semba',6,200,0.50)
# print(dog1.get_show_info())
# print(dog1.get_age())
# print(dog1.get_name())
# print(dog1.get_height())
# print(dog1.get_run())

class Bird(Animal):
    def __init__(self,name,age,can_fly,km):
        super().__init__(name,age)
        self.can_fly=can_fly
        self.km=km

    def get_can_fly(self):
        return self.can_fly

    def get_km(self):
        return self.km

    def set_can_fly(self,km):
        if km:
            self.km+=km
        else:
            print("Siz km kirgizmadingiz")

bird1=Bird('Bugut',15,'sky',100)


# bird1.set_can_fly(500)
# bird1.set_can_fly(400)
# bird1.set_can_fly(400)
#print(f"{bird1.get_show_info()},i can fly in the {bird1.get_can_fly()},{bird1.get_km()} ")

class Person:
    def __init__(self,name,last_name,tyil,place):
        self.name=name
        self.last_name=last_name
        self.tyil=tyil
        self.place=place

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_tyil(self):
        return self.tyil

    def get_place(self):
        return self.place

person1=Person('Asror','Abdurazoqov',2000,'Farg\'ona')

# print(person1.get_name())
# print(person1.get_last_name())
# print(person1.get_tyil())
# print(person1.get_place())
# print(f"{person1.get_name()} {person1.get_last_name()} {person1.get_tyil()}-yil tug\'ldi {person1.get_place()} viloyatida")

class Talaba(Person):
    def __init__(self,name,last_name,tyil,place,kurs,bosqich):
        super().__init__(name,last_name,tyil,place)
        self.kurs=kurs
        self.bosqich=1

    def get_kurs(self):
        return self.kurs

    def get_bosqich(self):
        return self.bosqich

    def set_bosqich(self,bosqich):
        self.bosqich += bosqich


talaba=Talaba('Asilek','Abdurazoqov',2001,'Farg\'ana',2,1)


# talaba.set_bosqich(1)
# print(f"{talaba.get_name()} {talaba.get_last_name()}, {talaba.get_tyil()}-yilda , {talaba.get_place()} viloyatida tugulgan, {talaba.get_kurs()}-kurs talabasi, raqami {talaba.get_bosqich()}")
#
# talaba.set_bosqich(4)
# print(f"{talaba.get_name()} {talaba.get_last_name()}, {talaba.get_tyil()}-yilda , {talaba.get_place()} viloyatida tugulgan, {talaba.get_kurs()}-kurs talabasi, raqami {talaba.get_bosqich()}")
#
# talaba.set_bosqich(4)
#
# print(f"{talaba.get_name()} {talaba.get_last_name()}, {talaba.get_tyil()}-yilda , {talaba.get_place()} viloyatida tugulgan, {talaba.get_kurs()}-kurs talabasi, raqami {talaba.get_bosqich()}")

# polimarfizm

class Telephone:
    def __init__(self,brand,year,colour,country):
        self.brand=brand
        self.year=year
        self.colour=colour
        self.country=country

    def get_brand(self):
        return self.brand

    def get_year(self):
        return self.year

    def get_colour(self):
        return self.colour

    def get_country(self):
        return self.country

    def get_show_info(self):
        return f"{self.brand} {self.year}-yida ishlab chiqarildi, {self.colour} rangda {self.country} davlatida"

smartphone=Telephone('Iphone',2024,'dark','USA')

# print(smartphone.get_brand())
# print(smartphone.get_year())
# print(smartphone.get_colour())
# print(smartphone.get_country())
# print(smartphone.get_show_info())

class Sumsang(Telephone):
    def __init__(self,brand,year,colour,country,price):
        super().__init__(brand,year,colour,country)
        self.brand=brand
        self.year=year
        self.colour=colour
        self.country=country
        self.price=price

    def get_price(self):
        return self.price

    def get_show_info(self):
        return f"Men {self.year}-yil {self.colour} rangli sumsung {self.brand} telephone bought its price is ${self.price} this phone was produced by {self.country} country"

sum=Sumsang('A 100',2025,'black','Korea',15000)

#print(sum.get_show_info())

# Encubsulatoin

# class FoodItem:
#     def __init__(self,name,price):
#         self.name=name   # public attribute
#         self.__price=price  # prive attribute
#
#     def get_name(self):
#         return self.name
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self,new_price):
#         if new_price>0:
#             self.__price=new_price
#         else:
#             print("Price can not be negative")
#
#     def __calculate_discount(self):
#         return self.__price*0.9
#
#     def get_discounted_price(self):
#         return self.__calculate_discount()
#
#
#
#
# fooditem=FoodItem('Apple',2.5)
#
# # print(fooditem.get_name())
# # print(fooditem.get_price())
# #
# # fooditem.set_price(20)
# # print(fooditem.get_price())
# print(fooditem.get_discounted_price())
# print(fooditem.__calculate_discount())
#

class Compuyter:
    def __init__(self,brand,colur,price):
        self.__brand=brand  # private
        self.colur=colur
        self.price=price

    def __get_brand(self):
        return self.__brand

    def get_general(self):
        return self.__get_brand()

    def get_colur(self):
        return self.colur

    def get_price(self):
        return self.price

comp=Compuyter('Iphone','dark',15000)

# print(comp.get_general())
# print(comp.get_colur())
# print(comp.get_price())
# print(comp.__get_brand())
# print(comp.__brand())


class FoodItem:
    def __init__(self,name,price):
        self.name=name
        self._price=price

    def _calculate_tax(self):
        return self._price*0.1

    def get_price_with_tax(self):
        return self._price + self._calculate_tax()

    def get_display(self):
        return f"Food Item: {self.name} , Price: ${self._price}"


    def _calculate_discount(self):
        return self._price*0.1

item = FoodItem("Apple",20)


# print(item._price)
# print(item._calculate_tax())
#
# print(item.get_display())
# print(item.get_price_with_tax())


class SpecialFood(FoodItem):
    def __init(self,name,price):
        super().__init__(name,price)
        self.name=name
        self.price=price

    def get_discounted_price(self):
        return self._price - self._calculate_discount()


special_item = SpecialFood('Pizza',10)

#print(special_item.get_discounted_price())

class Car:
    def __init__(self,brand,colour,price):
        self.brand=brand
        self.__colour=colour
        self.price=price

    def get_brand(self):
        return self.brand

    def get_colour(self):
        return self.__colour

    def __get_price(self):
        return self.price

    def get_show(self):
        return self.__get_price()


car1=Car('BMW','Black',90000)


# print(car1.get_show())
# print(car1.get_colour())
# print(car1.__colour)
# print(car1.__get_price())

class Anima:
    def __init__(self,name,age,pet_wild):
        self.name=name
        self._age=age
        self.pet_wild=pet_wild


    def _get_name(self):
        return self.name

    def get_age(self):
        return self._age

    def get_pet_wild(self):
        return self.pet_wild

    def get_show(self):
        return self._age + self._get_name()

anima1=Anima('Bear','20','wild')


#print(anima1.get_show())
# print(anima1._get_name())
# print(anima1._age)

class Aynima(Anima):
    def __init__(self,name,age,pet_wild,kind):
        super().__init__(name,age,pet_wild)
        self.name=name
        self.age=age
        self.pet_wild=pet_wild
        self.kind=kind

    def get_kind(self):
        return f"{self.kind.title()} {self._get_name()}"

aynina=Aynima('Lion',25,'wild','forest')

#print(aynina.get_kind())














































