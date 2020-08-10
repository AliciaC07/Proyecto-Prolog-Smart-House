class Planta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lugares = []

    def AddLugar(self, lugar):
        self.lugares.append(lugar)

