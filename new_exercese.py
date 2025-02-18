# class Person:
#     yeer=2020
#     def __init__(self,name,birth_year):
#         self.name=name
#         self.birth_year=birth_year
#
#     def calulate_age(self):
#         return self.year-self.birth_year
#from pydantic.v1.mypy import get_name


# class Tortbur:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def tort_per(self):
#         return 2*self.a+2*self.b
#
#     def tort_yuz(self):
#         return self.a*self.b
#
# yuz=Tortbur(2,5)
# print(yuz.tort_yuz())
#

#from abc import ABC, abstractmethod
#
#
# # Define an abstract class
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         """Abstract method that must be implemented in subclasses"""
#         pass
#
#
# # Subclass implementing the abstract method
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof! Woof!"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
#
# # Instantiate subclasses
# dog = Dog()
# cat = Cat()
#
# print(dog.make_sound())  # Output: Woof! Woof!
# print(cat.make_sound())  # Output: Meow!
#
# # Trying to instantiate an abstract class will result in an error
# # animal = Animal()  # TypeError: Can't instantiate abstract class Animal

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#
#     def get_name(self):
#         return self.name
#
#     def get_deposit(self,amount):
#         return self.__balanace-amount
#
#     def get_withdraw(self,amount):
#         return self.__balance+amount
#
#     def __check_balance(self):
#         return self.__balance
#
# bank=BankAccount('Olim',2000)
#
# bank.get_deposit(200)
# print(bank.get_deposit())
#

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_len(self):
#         return self.a+self.b
#
#     def get_s(self):
#         return self.a*self.b
# class Tort(Shape):
#
#      def get_len(self):
#          return self.a*self.b
#
#      def get_s(self):
#          return self.a*self.b
#
#
# tort=Tort()

# class BankAccount:
#     def __init__(self,name,account,account_numb):
#         self.name=name
#         self.__account=account
#         self.__account=account_numb
#
#     @property
#     def name(self):
#         return self.name
#
#     def set_ammount(self,amount):
#         self.__account=amount
#
#     def get_amount(self):
#         return self.__account
#
#     @property
#     def get_account_number(self):
#         return 8 * "#" + self.get_account_number[:4]
#
#
# person1=BankAccount('Ali',120241,651478954141554544)
# print(person1.get_amount)


import random

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Bank:
    def __init__(self,u:User):
        self.user=u
        self.__ac__no=None

    def create_account(self):
        if self.user.age<18:
            print("You are not allowed to create account")
        else:
            account_number=random.randint(100000,999999)
            self.__ac__no=account_number
            print(f"Your account number is {account_number}")

    def get_account_number(self):
        return self.__ac__no


john=User('John',17)
bank=Bank(u=john)
print(bank.user.name)


