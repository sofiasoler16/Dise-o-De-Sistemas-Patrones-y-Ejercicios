from comandos_base import Base


class ModificarRegistro(Base):
    def __init__(self, base):
        self.base = base


    def execute(self):
        self.base.conectar()
        self.base.modificarRegistro()
        self.base.guardarCambios()
        self.base.desconectar()