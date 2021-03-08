meyveler = ["elma", "armut", "karpuz"]
print(meyveler)

# listenin uzunluğu
print("listenin uzunluğu: ", len(meyveler))

# listeler sıralıdır ve indeks numaraları 0 dan başlar 
print(meyveler[0])
print(meyveler[1])
print(meyveler[2])

# indeks no negatif olursa sıra olarak sondan başlanır
# sonuncu elemanının indeksi -1 dir
print(meyveler[-3])
print(meyveler[-2])
print(meyveler[-1])

# listeden dilim olarak yeni bir liste almak
#          0  1  2  3   4   5
sayilar = [3, 5, 7, 11, 15, 99]
# 2. indeksten başla 5. (hariç) indekse kadar al
print(sayilar[2:5]) # [7, 11, 15] 

# 3. indekse kadar al
print(sayilar[:3]) # [3, 5, 7]

# 3. (dahil) indeksten sonra ne varsa 
print(sayilar[3:]) # [11, 15, 99]


# ÖĞE DEĞİŞTİRME
adlar = ["can", "cem", "ali"]
print(adlar)
adlar[1] = "ece"
print(adlar)

# ÇOKLU DEĞİŞTİRME
adlar[1:3] = ["oya", "kaya"]
print(adlar)

# 3 öğe yerine 1 öğe koyma
# üç adet 9un yerine bir adet 11 koy
sayilar = [3, 5, 7, 9, 9, 9, 77]
sayilar[3:6] = [11]
print(sayilar)

# araya öğe sokma
iller = ["adana", "afyon", "ağrı"]
# adana ve afyon arasına adıyamanı sok
iller.insert(1, "adıyaman")
print(iller)

# sonuna amasya ekle
iller.append("amasya")
print(iller)

# listeye liste ekleme
iller2 = ["ankara", "antalya", "artvin"]
iller.extend(iller2)
print(iller)

# listenin başına washington ekle
iller.insert(0, "washington")
print(iller)

# listenin ilk elemanını sil
del iller[0]
print(iller)

# listenin sonuna ağrı ekle
iller.append("ağrı")
print(iller)

# şu an listede 2 adet ağrı bulunmakta
iller.remove("ağrı") # sizce 2 ağrı da silinir mi?
print(iller) # ilk ağrı yı sildi !!!

# listedeki tüm elemanları sil
iller.clear()
print(iller) # []

