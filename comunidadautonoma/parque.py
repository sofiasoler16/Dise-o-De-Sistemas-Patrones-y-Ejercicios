class ParqueNacional:
    def __init__(self, nombre, fecha_declaracion):
        self.nombre = nombre
        self.fecha_declaracion = fecha_declaracion
        self.areas = []  # Lista de áreas en el parque

    def agregar_area(self, area):
        self.areas.append(area)

    def __repr__(self):
        return f"ParqueNacional({self.nombre}, Areas={len(self.areas)})"
