from TdP_collections.list.positional_list import PositionalList

# ___________                      ____ ________ 
# \__    ___/___ _____    _____   /_   /   __   \
#   |    |_/ __ \\__  \  /     \   |   \____    /
#   |    |\  ___/ / __ \|  Y Y  \  |   |  /    / 
#   |____| \___  >____  /__|_|  /  |___| /____/  
#              \/     \/      \/                 


class CircularPositionalList(PositionalList):

    def __init__(self):
        super().__init__()

    # DESCRIZIONE: Restituisce l' elemento nella posizione precedente a p , NONE se p non ha un predecessore e ValueError se p non è una position della lista
    # NOTE: Se c'è un solo elemento nella lista restituisce None
    def before(self,p):
        if len(self) == 1:
            return None
        try:
            pos = super().before(p)
        except BaseException :
            print("Posizione non valida")
        
        return pos.element() 

    # DESCRIZIONE: Restituisce l' elemento nella posizione successiva a p , NONE se p non ha un predecessore e ValueError se p non è una position della lista
    # NOTE: Se c'è un solo elemento nella lista restituisce None
    def after(self,p):
        if len(self) ==1:
            return None
        try:
            pos = super().after(p)
        except BaseException:
            print("Posizione non valida")  
        return pos.element()

    # DESCRIZIONE: restituisce True se la lista è vuota e False altrimenti
    # NOTE: --
    def Is_empty(self):
        return super().is_empty()

    # DESCRIZIONE: Restituisce True se la lista è ordinata e False altrimenti
    # NOTE: La funzione sorting_criterion verifica che la relazione d'ordine è verificata tra gli elementi contenuti nella lista
    def Is_sorted(self):
        j = len(self)
        if j == 0:
            raise ValueError('The list is empty') 
        else:    
            passo = self.first()
            flag = True
            while j > 1 and flag == True:
                flag = self.sorting_criterion(passo.element(), self.after(passo))
                passo = self.get_next_Position(passo)
                j -= 1
            if flag == True:
                return True
        return False

    # DESCRIZIONE: La funzione implementa il criterio di ordinamento richiamato dal metodo Is_sorted
    # NOTE: --
    def sorting_criterion(self,p,q):
        if int(p) <= int(q):
            return True
        return False

    # DESCRIZIONE: Inserisce l' elemento "e" in testa alla lista e restituisce la position del nuovo elemento
    # NOTE:  --
    def add_first(self,e):        

        if len(self) == 0:                             
            temp = super().add_first(e)              # Istruzioni per rendere la coda circolare 
            temp._node._prev = temp._node
            temp._node._next = temp._node
        else:                                                                   
            temp = super().add_first(e)
            temp._node._prev = self._trailer._prev                              
            self._trailer._prev._next = temp._node                              
        return temp

    # DESCRIZIONE: Inserisce l elemento "e" in coda alla lista e restituisce la position del nuovo elemento
    # NOTE: --
    def add_last(self,e):   
        
        if len(self) == 0:                                                      
            temp = self.add_first(e)
        else:
            temp = super().add_last(e)
            temp._node._next = self._header._next                               
            self._header._next._prev = temp._node                               
        return temp

    # DESCRIZIONE: Inserisce un nuovo elemento "e" prima del nodo della position p e restituisce la position del nuovo elemento
    # NOTE: --
    def add_before(self,p,e):
        try:
            node=self._validate(p)     
        except BaseException: 
            print("Position non valida")   
                   
        if p == self.first():
            temp = self.add_last(e)
        else:
            temp = super()._insert_between(e,node._prev,node)
        return temp

    # DESCRIZIONE: Inserisce un nuovo elemento "e" dopo il nodo nella position p e restituisce la position del nuovo elemento
    # NOTE: --
    def add_after(self,p,e): 
        try:
            node=self._validate(p)  
        except BaseException:
            print("Position non valida")
        

        if p == self.last():
            temp = self.add_first(e)
        else:
            temp = super()._insert_between(e,node,node._next)
        return temp

    # DESCRIZIONE: Restituisce una position contenente la prima occorrenza dell' elemento "e" nella lista o NONE se "e" non è presente
    # NOTE: --
    def find(self, e):
        
        j = len(self)
        if j == 0:
            raise ValueError('La lista è vuota')                                        
        else:
            temp = self.first()
            while j > 0:
                if temp.element() == e:
                    return temp
                temp = self.get_next_Position(temp)
                j -= 1
        return None

    # DESCRIZIONE: Sostituisce l' elemento in position p con "e" e restituisce il vecchio valore
    # NOTE: --
    def replace(self,p,e):
        
        old_value = p.element()
        try:
            super().replace(p,e)
        except BaseException:
            print("Position non valida")
        
        return old_value

    # DESCRIZIONE: Rimuove e restituisce l' elemento in position p dalla lista invalida p
    # NOTE: --
    def delete(self,p):
        try:
            node = self._validate(p)
        except BaseException:
            print ("Position non valida")
        if node == self._trailer._prev:              # istruzioni per conservare la circolarità della lista in caso di cancellazione del primo 
            self._trailer._prev = node._prev         # o dell'ultimo elemento
        if node == self._header._next:
            self._header._next = node._next
        return super().delete(p)

    # DESCRIZIONE: Rimuove tutti gli elementi dalla lista invalidando le corrispondenti position
    # NOTE: --
    def clear(self):
        j = len(self)
        if j == 0 :
            raise ValueError('La lista è vuota')
        else:
            while j > 0 : 
                temp = self.first()                                             
                self.delete(temp)
                j-=1

    # DESCRIZIONE:Restituisce il numero di occorrenze di "e" nella lista 
    # NOTE: --
    def count(self,e):

       
        j = len(self)
        count = 0
        if j == 0:
            raise ValueError('La lista è vuota')                                   
        else:
            for temp in self:
                if(temp == e):
                    count+=1
        
        if count == 0:
            return print("L'elemento non è presente nella lista")
        
        return count

    # DESCRIZIONE: Inverte l'ordine degli elementi nella lista
    # NOTE: Reverse effettuata senza utilizzo di una copia della lista
    def reverse(self):                                                               
        j = len(self)                                                                
        if j==0:                                                                     
            raise ValueError("La lista è vuota") 
        else:   
            primo = self.add_first(self.last().element())
            self.delete(self.last())
            while j > 1:
                primo = self.add_after(primo,self.last().element())
                self.delete(self.last())
                j-=1
            self._trailer._prev = primo._node

    # DESCRIZIONE: Restituisce la nuova CircularPositionalList che contiene gli stessi elementi della lista corrente memorizzati nello stesso ordine
    # NOTE: --
    def copy(self):
        copy = CircularPositionalList()
        if len(self) == 0:
            raise ValueError("La lista è vuota") 
        else:
            for e in self:
                copy.add_last(e)
        return copy

