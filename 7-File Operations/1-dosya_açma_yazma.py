
# DOSYA AÇMA VE DOSYAYA YAZMA İŞLEMLERİ



import os
print(os.getcwd())  # Bu komut, geçerli çalışma dizinini gösterecektir.
# Dosya açmak
#   open() 
#   yapısı: open(dosya adı,dosya erişme kipi)
#   "w" dosya kipi
#       write anlamına gelir.
#       "dosya ismi" yoksa oluşturuyor.
#       "dosya ismi" varsa o dosyayı silip tekrar oluşturuyor ve içindekiler gidiyor.
# işimiz bittiğinde dosyayı kapatmamız gerekiyor.
# 1 karakter 1byte olduğunu görebiliriz.

# "w" sadede dosya açıyor oluşturmuyor.
# write kısaltması

# bu dosyayı examples atına açıyor o yüzden dosya yolu kullanmak daha mantıklı

# open("bilgiler.txt","w")
# file=open("bilgiler.txt","w")
# file.write("katuna elima")
# file.close()


# Dosya yolunda çift \\ kullanıcaz.Unutma ikinci \ diğerine karşılık gelir.
# "encoding="utf-8"" bizim txt dosyasına türkçe karakter yazmamıza izin verir.
file2=open("C:\\Users\\gorke\\Desktop\\PYTHON-UDEMY\\7-DOSYA_ISLEMLERI\\bilgiler.txt","w",encoding="utf-8")
file2.write("drole\n")
file2.write("ase\n")
file2.write("drobem\n")
file2.close()


# "a" Kipiyle dosyalara yazmk
# append ekleme kelimesinin kısaltması 
#  eğer dosya yoksa oluşturur.
#  eğer dosya varsa sonuna gidip ekleme yapar.

file3=open("C:\\Users\\gorke\\Desktop\\PYTHON-UDEMY\\7-DOSYA_ISLEMLERI\\bilgiler.txt","a",encoding="utf-8")
file3.write("ekleme yap\n")
file3.write("ekle\n")
file3.close()



