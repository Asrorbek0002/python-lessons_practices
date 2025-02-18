# a= 'hello world'
# print(a)
# print(f"Amerikalik odamlar har doim {a} deb aytadi")
import random as r
def sontop(x=10):
    n=0
    start=1
    end=x
    taxmin1=r.randint(start,end)
    print("Keling o'ylagan sonni topish o'ynaymiz")
    print(f"{start} dan {x} gacha son o'ylayman .Topa olasizmi")
    ishora=True
    while ishora:
        qiymat1=int(input(">>>"))
        n+=1
        if qiymat1>taxmin1:
            print("Xato, men o'ylagan son bundan kichikroq.Yana harakat qiling ")
        elif qiymat1<taxmin1:
            print("Xato, men o'ylagan son bundan kattaroq.Yana harakat qiling ")
        else:
            print(f"TOPDINGIZ! {taxmin1} sonini o'ylagan edim .{n} ta taxmin bilan topdingiz")
            ishora=False
    return n


def sontop_com(x=10):
    n2=0
    start=1
    end=x
    print(f"{start} dan {end} gacha son o'ylang.Men topishga harakat qilaman")
    input("Son oylagan bolsangiz biror tugmani bosing>>>")
    ishora=True
    while ishora:
        n2+=1
        if start!=end:
            taxmin2=r.randint(start,end)
        else:
            taxmin2=start
        qiymat2=input(f"Siz {taxmin2} sonnini o'yladingiz:to'g'ri (t),"
                      f"men o'ylagan son bundan katta bolsa (+),yoki kichik (-)???>>>")
        if qiymat2=="+":
            start=taxmin2+1
        elif qiymat2=="-":
            end=taxmin2-1
        elif qiymat2=="t":
            print(f"Siz {taxmin2} sonini o'yladingiz va men {n2} ta tahmin bilan topdim")
            ishora=False
    return n2


def play(x=10):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_com=sontop_com(x)
        if taxminlar_user>taxminlar_com:
            print("Men yutdim")
        elif taxminlar_com>taxminlar_user:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana=int(input("Yana o'ynaysizmi, ha(1)/yo'q(0)"))
play()