#Aritmetik Operatörler
# + Toplama
# - Çıkarma
# * Çarpma
# / Bölme
# % Mod Alma
# ** Üs Alma
# // Taban Bölme
a = 10 
b = 2
sonuc = a + b
sonuc = a - b
sonuc = a * b
sonuc = a / b

#Not b = 0 olursa  ZeroDivisionError hatası alırız.

sonuc = a // b # Payı tam bölüp sonucu tam sayı olarak döndürür. 24.3 çıktı --> 24 olarak verir. (Kalan Önemsiz)
sonuc = a % b
sonuc = a ** b  # same as Math.Pow(a,b) in C# 10^2 


#Atama Operatörleri
# = Atama
# += Topla ve Ata
# -= Çıkar ve Ata
# *= Çarp ve Ata
# /= Böl ve Ata
# //= Taban böl ve ata
# %= Mod al ve ata
# **= Üs al ve ata
a = 5  #Atama işleminden sonra bellek üzerinde auto-inference ile a değişkeni int tipinde tanımlanır. reference-type mı value-type mı ayarlar.
a,b,c = 10,20,30 # a=10 b=20 c=30
a,b,c  = 10,20,(30,40) # a=10 b=20 c=(30,40) c tuple olarak tanımlanır.
d = 10,20 # d tuple olarak tanımlanır.
a += 2 # a = a + 2
a -= 2 # a = a - 2
a *= 2 # a = a * 2
a /= 2 # a = a / 2
a %= 2 # a = a % 2
a **= 2 # a = a ** 2
a //= 2 # a = a // 2
print(a,b,c)
print(a)

#Karşılaştırma Operatörleri
# == Eşit mi
# != Eşit Değil mi
# > Büyük mü
# < Küçük mü
# >= Büyük Eşit mi
# <= Küçük Eşit mi
#Mantıksal Operatörler
# and Ve
# or Veya
# not Değil
a,b,c,d = 2,2,2,10,5
sonuc = (a == b)
sonuc = (a != b)
sonuc = (a > b)
sonuc = (a < b)
sonuc = (a >= b)
sonuc = (a <= b)
sonuc = (a == b == c) # True
sonuc = (a == b == d) # False
sonuc = (a == b and b == c) # True
sonuc = (a == b and b == d) # False
sonuc = (a == b or b == d) # True
sonuc = (a == b or b == c) # True
sonuc = not (a == b) # False

eposta = "info@bircanyilmaz.com"
parola = "135790"
sonuc = (eposta == input("eposta: "))
sonuc = (parola == input("parola: "))


mezuniyet = input("Mezuniyet Durumu: ")
yas = input("Yas Girin : ")
ehliyetAlabilirMi = (mezuniyet == 'lise') or (mezuniyet == 'üniversite') and (yas >= 18)
print(ehliyetAlabilirMi)

x = 9
sonuc = x > 5 and x < 10  # True , True --> True  , True,False --> False , False,False --> False , False,True --> False
sonuc = x > 5 or (x % 2 == 0) # True , True --> True  , True,False --> True , False,False --> False , False,True --> True 
sonuc = not(x > 0) # same as !  False 



#Kimlik Operatörleri (Identity Operators)
# is  Nesne benzerliğini kontrol eder x is y
# is not Nesne benzerliğini kontrol eder x is not y
x = [2,4,6]
y = [2,4,6] # farklı on bellek alanlarına sahip iki farklı liste ancak icerikleri aynı
z = y # aynı bellek alanına sahip iki farklı referans
print(x == y) # True
print(x is y) # False same as x === y in C#
print(x is not y) # True  aynı nesne  değil midir diye sorar cevap evet
print(z is y) # True

print(sonuc)


#Üyelik Operatörleri (Membership Operators)
# in Listede varlık kontrolü yapar x in y
# not in Listede varlık kontrolü yapar x not in y
print(2 in x) # True nesnenin içerisinde bu eleman var mı
print(5 not in x) # True nesnenin içerisinde bu eleman yok mu