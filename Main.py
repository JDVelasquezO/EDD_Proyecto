import time
from Hash import TablaHash

t = TablaHash(10, "db1", "table1", 3)

# t0 = time.time()
# for item in range(0, 100000):
#     t.insertarDato(item)
t.insertarDato(["1", "Carlos", "25"])
t.insertarDato(["23", "Mario", "33"])
t.insertarDato(["34", "Daniel", "49"])
t.insertarDato(["45", "David", "20"])
t.insertarDato(["58", "Luis", "48"])
t.insertarDato(["67", "Rodrigo", "25"])
t.insertarDato(["70", "Alberto", "35"])
# t1 = time.time()

t.printTbl()

# t0 = time.time()
print(t.buscar("45"))
# t1 = time.time()
# print(t1 - t0)

"""print(20%7)
print(33%7)
print(21%7)
print(10%7)
print(12%7)
print(14%7)
print(56%7)
print(100%7)
"""