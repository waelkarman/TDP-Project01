from circularPositionalList import CircularPositionalList
from scoreBoard import ScoreBoard

# ___________                      ____ ________
# \__    ___/___ _____    _____   /_   /   __   \
#   |    |_/ __ \\__  \  /     \   |   \____    /
#   |    |\  ___/ / __ \|  Y Y  \  |   |  /    /
#   |____| \___  >____  /__|_|  /  |___| /____/
#              \/     \/      \/


def main():
    print('INIZIO DEL TESTING : CIRCULAR POSITIONAL LIST \n')
    print('(1) Creo la lista')
    list1 = CircularPositionalList()  # creazione della lista
    if list1.Is_empty() == True:  # verifica che la lista sia vuota
        print("(2) La lista è vuota")
    else:
        print("(2) La lista non è vuota")


    #inserimento degli elementi nella lista
    print("(3) Inserisco elementi all' interno della lista")
    list1.add_first(4)
    a = list1.add_first(5)
    b = list1.add_last(2)
    list1.add_last(3)
    list1.add_before(a, 25)
    list1.add_after(b, 15)
    print("(3) Stampa della lista \n")
    list1.printList()
    print("(3) Rimpiazzo l' elemento 2 con l' elemento 78\n")

    #verifica funzioni replace e delete
    old = list1.replace(b, 78)
    print("(3) La nuova lista è \n")
    list1.printList()
    print("(3) L'elemento rimpiazzato è : ", old)
    print("\n(3) Cancellazione dell'elemento 78")
    print("(3) L' elemento cancellato è", list1.delete(b), "La nuova lista è :")
    list1.printList()

    #copia della lista
    list2 = list1.copy()
    print("\n(4) La copia della lista è:")
    list2.printList()

    #verifica che entrambe le liste non siano vuote
    print('(5) La lista 1 è vuota?', list1.is_empty())
    print('(5) La lista 2 è vuota?', list2.is_empty())

    #verifica dell metodo count
    print("\n(6) Prova di count sulla lista 1, cerchiamo l'elemento 4")
    try:
    print(list1.count(4))
    except
    print("\n(6) Prova di count sulla lista 2, cerchiamo l'elemento 4")
    print(list2.count(4))

    #verifica dei metodi first,last,before,count,find e after su entrambe le liste
    print('(6) Il primo elemento della lista 1 è:', list1.first().element())
    print('(6) Il primo elemento della lista 2 è:', list2.first().element())

    print("(6) L' elemento successivo al primo della lista 1 è :",
        list1.after(list1.first()))
    print("(6) L' elemento successivo al primo della lista 2 è :",
        list2.after(list2.first()))

    print("(6) L' ultimo elemento della lista 1 è:", list1.last().element())
    print("(6) L' ultimo elemento della lista 2 è:", list2.last().element())

    print("(6) L elemento precedente all ultimo della lista 1 è :",
        list1.before(list1.last()))
    print("(6) L elemento precedente all ultimo della lista 2 è :",
        list2.before(list2.last()))

    #testing della find
    try:
        print("(6) Cerco l' elemento 4 e la find mi restituisce la position il cui elemento è:", list1.find(4).element() )
    except BaseException:
        print("ERRORE LISTA")
    #verifica della funzione reverse su entrambe le liste
    print("\n(7) Stampa della lista 1 prima dell' inversione:\n")
    list1.printList()
    print("(7) Stampa della lista 1 dopo l' inversione:")
    list1.reverse()
    list1.printList()

    #operazione identica sulla lista 2
    print("\n(7) Stampa della lista 2 prima dell' inversione:")
    list2.printList()
    print("\n(7) Stampa della lista 2 dopo l' inversione:")
    list2.reverse()
    list2.printList()

    #verifica dell'ordinamento delle liste
    try:
        print('\n(8) La prima lista è ordinata?', list1.Is_sorted())
    except BaseException:
        print("ERRROE NELLA LISTA")
    try:
        print('(8) La seconda lista è ordinata?', list2.Is_sorted())
    except BaseException:
        print("ERRORE NELLA LISTA")
    print("\n")


    #ordinamento delle 2 liste
    # creazione di due liste in cui salvare gli elementi ordinati
    sorted1 = CircularPositionalList()
    sorted2 = CircularPositionalList()

    print('(9) Ordinamento della lista 1 tramite bubble')
    iter_a = list1.bubblesorted()  # iteratore per lista1

    #for di ordinamento
    i = 0
    for e in iter_a:
        print("Elemento", i, ":", e)
        sorted1.add_last(e)
        i += 1

    print('(9) Ordinamento della lista 2 tramite bubble')
    iter_b = list2.bubblesorted()  # iteratore per lista2

    i = 0
    for e in iter_b:
        print("Elemento", i, ":", e)
        sorted2.add_last(e)
        i += 1

    print('\n(10) Creo due liste ordinate ricavate dalle 2 di partenza:')
    print('\n(10) sorted1:')
    sorted1.printList()

    print('\n(10) sorted2:')
    sorted2.printList()


    print('(11) applico la merge alle 2 liste ordinate e ottengo:')


 
    merge(sorted1, sorted2).printList()


    #test degli operatori
    print("\n(12) Verifica dell'operatore add")
    new = list1 + list2
    new.printList()

    print("\n(12) Verifica dell'operatore contain")
    print('(12) Salvo il riferimento all elemento 3 e lo cancello')
    try:
        save = list1.find(3)  # salvo la position dell'elemento 3
    except BaseException:
        print("ERRORE LISTA")
    list1.delete(save)  # cancello la position di 3
    print('(12) L elemento 3 è contenuto nella lista ? ',
        save.element() in list1)  # controllo se 3 è contenuto
    try:    
        print('(12) L elemento 5 è contenuto nella lista ? ', list1.find(
        5).element() in list1)  # controllo se 5 è contenuto
    except BaseException:
        print("ERRORE LISTA")

    print("\n(12) Verifica dell'operatore get_item")
    print("(12) Get first element:", list1[list1.first()])

    print("\n(12) Verifica dell'operatore len")
    print('(12) La dimensione è:', len(list1))
    print("\n")
    list1.printList()

    print("\nV(12) erifica dell'operatore set_item impostando 100 come primo valore")
    list1[list1.first()] = 100
    list1.printList()
    list1[save] = 99  # prova di set_item in caso venga inserita una position non valida    DA DECOMMENTARE PER IL TESTING

    print("\n(12) Verifica dell'operatore delete_item")
    print("(12) Cancellazione del primo elemento della lista")
    del list1[list1.first()]
    list1.printList()

    print("\n(12) Verifica dell'operatore __str__")
    list1.__str__()


    #---------------------------------------------------------------(')>
    #--------------------------------->> TESTING SCOREBOARD <<------(_)
    #---------------------------------------------------------------""

    print("\n\nINIZIO DEL TESTING : SCOREBOARD")
    print("(13) Creo lo score Board e lo riempio con valori casuali :")
    s=ScoreBoard()
    score1 = s.Score("Michele",250,"1995")
    score2 = s.Score("Vittorio",251,"1990")
    score3 = s.Score("Wael",300,"1969")
    score4 = s.Score("Vincenzo",500,"1956")
    score5 = s.Score("Alessandro",10,"1999")
    score6 = s.Score("Auletta",3,"99")
    score7 = s.Score("Diodato",10,"1499")
    score8 = s.Score("Foggia",40,"1399")
    score9 = s.Score("Marcelli",30000,"1299")
    score10 = s.Score("Gennaro",1,"1199")
    score11 = s.Score("Giulio",3,"1090")

    s.insert(score1)
    s.insert(score2)
    s.insert(score3)
    s.insert(score4)
    s.insert(score5)
    s.insert(score6)
    s.insert(score7)
    s.insert(score8)
    s.insert(score9)
    s.insert(score10)
    s.insert(score11)

    print("\n(14) Stampo i 5 migliori risultati:")
    i=0
    for e in s.top(5):
        print("Elemento", i, ":", e.value())
        i+=1

    print("\n(14) Stampo i 5 peggiori risultati:")
    h = 0
    for e in s.last(5):
        print("Elemento", h, ":", e.value())
        h += 1



    print('\n(15) Creo un nuovo scoreboard uguale al primo al solo scopo di testare la merge:')

    s2 = ScoreBoard()
    score1 = s2.Score("Michele",250,"1995")
    score2 = s2.Score("Vittorio",251,"1990")
    score3 = s2.Score("Wael",300,"1969")
    score4 = s2.Score("Vincenzo",500,"1956")
    score5 = s2.Score("Alessandro",10,"1999")
    score6 = s2.Score("Auletta",3,"99")
    score7 = s2.Score("Diodato",10,"1499")
    score8 = s2.Score("Foggia",40,"1399")
    score9 = s2.Score("Marcelli",30000,"1299")
    score10 = s2.Score("Gennaro",1,"1199")
    score11 = s2.Score("Giulio",3,"1090")

    s2.insert(score1)
    s2.insert(score2)
    s2.insert(score3)
    s2.insert(score4)
    s2.insert(score5)
    s2.insert(score6)
    s2.insert(score7)
    s2.insert(score8)
    s2.insert(score9)
    s2.insert(score10)
    s2.insert(score11)

    s.merge(s2) 

    print('\n(15) Stampa della lista dopo la merge:')
    i = 0
    for e in s.top(10):
        print("Elemento", i, ":", e.value())
        i += 1



def merge(list1, list2):
    if not isinstance(list1, CircularPositionalList):
            raise TypeError(
                "L'ogg passato non è istanza della classe corretta")
    if not isinstance(list2, CircularPositionalList):
            raise TypeError(
                "L'ogg passato non è istanza della classe corretta")

    l1c = list1.copy()
    iter2 = iter(list2)
    temp = l1c.first()
    while True:
        try:
            val = next(iter2)
        except StopIteration:
            break
        while val >= temp.element():
            temp = l1c._get_next_Position(temp)
            if temp == l1c.first():
                break
        l1c.add_before(temp, val)
    return l1c



if __name__ == "__main__":
    main()
