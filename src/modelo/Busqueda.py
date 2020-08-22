from pyswip import Prolog
class Busqueda:
    def buscarConsumoDeObjeto(self,Query):
        self.prologInstance = Prolog()
        self.prologInstance.consult('conocimientos.pl')
