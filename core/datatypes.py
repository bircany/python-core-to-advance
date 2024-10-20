#Python'da veri türleri
# Python'da veri türleri, bir değerin türünü belirler. Python'da birçok veri türü vardır, ancak en yaygın olanları şunlardır:


# Text Type:	str --> String
# Numeric Types:	int, float
# Boolean Type:	bool
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Binary Types:	bytes, bytearray, memoryview

#list,tuple,dict,set,frozenset,bytes,bytearray,memoryview,range gibi veri türleri daha sonra detaylı olarak incelenecek.

# Python'da veri türlerini belirlemek için type() fonksiyonunu kullanabilirsiniz.
# Örnek
# # Bu değişkenin türünü belirleyin:
# x = 5
# print(type(x))

isim = "Çınar"
yas = 7
kilo = 15.5 
ogrenciMi = True      #bool , True or False

print(type(isim)) #<class 'str'>
print(type(yas)) #<class 'int'>
print(type(kilo)) #<class 'float'>
print(type(ogrenciMi)) #<class 'bool'>

print("isim : " + isim + " yas : " + str(yas) + " kilo : " + str(kilo) + " Ögrenci mi : " + str(ogrenciMi)) 



# Python'da veri türlerini değiştirmek için dönüşüm fonksiyonlarını kullanabilirsiniz.
# Dönüşüm Fonksiyonları (Type Conversion Functions)
# Python'da veri türlerini dönüştürmek için aşağıdaki dönüşüm fonksiyonlarını kullanabilirsiniz:
# int() - int
# float() - float
# str() - str
# Örnek Bir tamsayıyı bir ondalık sayıya dönüştürün:
x = 5
y = float(x)
print(y)

# print("1.Sayıyı Girin : ")
# num1 = input()  #"10" Konsoldan girilen değer string değer olarak okunacak 
# print("2.Sayıyı Girin : ")
# num2 = input()  #"20"
# total = num1 + num2 
# print("Sayı Değeri : "  + total) #"1020" Dolayısıyla çıktı bir string değer olacak oyüzden konsoldan alınan değerin eğer işlem yapılacaksa inte çevrilmesi gerekir.
# # Ustte sıkıntı olmamasının sebebi zaten total değerinin string olması string concatda bir sıkıntı cıkartmaz.


# print("1.Sayıyı Girin : ")
# num1 = int(input())  #10
# print("2.Sayıyı Girin : ")
# num2 = int(input())  #20
# total = num1 + num2
# #print("Sayı Değeri : " + total) #30 TypeError: can only concatenate str (not "int") to str burda bu hatayı alıyorum o zaman.
# print("Sayı Değeri " + str(total)) #30 şeklinde yazmalıyım yada daha mantıklı olarak int değerlerle birlikte string değerleri yazdırmak için kullanılır.
# print("Sayı Değeri : " , total) #30 şeklinde yazmalıyım

#Peki Girilen Değer Double olursa ne olucak String'de hata varmadı runtime da ama diğerinde verdi çünkü double tipi int tipe çevirmeye çalıştık. 
x = int("1")
#X = int("10.5")
print(x)
#print(X) #Error String 10.5 değeri int tipine çevrilemez. Dolayısıyla bu değeri ya float tipine çevirmemiz gerekiyor  yada direk  float değeri int 'e çevirmek gerekiyor.
print("---------------------------")
x = float("10.5")
y = int(10.5)
print(x)
print(y) # int float girilen 10.5 değerini en yakın alt değeri alır. 10.5 -> 10.0

