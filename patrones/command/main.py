
from agrgar_registro import AgregarRegistro
from comandos_base import Base
from modificar_registro import ModificarRegistro


base = Base()

agregar_registro = AgregarRegistro(Base)
modificar_registro = ModificarRegistro(Base)

print(agregar_registro.execute())
print(modificar_registro.execute())


