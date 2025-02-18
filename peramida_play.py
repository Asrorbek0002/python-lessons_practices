# class Sana:
#     """Sanaydigan o'yin"""
#
#     def get_son(self):
#         sonlar=[]
#         son=0
#         while son<5:
#             son+=1
#             sonlar.append(son)
#         return sonlar
#
#
#     def get_son1(self):
#         sonlar1=[]
#         son1=6
#         while son1>0:
#             son1-=1
#             sonlar1.append(son1)
#             if son1==1:
#                 break
#         return sonlar1

    # def get_son(self):
    #    sonlar=[]
    #    for son in range(1,6):
    #      sonlar.append(son)
    #    return sonlar
    #
    # def get_rev(self):
    #     sonlar1=[]
    #     for son1 in list(range(1,6)):
    #         sonlar1.append(son1)
    #
    #     return sonlar1

# son1=Sana()
# print(son1.get_son())
# print(son1.get_son1)
#


# import time
#
# def print_pyramid(height):
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "*" * (2 * i - 1))
#         time.sleep(0.5)
#
# height = 5
# print_pyramid(height)
#
#
#
# def print_reverse_pyramid(height):
#     for i in range(height, 0, -1):
#         print(" " * (height - i) + "*" * (2 * i - 1))
#         time.sleep(0.5)
#
# height = 5
# print_reverse_pyramid(height)
#
#
# def print_pyramid(height):
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "*" * (2 * i - 1))
#         time.sleep(0.5)
#
# height = 5
# print_pyramid(height)
#
#



import time

class Pyramid:
    def __init__(self, height):
        self.height = height

    def print_pyramid(self):
        """Oddiy piramida chiqarish."""
        for i in range(1, self.height + 1):
            print(" " * (self.height - i) + "p" * (2 * i - 1))
            time.sleep(0.5)

    def print_reverse_pyramid(self):
        """Teskari piramida chiqarish."""
        for i in range(self.height, 0, -1):
            print(" " * (self.height - i) + "p" * (2 * i - 1))
            time.sleep(0.5)


height = 5

pyramid = Pyramid(height)

print("Oddiy piramida:")
pyramid.print_pyramid()

print("\nTeskari piramida:")
pyramid.print_reverse_pyramid()

print("Oddiy piramida:")
pyramid.print_pyramid()









