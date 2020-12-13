import time
from Hash import TablaHash

t1 = TablaHash(6, "db1", "profesores", 3)
t2 = TablaHash(5, "db1", "estudiantes", 3)
t3 = TablaHash(4, "db1", "cursos", 3)
t1.definePK([0])
t1.insertarDato(["ID", "Profesor", "Curso"])
t1.insertarDato([1, "Mario", "0107"])
t1.insertarDato([2, "Daniel", "0105"])
t1.insertarDato([3, "segio", "0159"])
t1.insertarDato([4, "Jose", "0174"])
t1.insertarDato(["María", "0107"])
t1.insertarDato(["Josefina", "0103"])

t2.insertarDato(["ID", "Estudiante", "0105"])
t2.insertarDato([1, "Estudiante1", "0107"])
t2.insertarDato([2, "Estudiante2", "0103"])
t2.insertarDato(["Estudiante3", "0104"])

t3.insertarDato(["IdProfesor", "idEstudiante"])
t3.insertarDato([1, 1])
t3.insertarDato([4, 2])

# t1 = time.time()
print("Tabla de profesores: ")
t1.printTbl()
# print("----------------------------")
# print("Tabla de estudiantes:")
# t2.printTbl()
# print(t.buscar(23))

# t0 = time.time()
# t1 = time.time()
# print(t1 - t0)
