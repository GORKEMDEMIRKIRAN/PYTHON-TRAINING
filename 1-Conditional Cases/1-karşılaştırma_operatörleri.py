

# MANTIKSAL DEĞERLER VE KARŞILAŞTIRMA OPERATÖRLERİ

##  Mantıksal Değerler (Boolean)
### True-False

a=True
print(type(a))
b=False
print(type(b))

### 0 farklı ise "TRUE" 0 ise "FALSE" 
print(bool(0.14))
print(bool(-1))
print(bool(0))

### bir değişkene sonradan değer atamak istersek "None"

z=None
print(z)

### KARŞILAŞTIRMA OPERATÖRLERİ
we1=12
we2=10
print(we1==we2)
print(we1!=we2)
print(we1>we2)
print(we1<we2)
print(we1>=we2)
print(we1<=we2)


# MANTIKSAL BAĞLAÇLAR


print("-"*50)
## "and" Operatörü
print("murat"=="murat" and 1<2)
print("murat"=="murat" and 3<2)


print("-"*50)
## "or" Operatörü
print("murat"=="murat" or 1<2)
print("murat"=="murat" or 3<2)


print("-"*50)
## "not"  Operatörü

print(not 2==2)
print(not 3==2)

print("-"*50)
## Operatörleri beraber kullanmak
dr=not 2>3 or(2!=2 and "murat"=="murat")
print(dr)





# IF-ELSE KOŞULLU DURUMLARI
print("-"*50)
a=2
if(a==2):
    print(a)
print("merhaba")


print("-"*50)
#yas=int(input("Yaşınızı giriniz: "))
yas=30
if (yas<18):
    print("bu mekana giremessiniz.")
else:
    print("mekana hoşgeldiniz.")
    

print("-"*50)
note=94
if (note>=90):
    print("AA")
elif(note>=85):
    print("AB")
elif(note>=80):
    print("BA")
elif(note>=75):
    print("BB")
elif(note>=70):
    print("BC")
elif(note>=65):
    print("CB")
elif(note>=60):
    print("CC")
elif(note>=55):
    print("CD")
elif(note>=50):
    print("CD") 
elif(note>=45):
    print("DD")     
else:
    print("Kaldınız.")














    
