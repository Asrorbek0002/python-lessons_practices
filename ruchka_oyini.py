# class Play:
#     """User1 klass"""
#     def __init__(self,play)
#         self.play=play
#
#     dt_turn1(self)
n=10
navbat = True
while True:

    if navbat == True:
        son = int(input(f"User1 can enter your options from {n}>>>"))
        if son>0 and son<4:
             n-=son
             son = 0
             navbat = False
        else: continue

    if navbat == False:
        son = int(input(f"User2 can enter your options from {n}>>>"))
        if son > 0 and son < 4:
            n -= son
            son = 0
            navbat = True
        else:
            continue
    # if n==0:
    #     print("User1 won in this compitetion")
    #     break
    # qiy2=int(input(f"User2 can enter your options from {n}>>>"))
    # if qiy2>=4 or qiy2<=0:
    #     continue
    # n-=qiy2
    # if n==0:
    #     print("User2 won in this compitetion")
    #     break














