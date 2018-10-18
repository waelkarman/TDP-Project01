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

    # DESCRIZIONE: restituisce l' elemento nella posizione precedente a p , NONE se p non ha un predecessore e ValueError se p non è una position della lista
    # NOTE: aggiunto se è un solo elemento, restituisce None
    # STATO: OK
    def before(self,p):
        if len(self) == 1:
            return None
        try:
            pos = super().before(p)
        except BaseException :
            print("Posizione non valida")
        
        return pos.element() 

    # DESCRIZIONE: restituisce l' elemento nella posizione successiva a p , NONE se p non ha un predecessore e ValueError se p non è una position della lista
    # NOTE: aggiunto se è un solo elemento, restituisce None
    # STATO: OK
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
    # STATO: OK
    def Is_empty(self):
        return super().is_empty()

    # DESCRIZIONE: restituisce True se la lista è ordinata e False altrimenti
    # NOTE: la funzione criterio verifica che le relazione d' ordine è verificata fra gli elementi contenuti nella lista, 
    # NOTE: Ecc da gestire nel test
    # STATO: OK
    def Is_sorted(self):
        j = len(self)
        if j == 0:
            raise ValueError('The list is empty') 
        else:    
            passo = self.first()
            res = True
            while j > 1 and res == True:
                res = self.sorting_criterion(passo.element(), self.after(passo))
                passo = self._get_next_Position(passo)
                j -= 1
            if res == True:
                return True
        return False

    # DESCRIZIONE: la funzione implementa il criterio di ordinamento richiamato dal metodo is_sorted
    # NOTE: --
    # STATO: OK
    def sorting_criterion(self,p,q):
        if int(p) <= int(q):
            return True
        return False

    # DESCRIZIONE: inserisce l' elemento e in testa alla lista e restituisce la position den nuovo elemento
    # NOTE:  --
    # STATO: OK
    def add_first(self,e):
        if len(self) == 0:                                                     #-->se la lista è vuota inseriamo l'elemento e lo facciamo puntare a se stesso
            temp = super().add_first(e)
            temp._node._prev = temp._node
            temp._node._next = temp._node
        else:                                                                   #-->altrimenti inseriamo l'elemento e modifichiamo i puntatori in modo che il nuovo elemento sia collegato all'ultimo
            temp = super().add_first(e)
            temp._node._prev = self._trailer._prev                              #-->collego il primo elemento all'ultimo
            self._trailer._prev._next = temp._node                              #-->collego l'ultimo elemento al primo
        return temp

    # DESCRIZIONE: inserisce l elemento e in coda alla lista e restituisce la position del nuovo elemento
    # NOTE: --
    # STATO: OK
    def add_last(self,e):                                                       #-->limitare i nodi header e trailer per non compromettere la struttura dati
        if len(self) == 0:                                                      #-->se la lista è vuota inseriamo l'elemento e lo facciamo puntare a se stesso
            temp = self.add_first(e)
        else:
            temp = super().add_last(e)
            temp._node._next = self._header._next                               #-->collego l'ultimo elemento al primo
            self._header._next._prev = temp._node                               #-->collego il primo elemento all'ultimo
        return temp

    # DESCRIZIONE: inserisce un nuovo elemento e prima del nodo della position p e restituisce la position del nuovo elemento
    # NOTE: aggiunta la validate sulla position, aggiunto try 
    # STATO: Testata ad inizio script di test
    def add_before(self,p,e):
        try:
            node=self._validate(p)     
        except BaseException: 
            print ("Position non valida")                                           #limitare i nodi header e trailer per non compromettere la struttura dati                                                  #da chiedere
        if p == self.first():
            temp = self.add_last(e)
        else:
            temp = super()._insert_between(e,node._prev,node)
        return temp

    # DESCRIZIONE: inserisce un nuovo elemento e dopo il nodo nella position p e restituisce la position den nuovo elemento
    # NOTE: aggiunta la validate sulla position, aggiunto try
    # STATO: Testata ad inizio script di test
    def add_after(self,p,e): 
        try:
            node=self._validate(p)  # da chiedere
        except BaseException:
            print("Position non valida")

        if p == self.last():
            temp = self.add_first(e)
        else:
            temp = super()._insert_between(e,node,node._next)
        return temp

    # DESCRIZIONE: restituisce una position contenente la prima occorrenza dell' elemento e nella lista o NONE se e non è presente
    # NOTE: gestire l'ecc nel test
    # STATO: OK
    def find(self, e):
        j = len(self)
        if j == 0:
            raise ValueError('La lista è vuota')                                        # rivedi
        else:
            temp = self.first()
            while j > 0:
                if temp.element() == e:
                    return temp
                temp = self._get_next_Position(temp)
                j -= 1
        return None

    # DESCRIZIONE:sostituisce l' elementoin position p con e restituisce il vecchio
    # NOTE: la validate è insita nel replace della superclasse 
    # STATO: OK
    def replace(self,p,e):
        save = p.element()
        try:
            super().replace(p,e)
        except BaseException:
            print("Position non valida")
        
        return save

    # DESCRIZIONE:rimuove e restituisce l' elemento in position p dalla lista invalida p
    # NOTE: aggiunta la validate e e usata la variabile node al posto di p.node, aggiunta try
    # STATO: TESTING
    def delete(self,p):
        try:
            node = self._validate(p)
        except BaseException:
            print ("Position non valida")
        if node == self._trailer._prev:
            self._trailer._prev = node._prev
        if node == self._header._next:
            self._header._next = node._next
        return super().delete(p)

    # DESCRIZIONE: rimuove tutti gli elementi della lista invalidando le corrispondenti position
    # NOTE: usato il metodo len
    # STATO: TESTING
    def clear(self):
        j = len(self)
             #prendo la dimensione
        if j == 0 :
            raise ValueError('La lista è vuota')
        else:
            while j > 0 : 
                temp = self.first()                                             
                self.delete(temp)
                j-=1

    # DESCRIZIONE:restituisce il numero di occorrenze di e nella lista 
    # NOTE: aggiunto l uso del foro al posto del while, gestire ecc nel test
    # STATO: TESTING
    def count(self,e):
        j = len(self)
        count = 0
        if j == 0:
            raise ValueError('La lista è vuota')                                   
        else:
            for temp in self:
                if(temp == e):
                    count+=1
        return count

    # DESCRIZIONE: inverte l'ordine degli elementi nela lista
    # NOTE: uso del metodo len, gestire ecc nel test!
    # STATO: OK
    def reverse(self):                                                               
        j = len(self)                                                                
        if j==0:                                                                     # E' possibile in O(1)?
            raise ValueError("La lista è vuota") 
        else:   
            primo = self.add_first(self.last().element())
            self.delete(self.last())
            while j > 1:
                primo = self.add_after(primo,self.last().element())
                self.delete(self.last())
                j-=1
            self._trailer._prev = primo._node

    # DESCRIZIONE: restituisce la nuova circularpositionallist che contiene gli stessi elementi della lista corrente memorizzati nello stesso ordine
    # NOTE: uso del metodo len aggiunta dell iteratore, gestire ecc nel test
    # STATO: OK
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

    # DESCRIZIONE: Crea una lista con tutti gli elementi di x e tutti gli elementi di y inseriti dopo l’ultimo elemento di x
    # NOTE: x + y
    # STATO: OK 
    def __add__(self, other):            
        copy=self.copy()
        for e in other:
            copy.add_last(e)
        return  copy

    # DESCRIZIONE: Restituisce True se p è presente nella lista e False altrimenti
    # NOTE: p in x
    # STATO: OK
    def __contains__(self, item):       
        pos = self.find(item)
        if pos == None:
            return False
        else:
            return True

    # DESCRIZIONE: Restituisce l’elemento contenuto nella position p
    # NOTE:  aggiunta la validate e le try
    # STATO: OK
    def __getitem__(self, position):  #restituisce l'elemento contenuto nella position p # controllare quando va fuori
        
        try:
            self._validate(position)
        except BaseException:
            print("Position non valida")                        
        walk = self.first() 
        while walk != position:
            walk = self._get_next_Position(walk)
        return walk.element()

    # DESCRIZIONE: Restituisce il numero di elementi contenuti in x
    # NOTE: --
    # STATO: OK
    def __len__(self):
        return self._size

    # DESCRIZIONE: Cancella l’elemento contenuto nella position p
    # NOTE: agg try
    # STATO: OK
    def __delitem__(self,p):
        try:
            self._validate(p)
        except BaseException:
            print("Position non valida")
        self.delete(p)

    # DESCRIZIONE: Generatore che restituisce gli elementi della lista a partire da quello che è identificato come primo fino a quello che è identificato come ultimo
    # NOTE: --
    # STATO: OK
    def __iter__(self):
      cursor = self.first()
      i=0
      while i < len(self):          
        save = self._get_next_Position(cursor)           
        yield cursor.element()
        cursor = save
        i+=1

    # DESCRIZIONE: Sostituisce l’elemento nella position p con e
    # NOTE: aggiunta condizione nel while per l uscita dal ciclo, agg try
    # STATO: OK
    def __setitem__(self, p, e):
        
        try:
            self._validate(p)   
        except BaseException:
            print("Position non valida")     
        temp = self.first()
        
        i=0
        while temp != p and i<len(self):        
            temp = self._get_next_Position(temp)
            i+=1
        self.replace(temp, e)

    # DESCRIZIONE: Rappresenta il contenuto della lista come una sequenza di elementi,separati da virgole, partendo da quello che è identificato come primo
    # NOTE: aggiunto l uso del metodo len
    # STATO: OK
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

    # DESCRIZIONE: che ordina gli elementi della CircularPositionalList e li restituisce nell’ordine risultante. Il generatore non deve modificare l’ordine in cui sono memorizzati gli elementi nella lista.
    # NOTE: --
    # STATO: OK
    def bubblesorted(self):
        n = len(self)
        copyed = self.copy()
        walk = copyed.first()
        for i in range(n):                   
            for j in range(0, n-i-1):
                if copyed[walk] > copyed[copyed._get_next_Position(walk)] :
                    temp = copyed[walk]
                    copyed[walk] = copyed[copyed._get_next_Position(walk)]
                    copyed[copyed._get_next_Position(walk)] =  temp
                walk = copyed._get_next_Position(walk)
            walk = copyed.first()
        
        for e in copyed:
            yield e

