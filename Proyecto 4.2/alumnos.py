class Alumnos():
    nombreAlumno = None
    notaAlumno = None

    def __init__(self):
       self.nombreAlumno = "Julio"
       self.notaAlumno = 20

    def registroAlumno(self,nombre, nota):
        self.nombreAlumno = nombre
        self.notaAlumno = nota
        if nota >= 10:
            return 'El alumno '+ nombre + ' Está APROBADO'
        else:
            return 'El alumno ' + nombre + ' Está REPROBADO'
    

alumno = Alumnos()
print("Nombre del mejor alumno:", alumno.nombreAlumno)
print("Nota del mejor alumno:", alumno.notaAlumno)


print()
resultado = alumno.registroAlumno("Juan", 15)
print("Nombre del alumno:", alumno.nombreAlumno)
print("Nota del alumno:", alumno.notaAlumno)
print(resultado)

