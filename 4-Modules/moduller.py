


# MODÜL MANTIĞI

# Pythonda her bir dosya bir modüldür.
# Her bir modül içinde foksiyonlar,sınıflar ve objeler barındırır.

# MODÜL KULLANIMI - MATH MODÜLÜ




# Yöntem1 -import modül adı

# Bir müdülü içe aktarmak yani programa dahil etmek için "import_modül_adı"

import math

print(dir(math))


print(math.factorial(5))
print(math.floor(5.6))


import math as matematik

matematik.factorial(6)


# Yöntem2 - form modül_adı import

# yıldızın anlamı math modülünün içindeki bütün fonksiyonları almak istiyorum demektir.
from math import * 

print(factorial(9))


# sadece "floor" ve "ceil" fonksiyonunu alıyoruz.
from math import floor,ceil





# KENDİ MODÜLÜMÜZÜ YAZMA

# 1 - Herhangi bir tane klasör oluşturuyoruz.
# 2 - Modülümüz ve deneme python dosyamız aynı dizinde olması gerektiği için 2 tane python dosyasını da bu klasör altında oluşturuyoruz.
# 3 - modül.py  ve deneme.py dosyası oluşturuyoruz.
# 4 - modül.py dosyasının içine istediğimiz kadar fonksiyonu yazıyoruz.
# 5 - son olarak deneme.py dosyasının içinde bu modül.py modülünü kullanıyoruz.


# Peki yazdığımız bir modülü her yerden kullanmak için yazdığımız modül1.py dosyasını
# python35/Lib Klasörünün altına atmamız gerekiyor.
# Bu modülü "math" modülü gibi kullanabiliriz.






