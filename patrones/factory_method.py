

from abc import ABC


class Triangulo(ABC):
    def __init__(self, lados):
        self.lados = lados

    def tipo(self):
        pass


# Productos concretos
class Equilatero(Triangulo):
    def tipo(self):
        return "Equilátero"


class Isosceles(Triangulo):
    def tipo(self):
        return "Isósceles"


class Escaleno(Triangulo):
    def tipo(self):
        return "Escaleno"


# Factory Method
class TrianguloFactory:
    def __init__(self, lados):
        self.lados = lados

    def crear_triangulo(self, lados):
        if lados[0] == lados[1] == lados[2]:
            return Equilatero(lados)
        elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
            return Isosceles(lados)
        else:
            return Escaleno(lados)
        

lados = [3,3,6]

fabrica = TrianguloFactory(lados)
triangulo = fabrica.crear_triangulo(lados)
print(f"Triángulo de tipo: " , triangulo.tipo())