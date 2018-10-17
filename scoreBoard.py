from circularPositionalList import CircularPositionList

# ___________                      ____ ________
# \__    ___/___ _____    _____   /_   /   __   \
#   |    |_/ __ \\__  \  /     \   |   \____    /
#   |    |\  ___/ / __ \|  Y Y  \  |   |  /    /
#   |____| \___  >____  /__|_|  /  |___| /____/
#              \/     \/      \/


class ScoreBoard():

    def __init__(self, x=10):
        self._size = x
        self._scoreBoard = CircularPositionList()

    class Score:  # classe score innestata in ScoreBoard

        def __init__(self, name, score, data):
            # self._scoreBoard=scoreBoard
            self._name = name
            self._score = score
            self._data = data

        def value(self):
            return self._score

        def data(self):
            return self._data

        def name(self):
            return self._name

        def __gt__(self, other):
            if(self.value() > other.value()):
                return True
            else:
                return False

        def __lt__(self, other):
            if(self.value() < other.value()):
                return True
            else:
                return False

    def size(self):
        return self._scoreBoard._size

    def __len__(self):
        return self._size

    def Is_empty(self):
        return self._scoreBoard.Is_empty()

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

    def top(self, i=1):
        j = 0
        for e in self._scoreBoard:
            if(i == 0):
                break
            if(j == i):
                break
            j += 1
            yield e

    def last(self,i= 1):
        j = 0
        temp = self._scoreBoard.copy()             # Viene cancellata temp? 
        temp.reverse()
        for e in temp:
            if(i == 0):
                break
            if(j == i):
                break
            j += 1
            yield e
        temp.clear()                            # PROBABILMENTE NON SERVE  

    def merge(self,list):  # controllo che siano due liste
        for i in list._scoreBoard:
            self.insert(i)
