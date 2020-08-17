from pyswip import Prolog

from src.modelo.Lugar import Lugar
from src.modelo.Objetos import Objeto
from src.modelo.Planta import Planta
from src.modelo.Singleton import Singleton


class PrologRepositorio(metaclass=Singleton):

    def __init__(self):
        self.prologInstance = Prolog()
        self.prologInstance.consult('conocimientos.pl')
        self.plantas = []
        self.minunit()
        print(self.plantas)

    def transform_prolog_name(self, name):
        preprocess_name = name.replace(' ', '_')
        return preprocess_name.lower()

    def minunit(self):
        for i in range(0, 10):
            nueva_planta = Planta("planta" + str(i))
            self.plantas.append(nueva_planta)

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

                    hecho = "electrodomestico(" + self.transform_prolog_name(aux2.nombre) + "," + str(aux2.unidad) + ")"
                    hechoestado = "estado_electrodomestico(" + self.transform_prolog_name(aux2.nombre) + ", apagado)"
                    self.prologInstance.assertz(hecho)
                    self.prologInstance.assertz(hechoestado)
                elif aux2.tipo == "Agua":
                    self.prologInstance.assertz(
                        "objeto_agua(" + self.transform_prolog_name(aux2.nombre) + ", " + str(aux2.unidad) + ")")
                elif aux2.tipo == "Contundente":
                    self.prologInstance.assertz(
                        "objeto(" + self.transform_prolog_name(aux2.nombre) + ", " + aux.nombre + ")")
                    self.prologInstance.assertz(
                        "estado_objeto(" + self.transform_prolog_name(aux2.nombre) + ", cerrado)")

    def InsertInfoHouse(self, name, location, plantas):
        hechos = "casa_info("
        hechos += self.transform_prolog_name(name)
        hechos += ","
        hechos += self.transform_prolog_name(location)
        hechos += ","
        planta = self.convert_strings_of_list(plantas)
        hechos += self.ciclo_transform(planta)
        hechos += ")"
        self.prologInstance.assertz(hechos)
        q2 = self.prologInstance.query("listing(casa_info)")
        for i in q2:
            print(i)

    def InsertPersons(self, persona):
        fam = "persona(" + self.transform_prolog_name(persona) + ", despierto)"
        famtype = "miembro_casa(" + self.transform_prolog_name(persona) + ")"
        self.prologInstance.assertz(fam)
        self.prologInstance.assertz(famtype)
        q2 = self.prologInstance.query("listing(persona)")
        for i in q2:
            print(i)

    def GetConsumoElectrico(self, place):
        consumo = 0.0
        query = self.prologInstance.query(
            "calcular_consumo_electrico(" + self.transform_prolog_name(place) + ", Consumo")
        for solution in query:
            consumo = solution["Consumo"]
        return consumo

    def CloseAllDoors(self):
        self.prologInstance.query("cerrar_puertas()")
        return "All doors closed"

    def convert_strings_of_list(self, lugares):
        nombres = []
        for i in lugares:
            nombres.append(i.nombre)
        return nombres

    def ciclo_transform(self, items):
        fact1 = ""
        fact1 += "["
        for aux in range(0, len(items)):
            fact1 += self.transform_prolog_name(items[aux])
            if aux == len(items) - 1:
                fact1 += "]"
            else:
                fact1 += ", "
        return fact1

# prue = PrologRepositorio()
# planta = Planta("planta1")
# lugare = Lugar("sala1")
# lugare1 = Lugar("cocina1")
# objeto = Objeto("telvision1", "Electrodomestico", 260)
# objeto1 = Objeto("bombillo1", "Electrodomestico", 0.06)
# objeto2 = Objeto("nevera", "Electrodomestico", 260)
# objeto3 = Objeto("lavamanos", "Agua", 88.8)
# objeto4 = Objeto("puerta1", "Contundente", 0)
# lugare.objetos.append(objeto)
# lugare.objetos.append(objeto1)
# lugare1.objetos.append(objeto2)
# lugare1.objetos.append(objeto3)
# lugare1.objetos.append(objeto4)
# planta.lugares.append(lugare)
# planta.lugares.append(lugare1)
# prue.InsertPlanta(planta)
# q = prue.prologInstance.query("listing(electrodomestico)")
# for i in q:
#     print(i)
# q1 = prue.prologInstance.query("listing(objeto_agua)")
# for i in q1:
#     print(i)
#
# q2 = prue.prologInstance.query("listing(estado_electrodomestico)")
# for i in q2:
#     print(i)
#
# q3 = prue.prologInstance.query("listing(objeto)")
# for i in q2:
#     print(i)
# q4 = prue.prologInstance.query("listing(estado_objeto)")
# for i in q4:
#     print(i)
