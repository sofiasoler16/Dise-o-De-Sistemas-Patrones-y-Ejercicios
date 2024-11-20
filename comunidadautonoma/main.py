from animal import Animal
from area import Area
from comunidad import ComunidadAutonoma
from parque import ParqueNacional
from vegetal import Vegetal


andalucia = ComunidadAutonoma("Andalucía", "Consejería de Medio Ambiente")

# Crear un parque nacional
parque = ParqueNacional("Doñana", "1969-10-28")
andalucia.agregar_parque(parque)

# Crear áreas en el parque
area1 = Area("Marismas", 500)
area2 = Area("Dunas", 300)
parque.agregar_area(area1)
parque.agregar_area(area2)

# Crear especies
encina = Vegetal("Quercus ilex", "Encina", 2000, True, "Primavera")
lince = Animal("Lynx pardinus", "Lince Ibérico", 50, "Invierno", "Carnívoro")

# Asociar especies a áreas
area1.agregar_especie(encina)
area1.agregar_especie(lince)

# Agregar alimentos al lince
conejo = Animal("Oryctolagus cuniculus", "Conejo", 500, None, "Herbívoro")
lince.agregar_alimento(conejo)

# Mostrar datos
print(andalucia)
print(parque)
print(area1)
print(encina)
print(lince)