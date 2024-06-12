


# NESNE TABANLI PROGRAMLAMA (OOP) (Objected Oriented Programming)

# Obje ve nesne nedir ?

# Kumandanın kendi içinde değişik özellikleri (attribute) ve fonksiyonları(metod) bulunur.
# kırmızı tuşa basınca televizyonun kapanması bu kumandanın metodlarıdır.
# bunun gibi pythondaki her şey bir objedir.
# listelere bakarsak liste objesinin birçok metodu ve özelliği bulunur.

# liste => obje
# append => metod

liste=[4,42,2]
liste.append(7)

sozluk=dict()

def total(a,b):
    return a+b


type(liste)          # liste objesi
type(sozluk)         # dictionary objesi
type((1,2,3))        # tuple objesi
type(total(65,5))    # fonksiyon objesi









# NESNE TABANLI PROGRAMLAMA -SINIFLAR

# CLASS ANAHTAR KELİMESİ

# Sınıflar ve classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını 
# tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz isterseniz
# bir araba class tanımlayarak yapımızı kurmaya çalışalım.

class Araba():
    model="Renault"        # sınıflarımızın özellikleri
    renk="Gümüş"
    beygir_gücü=110
    silindir=4
    

araba1=Araba()

print(araba1.model)


# Yani biz bir obje oluşturduğumuzda bu özelliklerin değerleri varsayılan olarak gelir.
# Bu özelliklerin değerlerine herhangi bir obje oluşturmadan da erişebiliriz.

print(araba1.renk)   # class ismi özellik ismi

# Her bi objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor.
# Bunun içinde özel bir metodu kullanmamız gerekmektedir.
# " __init__ "
# "init" metodu pythonda "yapıcı(constructor) fonksiyon olarak tanımlanır."
# Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur.
# Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.

# init fonksiyonu otomatik olarak çağrılır.
# self objeyi gösteren referans
# self metodlarımınızda en başta bulunması gereken bir parametredir.
# biz bir objenin bütün ozelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.

# Araba veri tipi

class Araba():
    model="Renault"        # sınıflarımızın özellikleri
    renk="Gümüş"
    beygir_gücü=110
    silindir=4
    def __init__(self):
       print("init fonksiyonu çağrıldı")
araba1=Araba()
print(araba1)


class car():
    def __init__(self,model,renk,beygir_gücü,silindir): # parametrelerimizin değerlerini objeleri oluştururken göndereceğiz.
        self.model=model                  # self.özellik_ismi= parametre değeri şeklinde objemizin "model" özelliğine değeri atıyoruz.
        self.renk=renk                    #
        self.beygir_gücü=beygir_gücü
        self.silindir=silindir
        
        
car1=car("Reno","Gümüş",100,6)
car2=car("Ibıza","kırmızı",150,4)

print(car1.model)
print(car2.model)
    
    
class car():
    def __init__(self,model="Bilgi Yok",renk="Bilgi Yok",beygir_gücü="Bilgi Yok",silindir="Bilgi Yok"): 
        self.model=model                 
        self.renk=renk                   
        self.beygir_gücü=beygir_gücü
        self.silindir=silindir
        




# NESNE TABANLI PROGRAMLAMA -METODLAR

# Sınıf içerisindeki metodları nasıl tanımlayacağımızı öğrenmeye çalışıcaz.
# İlk olarak yazılımcı sınıfı tanımlıyalım.


class software():
    def __init__(self,name,surname,phone_number,salary,language):
       self.name=name
       self.surname=surname
       self.phone_number=phone_number        # Yazılımcı objelerin özellikleri
       self.salary=salary
       self.language=[language]
    
    def information_see(self):
        print("""
              Yazılımcı objesinin özellikleri
              Name:{}
              Surname:{}
              Phone_number:{}
              Salary:{}
              Language:{}
              """.format(self.name,self.surname,self.phone_number,self.salary,self.language))
        
    def   do_raise(self,amount_raise):
        print("A raise is being made...")
        self.salary =self.salary + amount_raise   
        
    def   add_language(self,new_language):
        print("A language is adding made...")
        self.language.append(new_language)
        
       
   
software1=software("Yeliz","Binal",543,10000,["germany","english"])
print(software1.language)
print("="*50)
print(software1.information_see())
print("="*50)
print(software1.do_raise(1700))
print("="*50)
print(software1.add_language("france"))





# NESNE TABANLI PROGRAMLAMA -KALITIM (ınheritance)


# kalıtım ve miras alma konseptini öğrenmeye çalışacağız.
# Kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute) ve metodlarını miras almasıdır.

# inheritance nerede işimize yarar ?
# Örneğin bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz.
# Bunun için "yönetici","proje direktörü","işçi" gibi sınıflar oluşturmamız gerekiyor
# Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
# O zaman bu ortak özellikleri ve metodları tekrar tekrar bu sınıfların içinde tanımlamak yerine
# bir tane ana class tanımlanıp bu classların özelliklerini ve metodlarını almalarını sağlayabiliriz.
# Inheritance veya kalıtım'ın temel mantığı budur.


