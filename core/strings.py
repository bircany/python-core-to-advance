# String Data Type
# Öncelikle String Dediğimiz veri tipi bir karakter dizisidir.
# #Not: Python'da dizinler 0'dan başlar. İlk karakterin indexi 0, ikinci karakterin indexi 1, diye devam eder.
name = "Bircan"
name = ['B','i','r','c','a','n']
print(name[0])
 
kursAdi = "Python ile Programlama"
kursAciklama = "Güzel bir kurs."
kursSüresi = "20 Saat"

mesaj = "Kurs Adi : " +  kursAdi + " Kurs Aciklama : " + kursAciklama + " Kurs Süresi : " + kursSüresi
print(mesaj)
print(mesaj[0]) #K
print(mesaj[-1]) #son karakteri alır. t
print("*******************************")

# #String Length Bir dizenin uzunluğunu almak için len() fonksiyonunu kullanabilirsiniz.
adet = len(kursAdi)
print(adet) #22
# print(kursAdi(adet)) #Error out of range
print(kursAdi[adet-1]) 

# #String Slicing 
# Python'da bir dizenin bir alt kümesini almak için dilimleme kullanılır. Dize dilimleme, bir dizenin belirli bir aralığını almanıza olanak tanır.
# Dize dilimleme, aşağıdaki sözdizimini kullanır:
# #string[start:end]
#kursAdi = "Python ile Programlama"
print(kursAdi[0:5]) #Pytho  0'dan 5.indexe kadar olan karakterleri alır 5.indexi almaz.('0 dahil 5' dahil değil)
print(kursAdi[:6]) #Python
print(kursAdi[6:]) #ile Programlama 6.index'ten baslayıp 6.index dahil olmadan sona kadar olan karakterleri alır.
print(kursAdi[11:22]) #Programlama veya/
print(kursAdi[11:len(kursAdi)]) #Programlama 21 değil 22 dikkat edelim cunku 22.index'e kadar 22.indexi almayacak.
print(kursAdi[5:]) #n ile Programlama
# #Negatif indeksleme, bir dizenin sonundan karakterleri almanıza olanak tanır.
print(kursAdi[-11:-1]) #Programlam 10.index'den -1.index'e kadar olan karakterleri alır -1.indexi almaz. 
print(kursAdi[-11:0]) #Programlama


print(kursAdi[0:20:1]) #Python ile Programla 0'dan 20.indexe kadar olan karakterleri alır 20.indexi almaz.('0 dahil 20' dahil değil) 1'er 1'er atlayarak.
print(kursAdi[0:20:2]) #Pto l rgalm 0'dan 20.indexe kadar olan karakterleri alır 20.indexi almaz.('0 dahil 20' dahil değil) 2'şer 2'şer atlayarak.
print(kursAdi[::])
print(kursAdi[::1]) #Python ile Programlama 0'dan sona kadar olan karakterleri alır 1'er 1'er atlayarak.
print(kursAdi[::2]) #Pto l rgalm 0'dan sona kadar olan karakterleri alır 2'şer 2'şer atlayarak.
print(kursAdi[::-1]) #amalmargorP eli nohtyP  tersten yazdırır.
print(kursAdi[::-2]) #aagro l oty  tersten yazdırır 2'şer 2'şer atlayarak.


#--------------------------------------------------------------
#String Concatenation
# Python'da, + operatörü iki diziyi birleştirmek için kullanılır.
# Örnek

# #String Formatting
# Python'da, bir dizeyi biçimlendirmek için birkaç farklı yöntem vardır.
# Python'da bir dizeyi biçimlendirmek için kullanılan en yaygın yöntemler:
# % operatörü
# % operatörü, bir dizeyi biçimlendirmek için kullanılan eski bir yöntemdir. % operatörü, bir dizenin içine bir veya daha fazla değişken eklemek için kullanılır.% operatörü, aşağıdaki sözdizimini kullanır:
# "Dize % veri_türü" % değişken
    # %s - Dize (String)
    # %d - Tamsayı (Integer)
    # %f - Ondalık (Float)

# # format() metodu
# format() metodu, bir dizeyi biçimlendirmek için kullanılan modern bir yöntemdir. format() metodu, bir dizenin içine bir veya daha fazla değişken eklemek için kullanılır. 
# format() metodu, aşağıdaki sözdizimini kullanır:
# "Dize {}".format(değişken)


# # f-string
# f-string, Python 3.6'da tanıtılan en yeni bir biçimlendirme yöntemidir. f-string, bir dizeyi biçimlendirmek için kullanılan en yeni ve en kolay yöntemdir. f-string, aşağıdaki sözdizimini kullanır:
# f"Dize {değişken}"
ad = "Bircan"
soyad = "Yilmaz"
age = 22
meslek = "Yazilim Mühendisi"
mesaj = "My name is : " + ad + " " + soyad + " I'm " + str(age) + " years old. My job is " + meslek
print(mesaj)



mesaj = "My name is : {} {}. I'm {} years old. My job is {}".format(ad,soyad,age,meslek) #format() method
mesaj = "My name is : {0} {1}. I'm {2} years old. My job is {3}".format(ad,soyad,age,meslek)
mesaj = "My name is : {2} {1}. I'm {3} years old. My job is {0}".format(ad,soyad,age,meslek)
mesaj = "My name is : {a} {s}. I'm {y} years old. My job is {m}".format(a=ad,s=soyad,y=age,m=meslek)
mesaj = "My name is : %s %s. I'm %s years old. My job is %s" % (ad,soyad,age,meslek) # % method
mesaj = f"My name is : {ad} {soyad}. I'm {age} years old. My job is {meslek}" #f-string method
print(mesaj)

#--------------------------------------------------------------

# #String Methods  for more :  https://www.w3schools.com/python/python_ref_string.asp  https://www.geeksforgeeks.org/python-string-methods/
#Python'da bir dizeyi değiştirmek için birçok yöntem vardır. Python'da bir dizeyi değiştirmek için kullanılan en yaygın yöntemler
#Bütün string metotları orjinal obje üzerinde değişiklik yapmaz Strings are immutable'dır yeni bir nesne döndürür.

mesaj = " BTK Akademi, Python, Kursu "
sonuc = mesaj.upper() #Tüm karakterleri büyük harfe çevirir.
sonuc = mesaj.capitalize() #Sadece ilk karakteri büyük yapar.
sonuc = mesaj.title() #Her kelimenin ilk harfini büyük yapar.
sonuc = mesaj.lower() #Tüm karakterleri küçük harfe çevirir.
sonuc = "abc".isupper() #False
sonuc = "abc".islower() #True
sonuc = mesaj.replace("Python","C#") #Python kelimesini C# ile değiştirir.
sonuc = mesaj.startswith("BTK") #True
sonuc = mesaj.endswith("Kursu") #True
sonuc = mesaj.strip() #Baştaki ve sondaki boşlukları siler. 
sonuc = mesaj.split() #Boşluklara göre ayırır. --> her kelimeyi bir eleman olarak alır liste olarak döndürür. ['BTK', 'Akademi', 'Python', 'Kursu']
sonuc = mesaj.split()[0] #BTK
sonuc = mesaj.split(",") #Virgüle göre ayırır. [' BTK Akademi ', ' Python', ' Kursu ']
sonuc = mesaj.index("Python") #Python kelimesinin başlangıç indexini döndürür. 13 (Bir metinde bir kelimenin başlangıç indexini döndürür.)
sonuc = mesaj.find("Python") #Python kelimesinin başlangıç indexini döndürür. 13 (Bir metinde bir kelimenin başlangıç indexini döndürür.)

print(sonuc)





