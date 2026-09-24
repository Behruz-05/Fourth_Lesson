# ismlar = ['Ali', 'Behruz', 'Muhammad', 'Sardorbek', 'Shahboz']
#
# print(ismlar)

import random

ismlar = ['Akbar', 'Jasur', 'Navruz', 'Azimbek', 'Sherzod']

del ismlar[3]

tanlangan_ism = random.choice(ismlar)
tanlangan_ism2 = random.choice(ismlar)
print("Salom", tanlangan_ism, "bugun choyxona bormi?")
print(tanlangan_ism2, "choyxonaga boramizmi?")

sonlar = [5, 45, 3, 43, 6]

randomnumber = random.choice(sonlar)
randomnumber2 = random.choice(sonlar)

print(randomnumber+randomnumber2)

print(randomnumber-randomnumber2)

print(randomnumber*randomnumber2)

print(randomnumber/randomnumber2)
