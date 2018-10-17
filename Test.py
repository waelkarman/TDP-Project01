from circularPositionalList import CircularPositionList
from scoreBoard import ScoreBoard

# ___________                      ____ ________
# \__    ___/___ _____    _____   /_   /   __   \
#   |    |_/ __ \\__  \  /     \   |   \____    /
#   |    |\  ___/ / __ \|  Y Y  \  |   |  /    /
#   |____| \___  >____  /__|_|  /  |___| /____/
#              \/     \/      \/


print('INIZIO DEL TESTING.. \n')
list1 = CircularPositionList()  # creazione della lista
if list1.Is_empty() == True:  # verifica che la lista sia vuota
    print("La lista è vuota")
else:
    print("La lista non è vuota")


#inserimento degli elementi nella lista
list1.add_first(4)
a = list1.add_first(5)
b = list1.add_last(2)
list1.add_last(3)
list1.add_before(a, 25)
list1.add_after(b, 15)
print("Stampa della lista \n")
list1.printList()
print("Rimpiazzo dell'elemento 2 con l'elemento 78\n")

#verifica funzioni replace e delete
old = list1.replace(b, 78)
print("La nuova lista è \n")
list1.printList()
print("L'elemento rimpiazzato è : ", old)
print("\nCancellazione dell'elemento 78")
print('L elemento cancellato è', list1.delete(b), "La nuova lista è :")
list1.printList()


print("\nProva di count, cerchiamo l'elemento 4")
print(list1.count(4))

#copia della lista
list2 = list1.copy()
print("\nLa copia della lista è:")
list2.printList()

#verifica che entrambe le liste non siano vuote
print('La lista 1 è vuota?', list1.is_empty())
print('La lista 2 è vuota?', list2.is_empty())

#verifica dei metodi first,last,before,count,find e after su entrambe le liste
print('Il primo elemento della lista 1 è:', list1.first().element())
print('Il primo elemento della lista 2 è:', list2.first().element())

print('L elemento successivo al primo della lista 1 è :',
      list1.after(list1.first()))
print('L elemento successivo al primo della lista 2 è :',
      list2.after(list2.first()))

print('L ultimo elemento della lista 1 è:', list1.last().element())
print('L ultimo elemento della lista 2 è:', list2.last().element())

print('L elemento precedente all ultimo della lista 1 è :',
      list1.before(list1.last()))
print('L elemento precedente all ultimo della lista 2 è :',
      list2.before(list2.last()))

#verifica della funzione reverse su entrambe le liste
print("\nStampa della lista 1 prima dell' inversione:\n")
list1.printList()
print("Stampa della lista 1 dopo l' inversione:")
list1.reverse()
list1.printList()

#operazione identica sulla lista 2
print("\nStampa della lista 2 prima dell' inversione:")
list2.printList()
print("\nStampa della lista 2 dopo l' inversione:")
list2.reverse()
list2.printList()

#reverse a scopo di testing
list1.reverse()
list2.reverse()

#verifica dell'ordinamento delle liste
print('\nLa prima lista è ordinata?', list1.Is_sorted())
print('La seconda lista è ordinata?', list2.Is_sorted())
print("\n")


#ordinamento delle 2 liste
# creazione di due liste in cui salvare gli elementi ordinati
sorted1 = CircularPositionList()
sorted2 = CircularPositionList()

print('Ordinamento della lista 1')
iter_a = list1.bubblesorted()  # iteratore per lista1

#for di ordinamento
i = 0
for e in iter_a:
    print("Elemento", i, ":", e)
    sorted1.add_last(e)
    i += 1

print('Ordinamento della lista 2')
iter_b = list2.bubblesorted()  # iteratore per lista2

i = 0
for e in iter_b:
    print("Elemento", i, ":", e)
    sorted2.add_last(e)
    i += 1

print('\nCreo due liste ordinate ricavate dalle 2 di partenza:')
print('\nsorted1:')
sorted1.printList()

print('\nsorted2:')
sorted2.printList()




def merge(list1, list2):  # controllo che siano due liste
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


print('\nEseguo la merge fra le due liste e ottengo : ')
lis = merge(sorted1, sorted2)
lis.printList()


#test degli operatori
print("\nVerifica dell'operatore add")
new = list1 + list2
new.printList()

print("\nVerifica dell'operatore contain")
print('Salvo il riferimento all elemento 3 e lo cancello')
save = list1.find(3)  # salvo la position dell'elemento 3
list1.delete(save)  # cancello la position di 3
print('L elemento 3 è contenuto nella lista ? ',
      save.element() in list1)  # controllo se 3 è contenuto
print('L elemento 5 è contenuto nella lista ? ', list1.find(
    5).element() in list1)  # controllo se 5 è contenuto

print("\nVerifica dell'operatore get_item")
print("Get first element:", list1[list1.first()])

print("\nVerifica dell'operatore len")
print('La dimensione è:', len(list1))
print("\n")
list1.printList()

print("\nVerifica dell'operatore set_item impostando 100 come primo valore")
list1[list1.first()] = 100
list1.printList()
list1[save] = 99  # prova di set_item in caso venga inserita una position non valida    DA DECOMMENTARE PER IL TESTING

print("\nVerifica dell'operatore delete_item")
print("Cancellazione del primo elemento della lista")
del list1[list1.first()]
list1.printList()

print("\nVerifica dell'operatore __str__")
list1.__str__()


################################################# Prova ScoreBoard
s=ScoreBoard(8)
#score=Score("Michele",250,"95")self._scoreBoard.printList()
score1 = s.Score("Michele",250,"95")
score2 = s.Score("Vittorio",251,"90")
score3 = s.Score("Wael",300,"69")
score4 = s.Score("Ciao",500,"99")
score5 = s.Score("Ciao",10,"99")
score6 = s.Score("Ciao",3,"99")
score7 = s.Score("Ciao",10,"99")
score8 = s.Score("Ciao",40,"99")
score9 = s.Score("Ciao",30000,"99")
score10 = s.Score("Ciao",1,"99")


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



i=0
for e in s.top(5):
    print("Elemento", i, ":", e.value())
    i+=1
print('__----------------------------')

h = 0
for e in s.last(5):
    print("Elemento", h, ":", e.value())
    h += 1
print('----------------SEPARATORE------------------')

s2 = ScoreBoard(10)
score1 = s2.Score("Michele",250,"95")
score2 = s2.Score("Vittorio",251,"90")
score3 = s2.Score("Wael",300,"69")
score4 = s2.Score("Ciao",500,"99")
score5 = s2.Score("Ciao",10,"99")
score6 = s2.Score("Ciao",3,"99")
score7 = s2.Score("Ciao",10,"99")
score8 = s2.Score("Ciao",40,"99")
score9 = s2.Score("Ciao",30000,"99")
score10 = s2.Score("Ciao",1,"99")

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



s.merge(s2) #NON FUNZIONA


i = 0
for e in s.top(10):
    print("Elemento", i, ":", e.value())
    i += 1
print('__----------------------------')

s.printN(6)
print('__----------------------------')

list1.printN(6)
print('__----------------------------')
