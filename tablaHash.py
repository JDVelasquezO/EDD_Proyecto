
class NodoHash:

    def __init__(self):
        self.array = []

    def insert(self, dato):
        if self.buscarDato(dato):
            self.array.append(dato)
        else:
            print("dato existente")

    def buscarDato(self, dato):
        return False if dato in self.array else True

    def eliminar(self, dato):
        if not self.buscarDato(dato):
            self.array.remove(dato)
            if len(self.array) == 0:
                return 0
            else:
                return True
        else:
            return False
    def printArray(self):
        print(self.array)
    
class TablaHash:
    def __init__(self, size ):
        self.Size = size-1
        self.arreglo = []
        for i in range (0, size):
            self.arreglo.append(-1)
    
    def getSize(self):
        return self.Size
    
    def setSize(self, n):
        self.Size = n
    
    def getNodo(self):
        return self.arreglo
#dato sera de tipo nodo 
    def setNodo(self, nodo):
        self.arreglo = nodo

    def funcionHash(self, dato ):
        lenDato = dato
        return int(lenDato % self.Size)

    def sizeTabla(self):
        contadorAux = 0
        for i in self.arreglo:
            if i != -1:
                contadorAux +=1
        return contadorAux

    

    def insertarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        posicion_hash =int( posicion_hash)
        bandera = self.verificarDato(dato)
        if self.arreglo[posicion_hash] != -1:
            if bandera:
                nuevo_dato = self.arreglo[posicion_hash]
                nuevo_dato.insert(dato)
                print("dato agregado con exito")
            else:
                nuevo_dato = self.arreglo[posicion_hash]
                nuevo_dato.insert(dato)
                print("dato agregado con exito")
        else:
            nuevo_dato = NodoHash()
           # tupla = (dato, tupla)
            nuevo_dato.insert(dato)
            self.arreglo[posicion_hash] = nuevo_dato
            print("dato agregado con exito")
                

    def verificarDato(self, dato):
        aux_bol = False
        posicion_hash = self.funcionHash(dato)
        posicion_hash = int(posicion_hash)
        if self.arreglo[posicion_hash] != -1:

            if self.arreglo[posicion_hash].buscarDato(dato):
                aux_bol = True
                return aux_bol
        return aux_bol

    def eliminarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo_hash = self.arreglo[posicion_hash]
        if nodo_hash.eliminar(dato):
            print("dato eliminado")
        elif nodo_hash.eliminar(dato) == 0: 
            print("dato eliminado")
            self.arreglo[posicion_hash] = -1
        else:
            print("dato no eliminado")


    def printTbl(self):
        contador = 0
        for i in range(0,self.Size+1):
            if self.arreglo[i] != -1:
                print(str(contador) + " | " + str(self.arreglo[i].array))
            contador +=1
    def buscar(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo = self.arreglo[posicion_hash]
        if not nodo.buscarDato(dato):
            print("el dato es: " + str(self.arreglo[posicion_hash]))

t = TablaHash(8)
t.insertarDato(20)
t.buscar(20)
"""print(20%7)
print(33%7)
print(21%7)
print(10%7)
print(12%7)
print(14%7)
print(56%7)
print(100%7)
"""
