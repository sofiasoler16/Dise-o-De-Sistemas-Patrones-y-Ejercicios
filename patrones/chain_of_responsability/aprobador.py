
class Aprobador:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def aprobar(self,nota):
        if self.siguiente:
            return self.siguiente.aprobar(nota)
        
