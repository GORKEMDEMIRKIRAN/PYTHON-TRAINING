

# Problem 1

# Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
# Bunu yaparken try,except bloklarını kullanmayı unutmayın.

for element in liste:
    try:
        element=int(element)
        print(element)
    except:
        pass

