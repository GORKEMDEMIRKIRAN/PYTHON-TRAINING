

# DOSYA İŞLEMLERİ UYGULAMA - 3


# PROJE - 2


# "futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe 
# ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. Bu dosyadan herbir 
# takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 
# farklı dosyaya yazın.

# "futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

#                 Fernando Muslera,Galatasaray
#                 Atiba Hutchinson,Beşiktaş
#                 Simon Kjaer,Fenerbahçe
#                            //
#                            //
#                            //
#                            //
#                            //

#  "futbolcular.txt" Dosyası oluşturuldu.

def create_list(dt):
    dt=dt[:-1]
    row=dt.split(",")
    return row

with open("7-File Operations\\uygulama_3\\futbolcular.txt","r",encoding="utf-8") as file:
    gs=[]
    fb=[]
    bjk=[]
    for person in file:
        convert=create_list(person)
        # verinin başında boşluk var dikkat et.
        if convert[1].strip()=="Beşiktaş":
            bjk.append(person)
        elif convert[1].strip()=="Galatasaray":
            gs.append(person)
        else:
            fb.append(person)
    with open("7-File Operations\\uygulama_3\\bjk.txt","w",encoding="utf-8") as file1:
        for i in bjk:
            file1.write(i)
    with open("7-File Operations\\uygulama_3\\fb.txt","w",encoding="utf-8") as file2:
        for j in fb:
            file2.write(j)
    with open("7-File Operations\\uygulama_3\\gs.txt","w",encoding="utf-8") as file3:
        for k in gs:
            file3.write(k)
               
    
        
        

