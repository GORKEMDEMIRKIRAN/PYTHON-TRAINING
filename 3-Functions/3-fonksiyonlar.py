


#  METODLAR

# Bu veri tiplerinden oluşturulan her bir değişken pythonda obje(object) olarak düşünülür.
# Python geliştiricileri bu objelere birçok metod tanımlanmıştır.

# Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır.
# Şu şekilde kullanılır;

# obje.herhangi_bir_metod(değerler(opsiyonel))

# Liste objesi üzerinde bakalım.

a=[1,2,3,5,3,2,3,6,6]

print(type(a))

a.insert(1,"bilal")
print(a)

a.append("PYTHON")
print(a)

a.pop()
print(a)







#  FONKSİYONLAR

#  PRİNT(),TYPE() bunlar gömülü fonksiyonlar(built-in-function)
# Biz kendi özel fonksiyonlarımızı tanımlayabiliriz.(user-defined functions)


# FONKSİYONLARIN TANIMLANMASI
# def fonksiyon_Adı(parameter1 , parameter2 .... (opsiyonel)):
#          fonksiyon bloğu
#         Yapılacak işlemler
#           dönüş değeri - opsiyonel


def welcome():
    print("Hoşgeldiniz")
    
print(welcome())



def create(isim):
    print("isminiz: ",isim)
print(create("salih"))




def total(a,b,c):
    print("total: ",a+b+c)

print(total(5,6,7))



def factorial(number):
    factorial=1
    if (number==0 or number==1):
        print("FAKTÖRİYEL: ",factorial)
    else:
        while (number >=1):
            factorial=factorial*number
            number=number-1
        print("Faktöriyel: ",factorial)
    
    
    
    
    
# FONKSİYONLAR / RETURN

def toplama(a,b,c):
    print("toplamları",a+b+c)
    
def ikiye_carp(a):
    print("ikiyle çar",a*2)
    

# hata alırız
topla=toplama(1,2,4)
print(ikiye_carp(topla))



def toplama1(a,b,c):
    return a+b+c
def ikiyle_carp1(a):
    return a*2

toplam=toplama1(2,3,5)
print(ikiyle_carp1(toplam))







# return'Den sonra yazılan satırlar çalışmaz

def ucle_carp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyle_topla(a):
    print("2.fonksiyon çalıştı")
    return a+2
def derde_bol(a):
    print("3.fonksiyon çalıştı")
    return a/4


print(derde_bol(ikiye_carp(ucle_carp(5))))







# FONKSİYONLAR / FONKSİYONLARDA PARAMETRE TÜRLERİ

def selamla(isim):
    print("selam",isim)
    
def selamla2(isim="isimsiz"):
    print("selam",isim)
   

# Burada değer vermeden çalışmaz. 
print(selamla("murat"))
# burada değer vermeden çıktı alabiliyoruz
# bunlar foksiyonlarımızın varsayılan değerleri oluyor.
print(selamla2())


def bilgilerigöster(ad,soyad,numara):
    print("ad",ad,"soyad",soyad,"nuamra",numara)
    
def bilgilerigöster2(ad="Bilgi yok",soyad="Bilgi yok",numara="Bilgi yok"):
    print("ad",ad,"soyad",soyad,"nuamra",numara)
    
print(bilgilerigöster("ali","barak",234))
print(bilgilerigöster2())

print(bilgilerigöster("ali","barak",234,sep="/"))


# FONKSİYONLAR / ESNEK SAYIDA DEĞERLER


# burada 3 taneden fazla değer toplamıyor
# bunu esnek hale getirmeye çalışıyoruz.
def addition(a,b,c):
    print(a+b+c)
    
#  burada girdigimiz sınırsız sayıda değeri bir liste içinde tuttugunu görebiliriz.
def addition2(*a):
    print(a)

print(addition(1,3,45,6,55))

# şimdi üstte gördüğümüz fonksiyonda istenilen sayıda değer girebiliyoruz.
# şimdi bu değerleri for döngüsüyle gezerek toplayalım.

def addition3(*a):
    toplam=0
    for i in a:
        toplam=toplam+i
    print(toplam)

print(addition3(2,3,5,6,23,42,34,23,423,5,64,6,57,34,432,4,35))




# FONKSİYONLAR / GLOBAL VE YEREK(LOCAL) DEĞİŞKENLER




# Sınıfların(class) aslında bir kapsamı(scope) bulunur.
# python her bir değişkeni bir isim alanında(namespace) tanmlar
# Değişkenin isim alanı ise bu değişkenlerin nerelerde var olduğunu ve nerelerde kullanılabileceğini gösterir.
# Local örnek olarak fonksiyon içinde bulunan değişkenler fonksiyon dışında çalışmazlar.
# Global tanımaldığı andan itibaren her yerde ulaşılabilir.

def fonksiyon():
    a=10
    print(a)

print(fonksiyon())
# burada hata alırız çağırdığımız "a" local bir değişkendir.
print(a)



b=7
def fonksiyon2():
    print(b)
print(fonksiyon2())




# hata alırız "s" tanımlı değil
def fonksiyon3():
    print(s)
print(fonksiyon3())
s="pytphn"



# global ve local bir arada kullanalım

c=10
def fonksiyon4():
    c=2
    print(c)
print(fonksiyon4())
print(c)



d=6
def fonksiyon5():
    global d
    d=3
    print(d)
print(fonksiyon5())
print(d)



# Burada gördüğümüz gibi if ve while bloklarında tanımlanan değişkenler
# yerel bir değişken yerine global bir değişken olmaktadır.


if True:
    t=10
    print(t)
print(t)


while True:
    value=10
    print(value)
    break
print(value)






# FONKSİYONLAR / LAMBDA İFADELERİ

# Lambda ifadeleri(expression)
# Lmabda ifadeleri fonksiyonlarımızı oluşturmak için pythonda bulunan pratik bir yöntemdir.

# List comprehension hatırlayalım.


# Klasik liste oluşturma yöntemi
lst1=[1,2,3,4,6]
lst2=list()
for i in lst1:
    lst2.append(i)
print(lst2)

# List comprehension
lst3=[213,5,3,2,5]
lst4=[i*2 for i in lst3]
print(lst4)


# Lambda ifadeleri yapısı ( tek satırda oluşturulabilir.)

#   etiket= lambda parameter1, parameter2, .....: işlem



def carp(x):
    return x*2
print(carp(4))

carpma= lambda x : x*2
print(carpma(5))





def toplama(x,y,z):
    return c+y+z
print(toplama(10,11,12))

toplamam=lambda x,y,z:x+y+z
print(toplamam(3,4,2))




def terscevir(s):
    return s[::-1]
print(terscevir("asdgaefghj"))

ters=lambda s :s[::-1]
print(ters("pythpn"))













