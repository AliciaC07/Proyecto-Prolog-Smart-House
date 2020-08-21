from functools import partial

from src.visual.Helper import *
from src.visual.QtHelper import *
from src.visual.ShVistaObjetoElectrico import ShDetalleObjetoElectrico
from src.visual.resource_locator import *


class ShVistaLugar:
    def __init__(self, lugar):
        # Partes principales de la
        # ventana principal
        self.ventana_principal = None
        self.widget_padre = None
        self.scroll_area = None
        self.scroll_area_contents = None

        # Componentes de la ventana principal
        self.fuente_botones = None
        self.fuente_titulos = None
        self.botones = []
        self.labels = []
        self._labels = self.labels.append
        self._botones = self.botones.append

        # Instancias de la vista de la planta seleccionada.
        self.ventana_vista_objeto = None
        self.vista_objeto = None

        # Configurables
        self.resolucion = (800, 600)
        self.btn_offset = (150, 200)
        self.panel_dinamico_offset = (310, 10)
        self.cantidad_paneles = 4

        # Prolog instance
        self.lugar = lugar
        self.cantidad_objetos = len(self.lugar.objetos)

    def cabeceraVentana(self):
        pass

    def abrir_ventana_objeto(self, objeto):
        tipo_objeto = determinar_tipo_objeto(objeto)
        if tipo_objeto == ELECTRODOMESTICO:
            self.ventana_vista_objeto = QtWidgets.QMainWindow()
            self.vista_objeto = ShDetalleObjetoElectrico(objeto)
            self.vista_objeto.setupUi(self.ventana_vista_objeto)
            self.ventana_vista_objeto.show()
        else:
            print(objeto.nombre)
            print(objeto.tipo)
            print(objeto.naturaleza)
            print(objeto.unidad)

    def generar_objetos_disponibles(self):
        if self.cantidad_objetos > self.cantidad_paneles * 2 + 1:
            self.scroll_area_contents.setFixedSize(800, 600 + self.cantidad_objetos * 20)
            self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # Creación de las plantas dinámicas
        initial_left_pos = self.panel_dinamico_offset[1]
        initial_top_pos = self.panel_dinamico_offset[0]
        cnt_objetos = 0
        for i in self.lugar.objetos:
            cnt_objetos += 1
            if cnt_objetos > 4:
                initial_left_pos = 10
                initial_top_pos += self.btn_offset[0]
                cnt_objetos = 1
            icono = determinar_icono_objeto(i)
            btn_objeto = crear_boton_ico(self.scroll_area_contents, icono, i.nombre, partial(self.abrir_ventana_objeto, i),
                                         self.fuente_botones, initial_left_pos, initial_top_pos, 150, 100)
            initial_left_pos += self.btn_offset[1]
            self._botones(btn_objeto)

    def setupUi(self, ventana_principal):
        self.ventana_principal = ventana_principal
        # Fuentes de los botones y titulos de la cabecera de la ventana ShHome
        self.fuente_titulos = crear_fuente("Consolas", 16, es_negrita=True)
        self.fuente_botones = crear_fuente("Consolas", 12, es_negrita=False)
        self.ventana_principal.resize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setFixedSize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setWindowTitle("Lugar actual: " + self.lugar.nombre)
        self.ventana_principal.setWindowIcon(QtGui.QIcon(LOGO_ICON))
        self.widget_padre = QtWidgets.QWidget(self.ventana_principal)
        self.scroll_area = QtWidgets.QScrollArea(self.widget_padre)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(0, 0, self.resolucion[0], self.resolucion[1])
        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setFixedSize(self.resolucion[0], self.resolucion[1])
        self.scroll_area_contents.setGeometry(0, 0, self.resolucion[0], self.resolucion[1])
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.ventana_principal.setCentralWidget(self.widget_padre)
        self.cabeceraVentana()
        self.generar_objetos_disponibles()
