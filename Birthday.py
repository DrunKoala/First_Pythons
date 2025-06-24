import datetime
while True:
    yil = int(input("Hangi yilda Dogdun? "))
    ay = int(input("Kacinci ayda Dogdun? "))
    gun = int(input("Hangi gunde Dogdun? "))
    simdiki = datetime.datetime.now()
    if ay > simdiki.month:
        yas = simdiki.year - yil - 1
    elif gun > simdiki.day:
        yas = simdiki.year - yil - 1
    else:
        yas = simdiki.year - yil

    if gun > simdiki.day:
        kalan_gun = gun - simdiki.day

    print(f"Yasin bu:\033[32m{yas}\033[0m \nKalan Gun:{kalan_gun}")
