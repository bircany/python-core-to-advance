liste = [1,2,3,4,5,]
# for i in liste:  #liste iterable obje
#     print(i)

# print(dir(liste)) #has __iter__ ctor so it can be used for iterations. 

iterator = iter(liste) #<list_iterator object at 0x000001CF69D359C0> for döngüsünde iterable bir nesne için kendi iterator'unu otomatik oluşturur.

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#print(next(iterator)) StopIteration  aynı bağlı liste gibi bir sonraki objeye erişim sağlamak için kullanılıyor. (sanki indexi bilinmiyormuş gibi)
# for i in liste:  #liste iterable obje
#     print(i) #for döngüsü kendisi otomatik bir ıterator oluşturuyor. peki nasıl

# iterator = iter(liste)
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
    
list = MyNumbers(20,50)
myiter = iter(list)
# print(next(myiter))
# print(next(myiter))
while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break

# for x in list:
#     print(x)

