""" Python DOC String

Aşşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayın. Toplam ödenen ücret nedir , Ödenen miktarın kdv oranı nedir (%18)

Sadık Turan
05321234567
info@sadikturan.com
Kocaeli
Satın Alınan Ürünler 
********************************
Ürün Adı : Kablosuz Mouse 
Fiyatı : 550TL

Ürün Adı : Kablosuz Klavye
Fiyatı : 650TL

Ürün Adı : Dizüstü Bilgisayar
Fiyatı : 55000TL



"""
userName = "Sadık Turan"
userPhone = "05321234567"
userMail = "info@sadikturan.com"
userCity = "Kocaeli"
product1 = "Kablosuz Mouse"
product1Price = 550
product2 = "Kablosuz Klavye"    
product2Price = 650
product3 = "Dizüstü Bilgisayar"
product3Price = 55000
kdv = 0.18
total = product1Price + product2Price + product3Price
print("Toplam Ödenen Ücret : " + str(total))
print("Toplam KDV Oranı : " + str(total * kdv))

print("Ali" + str(100))
print(str(100) + "Ali")

#İleride Müşteri bilgileri ve ürün bilgileri veritabanından alınacak ve bu bilgiler üzerinden işlem yapılacak. Ayrıca Bunlar birer obje olacağı için bir sınıf üzerinden üretilecek.