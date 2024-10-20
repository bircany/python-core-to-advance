#Fonksiyonlar (İşlevler)
# Bir fonksiyon çalıştırılmayı bekleyen kod satırlarıdır. Belirli bir görevi gerçekleştirmek için kullanılan bir bloktur.
# Fonksiyonlar, bir işlevi birkaç kez kullanmanız gerektiğinde yararlıdır.
# Python'da bir fonksiyon tanımlamak için def anahtar kelimesini kullanılır.
# Bir fonksiyonun adını yazdıktan sonra, iki nokta üst üste (:) ekleyin. Bu, fonksiyon bloğunun başladığını belirtir. 
# Parantez içindeki bilgi, fonksiyonun ne tür bilgi alacağını belirler. Biz buna parametre diyoruz.
# Bir fonksiyona dışarıdan parametre gönderilebilir.
# Bir fonksiyonu çağırmak için, adını ve parantez içindeki bilgiyi kullanın.
# Bir amaca hizmet eden bir fonksiyon kişilere zaman kazandırır. (Math.sqrt() gibi belirli bir modülü kullanarak bir işlemi yapmak yerine)
# Fonksiyonlar sayesinde daha temiz kod yazılır.
# Fonksiyonlar "built-in" (Hazır Fonksiyonlar ; List Metotları vs, append() vs.) ve "user-defined" (Kendimiz Oluşturduğumuz) olarak ikiye ayrılırlar.

#Defining a Functio
def my_function():  #no args func
  print("Hello from a function")



#Calling a Function
my_function()  # Hello from a function


# def selamlama():
#     print("Merhaba")

# for i in range(10):
#     selamlama()  fark şu 10 defa selamlama() fonksiyonu çalıştırılacak.

def selamlama():
    for i in range(10):
        print("Merhaba")

# selamlama() #Merhaba 10 defa yazdırır. selamlama() fonksiyonu 1 kez çalıştırılacak
 

def yasHesapla():
    return yil() - 1998

# print(yasHesapla()) 

def yil():
    import datetime 
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour

def Merhaba():
    if saat() < 12:
        return "Günaydın"
    else:
        return "Merhaba"
    
def say_hello(name):  #args func
    return "Merhaba " + name

# print(say_hello("Bircan"))
# print(say_hello("Mehmet"))


def topla(a,b):
    return a + b

# topla(3+4) #7
# topla(5+6) #11

def yasHesapla(dogumYili):
    return yil() - dogumYili

# print(yasHesapla(1998)) #23
# print(yasHesapla(1990)) #31
 
def emekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65
    kalanYil = emeklilik - yas
    if kalanYil > 0:
        return f"{isim} Emekliliğinize {kalanYil} yil kaldı"
    else:
        return f"{isim} , Zaten {abs(kalanYil)}  Yil Önce Emekli Oldunuz"

print(emekliligeKacYilKaldi(2002,"Bircan"))
print(emekliligeKacYilKaldi(1950,"Ayşe"))
