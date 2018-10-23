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
    list1 = CircularPositionalList()                                        # creazione della lista
    if list1.Is_empty() == True:                                            # verifica che la lista sia vuota
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
    print("(3) Stampa della lista ")
    list1.printList()
    print("\n(3) Rimpiazzo l' elemento 2 con l' elemento 78\n")

    
    old = list1.replace(b, 78)                                              # verifica del metodo replace
    print("(3) La nuova lista è ")
    list1.printList()
    print("\n(3) L'elemento rimpiazzato è : ", old)
    print("\n(3) Cancellazione dell'elemento 78")
    print("(3) L' elemento cancellato è", list1.delete(b), "La nuova lista è :")
    list1.printList()

    #copia della lista
    try:
        list2 = list1.copy()
    except BaseException:
        print("ERRORE LISTA")
    print("\n(4) La copia della lista è:")
    list2.printList()

    #verifica che entrambe le liste non siano vuote
    print('\n(5) La lista 1 è vuota?', list1.is_empty())
    print('(5) La lista 2 è vuota?', list2.is_empty())

    #verifica del metodo count
    print("\n(6) Prova di count sulla lista 1, cerchiamo l'elemento 4")
    try:
        print("L'elemento 4 ha ",list1.count(4), "occorrenze nella lista" )
    except BaseException:
        print("ERRORE LISTA")
    print("\n(6) Prova di count sulla lista 2, cerchiamo l'elemento 4")
    try:
        print("L'elemento 4 ha ",list2.count(4), "occorrenze nella lista")
    except BaseException:
        print("ERRORE LISTA")

    #verifica dei metodi first,last,before,count,find e after su entrambe le liste
    print('\n(6) Il primo elemento della lista 1 è:', list1.first().element())
    print('(6) Il primo elemento della lista 2 è:', list2.first().element())

    print("\n(6) L' elemento successivo al primo della lista 1 è :",
        list1.after(list1.first()))
    print("(6) L' elemento successivo al primo della lista 2 è :",
        list2.after(list2.first()))

    print("\n(6) L' ultimo elemento della lista 1 è:", list1.last().element())
    print("(6) L' ultimo elemento della lista 2 è:", list2.last().element())

    print("\n(6) L elemento precedente all ultimo della lista 1 è :",
        list1.before(list1.last()))
    print("(6) L elemento precedente all ultimo della lista 2 è :",
        list2.before(list2.last()))

    #testing della find
    try:
        print("\n(6) Cerco l' elemento 4 e la find mi restituisce la position il cui elemento è:", list1.find(4).element() )
    except BaseException:
        print("ERRORE LISTA")

    #verifica della funzione reverse su entrambe le liste
    print("\n(7) Stampa della lista 1 prima dell' inversione:")
    list1.printList()
    print("\n(7) Stampa della lista 1 dopo l' inversione:")
    try:
        list1.reverse()
    except BaseException:
        print("ERORRE LISTA")
    list1.printList()

    #operazione identica sulla lista 2
    print("\n(7) Stampa della lista 2 prima dell' inversione:")
    list2.printList()
    print("\n(7) Stampa della lista 2 dopo l' inversione:")
    try:
        list2.reverse()
    except BaseException:
        print("ERRORE LISTA")
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


    # ordinamento delle 2 liste
    # creazione di due liste in cui salvare gli elementi ordinati
    sorted1 = CircularPositionalList()
    sorted2 = CircularPositionalList()

    print('(9) Ordinamento della lista 1 tramite bubble')
    iter_a = list1.bubblesorted()  # iteratore per lista1

    # for di ordinamento
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
    print('(10) sorted1:')
    sorted1.printList()

    print('\n(10) sorted2:')
    sorted2.printList()


    print('\n(11) applico la merge alle 2 liste ordinate e ottengo:')
    mergea = merge(sorted1, sorted2)
    mergea.printList()

    print('\n(11) Creo una terza lista: ')
    third = CircularPositionalList()
    third.add_first(465)
    third.add_first(48)
    third.add_first(13)
    third.add_first(12)
    third.add_first(1)
    third.printList()
    print("\n(11) applico la merge con il risultato della merge precedente:")
    merge(third,mergea).printList()


    #test degli operatori
    print("\n(12) Verifica dell'operatore add")
    new = list1 + list2
    new.printList()

    print("\n(12) Verifica dell'operatore contain")
    print('(12) Salvo il riferimento all elemento 3 e lo cancello')
    try:
        save = list1.find(3)                                       # salvo la position dell'elemento 3
    except BaseException:
        print("ERRORE LISTA")
    list1.delete(save)                                             # cancello la position di 3
    print('(12) L elemento 3 è contenuto nella lista ? ',
        save.element() in list1)                                   # controllo se 3 è contenuto
    try:    
        print('(12) L elemento 5 è contenuto nella lista ? ', list1.find(
        5).element() in list1)                                     # controllo se 5 è contenuto
    except BaseException:
        print("ERRORE LISTA")

    print("\n(12) Verifica dell'operatore get_item")
    print("(12) Get first element:", list1[list1.first()])

    print("\n(12) Verifica dell'operatore len")
    print('(12) La dimensione è:', len(list1))
    print("\n")
    list1.printList()

    print("\n(12) Verifica dell'operatore set_item impostando 100 come primo valore")
    list1[list1.first()] = 100
    list1.printList()
    print("\nVerifica di set_item impostando l'elemento di una position cancellata in precedenza dalla lista")
    list1[save] = 99                                                # prova di set_item in caso venga inserita una position non valida    

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
    
    #creazione dello scoreboard e di 11 score            
    s=ScoreBoard()
    score1 = s.Score("Michele",250,"1995")
    score2 = s.Score("Vittorio",251,"1990")
    score3 = s.Score("Wael",300,"1969")
    score4 = s.Score("Vincenzo",500,"1956")
    score5 = s.Score("Alessandro",10,"1999")
    score6 = s.Score("Alessio",3,"99")
    score7 = s.Score("Giovanni",10,"1499")
    score8 = s.Score("Lorenzo",40,"1399")
    score9 = s.Score("Angelo",30000,"1299")
    score10 = s.Score("Gennaro",1,"1199")
    score11 = s.Score("Giulio",3,"1090")

    #inserimento degli scores nello scoreboard
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
    try:
        for e in s.top(5):
            print("Elemento", i, ":", e.name(), '-', e.value())
            i+=1
    except TypeError:
        print("Indice non valido")   

    print("\n(14) Stampo i 5 peggiori risultati:")
    h = 0
    try:
        for e in s.last(5):
            print("Elemento", h, ":", e.name(), '-', e.value())
            h += 1
    except TypeError:
            print("Indice non valido")        
                    
        


    print('\n(15) Creo un nuovo scoreboard con gli stessi valori del primo al solo scopo di testare la merge:')

    s2 = ScoreBoard()
    score1 = s2.Score("Michele",250,"1995")
    score2 = s2.Score("Vittorio",251,"1990")
    score3 = s2.Score("Wael",300,"1969")
    score4 = s2.Score("Vincenzo",500,"1956")
    score5 = s2.Score("Alessandro",10,"1999")
    score6 = s2.Score("Roberta",3,"99")
    score7 = s2.Score("Roberto",10,"1499")
    score8 = s2.Score("Susanna",40,"1399")
    score9 = s2.Score("Angelo",30000,"1299")
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

    
    try:
        s.merge(s2) 
    except TypeError:
        print("Parametro passato al metodo scorretto")
    
    print('\n(15) Stampa dello scoreboard dopo la merge:')
    i = 0
    for e in s.top(10):
        print("Elemento", i, ":",e.name(),'-',e.value())
        i += 1

    print("\n(16) Cancelliamo tutte le liste utilizzate")  #list1,sorted1,sorted2,third
    list1.clear()
    sorted1.clear()
    sorted2.clear()
    third.clear()
    print('(16) Stampa della liste vuote: ')
    list1.printList()
    sorted1.printList()
    sorted2.printList()
    third.printList()


