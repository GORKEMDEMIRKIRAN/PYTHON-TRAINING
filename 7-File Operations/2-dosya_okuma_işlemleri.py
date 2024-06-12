

# DOSYA OKUMA İŞLEMLERİ




# "r" kipiyle okuma sağlıyoruz.
# read kısaltması
# dosya bulunmuyorsa ; FileNotFoundError hatası dönecektir.

# file4 aslında dosya üzerinde imleç görevi görüyor.
# dosyayı bulamıyor heralde şuanda sıkıntı var.


file4=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")
print(file4)
file4.close()


# Çıktılara dikkat edersen her bir çıktının arasında boşluk var.
# python otomatikman her çıktının sonuna "\n" karakteri koyuyor.
# bunun önüne geçmek için çıktı aldığımız döngüler veya değişkenlerin
# sonuna end="" koyarak \n kurtarırız.

try:
    file5=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")
    for i in file5:
        print(i,end="")
    file5.close()
except FileNotFoundError:
    print("dosya bulunamadı.")




# For döngüsü ile okuma

file6=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")
for i in file6:
    print(i,end="")
file6.close()


# read() fonksiyonu 

# eğer içine hiç bir değer verilmezse bütün dosyamızı okuyacaktır.
# bu fonksiyonlar belirli bir kısmı okuyabiliriz.
# dosyayı tekrar okuyup ikinci kez bastırırsak imleç dosya sonunda olduğu
# için başka birşey bastırmaz.
file7=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")
tools=file7.read()

print("Dosya içeriği1:\n",tools,sep="")
tools2=file7.read()
print("Dosya içeriği2:\n",tools2,sep="")
file7.close()

# readline() fonksiyonu

# her çağrıldğında sadece dosyanın bir satırını okur.
# her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.
# readlines büyün değerleri liste halinde verir.

file8=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")

print(file8.readline())

print(file8.readline())

file8.close()


# readlines() fonksiyonu

# dosyanın bütün satırlarını bir liste şeklinde döner.

file9=open("7-DOSYA_ISLEMLERI\\bilgiler.txt","r",encoding="utf-8")
print(file9.readlines())
file9.close()