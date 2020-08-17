from src.visual.tools.QtHelper import *
from functools import partial
from src.visual.PrologRepositorio import PrologRepositorio
import sys


# noinspection PyMethodMayBeStatic
class ShVistaPlanta:
    def __init__(self, planta):
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
        self.ventana_vista_planta = None
        self.vista_planta = None

        # Configurables
        self.resolucion = (800, 600)
        self.btn_offset = (150, 200)
        self.panel_dinamico_offset = (310, 10)
        self.cantidad_paneles = 4

        # Prolog instance
        self.planta = planta
        self.cantidad_lugares = len(self.planta.lugares)

    def abrir_panel_status(self):
        print("Se abrio la ventana de status.")

    def abrir_panel_clima(self):
        print("Se abrio la ventana de clima.")

    def abrir_panel_reportes(self):
        print("Se abrio la ventana de reportes.")

    def abrir_contenido_lugar(self, planta):
        print("Se abrio la " + planta.nombre)

    def cabeceraVentana(self):

        # Fuentes de los botones y titulos de la cabecera de la ventana ShHome
        self.fuente_titulos = crear_fuente("Consolas", 16, es_negrita=True)
        self.fuente_botones = crear_fuente("Consolas", 12, es_negrita=False)

        # Labels de la cabecera de la ventana ShHome
        lbl_estado = crear_label(self.scroll_area_contents, "Acciones Rápidas", self.fuente_titulos, 50, 35)

        lbl_img_estado = crear_img(self.scroll_area_contents, "assets/accion_rapida.png", 10, 30)

        lbl_lugares = crear_label(self.scroll_area_contents, "Lugares de " + self.planta.nombre,
                                  self.fuente_titulos, 50, 250)

        lbl_img_lugares = crear_img(self.scroll_area_contents, "assets/casa.png", 10, 245)

        # Botones de la cabecera de la ventana ShHome
        btn_reportes = crear_boton_ico(self.scroll_area_contents, "assets/grafico.png",
                                       "Apagar Todo", lambda: print("hey"), self.fuente_botones, 10, 90, 150, 50)

        self._labels(lbl_estado)
        self._labels(lbl_lugares)
        self._labels(lbl_img_lugares)
        self._labels(lbl_img_estado)
        self._botones(btn_reportes)

    def generar_lugares_disponibles(self):
        if self.cantidad_lugares > self.cantidad_paneles*2+1:
            self.scroll_area_contents.setFixedSize(800, 600 + self.cantidad_lugares*20)
            self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # Creación de las plantas dinámicas
        initial_left_pos = self.panel_dinamico_offset[1]
        initial_top_pos = self.panel_dinamico_offset[0]
        cnt_lugares = 0
        for i in self.planta.lugares:
            cnt_lugares += 1
            if cnt_lugares > 4:
                initial_left_pos = 10
                initial_top_pos += self.btn_offset[0]
                cnt_lugares = 1
            btn_lugar = crear_boton_ico(self.scroll_area_contents, "../assets/cocina.png",
                                        i.nombre, lambda: print("hola"), self.fuente_botones,
                                        initial_left_pos, initial_top_pos, 150, 100)
            initial_left_pos += self.btn_offset[1]
            self._botones(btn_lugar)

    def setupUi(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.resize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setFixedSize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setWindowTitle("Prolog Smart House")
        self.ventana_principal.setWindowIcon(QtGui.QIcon("assets/logo.png"))
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
        self.generar_lugares_disponibles()