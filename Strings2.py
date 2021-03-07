#    012345
s = "ankara"
print(s[2:5]) # 2.karakterden başla 5.(hariç) karaktere kadar yazdır


# eğer karakterlerin indeks numarası negatif verilirse
# sıra sondan hesaplanır
#  0123456789
#  0123454321
s="xyzAĞRIabc"
print(s[3:7])
print(s[3:-3])

uzun="afyonkarahisarlılaştıramadıklarımızdan mıymışsınız?"
# GÖREV: SORU İŞARETSİZ YAZDIR
print(uzun[0:-1])

# KARAKTER ATLAYARAK SEÇME
#    0123456789
#     1 3 5 7 9
s = "a1b2c3d4e5"
print(s[1::2]) ## 1.indeksten başla 2şer 2 şer zıplayarak al

# stringi tersine çevirme
s = "İSTANBUL"
print(s[-1::-1]) # sondan başla geriye doğru 1er zıplayarak al
print(s[::-1])


# belirli bir indeks sonrasını al
#    0123456789
s = "EVET HAYIR"
print(s[5:])

# belirli bir indekse kadar olanı al
print(s[:4])

# son 3 karakterini al
#-             ...321
sehir="afyonkarahisar"
print(sehir[-3:])

