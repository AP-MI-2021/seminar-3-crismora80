def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def nrIntregiLista(l):
    '''
    determina nr. intregi dintr-o lista
    :param l: lista de float-uri
    :return: nr. intregi din l
    '''
    rezultat = []
    for x in l:
        #if x == int(x):
        #if x % 1 == 0:
        if x.is_integer():
            rezultat.append(x)
    return rezultat

def testNrIntregiLista():
    assert nrIntregiLista([4.5, 2.3]) == []
    assert nrIntregiLista([1.0, 9.8, 7.0]) == [1.0, 7.0]

def celMaiMareNrDivCu(l, k):
    '''
    determina cel mai mare nr. dintr-o lista divizibil cu un nr. dat
    :param l: lista de float-uri
    :param k: nr. intreg
    :return: cel mai mare nr. din l divizibil cu un nr. dat sau None, daca nu exista
    '''

    ''' modul 1
    max = None
    for x in l:
        if x % k == 0 and (max is None or x > max):
            max = x
    return max
    '''

    ''' modul 2
    max = None
    nrDiv = []
    for x in l:
        if x % k == 0:
            nrDiv.append(x)
    for x in nrDiv:
        if max is None or x > max:
            max = x
    return max
    '''
    nrOdonateDesc = l[:]
    nrOdonateDesc.sort(reverse=True)
    for x in nrOdonateDesc:
        if x % k == 0:
            return x

def testCelMaiMareNrDivCu():
    assert celMaiMareNrDivCu([4.5, 6.0, 7.0], 4) is None
    assert celMaiMareNrDivCu([6.0, 8.0, 9.9], 3) == 6.0
    assert celMaiMareNrDivCu([8.0, 4.5, 10.0, 5.41, 2.3, 6.0], 2) == 10.0

def pfPalindrom(l):
    '''
    determina nr. dintr-o lista ale caror parte fractionara e palindrom
    :param l: lista de float-uri
    :return: determina nr. din l ale caror parte fractionara e palindrom
    '''
    rezultat = []
    for x in l:
        xStr = str(x)
        pf = xStr.split(".")[1]
        # pf[::-1] este pf inversat (ex.: "123" => "321")
        if pf == pf[::-1]:
            rezultat.append(x)
    return rezultat

def testPfPalindrom():
    assert pfPalindrom([2.211, 3.45]) == []
    assert pfPalindrom([5.0, 6.45, 3.1, 2.343]) == [5.0, 3.1, 2.343]

