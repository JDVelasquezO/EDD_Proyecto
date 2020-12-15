from Node import Node

class TablaHash:
    def __init__(self, size, db, name, nCols):
        self.id = 0
        self.Size = size-1
        self.values = list()
        self.headers = list()
        self.db = db
        self.name = name
        self.nCols = nCols
        self.genericId = 1
        self.sign = True
        self.pk = None
        for i in range (0, size):
            self.values.append(None)

    def alterAddPK(self, database, table, indices):
        self.pk = indices

    def setHeader(self, header):
        self.headers.append(header)

    def getSize(self):
        return self.Size

    def setSize(self, n):
        self.Size = n

    def getNodo(self):
        return self.values

    #dato sera de tipo nodo 
    def setNodo(self, nodo):
        self.values = nodo

    def funcionHash(self, dato):
        if isinstance(dato, list):
            lenDato = 0
            if len(dato) > 1:
                if len(self.pk) > 1:
                    if self.sign:
                        for i in self.pk:
                            lenDato += dato[i]
                        self.genericId = lenDato
                    node = self.buscar(self.genericId)
                    if node is None:
                        dato[0:0] = [self.genericId]
                    else:
                        self.genericId += 1
                        self.sign = False
                        self.funcionHash(dato)
                else:
                    lenDato = dato[self.pk[0]]
        else:
            lenDato = int(dato)
        return int(lenDato % self.Size)

    def sizeTabla(self):
        contadorAux = 0
        for i in self.values:
            if i is not None:
                contadorAux +=1
        return contadorAux   

    def insert(self, database, table, dato):
        if len(self.headers) == 0:
            self.setHeader(dato)
            return
        if len(dato) == self.nCols:
            if self.pk:
                posicion_hash = int(self.funcionHash(dato))
                bandera = self.verificarDato(dato, posicion_hash)
                if self.values[posicion_hash] is not None:
                    if bandera:
                        nuevo_dato = self.values[posicion_hash]
                        nuevo_dato.insert(dato)
                else:
                    nuevo_dato = Node()
                    nuevo_dato.post_in_hash = posicion_hash
                    nuevo_dato.insert(dato)
                    self.values[posicion_hash] = nuevo_dato
            else:
                self.nCols += 1
                self.insert(database, table, dato)
        else:
            node = self.buscar(self.genericId)
            if node is None:
                dato[0:0] = [self.genericId]
                self.alterAddPK(database, table, [0])
                self.insert(database, table, dato)
            else:
                self.genericId += 1
                self.insert(database, table, dato)

    def verificarDato(self, dato, position):
        aux_bol = False
        if self.values[position] is not None:
            if not self.values[position].buscarDato_binary(dato):
                aux_bol = True
        return aux_bol

    def eliminarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo_hash = self.values[posicion_hash]
        if nodo_hash.eliminar(dato):
            print("dato eliminado")
        elif nodo_hash.eliminar(dato) == 0: 
            print("dato eliminado")
            self.values[posicion_hash] = -1
        else:
            print("dato no eliminado")

    def printTbl(self):
        contador = 0
        print(f"i | {self.headers}")
        for i in range(0,self.Size+1):
            if self.values[i] != None:
                print(str(self.values[i].post_in_hash) + " | " + str(self.values[i].array))
            contador +=1

    def buscar(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo = self.values[posicion_hash]
        if nodo is not None:
            return nodo.busquedaB(dato)
        else:
            return None
