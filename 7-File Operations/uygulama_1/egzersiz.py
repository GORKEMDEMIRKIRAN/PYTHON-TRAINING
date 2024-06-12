

# BU KISIMDA "DOSYA.TXT" BULUNAN ÖĞRENCİ BİLGİLERİNE GÖRE HARF NOTLARI ATIYORUZ.

# İsimlere göre atadığımız harf notlarını "notlar.txt" dosyası oluşturup içine yazdırdık.





# dosya verilerinin içinde her satırın sonunda \n var unutma
# [:-1] yaparak sonunda bulunan \n siliyoruz.
def convert_to_data(data):
    data=data[:-1]         # \n aldı.
    row=data.split(",")    # split kullanımında çıktı liste halinde verilir.
    names=row[0]
    one=row[1]
    two=row[2]
    three=row[3]
    calculate=(0.30*float(one))+(0.30*float(two))+(0.40*float(three))
    row.insert(4,calculate)
    if (row[4] >= 90):
        letter = "AA"
    elif (row[4] >= 85):
        letter = "BA"
    elif (row[4] >= 80):
        letter = "BB"
    elif (row[4] >= 75):
        letter = "CB"
    elif (row[4] >= 70):
        letter = "CC"
    elif (row[4] >= 65):
        letter = "DC"
    elif (row[4] >= 60):
        letter = "DD"
    elif (row[4] >= 55):
        letter = "FD"
    else:
        letter = "FF"
        
    # Bu kısımda öğrenci isimleri ve bunlara atanan harf notlarını yazdırdık.
    # \n ile satır bazında çıktı aldık.
    return names + "------------------> " + letter + "\n"
    
    




# Bu kısımda not çıktılarını verenleri listeye ekledik.

with open("7-File Operations\\uygulama_1\\dosya.txt","r",encoding="utf-8") as file:
    average_list=[]
    for i in file:
        average_list.append(convert_to_data(i))

# Bu kısımda harf notlarının çıktılarını notlar.txt dosyası açarak içine yazdırdık.
        
    with open("7-File Operations\\uygulama_1\\notlar.txt","w",encoding="utf-8") as file2:
        for i in average_list:
            file2.write(i)
            
    
    
#  Burada ise "notlar.txt" dosyasını okuduk.
with open("7-File Operations\\uygulama_1\\notlar.txt","r",encoding="utf-8") as file:
    print(file.read())