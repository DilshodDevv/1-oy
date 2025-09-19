"""
3,9,2025
7-dars
MAVZU : RUYHATLAR BILAN ISHLASH
MUALLIF : DILSHOD OCHILOV
"""
#.sort()
#cars = ['bmw', 'mersades benz', 'volvo', 'geniral motors', 'tesla', 'audi']
#cars.sort()
#print(cars)
# cars = ['Bmw', 'mersades benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)
# Aksar holatlarda ro('yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. '
# Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.)
#Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
# cars = ['bmw', 'mercidez benz', 'gm', 'volvo', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
# cars = ['Bmw', 'mercidez benz', 'gm', 'volvo', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
#.sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro('yxat ichidagi elementlarning ketma-ketligini buzmagan holda '
#'ro')yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
#mehmonlar = [ 'Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytsrgan ruyhat:", sorted(mehmonlar))
# print(mehmonlar)
#sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
#print(sorted(mehmonlar,reverse=True))
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
#Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin.
#Buning uchun .reverse() metodidan foydalanamiz.
# fruits = ['pear', 'banan', 'apple', 'waremelon', 'lemon']
# fruits.reverse()
# print(fruits)
# fruts = ['pear', 'banan', 'apple','watermelon', 'lemon' ]
# print("elementlar soni:", len(fruits)) #len(fruits) ruyxat uzunligini qaytaradi
#Bu funktsiya yordamida biz ma('lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funktsiyasi yordamida '
#esa bu oraliqni ro')yxat shaklida saqlab olamiz:
# sonlar = list(range(0,10))
# print(sonlar)
#range() yordamida qadamni ham berishimiz mumkin:
# juft_sonlar = list(range(0,20,2)) # o dan 20 gacha 2 qadam  bilan sanaaydi
# toq_sonnlar = list(range(1,20,2)) # 1 dan 20 ga cha 2 qadamdan sanaydi
# print("juft  sonlar: ", juft_sonlar)
# print("toq sonlar : ", toq_sonnlar)
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun ro('yxatdagi eng kichik sonni topish '
# uchun min() funktsiyasidan, eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig(')indisini topish uchun'
#                              esa sum() funktsyasidan foydalansak bo')ladi:
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat= max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami:", jami)
#RUYHATNI KESISH
# cars = ['bmw', 'mersades benz','volvo','general motors', "tesla", 'audi']
# my_cars = cars[0:3] #0-indeksdan boshlab 3 ta element ajratib olamiz
# print(my_cars)
# print(cars[2:5]) #2-3-4-elementlarni ajratib olamiz
# print(cars[:4])# Ruyhat booshidan 4- gacha kesadi (0,1,2,3)
# print(cars[2:])# 2- elementdan boshlab ruyhat ohirigacha kesib oladi
#RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5]#sonlar degan ruyhat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ruyhatni sonlar ga tenglaymiz
# sonlar2.append(6)#sonlar2 ga 6 ni quushamiz
# sonlar2.append(7)#sonlar2 ga 7 ni qushamiz
# print('Bu sonlar ruyhati:', sonlar)
# print('bu sonlar2 ruyhati', sonlar2)
# sonlar = [1, 2, 3, 4, 5] #sonlar degan ruyhatni yaratamiz
# sonlar2 = sonlar[:] #[:] ruyhatni tuliq kuchirib oladdi
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ruyhati:", sonlar)
# print("bu sonlar2 ruyhati:", sonlar2)
#TUPLES - O'ZGARMAS RO'YXAT
# Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. Pythonda bunday ro('yxatlar tuples'
#  deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, dastur boshida beriladi va so')ngra o'zgartirib bo('lmaydi.'
#  List dan farqli ravishda, Tuple e')lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# toys = ('bus', 'car','bear','dino', 'snake','lizart')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
#tuple ichida biron narsani uzgartirib bulmaydi!!!
# toys = ('bus', 'car', 'bear', 'dino', 'snake','lizart')
# toys = list(toys) # o'zgarmas ruyhatni oddiy ruyhatga  (list) aylantiramiz
# # Ruyhatga uzgartirishni kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ruyhatni qaytadan o'zgarmas ruyhatga (Tuple) uzgartiramiz
# print(toys)
