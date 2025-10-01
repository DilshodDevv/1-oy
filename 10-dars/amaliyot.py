"""
10-dars
3,27,2025
MAVZU:BIR NECHA SHARTLSRNI TEKSHIRISH
MUALLIF: DILSHOD OCHILOV
"""
# son = int(input("juft son kiritingf "))
# if son%2==0:
#     print("rahmat")
# else:
#     print("siz toq son kirittingiz")
# yosh = int(input("yoshingizni kiriting "))
# if yosh <= 4 or yosh > 60:
#     print("sizga kirish tekin")
# elif yosh<18:
#     print("sizga kirish 10000 so'm")
# elif yosh<=18:
#     print("sizga kirish 20000 so'm")
# print ("ikkita son kiriting")
# a = int(input("a = "))
# b = int(input("b = "))
# if a== b :
#     print("sonlar teng")
# elif a> b:
#     print("a katta")
# else:
#     print("b katta")
# mahsulotlar=['pamidor','piyoz','sabzi','balgariski','sarimsoq piyoz','sholgom','choy','qalampir','sut','gusht','chakki']
# savat=[]
# for savatga in range(5):
#     savat.append(input(f"savatga {savatga+1} ninchi maqhsulotni kiritingiz "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"dukonda mahsulot bor{mahsulot}")
#     else:
#         print(f"dukonda {mahsulot} yuq")
# foydalanuvchilar = ['dilshod','bektosh','shahzod','islom','saddi']
# yangi = input("yangi login kiriting\n>>>")
# if yangi in foydalanuvchilar:
#     print("Login band")
# else:
#     print("Xush kelibsiz foydalanuvchi")
son = int(input("biror son kiriting"))
for n in range(2,11):
    if not (son%n):
        print(f"{son} son {n} ga qoldiqsiz bulinadi")

