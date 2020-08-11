from pyswip import Prolog

from src.modelo.Lugar import Lugar
from src.modelo.Objetos import Objeto
from src.modelo.Planta import Planta


class PrologRepositorio:

    def __init__(self):
        self.prologInstance = Prolog()
        self.prologInstance.consult('conocimientos.pl')

    def transform_prolog_name(self, name):
        preprocess_name = name.replace(' ', '_')
        return preprocess_name.lower()

    def InsertPlanta(self, planta):
        fact = "planta("
        fact += self.transform_prolog_name(planta.nombre)
        fact += ", "
        lugars = self.convert_strings_of_list(planta.lugares)
        fact += self.ciclo_transform(lugars)
        fact += ")"
        print(fact)
        self.prologInstance.assertz(fact)
        for aux in planta.lugares:
            fact2 = "lugar("
            fact2 += self.transform_prolog_name(aux.nombre)
            fact2 += ", "
            fact2 += "20"
            fact2 += ", "
            obs = self.convert_strings_of_list(aux.objetos)
            fact2 += self.ciclo_transform(obs)
            fact2 += ")"
            self.prologInstance.assertz(fact2)
            print(fact2)
            for aux2 in aux.objetos:
                if aux2.tipo == "Electrodomestico":
                    self.prologInstance.assertz(
                        "electrodomestico(" + self.transform_prolog_name(aux2.nombre) + "," + str(aux2.unidad) + ")")
                    self.prologInstance.assertz(
                        "estado_electrodomestico(" + self.transform_prolog_name(aux2.nombre) + ", apagado)")
                elif aux2.tipo == "Agua":
                    self.prologInstance.assertz(
                        "objeto_agua(" + self.transform_prolog_name(aux2.nombre) + ", " + str(aux2.unidad) + ")")
                elif aux2.tipo == "Contundente":
                    self.prologInstance.assertz(
                        "objeto(" + self.transform_prolog_name(aux2.nombre) + ", " + aux.nombre + ")")
                    self.prologInstance.assertz(
                        "estado_objeto(" + self.transform_prolog_name(aux2.nombre) + ", cerrado)")


    def convert_strings_of_list(self, lugares):
        nombres = []
        for i in lugares:
            nombres.append(i.nombre)
        return nombres

    def ciclo_transform(self, items):
        fact1 = ""
        fact1 += "[ "
        for aux in range(0, len(items)):
            fact1 += self.transform_prolog_name(items[aux])
            if aux == len(items) - 1:
                fact1 += "]"
            else:
                fact1 += ", "
        return fact1


prue = PrologRepositorio()
planta = Planta("planta1")
lugare = Lugar("sala1")
lugare1 = Lugar("cocina1")
objeto = Objeto("telvision1", "Electrodomestico", 260)
objeto1 = Objeto("bombillo1", "Electrodomestico", 0.06)
objeto2 = Objeto("nevera", "Electrodomestico", 260)
objeto3 = Objeto("lavamanos", "Agua", 88.8)
objeto4 = Objeto("puerta1", "Contundente", 0)
lugare.objetos.append(objeto)
lugare.objetos.append(objeto1)
lugare1.objetos.append(objeto2)
lugare1.objetos.append(objeto3)
lugare1.objetos.append(objeto4)
planta.lugares.append(lugare)
planta.lugares.append(lugare1)
prue.InsertPlanta(planta)
q = prue.prologInstance.query("listing(electrodomestico)")
for i in q:
    print(i)
q1 = prue.prologInstance.query("listing(objeto_agua)")
for i in q1:
    print(i)

q2 = prue.prologInstance.query("listing(estado_electrodomestico)")
for i in q2:
    print(i)

q3 = prue.prologInstance.query("listing(objeto)")
for i in q2:
    print(i)
q4 = prue.prologInstance.query("listing(estado_objeto)")
for i in q4:
    print(i)