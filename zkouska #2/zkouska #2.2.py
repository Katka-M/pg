def vrat_treti(seznam): 
    #má seznam 3 prvky?
    if len(seznam) >= 3: #len(seznam) počet prvků v seznamu  
        return seznam[2]
    else:
        return None


def prumer(cisla):
    return sum(cisla) / len(cisla)


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
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,1,3,1,2,1]
    }
    student["vek"] += 1
    print(student["znamky"][4]) #když chceme jenom prijmeni --> print(student["prijmeni"])
# když chci 5 známku v pořadí --> print(student["znamky"][4])