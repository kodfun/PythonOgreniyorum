# döngü ile elemanları yazdır

mevsimler = ["ilkbahar", "yaz", "sonbahar", "kış"]

for x in mevsimler:
    print("* " + x)

# ara bilgi:
# 0 dan 5e (hariç) kadar olan sayıları yazdır
for i in range(5):
    print(i)

# mevsimleri indeks numaralarıyla erişerek yazdır
for i in range(len(mevsimler)):
    print("- "+ mevsimler[i])

# mevsimleri while döngüsü kullanarak yazdır
i = 0
while i < len(mevsimler):
    print("= " + mevsimler[i])
    i += 1

# for loop kısa yolu
[print("+ " + x) for x in mevsimler]