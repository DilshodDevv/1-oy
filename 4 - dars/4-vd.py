"""
3.1.2025
4-dars
Mavzu: STRING (MATN)
Muallif : Dilshod Ochilov
"""
shahar = "hohlagan alifbodan foydalansa buladi"
matn = " Men yangi 📱 oldim"
print ( matn )
ism = "Ahmad"
print( " Mening ismim " + ism )
ism = "Ahad"
familiya = 'Qayum'
print(ism + familiya)
ism = ' Ahad '
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qushish
# f-string
ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)
ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
#Mtinga bushliq qushish uchun \t belgisidan , yangi qatordan boshlash uchun \n belgisidan foydalanamiz
print(' Hello World ')
print( ' hello \t world')
print( ' Hello \n World')
#Pythtonda string ustida amalfa oshirish mukun bulgan tayyor amallar tuplami mavjud . Bunday amallar  to'plami metodlar
# deb ataladi
#Metodlarni qullash uchun metod nomi matndan sung .metod_nomi()ko'rinishida yoziladi
#Keling bunnday metoodlarning ba'zilari bilan tanishaylik
#upper() va lower() METODLARI
#upper() metodi matinning har bir harifini katta harifga uzgartiradi.
ism = " Ahad "
familiya = 'Qayum'
ism_sharif = f" {ism} {familiya}"
print(ism_sharif.upper())
#lower() metodi esa aksincha , har bir harifini kichik  harifga o'zgartiradi.
ism = 'Ahad'
familiya =  'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())
#title() va capitalize() METODLARI
#title() metodi matindagi har bir so'zning birinchi harifini katta harf bilan yoziladi
ism_sharif = 'james bond'
print(ism_sharif.title())
#capitalize() esa faqatgina eng birinch so'zining birinchi harfini katta bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.capitalize())
#strep(),rstrep()va lstrep() METODLARI
# bu metodlar matinning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#lstrep() - matn boshidagi bushliqni olib tashlaydi
#rstrep() - matn oxiridagi bushliqni olib tashlaydi
#strep() - matn boshi va oxiridagi bo'shliqni olib tashlaydi
meva = "    olma   "
print("Men " + meva.lstrip() + ' yaxshi kuraman')
print("Men " + meva.rstrip() + " yaxshi kuraman")
print("Men " + meva.strip() + " yaxshi kuraman")
print("Men " + meva + " yaxshi kuraman")
# INPUT - FOYDALANUVCHI BILAN MULOQOT
#Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichiga berayotgan edik.
#Keling endi qiymatni uzimiz emas , balki dastur foydalanuvchilariga kirish imkonini beramiz.
#Buning uchun input() funksiyasidan foydalanamiz
ism = input("Ismingiz  nima ?")
print("Assalomu alaykum, " + ism)
#Yuqoridagi dastur , avval 1-qatorda foydalanuvchining ismini suraydi . Foydalanuvchi ismini kiritib ,Enter tugmasini
#bosgach , foydalanuvchi kiritgan matn ism degan o'zgaruvchiga yuklanadi va dasturining 2-qatorida bajariladi:
ism = input("Ismingiz nima?\n >>>")#foydalanuvchi ismini yagi qatorga kiritadi.
print("Assalomu alaykum, " + ism.title())