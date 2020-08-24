import urllib.parse

import requests
from pyswip import *

from src.modelo.Planta import Planta
from src.modelo.Singleton import Singleton


class PrologRepositorio(metaclass=Singleton):

    def __init__(self):
        self.prologInstance = Prolog()
        self.prologInstance.consult('conocimientos.pl')
        self.plantas = []

    def actualizar_persona_totalidad(self, nombre, lugar, estado):
        self.debug_listing("persona")
        self.debug_listing("ubicacion_persona")
        q1 = self.prologInstance.query("actualizar_miembro_casa(" + nombre + "," + estado + "," + lugar + ")")
        print(nombre)
        print(lugar)
        print(estado)
        for sol in q1:
            print(sol)
        self.debug_listing("persona")
        self.debug_listing("ubicacion_persona")

    def simular_intruso(self):
        self.debug_listing("estado_objeto")
        self.debug_listing("intruso")
        q1 = self.prologInstance.query("simular_intruso()")
        for sol in q1:
            print(sol)
        self.debug_listing("intruso")
        self.debug_listing("estado_objeto")

    def obtener_lugares(self):
        q1 = self.prologInstance.query("lugar(Nombre,_,_)")
        lugares = []
        for sol in q1:
            lugares.append(str(sol["Nombre"]))
        return lugares

    def obtener_miembros_casa(self):
        q1 = self.prologInstance.query("miembro_casa(Miembro)")
        miembros = []
        for sol in q1:
            miembros.append(str(sol["Miembro"]))
        return miembros

    def obtener_estado_persona(self, nombre):
        q1 = self.prologInstance.query("persona(" + nombre + ", Estado)")
        estado = None
        for sol in q1:
            estado = sol["Estado"]
        return estado

    def obtener_lugar_persona(self, nombre):
        q1 = self.prologInstance.query("ubicacion_persona(Lugar," + nombre + ")")
        lugar = None
        for sol in q1:
            lugar = sol["Lugar"]
        return lugar

    def apagar_electrodomesticos_lugar(self, lugar):
        self.debug_listing("estado_electrodomestico")
        q1 = self.prologInstance.query("apagar_electrodomesticos_lugar(" + self.transform_prolog_name(lugar.nombre) + ")")
        for sol in q1:
            print(sol)
        self.debug_listing("estado_electrodomestico")

    def apagar_agua_lugar(self, lugar):
        self.debug_listing("estado_objeto_agua")
        q1 = self.prologInstance.query("apagar_agua_lugar(" + self.transform_prolog_name(lugar.nombre) + ")")
        for sol in q1:
            print(sol)
        self.debug_listing("estado_objeto_agua")

    def get_consumo_electrico_por_fecha(self, Mes, Anyo):
        q1 = self.prologInstance.query("calculo_electricidad_por_fecha("+str(Mes)+","+str(Anyo)+",Consumo)")
        consumo = 0
        for sol in q1:
            consumo = sol["Consumo"]
        return consumo

    def get_consumo_agua_por_fecha(self, Mes, Anyo):
        q1 = self.prologInstance.query("calculo_agua_por_fecha("+str(Mes)+","+str(Anyo)+",Consumo)")
        consumo = 0
        for sol in q1:
            consumo = sol["Consumo"]
        return consumo

    def get_unidad_electrica(self):
        q1 = self.prologInstance.query("unidad_electrica(Unidad, _)")
        res = None
        for sol in q1:
            res = sol["Unidad"]
        return str(res)

    def get_unidad_agua(self):
        q1 = self.prologInstance.query("unidad_agua(Unidad, _)")
        res = None
        for sol in q1:
            res = sol["Unidad"]
        return str(res)

    def ahorro_recursos(self):
        self.debug_listing("estado_electrodomestico")
        self.debug_listing("estado_objeto_agua")
        q1 = self.prologInstance.query("ahorro_recursos()")
        for sol in q1:
            print(sol)
        self.debug_listing("estado_electrodomestico")
        self.debug_listing("estado_objeto_agua")

    def get_info_casa(self):
        q1 = self.prologInstance.query("casa_info(Nombre, Ubicacion, _)")
        q2 = self.prologInstance.query("unidad_agua(Unidad, Precio)")
        q3 = self.prologInstance.query("unidad_electrica(Unidad, Precio)")
        nombre_casa = None
        direccion = None
        latitud = None
        longitud = None
        unidad_agua = None
        precio_agua = None
        unidad_electrica = None
        precio_elec = None
        for sol in q1:
            nombre_casa = sol["Nombre"]
            direccion = sol["Ubicacion"]
        for sol in q2:
            unidad_agua = sol["Unidad"]
            precio_agua = sol["Precio"]
        for sol in q3:
            unidad_electrica = sol["Unidad"]
            precio_elec = sol["Precio"]
        return nombre_casa, direccion, latitud, longitud, unidad_agua, precio_agua, unidad_electrica, precio_elec

    def transform_prolog_name(self, name):
        preprocess_name = name.replace(' ', '_')
        return preprocess_name.lower()

    def obtener_nombre_aire(self, lugar):
        return "aire_acondicionado_" + self.transform_prolog_name(lugar.nombre)

    def minunit(self):
        for i in range(0, 10):
            nueva_planta = Planta("planta" + str(i))
            self.plantas.append(nueva_planta)

    def actualizar_info_aire(self, lugar, estado, temperatura, modo, vel):
        self.debug_listing("aire_acondicionado")
        nombre_lugar = self.transform_prolog_name(lugar.nombre)
        ans = None
        if estado == "encendido":
            self.encender_aire_acondicionado(lugar)
        elif estado == "apagado":
            self.apagar_aire_acondicionado(lugar)
        else:
            print("Actualizar")
        check = self.prologInstance.query(
            "actualizar_info_aire(" + nombre_lugar + "," + str(temperatura) + "," + modo + "," + vel + ")")
        for sol in check:
            print(sol)
        self.debug_listing("aire_acondicionado")
        return ans

    def apagar_aire_acondicionado(self, lugar):
        aire = self.obtener_nombre_aire(lugar)
        self.debug_listing("estado_electrodomestico")
        res = self.prologInstance.query("apagar_electrodomestico(" + aire + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_electrodomestico")
        self.debug_listing("consumo")
        return self.obtener_estado_aire(lugar) == "apagado"

    def encender_aire_acondicionado(self, lugar):
        aire = self.obtener_nombre_aire(lugar)
        res = self.prologInstance.query("encender_electrodomestico(" + aire + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_electrodomestico")
        return self.obtener_estado_aire(lugar) == "encendido"

    def get_info_aire(self, lugar):
        """
        Dado un lugar, otiene informacion general del aire, como
        estao, temperatura, modo y velociadd de aire.
        :param lugar:
        :return: (estado, temperatura, modo, vel)
        """
        nombre_lugar = self.transform_prolog_name(lugar.nombre)
        estado = self.obtener_estado_aire(lugar)
        temperatura = None
        modo = None
        vel = None
        query = self.prologInstance.query("aire_acondicionado(" + nombre_lugar + ",Temp,Modo,Vel)")
        for sol in query:
            temperatura = sol["Temp"]
            modo = str(sol["Modo"])
            vel = str(sol["Vel"])
        return str(estado), temperatura, modo, vel

    def obtener_estado_aire(self, lugar):
        """
        Permite obtener el estado de un aire_acondicionado, dado el lugar.
        Recordar que se tiene que pasar el lugar, para luego calcular el nombre
        del aire.
        :param lugar:
        :return: estado(str)
        """
        aire = self.obtener_nombre_aire(lugar)
        ans = None
        check = self.prologInstance.query("estado_electrodomestico(" + aire + ", Estado, _, _)")
        for sol in check:
            ans = str(sol["Estado"])
        return ans

    def InsertPlanta(self, planta, unidade):
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
            aire = "aire_acondicionado(" + self.transform_prolog_name(aux.nombre) + ", 30, auto, bajo)"
            if unidade == "KWatt":
                aire_electro = "electrodomestico(aire_acondicionado_" + self.transform_prolog_name(aux.nombre) + ", 2)"
            else:
                aire_electro = "electrodomestico(aire_acondicionado_" + self.transform_prolog_name(
                    aux.nombre) + ", 2000)"
            aire_estado = "estado_electrodomestico(aire_acondicionado_" + self.transform_prolog_name(
                aux.nombre) + ", apagado, date(0,0,0), time(0,0,0)) "
            self.prologInstance.assertz(fact2)
            self.prologInstance.assertz(aire)
            self.prologInstance.assertz(aire_electro)
            self.prologInstance.assertz(aire_estado)
            q2 = self.prologInstance.query("listing(electrodomestico)")
            for i in q2:
                print(i)
            print(fact2)
            for aux2 in aux.objetos:
                for aux3 in aux2.tipo:

                    if aux3 == "Electrodomestico":
                        hecho = "electrodomestico(" + self.transform_prolog_name(aux2.nombre) + "," + str(
                            aux2.unidad) + ")"
                        hechoestado = "estado_electrodomestico(" + self.transform_prolog_name(
                            aux2.nombre) + ", apagado, date(0,0,0), time(0,0,0))"
                        self.prologInstance.assertz(hecho)
                        self.prologInstance.assertz(hechoestado)
                    elif aux3 == "Agua":
                        if aux2.naturaleza == "Lavamanos":
                            self.prologInstance.assertz(
                                "objeto_agua(" + self.transform_prolog_name(aux2.nombre) + ", continuo," + str(
                                    aux2.unidadAgua) + ")")
                        else:
                            self.prologInstance.assertz(
                                "objeto_agua(" + self.transform_prolog_name(aux2.nombre) + ", fijo," + str(
                                    aux2.unidadAgua) + ")")
                        self.prologInstance.assertz("estado_objeto_agua(" + self.transform_prolog_name(
                            aux2.nombre) + ", cerrado, fecha(0,0,0), tiempo(0,0,0))")

                    elif aux3 == "Contundente":
                        self.prologInstance.assertz(
                            "objeto(" + self.transform_prolog_name(aux2.nombre) + ", " + self.transform_prolog_name(
                                aux2.naturaleza) + "," + self.transform_prolog_name(aux.nombre) + ")")
                        self.prologInstance.assertz(
                            "estado_objeto(" + self.transform_prolog_name(aux2.nombre) + ", cerrado)")
        q2 = self.prologInstance.query("listing(electrodomestico)")
        for i in q2:
            print(i)
        q4 = self.prologInstance.query("listing(objeto_agua)")
        for i in q4:
            print(i)
        q3 = self.prologInstance.query("listing(objeto)")
        for i in q3:
            print(i)
        q5 = self.prologInstance.query("listing(estado_electrodomestico)")
        for i in q5:
            print(i)

    def es_electrodomestico(self, objeto):
        self.debug_listing("electrodomestico")
        nombre = self.transform_prolog_name(objeto.nombre)
        return bool(list(self.prologInstance.query("electrodomestico(" + nombre + ", _)")))

    def es_objeto_agua(self, objeto):
        self.debug_listing("electrodomestico")
        nombre = self.transform_prolog_name(objeto.nombre)
        return bool(list(self.prologInstance.query("objeto_agua(" + nombre + ",_,_)")))

    def InsertInfoHouse(self, name, location, plantas, unidade, unidada, precioe, precioa):
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) + '?format=json'
        response = requests.get(url).json()
        ubicacion_prolog = "('" + location + "'," + str(response[0]["lat"]) + "," + str(response[0]["lon"]) + ")"
        hechos = "casa_info("
        hechos += self.transform_prolog_name(name)
        hechos += ","
        hechos += ubicacion_prolog
        hechos += ","
        planta = self.convert_strings_of_list(plantas)
        hechos += self.ciclo_transform(planta)
        hechos += ")"
        self.prologInstance.assertz(hechos)
        self.prologInstance.assertz(
            "unidad_electrica(" + self.transform_prolog_name(unidade) + ", " + str(precioe) + ")")
        self.prologInstance.assertz("unidad_agua(" + self.transform_prolog_name(unidada) + ", " + str(precioa) + ")")
        q2 = self.prologInstance.query("listing(casa_info)")
        for i in q2:
            print(i)
        q3 = self.prologInstance.query("listing(unidad_electrica)")
        for i in q3:
            print(i)
        q4 = self.prologInstance.query("listing(unidad_agua)")
        for i in q4:
            print(i)

    def InsertPersons(self, persona):
        fam = "persona(" + self.transform_prolog_name(persona) + ", despierto)"
        famtype = "miembro_casa(" + self.transform_prolog_name(persona) + ")"
        lugar = self.obtener_lugares()[0]
        ubicacion = "ubicacion_persona(" + self.transform_prolog_name(lugar) + "," + persona + ")"
        self.prologInstance.assertz(fam)
        self.prologInstance.assertz(famtype)
        self.prologInstance.assertz(ubicacion)
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

    def obtener_estado_electrodomestico(self, electrodomestico):
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        print(nombre)
        ans = None
        check = self.prologInstance.query("estado_electrodomestico(" + nombre + ", Estado, _, _)")
        for sol in check:
            ans = str(sol["Estado"])
        return ans

    def apagar_electrodomestico(self, electrodomestico):
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        self.debug_listing("estado_electrodomestico")
        res = self.prologInstance.query("apagar_electrodomestico(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_electrodomestico")
        self.debug_listing("consumo")
        return self.obtener_estado_electrodomestico(electrodomestico) == "apagado"

    def encender_electrodomestico(self, electrodomestico):
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        self.debug_listing("estado_electrodomestico")
        print(electrodomestico.nombre)
        print(electrodomestico.tipo)
        print(electrodomestico.naturaleza)
        print(electrodomestico.unidad)
        print(electrodomestico.unidadAgua)
        res = self.prologInstance.query("encender_electrodomestico(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_electrodomestico")
        return self.obtener_estado_electrodomestico(electrodomestico) == "encendido"

    def debug_listing(self, sentencia):
        res = self.prologInstance.query("listing(" + sentencia + ")")
        for output in res:
            print(output)

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

    def cerrar_objeto(self, objeto):
        nombre = self.transform_prolog_name(objeto.nombre)
        self.debug_listing("estado_objeto")
        res = None
        if objeto.naturaleza == "Puerta":
            res = self.prologInstance.query("cerrar_puerta(" + nombre + ")")
        elif objeto.naturaleza == "Ventana":
            res = self.prologInstance.query("cerrar_ventana(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_objeto")

    def abrir_objeto(self, objeto):
        nombre = self.transform_prolog_name(objeto.nombre)
        self.debug_listing("estado_objeto")
        res = None
        if objeto.naturaleza == "Puerta":
            res = self.prologInstance.query("abrir_puerta(" + nombre + ")")
        elif objeto.naturaleza == "Ventana":
            res = self.prologInstance.query("abrir_ventana(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_objeto")

    def obtener_estado_objeto(self, objeto):
        nombre = self.transform_prolog_name(objeto.nombre)
        ans = None
        check = self.prologInstance.query("estado_objeto(" + nombre + ", Estado)")
        for sol in check:
            ans = str(sol["Estado"])
        return ans

    def obtener_tipo_objeto_agua(self, objeto):
        nombre = self.transform_prolog_name(objeto.nombre)
        ans = None
        check = self.prologInstance.query("objeto_agua(" + nombre + " , TipoObjetoAgua, _).")
        for res in check:
            ans = str(res["TipoObjetoAgua"])
        return ans

    def usar_objeto_agua(self, objeto):
        """
        Llama a un objeto de agua fijo desde la regla usar_objeto_agua, para guardar
        el consumo de ese objeto en prolog. El metodo se probo y funciona correctamente.
        """
        self.debug_listing("consumo")
        nombre = self.transform_prolog_name(objeto.nombre)
        ans = None
        check = self.prologInstance.query("usar_objeto_agua(" + nombre + ")")
        for res in check:
            print(res)
        self.debug_listing("consumo")

    def obtener_estado_objeto_agua(self, electrodomestico):
        """
        Busca el estado actual de un objeto de agua en prolog, y devuelve su resultado sin convertir a string.
        El metodo se probo y funciona correctamente.
        """
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        ans = None
        check = self.prologInstance.query("estado_objeto_agua(" + nombre + ", Estado, _, _)")
        for sol in check:
            ans = str(sol["Estado"])
        return ans

    def cerrar_objeto_agua(self, electrodomestico):
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        self.debug_listing("estado_objeto_agua")
        res = self.prologInstance.query("cierre_objeto_agua(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_objeto_agua")
        self.debug_listing("consumo")
        return self.obtener_estado_electrodomestico(electrodomestico) == "apagado"

    def abrir_objeto_agua(self, electrodomestico):
        nombre = self.transform_prolog_name(electrodomestico.nombre)
        self.debug_listing("estado_objeto_agua")
        print(electrodomestico.nombre)
        print(electrodomestico.tipo)
        print(electrodomestico.naturaleza)
        print(electrodomestico.unidad)
        print(electrodomestico.unidadAgua)
        res = self.prologInstance.query("abrir_objeto_agua(" + nombre + ")")
        for check in res:
            print(check)
        self.debug_listing("estado_objeto_agua")
        return self.obtener_estado_electrodomestico(electrodomestico) == "encendido"

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
