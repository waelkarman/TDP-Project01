from circularPositionalList import CircularPositionalList

# ___________                      ____ ________
# \__    ___/___ _____    _____   /_   /   __   \
#   |    |_/ __ \\__  \  /     \   |   \____    /
#   |    |\  ___/ / __ \|  Y Y  \  |   |  /    /
#   |____| \___  >____  /__|_|  /  |___| /____/
#              \/     \/      \/


class ScoreBoard():

    def __init__(self, x=10):
        self._size = x
        self._scoreBoard = CircularPositionalList()

    class Score:  # classe score innestata in ScoreBoard

        def __init__(self, name, score, data):
            # self._scoreBoard=scoreBoard
            self._name = name
            self._score = score
            self._data = data

        # DESCRIZIONE:  Ritorna lo score nell'ogg. Score
        # NOTE: Serve solo per accedere agli elementi non in maniera diretta, essendo privati
        # STATO: OK
        def value(self):
            return self._score

        # DESCRIZIONE: Ritorna la data nell'ogg. Score
        # NOTE:  Serve solo per accedere agli elementi non in maniera diretta, essendo privati
        # STATO: OK
        def data(self): 
            return self._data

        # DESCRIZIONE:Ritorna il nome nell'ogg. Score
        # NOTE: Serve solo per accedere agli elementi non in maniera diretta, essendo privati
        # STATO:
        def name(self):
            return self._name

        # DESCRIZIONE: Greater than
        # NOTE: Utiliy
        # STATO: OK
        def __gt__(self, other):
            if(self.value() > other.value()):
                return True
            else:
                return False

        # DESCRIZIONE: Less than
        # NOTE: Utility 
        # STATO: OK
        def __lt__(self, other):
            if(self.value() < other.value()):
                return True
            else:
                return False

    # DESCRIZIONE: Restituisce il numero di Score presenti nello ScoreBoard
    # NOTE: 
    # STATO: Ok
    def size(self):
        return self._scoreBoard._size

    # DESCRIZIONE: Restituisce la dimensione dello ScoreBoard
    # NOTE:
    # STATO: OK
    def __len__(self):
        return self._size

    # DESCRIZIONE: Restituisce True se non ci sono Score nello ScoreBoard e False altrimenti
    # NOTE:
    # STATO:
    def Is_empty(self):
        return self._scoreBoard.Is_empty()

    # DESCRIZIONE: Inserisce un nuovo Score nello ScoreBoard se e solo se non è peggiore dei risultati correntemente salvati. Non incrementa la dimensione dello Scoreboard
    # NOTE: DA RIFARE EVENTUALMENTE 
    # STATO:--
    def insert(self, s):  # controllare che uno score sia effettivamente uno score
        if self.Is_empty() == True:  # se la lista è vuota inserisco normalmente
            self._scoreBoard.add_last(s)  # inserimento in coda
        # se lo scoreboard è pieno devo rimpiazzare
        elif self._size == len(self._scoreBoard):
            if s.value() > self._scoreBoard.last().element().value():  # se s è maggiore del più piccolo li scambio
                self._scoreBoard.delete(self._scoreBoard.last())
                self._scoreBoard.add_last(s)
                temp = self._scoreBoard.last()
                # continuo a scambiare finchè non trovo un elemento più grande
                while temp.element().value() > self._scoreBoard.before(temp).value():
                    save = self._scoreBoard._get_prev_Position(
                        temp)  # salvo la successiva
                    elemtemp = temp.element()
                    self._scoreBoard.replace(temp, save.element())
                    self._scoreBoard.replace(save, elemtemp)
                    temp = save
                    if temp == self._scoreBoard.first():
                        break

        elif self._size > len(self._scoreBoard):
            if s.value() > self._scoreBoard.last().element().value():
                self._scoreBoard.add_last(s)
                temp = self._scoreBoard.last()
                while temp.element().value() > self._scoreBoard.before(temp).value():
                    save = self._scoreBoard._get_prev_Position(temp)
                    elemtemp = temp.element()
                    self._scoreBoard.replace(temp, save.element())
                    self._scoreBoard.replace(save, elemtemp)
                    temp = save
                    if temp == self._scoreBoard.first():
                        break
            else:
                self._scoreBoard.add_last(s)

    # DESCRIZIONE: Stampa N elementi dello ScoreBoard circolarmente
    # NOTE:
    # STATO: OK
    def printN(self, n):
        temp = self._scoreBoard.first()
        i = 0
        while n > 0:
            if temp == self._scoreBoard.first():
                i = 0
            print("Elemento", i, ":", temp.element().value())
            temp = self._scoreBoard._get_next_Position(temp)
            n -= 1
            i += 1

    # DESCRIZIONE: Restituisce i migliori i score nello ScoreBoard
    # NOTE:
    # STATO: OK
    def top(self, i=1): 
        j = 0
        for e in self._scoreBoard:
            if(i == 0):
                break
            if(j == i):
                break
            j += 1
            yield e

    # DESCRIZIONE: Restituisce i peggiori i score nello ScoreBoard
    # NOTE: temp viene cancellata?
    # STATO:
    def last(self,i= 1):
        j = 0
        temp = self._scoreBoard.copy()              
        temp.reverse()
        for e in temp:
            if(i == 0):
                break
            if(j == i):
                break
            j += 1
            yield e
        temp.clear()                            # PROBABILMENTE NON SERVE  

    # DESCRIZIONE: Fonde lo ScoreBoard corrente con new selezionando i 10 migliori risultati
    # NOTE:
    # STATO:
    def merge(self,list):  # controllo che siano due liste
        for i in list._scoreBoard:
            self.insert(i)
