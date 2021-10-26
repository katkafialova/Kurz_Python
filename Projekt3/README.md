# Popis projektu
Třetí projekt do kurzu Python Akademie, který získává z webových stránek výsledky parlamentních voleb.

# Knihovny
V souboru `Reguirements.txt` najdete využité knihovny.

Pro instalaci použijte příkaz:

pip install `-r requirements.txt`

# Spuštění projektu
---
Spuštění souboru ```election scraper.py``` v rámci příkazového řádku požaduje 2 povinné argumenty.

```python
python election_scraper <odkaz-uzemniho-celku> <vysledny-soubor>
```

Následně se vám stáhnou výsledky jako soubor s příponou ```.csv```.

# Ukázka
```
--------------------------------------------------------------------------------
==============================Election scraper app==============================
--------------------------------------------------------------------------------
Stahuji data z url:  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
Stahuji data do souboru:  Benesov.csv
--------------------------------------------------------------------------------
Hotovo! Data jsou uložena v souboru Benesov.csv
================================================================================
```

