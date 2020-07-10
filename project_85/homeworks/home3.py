"""Kullanıcıdan bir sayı alın.
Bu sayının (önce bir bak hele, sayı mı değil mi?) 1'den 10'a kadar bir sayı mı,
yoksa 100'e kadar bir sayı mı, yoksa 1000'e kadar bir sayı mı,
yoksa 10.000'e kadar bir sayı mı, yoksa 100.000'e kadar bir sayı mı,
yoksa 1.000.000'a kadar bir sayı mı, yoksa milyondan da mı büyük olduğunu tespit edip,
şık bir mesaj veriniz."""
a = input("bir sayı giriniz: ")

while True:
    try:
        a = int(a)
        break
    except ValueError:
        print("lütfen bir sayı girerek tekrar deneyiniz")


if a >= 1_000_000:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 100_000:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 10_000:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 1000:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 100:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 10:
    print("girdiniz sayı", a, "den büyük yada eşit")
elif a >= 1:
    print("girdiniz sayı", a, "den büyük yada eşit")
else:
    print("sanırım negativ sayı girdiniz...")