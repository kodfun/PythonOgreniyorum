dunyaDonerMi=True
#dunyaDonerMi=False

print("döner" if dunyaDonerMi else "dönmez")

if dunyaDonerMi:
    print("Evet, dünya döner.")
else:
    print("Hayır, dünya dönmez.")

print(1 < 3) # True
print(5 < 3) # False
print(5 == 5) # True

# boolean aleminde 2 değer vardır True ya da False
# ancak diğer türlerdeki değerlerin True ve False karşılığı olabilir
# örneğin sayılardan 0 False gibi kabul edilirken
# yine sayılardan 1, 5, 8 ise True gibi kabul edilir
print(bool(0)) # False
print(bool(1)) # True
print(bool(4)) # True

# stringlerde ise boş string false diğerleri true kabul edilir
print(bool("")) # False
print(bool("ankara")) # True

# diğer dillerde null olarak bilinen None değeri ise false kabul edilir
print(bool(None)) # False