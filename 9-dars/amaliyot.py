"""
3,21,2025
9-dars
MAVZU:IF ELSE
MUALLIF:DILSHOD OCHILOV
"""
# cars = ['toyota', 'mazda' , 'huyundai', 'gm', 'kia']
# for moshin in  cars:
#     if moshin == "gm":
#         print(moshin.upper())
#     else:
#         print(moshin.title())
# xonadoshlar = ['dilshod' , 'burhoniddin' , 'shahzod' , 'diyor']
# for aka in xonadoshlar:
#     if aka == "diyor":
#         print(aka.title() , 'aka')
#     else:
#         print(aka.title())
# cars=['toyota' ,'mazda' ,'huyundai' ,'gm' ,'kia']
# for moshin in cars:
#     if moshin !="gm":
#         print(moshin.title())
#     else:
#         print(moshin.upper())
# membir = input("loginingizni kiriting>>>\n")
# if membir.lower()=="admin":
#     print("Xush kelibsiz Admin .Foydalanuvchilar ro'yxatini kurasizmi?")
# else:
#     print(f"xush kelibsiz , {membir} ")
# x = float(input("birinchi sonni kiriting\n>>>"))
# y = float(input("ikkinchi sonni kiriting\n>>>"))
# if x==y :
#     print("sonlar teng ", x ," = ",y)
# else:
#     print(f"sonlar teng emas")
# son = int(input("istalgan son kiriting\n>>>"))
# if son < 0:
#     print("manfiy")
# elif son>0:
#     print("musbat")
# else:
#     print("0")
# son = int(input("istalgan son kiriting\n>>>"))
# if son>0 :
#     print(f"sonning kivadrati {son**2}")
# elif son<0:
#     print("musbat son kiriting")
# else:
#     print(0)
cars =["toyota ","mazda ", "hyundai ","gm ","kia"]
for car in cars :
    if car == "kia":
        print(car.upper())
    else:
        print(car.title())
for car in cars :
    if car!= "kia":
        print(car.title())
    else:
        print(car.upper())
login = input("\n>>>")
print(f"iltimos loginingizni kiriting {login}")
if login=="admin":
    print("Xush kelibsiz, admin .foydalanuvchilar ruyhatini kurasizmi?")
else:
    print(f"Xush kelibsiz {login}")
a = float(input("iltimos birinchi sonni kiriting\n>>>"))
b = float(input("iltimos ikkinchi sonni kiriting\n>>>"))
if a==b:
    print("ikkisi teng")
elif a>b:
    print("a katta b dan")
else:
    print("a b dan kichkina")
a= int(input("istalgan sonni kiriting\n>>>"))
if a<0:
    print("son manfiy")
else:
    print("son musbat")
son=int(input("son kiriting"))
if son<0:
    print("musbat son kiriting")
else:
    print(f"ildizi{(son)**(1/2)}")

