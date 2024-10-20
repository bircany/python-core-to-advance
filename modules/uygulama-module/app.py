"""
    module1(db) : urunler
    module2(methods) : urunEkle(), urunGuncelle(),urunleriGetir()
    module3(app) : 

    yeni ürün ekleme => urunEkle("iphone15",60000)
    ürün güncelleme => urunGuncelle(1,"iphone15 pro",80000)
    ürünleri listeleme => urunleriGetir()
"""
from methods import *

urunEkle("iphone 20",100000)
urunGuncelle(3,"iphone 17",75000)

for i in  urunleriGetir():
    print(f"id: {i['id']} ürün adı: {i['urunAdi']} fiyat: {i['fiyat']}")
#     # print(i)
#     # print(i["urunAdi"],i["fiyat"])
 

