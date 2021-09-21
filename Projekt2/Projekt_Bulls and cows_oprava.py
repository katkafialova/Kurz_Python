import random
oddelovac = "-" * 40


def uvodni_text():
    print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")


def tvorba_cisla():
    cisla = []
    while len(cisla) != 4:
        cisla.append(random.randrange(0, 10))
        if cisla[0] == 0 or len(set(cisla)) < 4 and len(cisla) == 4:
            cisla.clear()
    return cisla


def podminky_hry():
    while True:
        cisla = input('Zadej tip: ')
        if not cisla.isnumeric():
            print("Zadejte čtyřmístné unikátní číslo nezačínající nulou!")
        elif len(cisla) != 4 or not cisla.isnumeric() or cisla[0] == "0":
            print("Zadejte čtyřmístné unikátní číslo nezačínající nulou!")
        elif len(set(cisla)) < 4:
            print("Zadejte čtyřmístné unikátní číslo nezačínající nulou!")
        else:
            return cisla


def hra():
    pokus = 0
    uvodni_text()
    cisla = tvorba_cisla()
    while True:
        bulls, cows = kontrola(cisla, podminky_hry())
        pokus += 1
        if bulls == 4:
            break
        jednotne_mnozne_cislo(cows, bulls)
    print("Uhodnuto! Počet pokusů: ", pokus)
    print(oddelovac)


def jednotne_mnozne_cislo(cows, bulls):
    if cows == 1:
        cows_nazev = "cow"
    else:
        cows_nazev = "cows"
    if bulls == 1:
        bulls_nazev = "bull"
    else:
        bulls_nazev = "bulls"
    print(bulls, bulls_nazev, ",", cows, cows_nazev)
    print(oddelovac)


def kontrola(cisla, tip):
    bulls, cows = 0, 0
    for i, cislo in enumerate(cisla):
        if cislo == int(tip[i]):
            bulls += 1
        if str(cislo) in tip:
            cows += 1
    cows -= bulls
    return bulls, cows


hra()
