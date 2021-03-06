# bu iki satır console ekranını temizlemek için
import os
os.system("cls") 

# a ve b integer değişkenleri
a = 3
b = 4
print(a * b)

# değişkenler dinamik, türü değişebilir
# artık a ve b birer string (metin)
a = "ali"
b = "yılmaz"
print(a + " " + b)

# casting
x = str(3) # "3"
y = int(3) # 3
z = float(3) #3.0
print(x, "\t", type(x))
print(y, "\t", type(y))
print(z, "\t", type(z))

# string "" ile ya da '' ile tanımlanabilir
str1 = "word"
str2 = 'kelime'
print(str1, str2)

# değişkenler case sensitive (büyük küçük harf duyarlı)
a = "ayrı"
A = "apayrı"
print(a, A, sep="-")

# çok değişken çok değer
a,b,c=1,3,5
print(a,b,c)

# diziden değişkenlere
a,b,c=["can","cem","ali"]
print(a,b,c)

a,*b=1,3,5 # a=1 b=[3,5]
print (a,b) 

# string uç uca ekleme (concatenation)
cumle = "ali" + " " + "ata" + " " + "bak"
print(cumle)

# + operatörü ile string ve int birlestirilemez!
# print("abc" + 1) # ERROR

# GLOBAL VARIABLES (GLOBAL DEĞİŞKENLER)
ad = "Hakan"

# tanımladığımız fonksiyonda ad global değişkenini kullandık
def merhabaDe():
    print("Merhaba " + ad)

merhabaDe()

# global değişkenleri fonksiyon içinde de tanımlayabilirsiniz

def birFonksiyon():
    global birDegisken 
    birDegisken = 123
    print("birFonksiyon fonksiyonu çalıştı..")

birFonksiyon()
print(birDegisken)