def menu():
    print("(1-\033[31mPara Cekmek\033[0m)", "(2-\033[32mPara Yatir\033[0m)",
          "(3-\033[33mPara Kontrol\033[0m)", "(4-\033[36mPara Cevirici\033[0m)", "(5-\033[91mCikis\033[0m)")


def cekmek():
    while True:
        global para
        try:
            ne_kadar = float(input("\033[95mNe kadar\033[0m:"))
            if ne_kadar > para:
                print("\033[91m!!!!O kadar paran yok fakir!!!!\033[0m")
            else:
                para = para - ne_kadar
                print(f"\033[32mBakiye\033[0m:{para:.2f} {para_birimi}")
            break
        except ValueError:
            print("Hata")


def yatirmak():
    while True:
        global para
        try:
            ne_kadar = float(input("\033[95mNe kadar\033[0m:"))
            para = para + ne_kadar
            print(f"\033[32mBakiye\033[0m:{para} {para_birimi}")
            break
        except ValueError:
            print("Hata")


def cevirici():
    while True:
        global para, para_birimi
        print(f"Mecvut bakiye:{para:.2f} {para_birimi}")
        birim = input(
            f"Su anki para birminiz:{para_birimi} Hangi para biri olsun:(USD/TL/AZN)").upper()
        if para_birimi == "TL" and birim == "USD":
            para = para / 40
            para_birimi = "USD"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        elif para_birimi == "TL" and birim == "AZN":
            para = para / 23
            para_birimi = "AZN"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        elif para_birimi == "AZN" and birim == "USD":
            para = para * 0.588
            para_birimi = "USD"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        elif para_birimi == "AZN" and birim == "TL":
            para = para * 23
            para_birimi = "TL"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        elif para_birimi == "USD" and birim == "AZN":
            para = para * 1.7
            para_birimi = "AZN"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        elif para_birimi == "USD" and birim == "TL":
            para = para * 40
            para_birimi = "TL"
            print(f"Bakiye:{para:.2f} {para_birimi}")
        else:
            print("Bu dönüşüm desteklenmiyor.")
            print(f"Yeni bakiye: {para:.2f} {para_birimi}")
        break


def kontrol():
    print(f"\033[32mBakiye\033[0m:{para:.2f}{para_birimi}")


para = 0
para_birimi = "USD"
while True:
    menu()
    secim = int(input("\033[94mIslem\033[0m:"))
    if secim == 1:
        cekmek()
    elif secim == 2:
        yatirmak()
    elif secim == 3:
        kontrol()
    elif secim == 4:
        cevirici()
    elif secim == 5:
        print("Bye")
        break
    else:
        print("Lutfen gecerli islem giriniz")
