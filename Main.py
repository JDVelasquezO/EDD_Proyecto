import time
from Tytus import Tytus
from DataBase import Database
from Hash import TablaHash

db1 = Database("db1")

t1 = TablaHash(6, "db1", "profesores", 3)
t2 = TablaHash(3, "db1", "estudiantes", 2)
t3 = TablaHash(2, "db1", "cursos", 3)
# db1.createTable("db1", "profesores", 3)

t1.alterAddPK("db1", "profesores", [0])
t3.alterAddPK("db3", "cursos", [1, 2])

t1.insert("db1", "table1", [1, "Jose", "0174"])
t1.insert("db1", "table1", [2, "María", "0107"])
t1.insert("db1", "table1", [3, "Josefina", "0103"])
t1.insert("db1", "table1", [4, "Mario", "0107"])
t1.insert("db1", "table1", [5, "Daniel", "0105"])
t1.insert("db1", "table1", [6, "segio", "0159"])

t1.eliminarDato(3)
t1.eliminarDato(6)
t1.editar(1, "Pedro", 4)

# t2.definePK([0])
t2.insert("db1", "table1", ["Jorge", "0105"])
t2.insert("db1", "table1", ["Mariano", "0107"])
t2.insert("db1", "table1", ["Ricardo", "0103"])
t2.insert("db1", "table1", ["Nicole", "0104"])
t2.eliminarDato(2)

t3.insert("db1", "table1", ["0107", 1, 1])
t3.insert("db1", "table1", ["0103", 4, 2])
t3.insert("db1", "table1", ["0105", 2, 5])
t3.insert("db1", "table1", ["0108", 2, 4])
t3.insert("db1", "table1", ["0109", 3, 1])

# t1 = time.time()
print("Tabla de profesores: ")
t1.printTbl()
print("----------------------------")
print("Tabla de estudiantes:")
t2.printTbl()
print("----------------------------")
print("Tabla de cursos:")
t3.printTbl()
print(t2.buscar(3))

# t0 = time.time()
# t1 = time.time()
# print(t1 - t0)
