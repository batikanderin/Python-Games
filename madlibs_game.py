
from random import choice
#Rastgele sayilarla dictionary iceresinde secebilmek icin choiceu cagirdik.
a = choice(range(0,5))
v = choice(range(0,5))
v2 = choice(range(0,5))
f = choice(range(0,5))

#Rastgele kelimeler sececegimiz dictioaryi olusturduk
Words = {
    'adj': ['yakisikli','cirkin','cekici','hos','alimli'],
    'verb': ['yuru','kos','gel','git','uc'],
    'verb2': ['bak','yuz','zipla','atla','bayil'],
    'famous_person': ['messi','ronaldo','neymar','balotelli','belhanda']
}

#Cumle icresindeki bosluklari dictonary iceresinden rastgele cagiracagimiz cumlemizi yazdik.
Cumle=f"Kim {Words['famous_person'][f]} gibi olmak istemez ki. Onun gibi {Words['adj'][a]} ve {Words['adj'][f]}.\
Ama onun gibi olmak icin surekli {Words['verb'][v]} yapmak ve {Words['verb2'][v2]} yapmak gerekir. "

print(Cumle)
