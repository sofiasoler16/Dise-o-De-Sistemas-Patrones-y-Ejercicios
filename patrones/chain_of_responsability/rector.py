from aprobador import Aprobador

class Rector(Aprobador):
    def aprobar(self, nota):
        if nota > 7:
            return "Beca completa aprobada por Rectorado"
        else:
            return "Beca rechazada"