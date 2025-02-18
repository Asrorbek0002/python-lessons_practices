from pprint import pprint
class Avto:
    __num__avto=0
    """Avtomobil classi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning hususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        Avto.__num__avto += 1

    def __repr__(self):
        return f"Avto: {self.make}  {self.model}"

    def __eq__(self,y):
        return self.narh==y.narh

    def __lt__(self,y):
        return self.narh<y.narh

    def __le__(self,y):
        return self.narh<=y.narh

    def __gt__(self,y):
        return self.narh>y.narh

    def __ge__(self,y):
        return self.narh>=y.narh



class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name=name
        self.avtolar=[]

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __getitem__(self,index):
        return self.avtolar[index]

    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")

    def __len__(self):
        return len(self.avtolar)

    def __call__(self,*qiymat):
       if qiymat:
           for avto in qiymat:
               self.add_avto(avto)
       else:
           return [avto for avto in self.avtolar]

    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {y}")
            yangi_salon.avtolar=self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y,Avto):
            self.add_avto(y)

salon1=AvtoSalon('MaxAvto')
salon2=AvtoSalon("Avto Lider")
avto1=Avto('GM','Malibu','Qora',2020,40000)
avto2=Avto('GM','Lacetti','Oq',2020,40000)
avto3=Avto('Toyota','Carrolla','Silvir',2018,45000)
avto4=Avto('Mazda','6','Qizil','2015',35000)
avto5=Avto('Valkswage','Polo','Qora',2017,30000)
avto6=Avto('Honda','Accard','Oq',2017,42000)
salon2(avto4,avto5,avto6)
salon1.add_avto(avto1,avto2,avto3)




print(salon1)
print(salon1())
print(avto4)
print(salon1 + avto4)
print(salon1())
# print(salon1)
# print(salon2)
# print(salon1())
# print(salon2())
# salon3=salon1 + salon2
# pprint(salon3[:])
# print(salon3.name)
# salon3=salon1 + salon2
# print(salon3[:])
# print(salon1)
# print(salon1())
# print(salon2)
# print(salon2())
# pprint(salon1())
# salon1(avto4,avto5)
# pprint(salon1())
# salon1(avto6)
# pprint(salon1())

#salon1[0]=Avto('BMW','x7','qora',2020,70000)
#print(len(salon1))
#print(salon1[0])
# print(salon1[0])
# print(salon1[1])
# print(salon1[2])
# print(salon1[:])
# print(isinstance(avto1,Avto))
# print(isinstance(avto2,AvtoSalon))
#
#print(salon1)
#print(avto1>=avto2)
# x,y=10,20
# print(x<y)
# print(x>y)
# print(avto1==avto2)
# # __eq__(self,y) i use compare
# __repr__()  method when i report about object it can print
#print(avto1)
#pprint(dir(Avto))
#print(avto1.model)
#print(avto1)


