#---------------------------------------------------------------(')> 
#--------------------------------->> DEFINIZIONE OPERATORI <<---(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: Crea una lista con tutti gli elementi di 'x' e tutti gli elementi di 'y' inseriti dopo l’ultimo elemento di 'x'
    # NOTE: x + y 
    def __add__(self, other):            
        copy=self.copy()
        for e in other:
            copy.add_last(e)
        return  copy

    # DESCRIZIONE: Restituisce True se 'p' è presente nella lista e False altrimenti
    # NOTE: p in x
    def __contains__(self, item):       
        pos = self.find(item)
        if pos == None:
            return False
        else:
            return True

    # DESCRIZIONE: Restituisce l’elemento contenuto nella position 'p'
    # NOTE: x[p]
    def __getitem__(self, position):  
        try:
            self._validate(position)
        except BaseException:
            print("Position non valida")                        
        walk = self.first() 
        while walk != position:
            walk = self.get_next_Position(walk)
        return walk.element()

    # DESCRIZIONE: Restituisce il numero di elementi contenuti in x
    # NOTE: len(x)
    def __len__(self):
        return self._size

    # DESCRIZIONE: Cancella l’elemento contenuto nella position p
    # NOTE: x.del[p]
    def __delitem__(self,p):
        try:
            self._validate(p)
        except BaseException:
            print("Position non valida")
        self.delete(p)

    # DESCRIZIONE: Generatore che restituisce gli elementi della lista a partire da quello che è identificato come primo fino a quello che è identificato come ultimo
    # NOTE: iter()
    def __iter__(self):
      generator = self.first()
      i=0
      while i < len(self):          
        current = self.get_next_Position(generator)           
        yield generator.element()
        generator = current
        i+=1

    # DESCRIZIONE: Sostituisce l’elemento nella position p con e
    # NOTE: x[p] = e
    def __setitem__(self, p, e):
        try:
            self._validate(p)   
        except BaseException:
            print("Position non valida")     
        temp = self.first()
        i=0
        while temp != p and i<len(self):        
            temp = self.get_next_Position(temp)
            i+=1
        self.replace(temp, e)

    # DESCRIZIONE: Rappresenta il contenuto della lista come una sequenza di elementi,separati da virgole, partendo da quello che è identificato come primo
    # NOTE: --
    def __str__(self): 
        stringa = ''
        for e in self:
            stringa = stringa + str(e)
            stringa = stringa + ','
        stringa = stringa[0:len(stringa)-1]
        print(stringa)


