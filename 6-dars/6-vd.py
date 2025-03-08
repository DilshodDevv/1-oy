"""
3,8,2025
6-dars
Mavzu:List(ruyhat)
MUALLIF:Dilshod Ochilov
"""
# mevalar =['olma', 'anjir', 'shaftoli', 'o\'rik']#mevalar ruyhati (natinlar)
# narhlar =[12000, 18000, 10900, 22000]#narhlar ruyhati (sonlar)
# sonlar =['bir', 'ikki', 3, 4, 5]# sonlar va matinlar aralash ruyhat
# ismlar =[] # bo'sh ruyhat
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("birinchi meva :" , mevalar[0])
# print("ikkinchi meva :" , mevalar[1])
# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("birinchi meva: ", mevalar[0].title())
# print("ikkinchi meva: ", mevalar[1].upper())
# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])
# print(narhlar[1]+30000)
# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin.
# Bu usul Listning uzunligini bilmaganda juda asqotadi.
# car_models = ['Toyata', 'GM', 'Volvo', 'BMW', 'Huyunday', 'Kia', 'Volkisvogen']
# print(car_models[-1])#Listning eng oxirgi elimentiga -1 bilan murojat qilishimiz mumkin
#ELIMINTLARNI UZGARTIRISH
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0]  = 13000# 1-qiymatni 13000 ga uzgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga uzgartizamiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatnga 2000 qushamiz
# print ( narhlar )
#YANGI ELIMENT QUSHISH
#.append() metodi
#Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
# mevalar = [ 'olma ', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz")#mevalarga tarvuzni qushamiz
# print (mevalar)
# cars= [] #bush ruyhat yaratamiz
# cars.append('Lacceti')#ruyhatga qushib olamiz
# cars.append('Nexia 3')
# cars.append('Cobolit')
# print(cars)
#.insert()metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz.
# .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
# cars = ['Lacetti', 'Nexa 3', 'Cobolit']
# cars.insert(0, 'Mallubu')#birinchi o'rindagisiga yangi qiymat qushamiz
# print(cars)
# cars.insert(2, 'Damas')#3- urindagisiga yangi qiymat qushamiz
# print(cars)
#Elementni o'chirish
#Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik ', 'anor']
# del mevalar[1] # 2- elementni uchirib tashlaydi
# print(mevalar)
#.remove(qiymat)
#Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.
#Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')# Ruyxatdan shaftolini uchiradi
# print(mevalar)
# hayvonlar = ['it', 'mushuk', 'sigir', "qo'y", 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ruyhatta 2 ta mushuk bor , ulardan birinchisini o'chiradi
# print(hayvonlar)
# Elementlarni sug'urib olish'
# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab
# qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
#.pop(indeks)
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)#Ruyhatdan banani sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("olinmagan mahsulotlat : ", bozorlik)




