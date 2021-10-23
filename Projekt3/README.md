# Popis projektu
Třetí projekt do kurzu Python Akademie, který získává z webových stránek výsledky parlamentních voleb.

# Knihovny
V souboru `Reguirements.txt` najdete využité knihovny.

Pro instalaci použijte příkaz:

pip install `-r requirements.txt`

# Spuštění projektu
Výsledný soubor `Elections Scraper app.py` budete spouštět pomocí 2 argumentů:
* První argument obsahuje odkaz, který územní celek chcete scrapovat
* Druhý argument obsahuje jméno výstupního souboru

# Ukázka
```
--------------------------------------------------------------------------------
==============================Election scraper app==============================
--------------------------------------------------------------------------------

    1)Otevři následující odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
    2)Vyber si územní celek kliknutím na "X"
    
--------------------------------------------------------------------------------
Vlož odkaz zvoleného územního celku: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
--------------------------------------------------------------------------------
Nyní napiš název souboru pro uložení dat: Benesov
--------------------------------------------------------------------------------
Probíhá exportování
================================================================================

    Hotovo! Data jsou uložena v souboru
    
================================================================================
```

