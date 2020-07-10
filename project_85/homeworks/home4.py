"""Müşteri Lidl'dan (ya da herhangi bir ekonomik süpermarketten) alışveriş yaptı.
Miktar herhangi bir rakam olabilir.. Örnek: 12.34 ya da 56.78 Euro.
Ve müşteri kasiyere herhangi bir banknot ya da banknotlar ya da bozukluklar verebilir.
Örnek: 20 Euro, 30 Euro, 50 Euro, 65 Euro ya da 100 Euro ya da 200 ya da 500. (500'den çok olmasın, fazla harcamayın..)
Şimdi, sizin göreviniz (elbette kabul ederseniz) bir program yazıp, bu 2 miktarı kasiyerden almak ve..
Ve, mümkün olan en az adette para kullanarak para üstünü vermek.
Yani, para üstü 2 Euro tutuyorsa, 2 tane 1 Euro ya da 4 tane 50 Cent değil, direkt 2 Euro vermeniz gerekiyor. Para üstü 1.99 ise, durum farklı tabii..
Yuvarlamaları noktadan sonraki 2 haneden sonra yapmanız gerekiyor. Neden? Çünkü, tedavüldeki en küçük para 1 Cent.
Tedavüldeki Euro banknotları: 500, 200, 100, 50, 20, 10, 5 Euro.
Tedavüldeki Euro bozuklukları: 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 Euro. (Son 6 tanesinin Cent seviyesinde olduğunu dememe gereNk yok herhalde..)"""

cost = float(input("lütfen tutan mitkatı giriniz: "))
customer = float(input("lütfen verilen mitkatı giriniz: "))
change = customer - cost


change_list = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]

if change > 0:
    for i in change_list:
        change = float("{:.2f}".format(change))
        a = change // i
        if a != 0:
            print(i, "lik", a, "tane", end=", ")
        change = change % i
elif change == 0:
    print("para üstüne gerek yok")
else:
    print("eksil para girdiniz")

"""
paper_change = int(change)
cent_change = change - paper_change
paper_change_list = [500, 200, 100, 50, 20, 10, 5, 2, 1]
cent_change_list = [0.5, 0.2, 0.1, 0.05, 0.01]
for i in paper_change_list:
    a = paper_change // i
    if a != 0:
        print(i, "lik", a, "tane", end=", ")
    paper_change = paper_change % i

print()

for i in cent_change_list:
    a = cent_change // i
    if a != 0:
        print(i, "lik", a, "tane", end=", ")
    cent_change = cent_change % i"""