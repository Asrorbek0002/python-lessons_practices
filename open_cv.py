# import cv2
#
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
# while True:
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]
#
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
#
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#



# import random as r
#
# def sontop(x=10):
#     n=0
#     start=1
#     end=x
#     taxmin1=r.randint(start,end)
#     print("Keling o'ylagan sonni topish o'ynaymiz")
#     print(f"{start} dan {x} gacha son o'ylayman .Topa olasizmi")
#     ishora=True
#     while ishora:
#         qiymat1=int(input(">>>"))
#         n+=1
#         if qiymat1>taxmin1:
#             print("Xato, men o'ylagan son bundan kichikroq.Yana harakat qiling ")
#         elif qiymat1<taxmin1:
#             print("Xato, men o'ylagan son bundan kattaroq.Yana harakat qiling ")
#         else:
#             print(f"TOPDINGIZ! {taxmin1} sonini o'ylagan edim .{n} ta taxmin bilan topdingiz")
#             ishora=False
#     return n
#
#
# def sontop_com(x=10):
#     n2=0
#     start=1
#     end=x
#     print(f"{start} dan {end} gacha son o'ylang.Men topishga harakat qilaman")
#     input("Son oylagan bolsangiz biror tugmani bosing>>>")
#     ishora=True
#     while ishora:
#         n2+=1
#         if start!=end:
#             taxmin2=r.randint(start,end)
#         else:
#             taxmin2=start
#         qiymat2=input(f"Siz {taxmin2} sonnini o'yladingiz:to'g'ri (t),"
#                       f"men o'ylagan son bundan katta bolsa (+),yoki kichik (-)???>>>")
#         if qiymat2=="+":
#             start=taxmin2+1
#         elif qiymat2=="-":
#             end=taxmin2-1
#         elif qiymat2=="t":
#             print(f"Siz {taxmin2} sonini o'yladingiz va men {n2} ta tahmin bilan topdim")
#             ishora=False
#     return n2
#
#
# def play(x=10):
#     yana=True
#     while yana:
#         taxminlar_user=sontop(x)
#         taxminlar_com=sontop_com(x)
#         if taxminlar_user>taxminlar_com:
#             print("Men yutdim")
#         elif taxminlar_com>taxminlar_user:
#             print("Siz yutdingiz")
#         else:
#             print("Durrang")
#         yana=int(input("Yana o'ynaysizmi, ha(1)/yo'q(0)"))
#
# play()
#


































