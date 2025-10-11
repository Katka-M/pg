#poznámky si dělám pro sebe pro budoucí učení :)

def cislo_text(cislo):
    # tohle mi zařídí, že k celým číslům dostanu slovní popis čísla
    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }
    
    teen = {
        11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }
    # slovník, aby počítač věděl, jak se jednotlivá čísl jemnují
    desitky_plne = {
        10: "deset", 20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát", 60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát"
    }

    if 0 <= cislo < 10:
        return jednotky[cislo]
    
    # === TOTO JE ORAVA ===
    # Přidáme podmínku speciálně pro číslo 10
    if cislo == 10:
        return desitky_plne[cislo]
    # ======================
    
    if 10 < cislo < 20:
        return teen[cislo]

    if cislo == 100:
        return "sto"
    
    if 20 <= cislo < 100:
        desitka_hodnota = (cislo // 10) * 10
        jednotka_hodnota = cislo % 10
        
        if jednotka_hodnota == 0:
            return desitky_plne[desitka_hodnota]
        else:
            return f"{desitky_plne[desitka_hodnota]} {jednotky[jednotka_hodnota]}"

    # Tato zpráva se nyní zobrazí jen pro čísla větší než 100 nebo menší než 0
    return "Číslo musí být celé a mezi 0 a 100"

zadany_text = input("Zadej celé číslo od 0 do 100: ")
#zeptám se uživatele, aby zadal nějaké číslo 0-100

zadane_cislo = int(zadany_text)
#převede se zadaný "input" na celé číslo

slovni_nazev = cislo_text(zadane_cislo)
#zavolám si funkci se zadaným číslem

print(f"{zadane_cislo} = {slovni_nazev}")
#vyhodí se mi slovní jméno čísla