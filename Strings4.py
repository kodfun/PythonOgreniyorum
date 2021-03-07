# string uç uca ekleme (string concatenation)
print("ali" + " ata " + "bak")

# python'da string ve int uç uca eklenemez
## error: print("ankara plaka no: " + 6)

metin = "ankara plaka no: {}"
print(metin.format(6))

# yöntem 2:
plaka = 16
print(f"bursa plaka: {plaka}")

print("Ben {}, {} ve {} renklerini severim"
        .format("sarı", "mavi", "gri"))
print("Ben {1}, {2} ve {0} renklerini severim"
        .format("sarı", "mavi", "gri"))

# escape characters
# özel karakterleri başına ters slash koyarak ifade edebilirsiniz
print("Türkiye'nin başkenti \"Ankara\"dır.")

# yeni satır: \n
print("ali\ncan\ncem")

# tab
print("ali\tcan\tcem")

# bkz: https://www.w3schools.com/python/python_strings_escape.asp