class worker():
    def __init__(self,name,salary,department):
        print("Çalışan sınıfının init fonksiyonu")
        self.name=name
        self.salary=salary
        self.department=department

    def see_information(self):
        
        print("Çalışan sınıfının bilgileri......")
        print("Name: {} \nSalary: {} \nDepartment: {}\n".format(self.name,self.salary,self.department))
    
    def change_department(self,new_department):
        self.department=new_department
    
class manager(worker):     
    def do_raise(self,raise_amount):
        self.salary=self.salary + raise_amount
        
 
        
manager1=manager("Mustafa murat coşkun",70000,"Bilişim")
print(manager1)


print(manager1.see_information())

print(manager1.change_department("Yönetim"))
print(manager1.see_information())

print(manager1.do_raise(32000))
print(manager1.see_information())



# OVERRIDING (IPTAL ETME)

# Eğer biz miras aldığımız metdoları aynı isimle kendi sınıfımızda tekrar tanımlarsak,
# artık metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır.

# Örneğin artık çalışan sınıfının "init" metodunu kullanmak yerine yöentici sınıfında "init" metodunu 
# override edebiliriz.  Böylelikşe yönetici sınıfına ekstra özellikleri (attribute) ekliyebiliriz.




class managerr(worker):
    def __init__(self,name,salary,department,number_person):
        
        print("Yönetici sınıfının init fonk.")
        self.name=name
        self.salary=salary
        self.department=department
        self.number_person=number_person
    
    def see_information(self):
        
        print("Çalışan sınıfının bilgileri......")
        print("Name: {} \nSalary: {} \nDepartment: {}\n".format(self.name,self.salary,self.department))
    
    def change_department(self,new_department):
        self.department=new_department 
            
    def do_raise(self,raise_amount):
        self.salary=self.salary + raise_amount


manager2=managerr("Oğuz artıran",3500,"bilişim",10)

print(manager2)

print(manager2.see_information())

print(manager2.change_department("Yönetim"))
print(manager2.see_information())

print(manager2.do_raise(32000))
print(manager2.see_information())



# super anahtar kelimesi

# en genel anlamı miras aldığımız sınıfın metodlarını alt sınıflarından kullanmamıza sağlar.
# çalışan sınıfında 3 tane özellik var.
# yönetici sınıfında 3 tane aynı 1 tane farklı özellik var.
# şimdi ben bu süper anahtar ile çalışan sınıfındaki özellikleri yönetici sınıfında çağırıp
# kalan 1 özellik yani "kişi sayısını" ekliyeceğim.



class worker():
    def __init__(self,name,salary,department):
        print("Çalışan sınıfının init fonksiyonu")
        self.name=name
        self.salary=salary
        self.department=department

    def see_information(self):
        
        print("Çalışan sınıfının bilgileri......")
        print("Name: {} \nSalary: {} \nDepartment: {}\n".format(self.name,self.salary,self.department))
    
    def change_department(self,new_department):
        self.department=new_department
    
class managerr(worker):
    def __init__(self,name,salary,department,number_person):
        
        # yukarıda ki 3 özelliği tekrar yazmadan çağırdık.
        super().__init__(name,salary,department)
        print("Yönetici sınıfının init fonk.")
    
        self.number_person=number_person
    
    def see_information(self):
        
        print("Çalışan sınıfının bilgileri......")
        print("Name: {} \nSalary: {} \nDepartment: {}\n".format(self.name,self.salary,self.department))
    
    def change_department(self,new_department):
        self.department=new_department
            
    def do_raise(self,raise_amount):
        self.salary=self.salary + raise_amount
        



# NESNE TABANLI PROGRAMLAMA - ÖZEL METODLAR

# Bunların çoğunu biz tanımlamasakta python tarafından varsayılan olarak tanımlanır
# ancak bu metodların bazıları da özel olarak bizim tanımlamamız gerekmektedir.
# Gördüğümüz "__init__" metodları bu metodlara örnektir.


# pass ile boş bırakıyoruz.
class Kitap():
    pass

# biz çağırmasak bile python init kendi çağırıyor.
kitap=Kitap()  ## __init__ metodu

print(kitap)   ## str_metodu python kendi tanımlamış

# aslında python burada len metodunu çağırmak istiyor
# ama nasıl tanımalyacağını bilmediği için bizim tanımlamamızı istiyor.

# len(kitap) ## __len__ metodu

# del kitap ## __del__ metodu


class Kitap():
    def __init__(self,name,writer,page_number,type):
        print("İnit fonksiyonu")
        self.name=name
        self.writer=writer
        self.page_number=page_number
        self.tpye=type
    def __str__(self):
        return "isim: {}\nYazar: {}\nSayfa sayısı: {}\nTürü: {}".format(self.name,self.writer,self.page_number,self.tpye)
        
    def __len__(self):
        return self.page_number
    
    # burada python del metodunu aslında override etmiyorum.
    # sadece ektra özellikler ekliyorum.
    def __del__(self):
        print("Kitap objesi siliniyor....")
        
kitap=Kitap("İstanbul hatırası","Ahmet ümit",561,"Polisiye")
kitap1=Kitap("İstanbul hatırası","Ahmet ümit",561,"Polisiye")

# str python yerine biz dönüştürdük.
print(kitap)

# len biz tanımlayınca sayfa sayısını verdi.
print(len(kitap))

del kitap1