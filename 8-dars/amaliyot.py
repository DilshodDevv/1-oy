"""
3,12,2025
8-dars
MAVZU:FOR TAKRORLASH OPERATORI
MUALLIF: DILSHOD OCHILOV
"""
# ismlar = ['Diyor','Shahzod','Burhonidin','Dilshod','Islom']
# for n in ismlar:
#     print("Salom",n)
#     print("kod",len(ismlar),"marta takrorlandi")
# sonlar = list(range(11,100,2))
# for n in sonlar:
#   print(f"{n} ning kubi {n**3} ga teng")
# kinolar = []
# print("yoqtirgan 5 ta kinoyingizni kiriting")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino : "))
# print(kinolar)
# suhbat = int(input("bugun nechta odam bilan suhbatlashdingiz?>>>"))
# ismlar = []
# for k in range(suhbat):
#     ismlar.append(input(f"{k+1}-suhbat qilgan odamingiz kim edi: "))
#     print(ismlar)
ismlar = ["Ali ","Vali ","hasan ","husan ","shohruh "]
for ism in ismlar:
    print(ism)
for taklif in ismlar :
    print("salom "+ taklif)
    print(f"kod {len(ismlar)} marta takrorlandi")
sonlar=list(range(11,100,2))
print(sonlar)
for kubi in sonlar :
    print("kubi \n >>>" +str( kubi**3))
# kino=[]
# for kinolar in range(5) :
#     kino.append(input(f"{kinolar + 1} istalgan sevimli kinongizni kiriting"))
# print(kino)
suhbatlashganlar=[]
soni = int(input("bugun nechta odam bilan suhbatlashdiz\n>>>"))
for n in range(soni) :
    suhbatlashganlar.append(input(f"{n+1} - si"))
print(suhbatlashganlar)