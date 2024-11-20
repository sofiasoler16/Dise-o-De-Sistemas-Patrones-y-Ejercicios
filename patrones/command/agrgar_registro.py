from comandos_base import Base


class AgregarRegistro(Base):
    def __init__(self, base):
        self.base = base

    def execute(self):
        self.base.conectar()
        self.base.agregar()
        self.base.guardar()
        self.base.desconectar()