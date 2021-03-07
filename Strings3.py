# STRING MANIPULATION
s = "Ankara"
print(s.upper())
print(s.lower())

# ETRAFINDAKİ BOŞLUKLARI YOK ETME
s = "    Ankara    "
print("---" + s + "---")
print("---" + s.strip() + "---")
print("---" + s.rstrip() + "---")
print("---" + s.lstrip() + "---")

s="ankara"
print(s.replace("a", "@"))

# string parçalayarak listeye dönüştür
# (list konusu ileride işlenecek)
s = "ali,can,cem"
liste = s.split(",")
print(liste) # ['ali', 'can', 'cem']
print(liste[0])
print(liste[1])
print(liste[2])



