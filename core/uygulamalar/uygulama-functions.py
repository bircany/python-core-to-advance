#1-Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def kelimeyiYazdir(kelime,adet):
    print(kelime * adet)
kelimeyiYazdir("Merhaba ",5)

#2-Dikdörtgenin alanını ve çevresini hesaplayan bir fonksiyon yazın.
def dikdortgenAlanHesapla(a,b):
    alan = a * b
    return alan
def dikdortgenCevreHesapla(a,b):
    cevre = 2 * (a + b)
    return cevre
def dikdortgenAlanVeCevreHesapla(a,b):
    alan = dikdortgenAlanHesapla(a,b)
    cevre = dikdortgenCevreHesapla(a,b)
    return alan,cevre #tuple olarak döner aynı anda iki değer döndürmek için.
print(dikdortgenAlanVeCevreHesapla(3,4))

#3- Kendisine Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.(0 ve 100 arasındaki asal sayıları bulun)
def asalSayiBul(sayi1,sayi2):
    asalSayilar = []
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                asalSayilar.append(sayi)
    print(asalSayilar)
asalSayiBul(0,100)

#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren bir fonksiyon yazın.
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(1,sayi+1):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler
print(tamBolenleriBul(20))

#5-Kendisine gönderilen bir sayının asal sayı olup olmadığını belirten bir fonksiyon yazın.
def asalSayiMi(sayi):
    if sayi > 1:
        for i in range(2,sayi):
            if sayi % i == 0:
                return False
        else:
            return True
    else:
        return False
print(asalSayiMi(11))

#6-Kendisine gönderilen bir sayının faktöriyelini hesaplayan bir fonksiyon yazın.
def faktoriyel(sayi):
    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        return 1
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i
        return faktoriyel
print(faktoriyel(5))

#7-Yazı Tura Uygulamasını fonksiyon kullanarak yaızn.(Random modülü kullanılacak)
def yaziTura():
    import random as r
    para = r.randint(0,1)
    if para == 0:
        return "Yazı"
    else:
        return "Tura"
print(yaziTura())

