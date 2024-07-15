import bank_danych_lokalnych

if __name__ == '__main__':

    #1. Lista tematów głównych z katalogu
    temat = bank_danych_lokalnych.BankDanychLokalnych.tematy()
    print(temat[0])

    #2. Lista subtematów
    loop = temat[1]
    while loop!="False":
        s = input('Podaj wybrany temat i pobierz sub-tematy: ')
        subtemat = bank_danych_lokalnych.BankDanychLokalnych.subtematy(s)
        print(subtemat[0])
        if subtemat[1]=="False":
            break
        else:
            loop=subtemat[1]

    #3. Lista zmiennych dla subtematu
    #z = input('Podaj wybrany sub-temat i pobierz dla niego zmienne: ')
    #zmienne = bdl_api.BankDanychLokalnych.zmienne(z)
    #print(zmienne)

    #4. Pobierz wszytskie dane dla jednoski: Polska
    #d = input('Podaj zmienną aby pobrać dane dla podstawowej agregacji: ')
    #dane = bdl_api.BankDanychLokalnych.dane(d)
    #print(dane)