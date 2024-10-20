#Atama Operatorleri 
a,b,c = 4 ,8 ,(12,2)
#1 - Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c sayısının toplamının farkı nedir?
sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))
sonuc = (sayi1 * sayi2) - (a + b + c[0] + c[1])
# sonuc = (sayi1 * sayi2) - sum((a,b,c[0],c[1]))
# sonuc = (sayi1 * sayi2) - (a + b + sum(c))

#2- c'nin b'ye kalansız bölümünü hesaplayın.
sonuc = (c[0] + c[1]) // b

#3- (a,b,c) toplamının mod 7'si nedir?
sonuc = ( a + b + (c[0] + c[1]) ) % 7
# sonuc = sum((a,b,c)) % 7

#4- b' nin a. kuvvetini hesaplayın.
sonuc = b ** a

#5- a,*b,c = (2,4,6,8,13) işlemine göre c'nin küpü nedir
a,*b,c = (2,4,6,8,13) # a=2, b=[4,6,8], c=13
sonuc = c ** 3

#5 a,b,*c = (2,4,6,8,13) işlemine göre c'nin değerleri toplamı nedir ?
a,b,*c = (2,4,6,8,13) # a=2, b=4, c=[6,8,13]
# sonuc = sum(c)
sonuc = c[0] + c[1] + c[2]

print(sonuc)

##################################################
# Girilen 2 sayıdan hangisi büyüktür
sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))
sonuc = (sayi1 > sayi2) 
print(f"{sayi1}{sayi2}'den büyük : {sonuc}")


# Girilen bir sayının tek çift kontrolü
sayi = int(input("Sayıyı giriniz: "))
sonuc = (sayi % 2 == 0)
print(f"Girilen sayı çift mi : {sonuc}")

#Girilen 3 sayıdan hangisi daha büyük
sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))
sayi3 = int(input("3. sayıyı giriniz: "))
sonuc = (sayi1 > sayi2 and sayi1 > sayi3) # sayi1 en büyük
sonuc = (sayi2 > sayi1 and sayi2 > sayi3) # sayi2 en büyük
sonuc = (sayi3 > sayi1 and sayi3 > sayi2) # sayi3 en büyük
print(f"En büyük sayı : {sonuc}")


# Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol edin 50 ve üstü başarılı
not1 = int(input("1. Notu giriniz: "))
not2 = int(input("2. Notu giriniz: "))
not3 = int(input("3. Notu giriniz: "))
ortalama = ( ((not1 + not2) / 2)*0.4 + not3*0.6)
sonuc = ortalama >= 50
output = f"Öğrencinin ortalama notu : {round(ortalama,2)} ve durumu : {sonuc}"

################################

#Yaşı 18'den büyük yada veli izni varsa bir işte çalışabilir durumunu kontro ledin
yas = int(input("Yaşınızı giriniz: "))
izin = input("Veli izni var mı (e/h): ")
sonuc = (yas >= 18 or izin == "e")
print(f"Çalışabilir mi : {sonuc}")

#Ders notu 50-100 arasındaysa geçti dğeilse kalsın bilgisini yazdır
notu = int(input("Notunuzu giriniz: "))
sonuc = (notu >= 50 and notu <= 100)
print(f"Dersten geçti mi : {sonuc}")

#Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumu

ortalama = 80
zayifSayisi = 1
sonuc = (ortalama >= 70 and zayifSayisi == 0)
print(f"Teşekkür belgesi alabilir mi : {sonuc}")

#İşe girmek için en az önlisans ayda lisans mezunu olma durumunu kontrol edin Sigara kullanmama koşulu ekleyin
egitim = "lise" 
sigara_icme = False
sonuc = ((egitim == "onlisans" or egitim == "lisans") and (not(sigara_icme)))
print(f"İşe alınabilir mi : {sonuc}")

#Uygulamaya giriş kontrolünü "usename yada email" ve "paarola" için yapalım
email = "info@bircanyilmaz.com"
usename="bircanyilmaz"
password = "12345"
girilen_bilgi = input("Kullanıcı adı yada email giriniz: ")
girilen_parola = input("Parola giriniz: ")
sonuc = (email == girilen_bilgi or usename == girilen_bilgi) and (password == girilen_parola)

print(sonuc)