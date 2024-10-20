import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.urun["urunAdi"]
sonuc = module.urun["renkler"]
sonuc = module.toplama(10,20)

import module as m
sonuc = m.sayilar 

from module import sayi,sayilar,urun
sonuc = sayi
sonuc = sayilar
sonuc = urun

from module import *
sonuc = sayi
sonuc = sayilar
sonuc = urun
sonuc = toplama(10,20)

print(sonuc)