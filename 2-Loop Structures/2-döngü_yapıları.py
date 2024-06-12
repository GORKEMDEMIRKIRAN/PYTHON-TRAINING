





# FOR DÖNGÜLERİ


## in Operatörü
## bir elemanın başka bir listede demette veya stringle (karakter dizileri)
## bulunup bulunmadığını kontrol eder.


er="a" in "merhaba"
er2=4 in [1,2,3,4]

print(er)
print(er2)




liste=[1,2,3,4,5,6,7,8,9]
for eleman in liste:
    print(eleman)
    
    
    
    
toplam=0
lt=[1,5,8,4,23,54,23,66]
for er in lt:
    toplam=toplam+er
    print("toplam: {} eleman: {}".format(toplam,eleman))
print(toplam)





list=[45,32,12,4,54,32,22,75,34]
for dr in list:
    if dr % 2 == 0:
        print(dr)
   
   
        

demet=(1,2,3,4,5,6,7)
for a in demet:
    print(a)





my_list=[(1,2),(3,4),(5,6)]
for vr in my_list:
    print(vr)
    


for (i,j) in my_list:
    print("i:{} j:{}".format(i,j))



tt_list=[(1,2,3),(5,3,3),(3,2,1)]
for (i,j,k) in tt_list:
    print(i,j,k)





## Sözcükler üzerinde gezinmek(Dictionary)
## 3 adet metod vardır. keys(),values(),items()

sozluk={"bir":1,"iki":2,"üç":3}

print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())





# WHILE DÖNGÜLERİ

## belli bir koşul sağlandığı sürece bloklar işlemler gerçekleştirmeye devam eder.
## koşul durumunun bir süre sonra "False" olması gereklidir.

##  while(koşul):
##      işlem1
##      işlem2
##      işlem3




i=0
while(i<10):
    print("i'nin değeri",i)
    i=i+1




lst=[1,2,3,4,5,3,2,2,1,4,6,56,3,23]
index=0
while(index<len(lst)):
    print("index: ",index,"Liste elemanı",lst[index])
    index=index+1







# RANGE FONKSİYONU

## 3 değer alır ,ilk değer başlangıç, ikinci değer bitiş ,üçüncü değer artık değeridir.
## range başına "*" koyabiliriz.

range(0,20)
print(*range(0,20))

print(*range(15))

print(*range(0,100,4))

print(*range(100,0,-2))


for i in range(1,20):
    print("*"*i)
    



# DÖNGÜLERDE KULLANILAN İFADELER: Break and Continue


## Break İfadesi
## Döngü hiç bir zaman koşula bağlı kalmadan sonlanır.


i=0
while(i<10):
    print("i:",i)
    i=i+1
    

rts=[1,2,3,4,5]
for i in rts:
    if(i==3):
        break
    print("i:",i)



while True:
    isim=input("isim( çıkmak için q bas): ")
    if (isim=="q"):
        print("Programdan çıkılıyor....")
        break
    print("isminiz: ",isim)



## Continue İfadesi
## Geri kalan işlemlerini yapmadan direk bloğun başına döner.

tye=[123,43,534,123,123,535,456,56,3,45,345,34,5,4]
for i in tye:
    if(i==56 or i==34):
        continue
    print("i:",i)








## LIST COMPREHENSION

lost=[1,2,3,1,2,3,4,5,6,9]


lost1=[]

for i in lost:
    lost1.append(i)
print(lost1)



lost3=[3,4,6,2,3]
lost4=[i for i in lost3]
print(lost4)


lost5=[i*3 for i in lost3]
print(lost5)


lost6=[(2,3),(4,4),(4,7)]
lost7=[i*j for i,j in lost6]
print(lost7)

 
s="python" 
lost8=[i*3 for i in s]
print(lost8)



lost9=[[1,2,3],[4,5,6],[6,5,4]]
lost10=[]

for i in lost9:
    for x in i:
        lost10.append(x)
print(lost10)

# İç içe yazılmış hali
lost11=[x for i in lost9 for x in i]
print(lost11)






