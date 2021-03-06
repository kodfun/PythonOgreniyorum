# stringler '' ya da "" ile tanımlanır
a = "hello"
b = 'merhaba'

# çok satırlı string
c = """lorem ipsum
dolor sit amet
consectetur"""

print(a)
print(b)
print(c)

# bir çeşit string uç uca eklemesi (string concatenation)
s = 'abc' 'xyz'
print(s)

# string'ler dizi gibidir
# python'da karakter veri tipi yoktur
# örneğin istanbul stringinin 3. karakterini yazdıralım
city="istanbul"
print(city[3]) # a

# escape sequences
# özel karakterler ters slash akabindeki özel harflerle tanımlanır
# \n : yeni satır (new line)
# \t : tab
s = '\new \tablet' 
print(s)

# eğer escape olayını iptal etmek isterseniz
# string önüne r koyunuz
s = r'\new \tablet' 
print(s)
# r: ingilizce raw kelimesinin baş harfi (ham/olduğu gibi)

# STRING KARAKTERLERİNİ TEK TEK YAZDIRMA
for c in "ANKARA":
    print(c)

# STRING UZUNLUK
s = "KodluYorum"
print(len(s))


# string içinde string var mı diye kontrol edelim
if ("ka" in "ankara"):
    print("ankara, ka içerir.")
else:
    print("ankara, ka içermez.")