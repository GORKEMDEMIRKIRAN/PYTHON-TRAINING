


# HATA YAKALAMA

# try-except-finally

# try,except blokları

# try:
#      hata çıkarabilecek kod
#      hata çıkarsa except bloguna giricek.
#      geri kalan try blogundakiler çalışmayacaktır.
# except hata1:
#      hata oluştugunda burası çalışıcaktır.
# finally:
#      mutlaka çalışması gereken kodlar buraya yazılıcak.
#      Bu blok her türlü çalışıcaktır.

try:
    a=int("asd2452")
    print("program burada")
except:
    print("bir hata oluştu")
print("blok sona erdi.")




try:
    b=int("asf34")
    print("program burada")
except ValueError:
    print("bir hata oluştu.")
print("blok son")





try:
    a=int(input("sayı1: "))
    b=int(input("sayı2: "))
    print(a/b)
except ValueError:
    print("lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez.")
print("blok bitti")



try:
    a=int(input("sayı1: "))
    b=int(input("sayı2: "))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("input hatalı")
print("blok bitti")



try:
    a=int(input("sayı1: "))
    b=int(input("sayı2: "))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("input hatalı")
finally:
    print("çıktılar hazır.")
print("blok bitti")


# HATA FIRLATMAK

# Bazen kendi yazdığımız fonk. yanlış kullanılırsa kendi hatalarımızı üretip pythonda
# bu hataları fırlatabiliriz.
# Bunun içinde "raise" anahtar kelimesini kullanıcaz.
# hata fırlatma şu şekilde yapılabilmektedir.

#  raise HataAdı(opsiyonel hata mesajı)

# verilen string'i ters çevirmek

def terscevirme(s):
    if (type(s) != str):
        raise ValueError("lütfen doğru bir input girin.")
    else:
        return s[::-1]


print(terscevirme("python"))
print(terscevirme(23))
