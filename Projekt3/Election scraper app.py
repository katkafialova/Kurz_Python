# Kateřina Fialová - 3.projekt

# Knihovny
from bs4 import BeautifulSoup
import requests
import csv


# Oddělovače
separator1 = "-" * 80
separator2 = "=" * 30
separator3 = "=" * 80


def main():
    print(separator1)
    print(separator2 + "Election scraper app" + separator2)
    print(separator1)
    print("""
    1)Otevři následující odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
    2)vyber si územní celek kliknutím na "X"
    """)
    print(separator1)

    url_uzemni_celek = zadani_url_uzemni_celek()
    print(separator1)
    nazev_souboru = zadani_nazvu_souboru()

    soup = ziskat_data(url_uzemni_celek)
    data_list = data_to_list(soup)

    with open(nazev_souboru, "w", newline="") as file:
        zahlavi= data_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=zahlavi)
        writer.writeheader()
        writer.writerows(data_list)

    print("""
    Hotovo! Data jsou uložena v souboru
    """)
    print(separator3)


# Vložení URL a kontrola pomocí if
def zadani_url_uzemni_celek():
    url_uzemni_celek = input("Vlož odkaz zvoleného územního celku: ")
    if "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" in url_uzemni_celek and "&xnumnuts=" in url_uzemni_celek:
        return url_uzemni_celek
    else:
        print("Vložil si špatný odkaz. Vlož ho znovu.")
        quit()


# Pojmenování souboru pro uložení dat a kontrola pomocí if
def zadani_nazvu_souboru():
    nazev_souboru = input("Nyní napiš název souboru pro uložení dat: ")
    if ".csv" not in nazev_souboru:
        nazev_souboru += ".csv"
        print(separator1)
        print("Probíhá exportování")
        print(separator3)
    return nazev_souboru


# Vytažení dat z Beautifulsoup objektu
def ziskat_data(url_uzemni_celek):
    r = requests.get(url_uzemni_celek)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def data_zahlavi(tr):
    tds = tr.find_all("td")
    id = tds[0].getText()
    obec = tds[1].getText()
    url2 = tds[0].find("a").get("href")
    return id, obec, url2


def data_do_csv_tabulky(zahlavi_udaje):
    id, obec, url2 = zahlavi_udaje
    url1 = "https://volby.cz/pls/ps2017nss/" + url2
    soup = ziskat_data(url1)
    tabulky = soup.find_all("table")
    bunky = tabulky[0].find_all("td")
    csv_tabulka = {"Kód obce": id, "Název obce": obec, "Voliči": bunky[3].getText(), "Obalky": bunky[6].getText(), "Platné hlasy": bunky[7].getText()}

    for tabulka in tabulky[1:]:
        trs = tabulka.find_all("tr")
        for tr in trs[2:-1]:
            tds = tr.find_all("td")
            jmena_stran = tds[1].getText()
            volici_celkem = tds[2].getText()
            csv_tabulka[jmena_stran] = volici_celkem
    return csv_tabulka


def data_to_list(soup):
    volici2 = soup.find_all("div", {"class": "t3"})
    data_list = []
    for tabulka in volici2:
        radky = tabulka.find_all("tr")
        for row in radky[2:]:
            data_list.append(data_do_csv_tabulky(data_zahlavi(row)))
        return data_list


main()
