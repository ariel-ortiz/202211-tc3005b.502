class Estudiante:

    def __init__(self, nombre, matricula):
        self.__nombre = nombre
        self.__matricula = matricula

    def __str__(self):
        return f'Soy un estudiante ({self.__matricula}, {self.__nombre})'

class EstudianteTrabador(Estudiante):

    def __init__(self, nombre, matricula, sueldo):
        super().__init__(nombre, matricula)
        self.__sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} y también trabajo y gano ${self.__sueldo:,.2f}'

e1 = Estudiante('Juan', 123)
print(id(e1), e1)
e2 = EstudianteTrabador('María', 199, 50_000)
print(id(e2), e2)
print(e1 is e2)
print(e1 == e2)
print()
print(type(e1))
print(isinstance(e1, Estudiante))
print(isinstance(e1, object))
print(isinstance(e1, EstudianteTrabador))
print()
print(type(e2))
print(isinstance(e2, Estudiante))
print(isinstance(e2, object))
print(isinstance(e2, EstudianteTrabador))
print()
print(type(type(type(e1))))
print()
print(type(e1) == Estudiante)
print(type(e1) == object)

e2.sueldo = 12_000
print(e2.sueldo)
