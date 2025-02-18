# import random as r
# son=r.randint(0,10)
# print(son)
# ishora=True
# while ishora:
#     qiy=int(input('>>>'))
#     if qiy>son:
#         print("You win in this match")
#         break
#     else:
#         print("You did not win")




# import random as r
#
# def oyin(x):
#     n=0
#     start=1
#     end=x
#     tax=r.randint(start,end)
#     print("Keling oylangan sonni topish o'ynaymiz")
#     print(f"Men {start} dan {end} gacha son o'yladim topa olsizmi")
#     ishora=True
#     while ishora:
#         n+=1
#         qiy=int(input('>>>'))
#         if qiy>tax:
#             print("Xato,men o'ylagan son bundan kichik")
#         elif qiy<tax:
#             print("Xato, men oylagan son bundan katta")
#         else:
#             print(f"TOPDINGIZ, men {tax}  sonni oylagan edim {n} ta taxmin bilan topdingiz")
#             ishora=False
#
#     return n
#
# print(oyin(10))
#
# def kom_oyin(x):
#     start=1
#     end=x
#     print(f" Siz {start} dan {end} gacha son oylang ,men topishga harakat qilaman")
#     input("Biror son oylagan bolsangiz biror tugmani bosing>>>")
#     n1=0
#     ishora=True
#     while ishora:
#         n1+=1
#         if start!=end:
#             tax2=r.randint(start,end)
#         else:
#             tax2=start
#         qiy2=input(f"Siz {tax2} ni o\'yladiz agar men o'ylagan son siz o\'ylagan sondan katta bo'lsa '+' aks holda '-' teng bo'lsa 't' ")
#         if qiy2=='+':
#              start=tax2+1
#         elif qiy2=='-':
#             end=tax2-1
#         elif qiy2=='t':
#             print(f"Siz yutdingiz {n1} ta taxmin bilan")
#             ishora=False
#
#     return n1
#
# print(kom_oyin(10))
#
















