"""
*Yarıçağı verilenn bir dairenin alan ve çevresini hesaplayın.
* Alan : πr^2 Çevre : 2πr
** Klavyeden girilen km bilgisini mil cinsinden hesaplayın
mil = km & 1.609.344

"""

pi = 3.14
r = float(input("Daire'nin yarıçapını girin : "))
alan = pi * r ** 2
cevre = 2 * pi * r
print("Yarıcapı girilen dairenin alanı : " , alan)
print("Yarıcapı girilen dairenin cevresi : " , cevre)



km = float(input("Km cinsinden bir değer girin : "))
mil = km / 1.609344
mil = round(mil, 2) #Virgülden sonra 2 basamak alır.
print(str(km) + " km = " + str(mil) + " mil eder.")




