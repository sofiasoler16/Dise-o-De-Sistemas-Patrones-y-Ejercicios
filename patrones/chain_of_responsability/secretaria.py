
from aprobador import Aprobador

class Secretaria(Aprobador):
    def aprobar (self, nota):
        if nota < 5:
            return "Secretaria rechaza la beca"
        else:
            return super().aprobar(nota)