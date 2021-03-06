# bu iki satır console ekranını temizlemek için
import os
os.system("cls") 

print("Bu program girdiğiniz sayının tek mi çift mi olduğunu söyler.")

# sayı tek mi çift mi
sayi = int(input("Sayı: "))

if sayi % 2 == 0:
    print("çift")
else:
    print("tek")