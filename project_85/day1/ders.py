ad = input("adınızı giriniz... ")
soyadı = input("souadınızı giriniz... ")
yas = input("yaşınızı giriniz... ")

isim = ad + " " + soyadı
print(isim)
print("adı {ad}, soyadı {so}, yaşı{ya}".format(ad=ad, so=soyadı, ya=yas))

isim = isim.replace(ad, "ali")
print(isim)

print(f"adınız: {ad}")
print(f"yaşınız: {yas}")



