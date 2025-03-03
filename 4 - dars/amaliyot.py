"""
3.1.2025
4-dars
MAVZU: SRTING(MATN)
MUALLIF:DILSHOD OCHILOV
"""
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + ' ' +"ko'chasi ,", mahalla + ' ' + "mahallasi ," , tuman + ' ' + "tumani ,", viloyat + ' ' +"viloyati ," )
print ( 'Iltimos quyidagi malumotlarni kiriting ')
kocha = input('Kuchangizni?\n>>>')
mahalla = input(" Mahallangiz?\n>>>")
tuman = input(" tumaningiz?\n>>>")
viloyat = input(" viloyatingiz?\n>>>")
print(kocha + ' ' + "ko'chasi,", mahalla + ' ' + "mahallasi,", tuman + ' ' + "tumani,", viloyat + ' ' + "viloyati")
# print ( 'Iltimos quyidagi malumotlarni kiriting ')
kocha = input('Kuchangizni?\n>>>')
mahalla = input(" Mahallangiz?\n>>>")
tuman = input(" tumaningiz?\n>>>")
viloyat = input(" viloyatingiz?\n>>>")
print(kocha + ' ' + "ko'chasi,\n", mahalla + ' ' + "mahallasi,\n", tuman + ' ' + "tumani,\n",
      viloyat + ' ' + "viloyati")
manzil = f"{kocha} kuchasi ,{mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati "
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
x = input("ismingi,\n>>>")
print(x.capitalize())