# DESCRIZIONE: prende due liste ordinate e le fonde in una nuova lista ordinata contentente gli elementi di entrambe
def merge(list1, list2): 
    if not isinstance(list1, CircularPositionalList):
            raise TypeError(
                "L'oggetto passato non è istanza della classe corretta")
    if not isinstance(list2, CircularPositionalList):
            raise TypeError(
                "L'oggetto passato non è istanza della classe corretta")

    third = CircularPositionalList()
    p1 = list1.first()
    p2 = list2.first()
    j1 = len(list1)
    j2 = len(list2)

    while True:                                        # confronta gli elementi delle due liste e li inserisce nella nuova lista
        if p1.element() <= p2.element():    
            third.add_last(p1.element())
            p1 = list1.get_next_Position(p1)
            j1-=1
        if p1.element() >= p2.element():
            third.add_last(p2.element())
            p2 = list2.get_next_Position(p2)
            j2-=1
        if j1 == 0 or j2 == 0:
            break

    # nel caso in cui rimangono degli elementi non inseriti in una delle due liste, essi vengono aggiunti in coda alla nuova lista
    
    if j1 == 0:                                       
        while j2 != 0:
            third.add_last(p2.element())
            p2 = list2.get_next_Position(p2)
            j2-=1
    if j2 == 0:
        while j1 != 0:
            third.add_last(p1.element())
            p1 = list1.get_next_Position(p1)
            j1-=1
    return third    



if __name__ == "__main__":
    main()
    input("Press ENTER to continue...")
