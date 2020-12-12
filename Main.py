import time
from Hash import TablaHash

t = TablaHash(10, "db1", "table1", 3)

# t0 = time.time()
# for item in range(0, 100000):
#     t.insertarDato(item)
t.insertarDato(["ID", "Nombre", "Edad"])
t.insertarDato([1, "Mario", "33"])
t.insertarDato([2, "Mario", "33"])
t.insertarDato([6, "segio", "33"])
t.insertarDato([23, "Jose", "33"])
# t.insertarDato([25, 16,])
t.insertarDato(["María", "33"])
t.insertarDato(["Josefina", "34"])
t.insertarDato([24, "David", "33"])
t.insertarDato([9, "David", "33"])
t.insertarDato([23, "David", "33"])

# t1 = time.time()
t.printTbl()
print(t.buscar(23))

# t0 = time.time()
# t1 = time.time()
# print(t1 - t0)
