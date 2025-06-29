import random
while True:
    print("""Bu Kod 1-1000 arasinda rakam secicek
    Size sicak soguk diye deger verecek
    Sizde rakami bulmaya calisacaqsiniz""")
    b1 = random.randint(1, 1000)
    buz_gibi = 300
    soguk = 200
    sicak = 100
    yaniyo = 50
    eriyo = 10
    while True:
        a1 = int(input("Rakam Giriniz: "))
        fark = abs(b1 - a1)
        if fark == 0:
            print("Dogru tahmin")
            break
        elif fark <= eriyo:
            print("Eriyo 10=>")
        elif fark <= yaniyo:
            print("Yaniyo 50=>")
        elif fark <= sicak:
            print("Sicak 100=>")
        elif fark <= soguk:
            print("Soguk 200=>")
        elif fark <= buz_gibi:
            print("Buz gibi 300=>")
        else:
            print("Asiri uzaksin yeniden dene")

    tekrar = input("Yeniden Tahmine ne dersiniz?(evet/hayir)").lower
    if tekrar != "evet":
        print("Bye bye")
        break
