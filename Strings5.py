# STRING METOTLARI
# https://www.w3schools.com/python/python_strings_methods.asp

s = "merhaba DÜNYA" 

print(s.capitalize())
print(s.upper())
print(s.lower())

print("01234567890123456789")
print("KODLUYORUM".center(20))
print("KODLUYORUM".center(20,"*"))

# KAÇ TANE A HARFİ GEÇİYOR?
s = "ankara"
print(s.count("a"))

# true ya da false döndürür
print(s.endswith("ra")) # ile biter mi
print(s.startswith("an")) # ile başlar mı

# sadece harf ve rakamdan mı oluşur
print("ankarağ123".isalnum()) # True
print("ankarağ123*".isalnum()) # False

# sadece harf mi
print("ankara".isalpha()) # True
print("ankara1".isalpha()) # False

# sadece sayılardan mı oluşuyor
print("a123".isnumeric()) # False
print("123".isnumeric()) # True 
print("123.22".isnumeric()) # False
print("½11".isnumeric()) # True

# sadece rakamlardan mı oluşuyor
print("½11".isdigit()) # False
print("11".isdigit()) # True

# NOT: ½ bir sayısal (numeric) karakter iken kendisi bir rakam (digit) değildir.

s = "ANKARALI EVREN"
table = s.maketrans("AIE", "@13")
print(s)
print(s.translate(table))

# string parçalama (string -> list)
liste = "elma-armut-çilek".split('-')
print(liste)
print(liste[0])
print(liste[1])
print(liste[2])


# satırlara göre böl
s = """Turkey
Italy
Spain
France
USA"""
print(s)
liste = s.splitlines()
print(liste)

# önce bir liste tanımlayalım
cities = ["ankara", "bursa", "izmir", "elazığ"]
print(cities)
# liste elemanlarının aralarına = koyarak birleştirik tek bir string yapalım
print("=".join(cities))

# bir string içinde başka bir stringin hangi sırada olduğu:
#       0123456789012
uzun = "I LOVE PYTHON"
print(uzun.index("LOVE")) #2
print(uzun.index("I")) #0
print(uzun.index("PY")) #7
# print(uzun.index("JAVA")) ## HATA FIRLATIR

# bir string içinde başka bir stringin hangi sırada olduğu:
#       0123456789012
uzun = "I LOVE PYTHON"
print(uzun.find("LOVE")) #2
print(uzun.find("I")) #0
print(uzun.find("PY")) #7
print(uzun.find("JAVA")) #-1

# NOT: index ve find farkı: find string'i bulamayınca -1 döndürür, index ise hata fırlatır

# başlık yapma 
baslik = "kara ambar kamyoncular derneği"
print(baslik.title()) # Kara Ambar Kamyoncular Derneği

# aramaya sağdan başla
#    01234567890
s = "KOŞ ALİ KOŞ"
print(s.find("KOŞ")) #0
print(s.rfind("KOŞ")) #8


# string içinde başka bir string var mı yok mu
print("ka" in "ankara") #True
print("zz" in "ankara") #False
print("ankara".find("ka") > -1) #True
print("ankara".find("zz") > -1) #False

# hepsi büyük mü
print("Ankara".isupper()) #false
print("ANKARA".isupper()) #true
print("123ANKARA123".isupper()) #true

# büyüğü küçüğe küçüğü büyüğe çevir
s = "KüÇüKlÜ bÜyÜkLü"
print(s.swapcase()) #kÜçÜkLü BüYüKlÜ

# fazlası için:
# https://www.w3schools.com/python/python_strings_methods.asp

