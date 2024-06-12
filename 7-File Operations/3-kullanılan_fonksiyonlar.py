

#   DOSYALARDA KULLANILAN FONKSİYONLAR


# Dosyalarda kullanılan metodları öğrenmeye çalışacağız.



# Dosyalarda Otomatik Kapatma

with open("7-File Operations\\bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)
    
# dosyanın en sonuna gidiyoruz.
# ancak biz imleci dosyanın her hangi bir yerine götürmek isteyebiliriz.

# Bunun için, seek() fonksiyonunu kullanıcaz.

# Önce imlecin hangi byte olduğunu öğrenmek için tell() bakıcaz.
with open("7-File Operations\\bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())
    

# burada başka bir byte görerek bakalım.
with open("7-File Operations\\bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())
    
    
with open("7-File Operations\\bilgiler.txt","r",encoding="utf-8") as file:    
    file.seek(5)
    icerik=file.read(10)
    print(icerik)
    

