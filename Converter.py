while True:
    s1 = {1: "Kg = Gram = Ton",
          2: "Metr = Santim = Km",
          3: "Litr = ml = Ton",
          4: "Dakika = Saat = Saniye",
          5: "Gun = Hafta = Ay = Yil",
          6: "Saniye ses = Mesafe ses",
          7: "Km saat hiz = saniyede = dakika"}
    for k, v in s1.items():
        print(f"{k}.({v})")
    while True:
        try:
            s = int(input("işlem?(1-7): "))
            if s in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print(" \nRakam giriniz!!")
        except ValueError:
            print(" \nLutfen Sayi Giriniz!!")

    if s == 1:
        kg = float(input("Kac kilogram?: "))
        print(f"{round(kg)} kg = {round(kg * 1000)} gram = {round(kg / 1000)} ton")

    elif s == 2:
        metr = float(input("Kac metr?: "))
        print(
            f"{round(metr)} Metr = {round(metr * 100)} Santim = {round(metr / 1000)} Km\n")

    elif s == 3:
        litr = float(input("Kac litr?: "))
        print(
            f"{round(litr)} litr = {round(litr * 1000)} Ml = {round(litr / 1000)} Ton\n")

    elif s == 4:
        dakika = float(input("Kac dakika?: "))
        print(
            f"{round(dakika)} Dakika = {round(dakika / 60)} Saat {round(dakika * 60)} Saniye\n")

    elif s == 5:
        Gun = float(input("Kac Gun?: "))
        print(f"{round(Gun)} Gun = {round(Gun / 7)} Hafta = {round(Gun / 30)} Ay = {round(Gun / 365)} Yil\n")

    elif s == 6:
        Ses = float(input("Kac Saniye Ses?: "))
        print(f"{round(Ses)} Saniye Ses = {round(Ses * 343)} Metr\n")

    elif s == 7:
        km = float(input("Kac km hiz ?: "))
        print(
            f"{round(km, 2)} Km/Saat = {round(km * 0.27778, 2)} Metr/Saniye = {round(km / 60, 2)} Km/Dakika\n")

    tekrar = input("Tekrar??: ")
    if tekrar != "evet":
        print("Sagolun")
        break
