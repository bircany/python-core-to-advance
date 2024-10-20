# title = "Python ile Programlama Dersleri"
# # 1- 'title' değişkeni içerisindeki karakter sayısı.
# print(len(title))
# # 2- 'title' değişkenindeki 'Python' kelimesini alın.
# print(title[0:6])
# # 3- 'title' değişkenindeki ilk 5 ve son 5 karakterini alın.
# print(title[:5] + title[-5:])
# #4-'title' değişkenini tersten yazdırın.
# print(title[::-1])
 
# #5-Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırın.
# #Örnek : Çınar Turan isimli öğrencinin 1.notu :60 , 2.notu :60 ve not ortalaması : 60 olarak hesaplanmıştır.

# isim = input("Öğrenci Adı : ")
# soyisim = input("Öğrenci Soyadı : ")
# not1 = float(input("1.Not: "))
# not2 = float(input("2.Not: "))
# ortalama = (not1 + not2) / 2
# mesaj = f"{isim} {soyisim} isimli öğrencinin 1.notu : {not1} , 2.notu : {not2} ve not ortalaması : {ortalama} olarak hesaplanmıştır."
# print(mesaj)

#######################################################################

kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website  = "https://www.btkakademi.gov.tr/"

# 1- 'kursAdi' değişkenindeki karakter sayısı. , boşluk sayisi
sonuc = kursAdi.count("")
sonuc = kursAdi.count(" ")

# # 2 - 'kursAdi' değişkenindeki 'Python' kelimesinin başlangıç konumunu bulun. , 'ile' kelimesi var mı  varsa nerede
sonuc = kursAdi.index("Python")
sonuc = kursAdi.find("ile") #19
sonuc = "ile" in kursAdi #True
#website değişkeni "www" içeriyor mu
sonuc = "www" in website

# 4- 'kursAdi' değişkenini tersten yazdırın.
sonuc = kursAdi[::-1]
# 5- 'website' değişkeninden www karakterlerini alın.
sonuc = website[8:11]

# 6- 'website' değişkenindeki uzantıyı alın.
sonuc = website[website.index("."):] #.btkakademi.gov.tr/

# 7- 'kursAdi' değişkenini boşluk karakterlerinden ayırın.
sonuc = kursAdi.split()

# 8- 'kursAdi' değişkenini boşluk karakterlerinden ayırın ve liste olarak döndürün.
sonuc = kursAdi.split() #['Btk', 'Akademi', 'Python', 'ile', 'Programlama', 'Dersleri']

#kursAdi içerisindeki tüm boşlukları "-" ile değiştirir."
sonuc = kursAdi.replace(" ","-")
#9- 'kursAdi' değişkenini '-' karakterinden ayırın ve liste olarak döndürün.
sonuc = kursAdi.split("-") #['Btk Akademi Python ile Programlama Dersleri']

#10- 'kursAdi' değişkenindeki karakterlerin hepsini * karakteri ile değiştirin.
sonuc = kursAdi.replace(" ","*")


#11- 'kursAdi' değişkenindeki Python kelimesini React ile değiştirin.
sonuc = kursAdi.replace("Python","React")

#12- 'Btk Akademi' karakter dizisinin baş ve sondaki boşluk karaktelerini silin.
sonuc = " Btk Akademi ".strip()
# 2- 'kursAdi' değişkenindeki karakterlerin tamamını küçük harf yapın.
sonuc = kursAdi.lower()
# 13- 'kursAdi' değişkenindeki karakterlerin tamamını büyük harf yapın.
sonuc = kursAdi.upper()
# 14- 'kursAdi' değişkenindeki karakterlerin sadece baş harflerini büyük yapın.
sonuc = kursAdi.title()


# website değişkeninde kaç adet '.' karakteri var
sonuc = website.count(".")
# website değişkeninde 'www' ile başlayıp 'gov' ile bitiyor mu
sonuc = website.startswith("www") and website.endswith("gov")
# website değişkeninde '.com' ifadesi var mı
sonuc = ".com" in website
# website değişkeni "https" ile başlayıp 'tr' ile bitiyor mu
sonuc = website.startswith("https") and website.endswith("tr")






#kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor
kursAdi.isalpha()
#kursAdi içerisindeki tüm karakterler alfabetik mi
kursAdi.isalnum()
#kursAdi içerisindeki tüm karakterler rakamlardan mı oluşuyor
kursAdi.isdigit()
#kursAdi içerisindeki tüm karakterler rakam mı
kursAdi.isnumeric()
#kursAdi içerisindeki tüm karakterler boşluk karakterlerinden mi oluşuyor
kursAdi.isspace()
#kursAdi içerisindeki tüm karakterler küçük harf mi
kursAdi.islower()
#kursAdi içerisindeki tüm karakterler büyük harf mi
kursAdi.isupper()
#kursAdi içerisindeki tüm karakterlerin baş harfi büyük mü
kursAdi.istitle()



print(sonuc)