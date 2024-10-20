#bellekte yer işgal etmeyen bir iterator üretir.

# def cube():
#     result = [] #bu bellekte yer işgal ediyor şuan

#     for i in range(500):
#         result.append(i**3)
#     return result

# print(cube())

def cube():
    for i in range(500):
        yield i ** 3 #bu bellekte herhangi bir yer kaplamadan değerleri saklamamı sağlıyor ama bellekte saklanmıyor yani 2.defa kullanamıyorum
#dikkat return kullanmıyoruz yani (bir liste geri döndürmüyoruz)
# generator = cube() #ıterate edilebilen bir iterable objesi geri döndürür.
# iterator = iter(generator)
#zaten generator bize iterable olan objeyi(cube()) zaten ıterator'e de kendi içinde çeviriyor oyüzden direk şöyle de kullanılabilir.
iterator = cube()

# print(next(iterator)) #biz her bu değeri istediğimizde o değer o anda üretilecek ve ekrana yazdırılacak
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in iterator:
    print(i)


#Yani özet olarak şöyle de yazılabilir
def cube():
    for i in range(5):
        yield i ** 3
for i in cube():
    print(i)