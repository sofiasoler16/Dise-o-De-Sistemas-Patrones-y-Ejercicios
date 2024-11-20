from aprobador import Aprobador

class Director(Aprobador):
    def aprobar (self, nota):
        if nota < 7:
            return "Director racepta media beca"
        else:
            return super().aprobar(nota)