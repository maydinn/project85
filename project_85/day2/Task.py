while True:
    a = input("Sayı giriniz: ")
    b = input("Sayı giriniz: ")
    islem = input("Lütfen bir işlem giriniz, A: Toplama, S: Çıkarma, M: Çarpma, D: Divide: ")
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Lütfen tam sayı giriniz")


if islem.upper() == "A":
    print("İki sayının toplamı: ", (a + b))
elif islem.upper() == "B":
    print("İki sayının farkı: ", (a - b))
elif islem.upper() == "C":
    print("İki sayının çarpımı: ", (a * b))
elif islem.upper() == "D":
    try:
        print("İki sayının bolümü: ", (a / b))
    except ZeroDivisionError:
        print("sıfırdan farklı bir değer giriniz")
else:
    print("yanlış işlem girdiniz")

