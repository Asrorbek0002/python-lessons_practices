# funksiya nima funksiyalar bir kodni Qayta qayta yozmaslik uchun ishni osonlashtiradi

# funksiya yaratamiz oddiy salom ber

# def sal_ber():
#     """Salom beruvchi funsiya"""
#     print('Assalomu aleykum')
#
# sal_ber()

# funksiyaga qiymat uzatish

# def salm_ber(ism):
#     """Foydalanuchi ismini qabul qilib ,unga ismi bilan qaytaradi"""
#     print(f"Assalomu aleykum hurmatli ,{ism.title()}")
#
# salm_ber('hasan')
# salm_ber('asror')
#

# Docstring biz har bir yaratgan funksiyaga tarif berish kerak agar biz boshqalar yaratgan funksiya nima vazifa bajarishini bilmoqchi bolsak docstringdan foydalanamiz

#print(salm_ber.__doc__)
# print(print.__doc__)
# print(type.__doc__)


# funksiyaga bir necha bor murojat qilish

# def son_top(first,second):
#     """
#     Funksiyaga bir necha bor murojat qilsh
#     """
#     print(f"{first} and {second}")
#
# son_top(3,5)
# son_top(3,0)

# argument va parametr FUNKsiya yaratishda qoyilgan elementlar parametr deb ataladi argument esa funksiya ichigA beriladi

#
# """
# bazi bir daslikda yoki darslarda ikkovini ham o\'rni almashtiriladi
#
# """
# """
# funksiyaga to\'gri tartibda argument uzatish
#
# """
# def tolq_ism(ism,familya):
#     """
#     Toliq ism qaytaruvchi dastur
#     :param ism:
#     :param familya:
#     :return:
#     """
#     print(f"Foydalanuvchi ismi:{ism.title()} \n"
#           f"Foydalanuvchi familyasi:{familya.title()}")
#
# tolq_ism('asror','abdurazoqov')
# tolq_ism('abdurazoqov','asror')
#
#
# def yosh(ism,tyil):
#     """
#     Foydalanuvchini yoshini qaytuvchi dastur
#     :param ism:
#     :param tyil:
#     :return:
#     """
#     print(f"{ism.title()} {2025-tyil} yoshda")
#
#
# yosh('asror',2000)
#
# #yosh(2000,'asror')
#
#
# """
# buni oldini olish uchun kalit soz orqali uzatishimiz mumkin
#
# """
# tolq_ism(familya='abdurazoqov',ism='asror')
# yosh(tyil=2000,ism='asror')
#

"""
standart qiymat uzatish parameter oldiga qiymat ham qoyiladi va standart qiymat har doim oxirga qoyidadi agar hatolik beradi

"""

# def yosh_hisb(tyil,joriy_yil=2025):
#     """
#     Foydalanuvchini yoshini hisoblaydigan dastur
#     :param tyil:
#     :param joriy_yil:
#     :return:
#     """
#     print(f"Siz {joriy_yil-tyil} da ekansiz")
# yosh_hisb(2000,2025)
#
#
# yosh_hisb(2005)
#

"""
qiymat qaytaruvchi funksiya 
i mean "return"
"""

# funkiyadan oddiy qiymat qaytarish
# def toliq_ism(ism,familya):
#     """Foydalanuvchini toliq ismini qaytarish"""
#     toliq_ism=f"{ism} {familya}"
#     return toliq_ism      # bizda retern shu toliq ismni qaytaradi
#
# talaba1=toliq_ism('asror','abdurazoqov')
# talaba2=toliq_ism('asilbek','abdurazoqov')
# print(f"Bugun darsga {talaba1.title()} va {talaba2.title()} keldi")
#

# ixtiyoriy argumentlar funksiyaga ixtiyoriy argument berish

# def toliq_ism_yasa(ism,familya,otasining_ismi=''):
#     """"Foydalanuvchini toliq ismini bilish dasturi"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {familya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familya}"
#     return toliq_ism.title()
#
# talaba1=toliq_ism_yasa('ali','hasanov')
# talaba2=toliq_ism_yasa('asrorbek','abdurazoqov','abdunazar o\'g\'li')
#
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")
#

#funksiyadan lugat yaratamiz
# def avto_info(kompanya,model,rang,korobka,yili,narhi=None):
#     avto={
#         'kompaniya':kompanya,
#         'model':model,
#         'rang':rang,
#         'korobka':korobka,
#         'yil':yili,
#         'narh':narhi
#
#     }
#
#     return avto
#
# avto1=avto_info('GM','Malibu','oq','avtomat',2021)
# avto2=avto_info('GM','Kobolt','qora','avtomat',2020,54000)
#
# avtos=[avto1,avto2]
# print("Only bozordagi movjud avtolar ro'yhati")
# for avto in avtos:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh="Nomalum"
#
#     print(f"{avto['rang'].title()} {avto['model']}. Narhi: {narh}")




#funksiyadan royhat yaratish

# def oraliq(min,max,step=2):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=step
#     return sonlar
#
# print(oraliq(1,10,2))
# print(oraliq(10,100,2))
#
#
# # funksiyalarni tsklda ishlatish
#
# print("Salimizdagi avtolar roytini shakilantiramiz")
# avtolar=[]
# while True:
#     print("Quyidagi malumotni kiriting")
#     kompaniya=input('Ishlab chiqaruvchi:')
#     model=input('model')
#     rang=input('rang')
#     korobka=input('korobka')
#     yil=input('yil')
#     narh=input('narh')
#     avtolar.append(avto_info(kompaniya,model,rang,korobka,yil,narh))
#     javob=input('Yana avto qo\'shasizmi')
#     if javob=='no':
#         break
#     else:
#         continue
#
# print(avtolar)


# funksiya va list

# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"{ism.title()}ning bahosini kiriting >>>")
#         baholar[ism]=baho
#     return baholar
#
# talabalar=['ali','vali','hasan','husan','botir']
# baholar=bahola(talabalar[:])
# print(baholar)
#
# # royhatga ozgartirish kiritish
#
# print(talabalar)
# # asl royhatga ozgartirish kiritishni oldinni olish
#

# talabalar=['ali','vali','hasan','husan','botir']
# baholar=bahola(talabalar[:])
# print(baholar)
# print(talabalar)












