# Kateřina Fialová - 3.projekt

# Knihovny
import requests
from bs4 import BeautifulSoup
import csv
import sys


# Oddělovače
separator1 = "-" * 80
separator2 = "=" * 30
separator3 = "=" * 80


def name():
    print(separator1)
    print(separator2 + "Election scraper app" + separator2)
    print(separator1)

    if len(sys.argv) < 2:
        print("Nezadali jste url")
        quit()
    url_uzemni_celek = sys.argv[1]
    if "https://volby.cz/pls/ps2017nss/ps32" not in url_uzemni_celek:
        print("Špatný zadaný odkaz")
        quit()
    if len(sys.argv) < 3:
        print("Zadejte název csv souboru")
        quit()
    nazev_souboru = sys.argv[2]

    print("Stahuji data z url: ", url_uzemni_celek)
    print("Stahuji data do souboru: ", nazev_souboru)
    print(separator1)

    soup = ziskat_data(url_uzemni_celek)
    data_list = data_to_list(soup)

    with open(nazev_souboru, "w", newline="") as file:
        zahlavi = data_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=zahlavi)
        writer.writeheader()
        writer.writerows(data_list)

    print("Hotovo! Data jsou uložena v souboru", nazev_souboru)
    print(separator3)


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


name()
