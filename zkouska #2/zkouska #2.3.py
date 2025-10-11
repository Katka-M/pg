
def prumer(cisla): # mohla bych napsat --> 
    return sum(cisla) / len(cisla)

def naformatuj_text(student):
    jmeno = student["jmeno"]
    prijmeni = student["prijmeni"]
    vek = student["vek"]

    prumer_znamek = prumer(student["znamky"])
    prumer_znamek = round(prumer_znamek, 2) #(prumer_znamek, 2) --> 2 je počet desetiných míst

    return f"Student: {jmeno} {prijmeni}, Vek: {vek}, Prumer znamek: {prumer_znamek}"



if __name__ == "__main__":

    seznam = [12, 50, 1, 3, 5]
#vyzvednutí prvku na 4 místě...tedy po 3 místě --> print(seznam[3])
   
    seznam[3] *= 3

    seznam.append(100) #na konci seznamu přidáme hodnotu 100

    seznam.sort() #od nejmenšího po největší
    seznam.reverse()  #obrátit pořadí

    seznam2 = [1,2,3]
    print(prumer(seznam))

    student = {
        "jmeno": "Tomas",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,1,3,1,2,1]
    }
    student["vek"] += 1
    print(naformatuj_text(student))