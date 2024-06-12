
# DOSYA İŞLEMLERİ UYGULAMA-2


# PROJE - 1

# Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız 
# programı geliştirerek kalanları "kalanlar.txt" dosyasında ve geçenleri "geçenler.txt" 
# dosyasına yazmaya çalışın.

def convert_to_data(data):
    data=data[:-1]        
    row=data.split(",")    
    names=row[0]
    one=row[1]
    two=row[2]
    three=row[3]
    calculate=(0.30*float(one))+(0.30*float(two))+(0.40*float(three))
    row.insert(4,calculate)
    
    def letter_note(row):
        if (row[4] >= 95):
            letter = "AA"
        elif (row[4] >= 90):
            letter = "AB"
        elif (row[4] >= 85):
            letter = "BA"
        elif (row[4] >= 80):
            letter = "BB"
        elif (row[4] >= 75):
            letter = "BC"
        elif (row[4] >= 70):
            letter = "CB"
        elif (row[4] >= 65):
            letter = "CC"
        elif (row[4] >= 60):
            letter = "CD"
        elif (row[4] >= 55):
            letter = "DC"
        elif (row[4] >= 50):
            letter = "DD"
        else:
            letter = "FF"
        return letter
    letter=letter_note(row)
    row.insert(5,letter)
    if row[5] == "FF":
        row.insert(6,"Kaldı")
    else:
        row.insert(6,"Geçti")
    return row



with open("7-File Operations\\uygulama_2\\dosya.txt","r",encoding="utf-8") as file:
    successfull=[]
    unsuccessfull=[]
    for inside in file:
        event=convert_to_data(inside)
        if event[6]=="Geçti":
            successfull.append(inside)
        else:
            unsuccessfull.append(inside)
    with open("7-File Operations\\uygulama_2\\başarılı.txt","w",encoding="utf-8") as file1:
        for i in successfull:
            file1.write(i)
    with open("7-File Operations\\uygulama_2\\başarısız.txt","w",encoding="utf-8") as file2:
        for j in unsuccessfull:
            file2.write(j)
         
         
         
         
         
         
         
         
           
    
        