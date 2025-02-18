# class Attack:
#     """People lose thier energy"""
#     def __init__(self,tak,giv):
#         """Energy lose"""
#         self.tak=tak
#         self.giv=giv
#
#     def get_att(self):
#         energy1=200
#         energy2=300
#         while True:
#             user1=int(input("Zarbani miqdorini kiriting>>>"))
#             if user1:
#                 energy1=energy1-user1
#             elif energy1=='0':
#                 break
#             user2=int(input('Zarbani miqdorini kiriting>>>'))
#             if user2:
#                 energy2=energy2-user2
#             elif energy2=='0':
#                 break
#
# a=Attack.get_att()
#

class Attack:
    """People lose their energy"""
    def __init__(self, tak, giv):
        """Energy lose"""
        self.tak = tak
        self.giv = giv

    def get_att(self):
        energy1 = 200
        energy2 = 300
        while True:
            user1 = int(input("Zarbani miqdorini kiriting>>> "))
            if user1:
                energy1 -= user1
                print(f"User1 energiyasi: {energy1}")



            if energy1 <= 0:
                print("User1 mag‘lub bo‘ldi!")
                break

            user2 = int(input("Zarbani miqdorini kiriting>>> "))
            if user2:
                energy2 -= user2
                print(f"User2 energiyasi: {energy2}")
            if energy2 <= 0:
                print("User2 mag‘lub bo‘ldi!")
                break


attack = Attack("Take energy", "Give energy")
attack.get_att()




