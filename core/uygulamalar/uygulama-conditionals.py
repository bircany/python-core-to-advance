#Bir aracın yakıt tipine göre(benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulama
benzinF = 39.35
dizelF = 41.71
lpgF = 20.28

mesafe = input("Gidilecek Mesafeyi Giriniz : ")
yakitTuketimi = float(input("Aracınızın 100 km'de tükettiği yakıt miktarını giriniz : "))
yakit = input(""" Yakıt Türünü Seçiniz : 
      1- Benzin
      2- Dizel
      3- LPG """)
total = float(mesafe) * (yakitTuketimi / 100)

if(yakit == "1"):
    total = benzinF * yakitTuketimi
elif(yakit == "2"):
    total = dizelF * yakitTuketimi
else:
    total = lpgF * yakitTuketimi
print(f"{mesafe} km yolculuk için ödemeniz gereken tutar : {total} TL")


#Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayın ve heasplanan ortalama göre not aralığına karşılık gelen değerlendirmeyi yazın.

yazili1 = int(input("1.Yazılı Notunu Giriniz : "))
yazili2 = int(input("2.Yazılı Notunu Giriniz : "))
sozlu = int(input("Sözlü Notunu Giriniz : "))
ortalama = (yazili1 + yazili2 + sozlu) / 3
if(ortalama >= 0 and ortalama <= 24):
    degerlendirme = 0
elif(ortalama >= 25 and ortalama <= 44):
    degerlendirme = 1
elif(ortalama >= 45 and ortalama <= 54):
    degerlendirme = 2
elif(ortalama >= 55 and ortalama <= 69):
    degerlendirme = 3
elif(ortalama >= 70 and ortalama <= 84):
    degerlendirme = 4
elif(ortalama >= 85 and ortalama <= 100):
    degerlendirme = 5
else:
    print("Geçersiz Not Girişi")
print(f"Ortalamanız : {ortalama} Notunuz : {degerlendirme}")
#bunu switch-case yapısı ile yapmak daha mantıklı olabilir. Ancak Python'da switch-case yapısı yoktur. 
