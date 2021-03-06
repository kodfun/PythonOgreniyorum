import random

# Bu program her çalıştığında zar atıp sonucunu söyler

zar = random.randrange(1, 7)
print("GELEN ZAR: ", zar)

# eğer 6 gelirse tebrik et
if zar == 6:
    print("TEBRİKLER!!! EN BÜYÜK ZAR GELDİ.")