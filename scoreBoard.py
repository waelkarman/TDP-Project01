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

    class Score:  

        def __init__(self, name, score, data):
            self._name = name
            self._score = score
            self._data = data

        # DESCRIZIONE:  Ritorna lo score dell'oggetto Score
        # NOTE: --
        def value(self):
            return self._score

        # DESCRIZIONE: Ritorna la data nell'ogg. Score
        # NOTE: --
        def data(self): 
            return self._data

        # DESCRIZIONE:Ritorna il nome nell'ogg. Score
        # NOTE: --
        def name(self):
            return self._name

        # DESCRIZIONE: Greater than
        # NOTE: Utility
        def __gt__(self, other):
            if(self.value() > other.value()):
                return True
            else:
                return False

        # DESCRIZIONE: Less than
        # NOTE: Utility 
        def __lt__(self, other):
            if(self.value() < other.value()):
                return True
            else:
                return False

    # DESCRIZIONE: Restituisce il numero di Score presenti nello ScoreBoard
    # NOTE: 
    def size(self):
        return self._scoreBoard._size

    # DESCRIZIONE: Restituisce la dimensione dello ScoreBoard
    # NOTE:
    def __len__(self):
        return self._size

    # DESCRIZIONE: Restituisce True se non ci sono Score nello ScoreBoard e False altrimenti
    # NOTE: -- 
    def Is_empty(self):
        return self._scoreBoard.Is_empty()

    # DESCRIZIONE: Inserisce un nuovo Score nello ScoreBoard se e solo se non è peggiore dei risultati correntemente salvati. Non incrementa la dimensione dello Scoreboard
    # NOTE: Lo scoreboard è implementato in modo che l'elemento con lo score più grande si trova in testa e il più piccolo in coda
    def insert(self, s):  
        if self.Is_empty() == True:                                 # se lo score board è vuoto si inserisce lo score 
            self._scoreBoard.add_last(s)  
        elif self._size == len(self._scoreBoard):                             #se lo scoreboard è pieno :
            if s.value() > self._scoreBoard.last().element().value():          # verifica se l' elemento da inserire è migliore del peggiore presente nello scoreboard, altrimenti non inserire 
                self._scoreBoard.delete(self._scoreBoard.last())               # nel caso bisogna inserire si inserisce al posto dell ultimo, e successivamente si effettuano gli swap fino a piazzare lo score nella posizione corretta 
                self._scoreBoard.add_last(s)
                temp = self._scoreBoard.last()
                while temp.element().value() > self._scoreBoard.before(temp).value():   
                    save = self._scoreBoard.get_prev_Position(
                        temp)  
                    elemtemp = temp.element()
                    self._scoreBoard.replace(temp, save.element())
                    self._scoreBoard.replace(save, elemtemp)
                    temp = save
                    if temp == self._scoreBoard.first():
                        break

        elif self._size > len(self._scoreBoard):                                # Se lo scoreboard non è pieno, verifica se il valore da inserire è migliore del peggior valore presente nello scoreboard.
            if s.value() > self._scoreBoard.last().element().value():           # In caso positivo, inserisci in coda e procedi con degli swap per piazzare lo score nella posizione giusta 
                self._scoreBoard.add_last(s)
                temp = self._scoreBoard.last()
                while temp.element().value() > self._scoreBoard.before(temp).value():
                    save = self._scoreBoard.get_prev_Position(temp)
                    elemtemp = temp.element()
                    self._scoreBoard.replace(temp, save.element())
                    self._scoreBoard.replace(save, elemtemp)
                    temp = save
                    if temp == self._scoreBoard.first():
                        break
            else:
                self._scoreBoard.add_last(s)                                    # se lo score non è pieno ma l elemento inserito è peggiore dell ultimo elemento presente, inserisci semplicemente in coda

    # DESCRIZIONE: Stampa N elementi dello ScoreBoard circolarmente
    # NOTE:--
    def printN(self, n):
        temp = self._scoreBoard.first()
        i = 0
        while n > 0:
            if temp == self._scoreBoard.first():
                i = 0
            print("Elemento", i, ":", temp.element().value())
            temp = self._scoreBoard.get_next_Position(temp)
            n -= 1
            i += 1

    # DESCRIZIONE: Restituisce i migliori i score nello ScoreBoard
    # NOTE:
    def top(self, i=1): 
        if i < 0:
            raise TypeError
                                
        j = 0
        for e in self._scoreBoard:
            if(i == 0):
                break
            if(j == i):
                break
            j += 1
            yield e

    # DESCRIZIONE: Restituisce i peggiori i score nello ScoreBoard
    # NOTE: --
    def last(self, i=1):
        if i < 0:
            raise TypeError
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

    # DESCRIZIONE: Fonde lo ScoreBoard corrente con new selezionando i 10 migliori risultati
    # NOTE:
    def merge(self,list):
        if not isinstance(list, ScoreBoard):
            raise TypeError
        for i in list._scoreBoard:
            self.insert(i)

            
    
