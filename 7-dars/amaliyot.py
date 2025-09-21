"""
3,9,2025
7-dars
MAVZU: RUYHATLAR BILAN ISHLASH
MUALLIF: OCHILOV DILSHOD
"""
# davlatlar = ["O'zbekiston",'Qozogizton','Turkmaniston','Tojikiston',"Qirg'iziston"]
# print(davlatlar)
# print(len(davlatlar))
# tartib = sorted(davlatlar)
# print(tartib)
# teskari = sorted(davlatlar, reverse=True)
# print(teskari)
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# juft_sonlar = list(range(120,1200,2))
# print(juft_sonlar)
# print(sum(juft_sonlar))
# print((max(juft_sonlar) + min(juft_sonlar))//2)
# print(len(juft_sonlar))
# print('boshidan ', juft_sonlar[:20],' urtasidan ',juft_sonlar[530:550],' oxiridan ',juft_sonlar[-20:])
# taomlar=['manti','shurva','qaymoq','qatiq','yahna']
# nonushta = taomlar[:]
# nonushta.remove('shurva')
# nonushta.remove('qaymoq')
# nonushta.remove('yahna')
# nonushta.append('choy')
# nonushta.append('saryog')
# nonushta=tuple(nonushta)
# nonushta = list(nonushta)
# nonushta[0]="quymoq va non "
#
# nonushta = tuple(nonushta)
# print(taomlar)
# print(nonushta)
#
# ismlar=['Shahzod ,Burhon ,Diyor ']
# print("salom" + ismlar[0] +"bugun choyxona bormi ?" )
ismlar = ["elbek","islom ","shahzod "]
print("salom "+ismlar[0], ", bugun choyxona bormi?" +ismlar[1] ," choyxonaga boramizmi" " nimaga limsan ",ismlar[2])
sonlar = [12,23,34,-34,3.5]
sonlar[0]= sonlar[0]+sonlar[-1]
sonlar [1]=sonlar[0]+2
sonlar[4]=sonlar[1]*sonlar[-2]
del sonlar[3]
print(sonlar)
del sonlar[0]
print(sonlar)
t_shaxs=["Temur","al-Xorazmiy","Navoiy"]
z_shaxs=["Mask","tramp","shavkat"]
print(f"men zamonaviy shaxslardan  {z_shaxs.pop(1)},tarixiy shaxslardan ,{t_shaxs.pop(0)}")
frends=[]
frends.append("islom")
frends.append("shahzod")
frends.append("elbek")
frends.append("sardor")
frends.append("asilbek")
print(frends)
frends.remove("elbek")
frends.remove("asilbek")
print(frends)
frends.insert(0,"diyor")
frends.insert(2,"temur")
frends.insert(-1,"shuh")
print(frends)
mehmonlarr =[]
mehmonlarr.append(frends.pop(0))
mehmonlarr.append(frends.pop(1))
mehmonlarr.append(frends.pop(3))
print("\n kelgan mehmoonlar", mehmonlarr)
mamlakat = ["O'zbekiston ", "Qozog'iston ", "Tojikiston ","Rossiya ","Amerka"]
print(mamlakat)
print(len(mamlakat))
print(sorted(mamlakat))
print(sorted(mamlakat ,reverse = True))
print(mamlakat)
mamlakat.reverse()
print(mamlakat)
mamlakat.sort()
print(mamlakat)
mamlakat.sort(reverse=True)
print(mamlakat)
sonlar=list(range(120,1200,2))
print(sonlar)
len(sonlar)
print(len(sonlar))
print(sum(sonlar))
print(max(sonlar)- min(sonlar))
print(len(sonlar))
print(sonlar[0:20])
print(sonlar[260:280])
print(sonlar[520:])
taomlar=["honim","somsa","shurva","jiz","yahna"]
nonushta=taomlar[:]
nonushta.remove("yahna")
nonushta.remove("jiz")
nonushta.remove("honim")
print(nonushta)
nonushta.append("choy")
nonushta.append("coffe")
print(nonushta)
nonushta=tuple(nonushta)
print(taomlar)
print(nonushta)
nonushta=list(nonushta)
nonushta[0]="qaymoq va non"
print(nonushta)
nonushta = tuple(nonushta)

