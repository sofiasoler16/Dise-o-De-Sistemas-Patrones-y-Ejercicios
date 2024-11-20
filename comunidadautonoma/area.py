class Area:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie  # en km²
        self.especies = []  # Lista de especies en el área

    def agregar_especie(self, especie):
        self.especies.append(especie)

    def __repr__(self):
        return f"Area({self.nombre}, Superficie={self.superficie} km², Especies={len(self.especies)})"