def procesareLista(l):
    '''
    determina nr. din lista în care float-urile
        cu partea întreagă a radicalului număr prim
        sunt puse ca string-uri cu caracterele în ordine inversă
    :param l: lista de float-uri pozitive
    :return: nr. din l în care float-urile
        cu partea întreagă a radicalului număr prim
        sunt puse ca string-uri cu caracterele în ordine inversă
    '''
    rezultat = []
    for x in l:
        radical = x**0.5
        pi = int(radical)
        ok = True
        if pi < 2:
            ok = False
        else:
            for i in range(2, pi//2 + 1):
                if pi % i == 0:
                    ok = False
        if ok:
            rezultat.append(str(x)[::-1])
        else:
            rezultat.append(x)
    return rezultat

def testProcesareLista():
    assert procesareLista([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]

def nrPozImpareDesc(l):
    '''

    :param l:
    :return:
    '''

    ''' modul 1a
    for i in range(1, len(l) - 2, 2):
        if l[i] < l[i+2]:
            return False
    return True
    '''

    ''' modul 1b
    for i in range(3, len(l), 2):
        if l[i-2] < l[i]:
            return False
    return True
    '''

    ''' modul 3
    elemPozImpare = []
    for i in range(1, len(l), 2):
        elemPozImpare.append(l[i])
    for i in range(1, len(elemPozImpare)):
        if elemPozImpare[i-1] < elemPozImpare[i]:
            return False
    return True
    '''

    ''' modul 4
    elemPozImpare = l[1::2]
    elemPozImpareSortate = elemPozImpare[:]
    elemPozImpareSortate.sort(reverse=True)
    for i in range(len(elemPozImpare)):
        if elemPozImpare[i] != elemPozImpareSortate[i]:
            return False
    return True
    '''

    nrPozImpare = l[1::2]
    for i in range(len(nrPozImpare) - 1):
        if nrPozImpare[i] < nrPozImpare[i+1]:
            return False
    return True

def testNrPozImpareDesc():
    assert nrPozImpareDesc([4.0, 5.0, 6.0, 3.0]) is True
    assert nrPozImpareDesc([4.0, 5.0, 6.0, 7.0]) is False
    assert nrPozImpareDesc([4.0, 5.0, 6.0, 3.0, 10.0]) is True
    assert nrPozImpareDesc([4.0, 5.0, 6.0, 3.0, 10.0, 1.0]) is True
    assert nrPozImpareDesc([4.0, 5.0, 6.0, 3.0, 10.0, 11.0]) is False

def inserareNrCifre(l):
    '''

    :return:
    '''
    rezultat = []
    for x in l:
        rezultat.append(x)
        nrCifre = len(str(x)) - 1
        '''
        optional, in functie de interpretarea problemei (in cazul in care se doreste sa se considere ca
        numerelor intregi nu li se numara si cifra 0 de dupa virgula ex. 1.0 are o singura cifra)
        if x == int(x):
            nrCifre-=1
        '''
        rezultat.append(nrCifre)
    return rezultat

def testInserareNrCifre():
    ''' test valabil pentru cazul optional de la linia 178
    assert inserareNrCifre([1.0, 12.34]) == [1.0, 1, 12.34, 4]
    '''
    assert inserareNrCifre([1.0, 12.34]) == [1.0, 2, 12.34, 4]

def listaEsteConstanta(l):
    '''

    :param l:
    :return:
    '''

    ''' modul 1
    if l == []:
        return False
    for i in range(1, len(l)):
        if l[i-1] != l[i]:
            return False
    return True
    '''

    if l == []:
        return False
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            return False
    return True

def testListaEsteConstanta():
    assert listaEsteConstanta([1.0]) is True
    assert listaEsteConstanta([3.0, 3.0]) is True
    assert listaEsteConstanta([2.0, 4.0]) is False
    assert listaEsteConstanta([]) is False

def main():
    testNrIntregiLista()
    testCelMaiMareNrDivCu()
    testPfPalindrom()
    testProcesareLista()
    testNrPozImpareDesc()
    testInserareNrCifre()
    testListaEsteConstanta()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afisare nr. intregi din lista")
        print("3. Afisare cel mai mare nr. cu un numar citit")
        print("4. Afisare nr. ale caror parte fractionara este palindrom")
        print("5. Afisare nr. din lista în care float-urile"
              " cu partea întreagă a radicalului număr prim "
              "sunt puse ca string-uri cu caracterele în ordine inversă")
        print("------------------------")
        print("6. Sa se determine daca nr. de pe pozitii impare sunt descrescatoare")
        print("7. Sa se determine lista formata daca dupa fiecare nr. se insereaza nr. sau de cifre")
        print("8. Sa se determine daca lista este constanta")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(nrIntregiLista(l))
        elif optiune == "3":
            k = int(input("Dati un nr.: "))
            max = celMaiMareNrDivCu(l, k)
            if max is None:
                print("Nu exista")
            else:
                print(max)
        elif optiune == "4":
            print(pfPalindrom(l))
        elif optiune == "5":
            print(procesareLista(l))
        # ---------------------
        elif optiune == "6":
            if nrPozImpareDesc(l):
                print("DA")
            else:
                print("NU")
        elif optiune == "7":
            print(inserareNrCifre(l))
        elif optiune == "8":
            if listaEsteConstanta(l):
                print("DA")
            else:
                print("NU")
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()