#---------------------------------------------------------------(')>
#--------------------------------->> ESERCIZI <<----------------(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: Ordina gli elementi della CircularPositionalList e li restituisce nell’ordine risultante. Il generatore non deve modificare l’ordine in cui sono memorizzati gli elementi nella lista.
    # NOTE: --
    def bubblesorted(self):
        n = len(self)
        copyed = self.copy()
        walk = copyed.first()
        for i in range(n):                                                         # implementazione algoritmo d'ordinamento bubblesort
            for j in range(0, n-i-1):                                        
                if copyed[walk] > copyed[copyed.get_next_Position(walk)] :
                    temp = copyed[walk]
                    copyed[walk] = copyed[copyed.get_next_Position(walk)]          # istruzioni per scambiare gli elementi in caso il corrente sia maggiore del successivo
                    copyed[copyed.get_next_Position(walk)] =  temp
                walk = copyed.get_next_Position(walk)
            walk = copyed.first()                                                  # aggiornamento della position 
        
        for e in copyed:
            yield e

#---------------------------------------------------------------(')>
#--------------------------------->> METODI DI TESTING <<-------(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: STAMPA PER CIRCULAR POSITION
    # NOTE: --
    def printList(self):
        i=0
        for e in self:
            print("Elemento",i,":",e)
            i+=1

    # DESCRIZIONE: STAMPA N ELEMENTI CIRCOLARMENTE
    # NOTE: --
    def printN(self,n):
        temp = self.first()
        i=0
        while n>0:
            if temp == self.first() :
                i=0
            print("Elemento", i, ":", temp.element())
            temp = self.get_next_Position(temp)
            n-=1   
            i += 1

#---------------------------------------------------------------(')>
#--------------------------------->> DEFINIZIONE UTILITY <<-----(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: Restituisce la Position successiva a p
    # NOTE: --
    def get_next_Position(self,p): 
        try:
            temp =  super().after(p)
        except BaseException:
            print("Position non valida")           
        return temp

    # DESCRIZIONE: Restituisce la Position precedente a p
    # NOTE: --
    def get_prev_Position(self,p):
        try: 
            temp = super().before(p)
        except BaseException:
            print("Postion non valida")
        return temp

    



        
       



