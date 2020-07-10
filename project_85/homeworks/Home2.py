"""Kullanıcıdan çapını! alacağınız dairenin çevresini ve alanını 4 haneli kesinlikle (noktadan sonra 4 hane) hesaplayıp, sonucu ekrana güzelce yazdırın.
Hata kontrolü yapmayı unutmayın..
Beklenmeyen bir durum görüldüğü takdirde, mentörünüze danışınız.
Kodlarınızı çocukların ulaşamayacağı yerde, direk güneş  ışığına maruz kalkmayacak şekilde saklayınız."""
import math
r = int(input("lütfen yarı çapı giriniz: "))
pi = math.pi


def area_circle():
    return pi * r ** 2


def per_circle():
    return 2 * pi * r


# print("Dairenin alanı:  %.4f dır\nDairenin çevresi: %.4f dir" % (area_circle(), per_circle()))

print("Dairenin alanı:  {0:.4f} dır\nDairenin çevresi:  {0:.4f} dir".format(area_circle(), per_circle()))

