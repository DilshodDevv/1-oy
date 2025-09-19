"""
10-dars
3,27,2025
MAVZU:BIR NECHA SHARTLARNI TEKSHIRISH
MUALLIF: DILSHOD OCHILOV
"""
# if-elif-else KETMA-KETLIGI
# Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin. Bunday holatda biz if-elif-else ketma-ketligidan
# foydalanamiz. elif - else va if so'zalrining jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi. Bunday if bilan
# boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin.
# Python avval if shartini tekshiradi, shart bajarilmasa elif ga o('tadi, birinchi elif sharti bajarilmasa keyingi elif ga'
#  o')tadi va hokazo davom etaveradi.
# Diqqat!if -elif - else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.
#Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan
# 4 yoshdan kichik bolallarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000
# 12 yosshdan kattalarga 10000
#Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
#
# print(f"Sizga kirish {price} so'm")
# Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin. Misol uchun, hayvonot bog'i qariyalar
# uchun chegirma e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin:
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")
# AND, OR OPERATORLARI
# Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi bilan, Python qolgan shartlarni
# tekshirmaydi va ularni bajarmaydi. Lekin ba'zida biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz mumkin,
# buing uchun AND va OR operatorlaridan foydalanamiz
# or operatori ingliz tilidan yoki deb tarjima qilinadi ikki va undan ko'p shartlardan biri bajarilishini tekshirishda
# ishlatiladi.
# Quyidagi misolni ko'raylik, foydalanuvchidan hafta kunini so'raymiz va agar kun shanba yoki yakshanba bo'lsa, bugun
# dam olish kuni degan xabarni chiqaramiz, aks holda bugun ish kuni degan xabarni chiqaramiz:
# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')
# AND OPERATORI
# and ingliz tilidan va degan manoni anglatadi va ikki  va undan kup shartlarni barchasi tekshirishda  ishlatiladi
#AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, agar shartlardan biri
# bajarilmay qolsa ham FALSE qiymati qaytadi.
# # kun = input("Bugun nima kun?")
# # harorat = float(input("Havo harorati qanday?"))
# # if kun.lower()=='yakshanba' and harorat>=30:
# #     print("Cho'milgani ketdik!")
# # elif kun.lower()=='yakshanba' and harorat<30:
# #     print("Uyda dam olamiz!")
# # else:
# #     print("ishlaymiz")
# # BIR NECHTA SHARTLARNI KETMA-KET YOZISH
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")
#BOOLEAN MA'LUMOTLAR TURI
#Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini ko'rdik. Bu qiymatlar
# boolean (mantiqiy) qiymatlar deb ataladi, va dasturlashda juda keng qo'llaniladi. Pythonda o'zgaruvchilarda boolean
# qiymatlarni ham saqlash mumkin.
#Quyidagi dasturga e'tibor bering. Deylik, restoranimizga kelgan mijoz 15000 so'mlik taom oldi, biz mijoz qo'shimcha
# choy va salat ham olgan (olmaganiga) qarab ularning narhini ham  yakuniy narhga qo'shishimiz kerak. Mijozning choy
# yoki salat olgan (olmaganini) biz TRUE va FALSE qiymatlari bilan belgiladik.
# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi
#
# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
#
# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz
# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi
#
# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
#
# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz
#RO'YXAT TARKIBINI TEKSHIRISH
#in OPERATORI
#in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'osh' in menu # menu da osh bormi?
#not in OPERATORI
# not in operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' not in menu # menu da manti yo'qmi?
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'osh' not in menu # menu da osh yo'qmi?
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')
#IKKI RO'YXATNI SOLISHTIRISH
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
#RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")




