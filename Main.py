import time
from Hash import TablaHash

t1 = TablaHash(6, "db1", "profesores", 3)
t2 = TablaHash(3, "db1", "estudiantes", 2)
t3 = TablaHash(4, "db1", "cursos", 3)

t1.definePK([0])
t1.insertarDato(["ID", "Profesor", "Curso"])
t1.insertarDato([1, "Jose", "0174"])
t1.insertarDato([2, "María", "0107"])
t1.insertarDato([3, "Josefina", "0103"])
t1.insertarDato([4, "Mario", "0107"])
t1.insertarDato([5, "Daniel", "0105"])
t1.insertarDato([6, "segio", "0159"])

# t2.definePK([0])
t2.insertarDato(["ID", "Estudiante", "Curso"])
t2.insertarDato(["Jorge", "0105"])
t2.insertarDato(["Mariano", "0107"])
t2.insertarDato(["Ricardo", "0103"])
t2.insertarDato(["Nicole", "0104"])

t3.definePK([1, 2])
t3.insertarDato(["Id", "Nombre", "IdProfesor", "idEstudiante"])
t3.insertarDato(["0107", 1, 1])
t3.insertarDato(["0103", 4, 2])
t3.insertarDato(["0105", 2, 4])

# t1 = time.time()
print("Tabla de profesores: ")
t1.printTbl()
print("----------------------------")
print("Tabla de estudiantes:")
t2.printTbl()
print("----------------------------")
print("Tabla de cursos:")
t3.printTbl()
# print(t2.buscar(3))

# t0 = time.time()
# t1 = time.time()
# print(t1 - t0)