#---------------------------------------------------------------(')>
#--------------------------------->> METODI DI TESTING <<-------(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: STAMPA PER CIRCULAR POSITION
    # NOTE:
    # STATO:
    def printList(self):
        i=0
        for e in self:
            print("Elemento",i,":",e)
            i+=1

    # DESCRIZIONE: STAMPA N ELEMENTI CIRCOLARMENTE
    # NOTE: --
    # STATO:OK
    def printN(self,n):
        temp = self.first()
        i=0
        while n>0:
            if temp == self.first() :
                i=0
            print("Elemento", i, ":", temp.element())
            temp = self._get_next_Position(temp)
            n-=1   
            i += 1

#---------------------------------------------------------------(')>
#--------------------------------->> DEFINIZIONE UTILITY <<-----(_)
#---------------------------------------------------------------""

    # DESCRIZIONE: Restituisce la Position dopo p
    # NOTE: --
    # STATO: OK
    def _get_next_Position(self,p): 
        try:
            temp =  super().after(p)
        except BaseException:
            print("Position non valida")           #Validate
        return temp

    # DESCRIZIONE: Restituisce la Position prima di p
    # NOTE: --
    # STATO: OK
    def _get_prev_Position(self,p):
        try: 
            temp = super().before(p)
        except BaseException:
            print("Postion non valida")
        return temp

"""
    da provare se è possibile 
    def _get_head(self):      # utility
        return self._header
    def _get_tail(self):
        return self._trailer
    def _set_head(self,new):
        self._header=new
    def _set_tail(self,new):
        self._header=new


    def reverseO1(self):
        head = _get_head()
        tail = _get_tail()
        self._set_head(tail)
        self._set_head(head)
        self._set_node_next(self._get_head(),self.last())
        self._set_node_prev(self._get_head(),None)
        self._set_node_next(self._get_tail(),None)
        self._set_node_prev(self._get_tail(),self.first())                                                                            
"""



