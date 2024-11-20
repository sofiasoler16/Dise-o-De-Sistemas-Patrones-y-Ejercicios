
from director import Director
from secretaria import Secretaria
from rector import Rector

# Chain of Responsability
# Permite que una peticion se pase a lo largo de una cadena de objetos
# Cada objeto decide si la maneja o la pasa al siguiente en la cadena
# Reduce el acomplamiento entre el emisor de la peticion y los objetos que la procesan

# Tenemos una interfaz que se va a poder implementar en todas las clases
# Nos sirve para evitar el uso de if-else

# Interfaz

cadena = Secretaria(Director(Rector()))

nota = 8

print(cadena.aprobar(nota))