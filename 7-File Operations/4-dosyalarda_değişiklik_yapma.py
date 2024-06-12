

#  Bu kısımda hem okuma hem yazma işlemini kullanıcaz.

# seek() okuma write() yazma işlemi yapıyor.
# bunun için "r+" kipini kullanıcaz.

with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as fl:
    print(fl.read())
    
with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as fl:
    fl.seek(10)
    fl.write("deneme")
    
with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as fl:
    print(fl.read())  
    
    
    
    
    
    
# DOSYALARIN SONUNDA DEĞİŞİKLİK YAPMA

# append metoduyla "a" kipiyke açalım ve dosya sonuna write() ekleme yapalım.
with open("7-File Operations\\bilgiler.txt","a",encoding="utf-8") as file:
    file.write("mert altan\n")
    
    

with open("7-File Operations\\bilgiler.txt","r",encoding="utf-8") as file:
    print(file.read())








# DOSYANIN BAŞINDA DEĞİŞİKLİK YAPMA

# Dosyamızın başına 1 tane satır eklemek için dosyamızı bütünüyle string halde
# alıp daha sonra satırımızı string'in başına eklemeliyiz.

with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as file:
    tools=file.read()
    print(tools)



with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as file:
    
    tools=file.read()
    
    new_tools="semiy yücel\n" + tools
    file.seek(0)
    file.write(new_tools)
    
    
    
    
    
    
    
    
    
# DOSYANIN ORTASINDA DEĞİŞİKLİK YAPMA

# Dosyanın ortasında değişiklik yapmak için her satırı liste halinde alan
# "readlines()" fonk. kullanıcaz. her hangi bir yerine "insert()" fonk.
# ekleme yaparak "for" döngüsüyle yazdırıcaz.

with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.readlines())  # liste halinde verdi.
    

with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as file:
    list=file.readlines()  # liste halinde verdi.    
    print(list)
    
    
with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as ft:    
    liste=ft.readlines()  # liste halinde verdi.    
    liste.insert(3,"ahmet dikec\n")
    ft.seek(0)
    for i in liste:
        ft.write(i)
        
with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as ft:         
    print(ft.read())
    
    
# "for" döngüsü yerine dosya içine yazan "writelines()" kullanabiliriz.
with open("7-File Operations\\bilgiler.txt","r+",encoding="utf-8") as ft:    
    liste=ft.readlines()  # liste halinde verdi.    
    liste.insert(3,"bds\n")
    ft.seek(0)
    ft.writelines(liste)  
    ft.read()
        

