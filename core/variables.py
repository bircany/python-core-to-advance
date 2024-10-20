#Variables -> Veri Değerlerini saklamak için değişkenleri kullanırız.
#Python'un bir değişkeni bildirmek için bir komutu yoktur. Bir değişken, ona ilk kez bir değer atadığınız anda oluşturulur.
#Java'daki veya C#'daki gibi bir değişken türü belirtmenize gerek yoktur;
#Python otomatik olarak değişken türünü belirler.
#int x = 5; -> Java     x = 5 -> Python  
#Python, değişken türünü belirlemek için değeri kullanır. otomatik olarak değişken türünü belirler. girilen value'nun türüne göre değişken türünü belirler. Buna dinamik türleme denir.

x = 5  # x is of type int
y = "Hello, World!"  # y is of type str (string)
print(x)
print(y)
# Note: Python is case-sensitive. x and X are two different variables.
#print(X)  # NameError: name 'X' is not defined
X = 6
print(X)
# Değişkenlerin herhangi bir özel tipte tanımlanmasına gerek yoktur ve hatta ayarlandıktan sonra tip değiştirebilirler.

x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)


# Python'da değişken adları büyük-küçük harfe duyarlıdır.
# Değişken adları bir harf veya alt çizgi karakteriyle başlamalıdır. Örnek: _age, age, age1 gibi.
# Değişken adları bir sayı ile başlayamaz.
# Değişken adlarında sadece alfa sayısal karakterler ve alt çizgi karakteri (_) kullanılabilir.
# Değişken adları boşluk içeremez.
# Değişken adları Python dilinde özel anahtar kelimelerle aynı olamaz.
# Değişken adları kısa olabilir (x ve y gibi) veya daha açıklayıcı olabilir (age, carname, total_volume gibi).
# Python'da değişken adları büyük-küçük harfe duyarlıdır. Bu, age, Age ve AGE'nin üç farklı değişken olduğu anlamına gelir.
# Python'da snake_case kullanılır. (değişken_adı) Örneğin: my_name, my_age, my_address gibi.
# Python'da CamelCase kullanılmaz. (DeğişkenAdı) Örneğin: myName, myAge, myAddress gibi.


# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"


#Birden Fazla Değişkene Değer Atamak
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
# Python print ifadesi genellikle değişkenleri çıktı olarak almak için kullanılır.
x = "awesome"
print("Python is " + x)

# Ayrıca bir değişkeni başka bir değişkene eklemek için + karakterini de kullanabilirsiniz: 
x = "Python is "
y = "awesome"
z = x + y
print(z) #String concatenation
# Python'da, + karakteri bir dizeyi başka bir dizeye eklemek için de kullanılabilir.

# Eğer bir dizeyi bir sayı ile birleştirmeye çalışırsanız, Python size bir hata verecektir:
# x = 5
# y = "John"
# print(x + y) #ERROR


# Python'da, + karakteri iki listeyi birleştirmek için de kullanılabilir:
x = ["apple", "banana"]
y = ["orange", "cherry"]
z = x + y
print(z)

# Python'da, + karakteri sayılar için matematiksel bir operatör olarak çalışır:
x = 5
y = 10
print(x + y) #Arithmetic Operator

# Dize değişkenleri tek veya çift tırnak işareti kullanılarak bildirilebilir:
x = "John"
# ya da bu
x = 'John'







#Kullanıcıdan konsol üzerinden veri almak için input() fonksiyonu kullanılır.
#input() fonksiyonu, kullanıcıdan bir giriş alır ve bir dize olarak döndürür.

print("Enter your name:")
firtstName = input()
print("Hello, " + firtstName)








