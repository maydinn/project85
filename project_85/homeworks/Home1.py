# Kullanıcıdan bir sayı alıp (tek rakamlı bu sayı s olsun),
# s+ss+sss sonucunu yardiriniz.
# (Tabii ki "yazdırınız" olacak, ama yardırmak da cuk oturmuş.. ;))
# Örnek: s=7, beklenen sonuç=861


def odd_num(x):
    if x % 2 != 0:
        return x
    else:
        print("lütfen tek sayı giriniz")


def result():
    odd = odd_num(int(input("lütfen tek sayı giriniz....")))
    return odd + int(str(odd)*2) + int(str(odd)*3)


print(result())
