print(3 + 4 * 5 / 2) #13 

# float bölmesi
print(10 / 3) # 3.3333333333333335

# tam sayı bölmesi
print(10 // 3) # 3

# 2 üzeri 3
print(2**3) #8

# 20'nin 7 ile bölümünden kalan
print(20 % 7) #6

# tüm operatörlerin listesi için bkz:
# https://www.w3schools.com/python/python_operators.asp

x = 3
x *= 3 # x'e onun 3 katını ata => 9

# kıyaslama operatörü
x = 87
IkiBasamakliMi = x > 9 and x < 100
print(IkiBasamakliMi)

# mantıksal operatör
metin = "keçiören"
# e ve i içerirse ve a içermezse 
sonuc = "e" in metin and \
        "i" in metin and \
        "a" not in metin
print(f"{metin} e ve i içerir ama a içermez: ", sonuc)

# Not: Yukarıda ters slash kullanmamızın amacı kodun devamının gelecek satırda olduğunu belirtmektir. Diğer dillerde olduğu gibi enter'a basarak yeni satırda kod yazmaya devam edemiyorsunuz. Bunu belirtmeniz gerekiyor.

# sayı 2ye ya da 3e bölünür mü
sayi = 33
sonuc = sayi % 2 == 0 or sayi % 3 == 0

# 2 nesne bellekte aynı mı
a = 3
b = 3
print(a is b) # değer tipi olduğu için True sonucunu verdi

a = ["ankara"]
b = ["ankara"]
print(a is b) # False listeler referans tipi olduğu için bellekte fiziksel olarak 2 ayrı adreste 2 ayrı liste tutulur yani a ve b farklı nesnelerdir
print(a == b) # True içeriğine bakıldı

# içinde mi operatörü
print("kara" in "ankara") # True
print(3 in [3, 5 ,7]) # True

# BITWISE OPERATÖR 
a = 5 # 0101
b = 9 # 1001
print(a | b) # 1101 : 13
print(a & b) # 0001 :  1

print(3 == "3") # False


