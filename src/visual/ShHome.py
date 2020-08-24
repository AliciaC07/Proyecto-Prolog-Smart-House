from datetime import datetime
from functools import partial
from multiprocessing import Lock

import matplotlib.pyplot as plt

from src.visual.PrologRepositorio import PrologRepositorio
from src.visual.QtHelper import *
from src.visual.ShVistaPlanta import ShVistaPlanta
from src.visual.info_casa import CasaInfo
from src.visual.resource_locator import *
# noinspection PyMethodMayBeStatic
from src.visual.vista_consumo import VistaConsumo


class ShHome:
    def __init__(self):
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
        self.ventana_vista_consumo = None
        self.vista_consumo = None
        self.ventana_ajustes = None
        self.vista_ajustes = None

        # Configurables
        self.resolucion = (800, 600)
        self.btn_offset = (150, 200)
        self.panel_dinamico_offset = (330, 10)
        self.cantidad_paneles = 4

        # Prolog instance
        self.prolog = PrologRepositorio()
        self.cantidad_plantas = len(self.prolog.plantas)

    def abrir_panel_status(self):
        self.ventana_ajustes = QtWidgets.QMainWindow()
        self.vista_ajustes = CasaInfo()
        self.vista_ajustes.setupUi(self.ventana_ajustes)
        self.ventana_ajustes.show()

    def abrir_panel_reportes(self):
        self.ventana_vista_consumo = QtWidgets.QMainWindow()
        self.vista_consumo = VistaConsumo()
        self.vista_consumo.setupUi(self.ventana_vista_consumo)
        self.ventana_vista_consumo.show()

    def abrir_contenido_planta(self, planta):
        print(planta.nombre)
        self.ventana_vista_planta = QtWidgets.QMainWindow()
        self.vista_planta = ShVistaPlanta(planta)
        self.vista_planta.setupUi(self.ventana_vista_planta)
        self.ventana_vista_planta.show()

    def generar_reporte_consumo_electrico(self):
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = []
        y_appender = y.append
        for element in x:
            consumo = self.prolog.get_consumo_electrico_por_fecha(element, datetime.today().year)
            y_appender(consumo)
        plt.plot(x, y)
        plt.xlabel('Meses')
        plt.ylabel('Consumo( ' + self.prolog.get_unidad_electrica() + ')')
        plt.xticks(x, meses)
        plt.show()

    def generar_reporte_consumo_agua(self):
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = []
        y_appender = y.append
        for element in x:
            consumo = self.prolog.get_consumo_agua_por_fecha(element, datetime.today().year)
            y_appender(consumo)
        plt.plot(x, y)
        plt.xlabel('Meses')
        plt.ylabel('Consumo( ' + self.prolog.get_unidad_agua() + ')')
        plt.xticks(x, meses)
        plt.show()

    def modo_eco(self):
        self.prolog.ahorro_recursos()

    def cabeceraVentana(self):
        pass
        # Labels de la cabecera de la ventana ShHome
        lbl_estado = crear_label(self.scroll_area_contents, "Dashboard", self.fuente_titulos, 50, 35)
        lbl_img_estado = crear_img(self.scroll_area_contents, "assets/reportes.png", 10, 30)
        lbl_plantas = crear_label(self.scroll_area_contents, "Plantas de su Casa", self.fuente_titulos, 50, 270)
        lbl_img_planta = crear_img(self.scroll_area_contents, "assets/casa.png", 10, 265)

        # Botones de la cabecera de la ventana ShHome
        btn_reportes = crear_boton_ico(self.scroll_area_contents, REPORTES_ICON, "Consumo",
                                       partial(self.abrir_panel_reportes), self.fuente_botones, 10, 90, 150, 50)

        btn_eco = crear_boton_ico(self.scroll_area_contents, ECO_ICON, "Modo Eco",
                                  partial(self.modo_eco), self.fuente_botones, 10, 170, 150, 50)

        btn_reportes_status = crear_boton_ico(self.scroll_area_contents, AJUSTES_ICON, "Info/Ajustes",
                                              partial(self.abrir_panel_status), self.fuente_botones, 200, 90, 150, 50)

        btn_elec = crear_boton_ico(self.scroll_area_contents, BOMBILLO_ENCENDIDO_ICON, "Reporte Luz",
                                   partial(self.generar_reporte_consumo_electrico),
                                   self.fuente_botones, 400, 90, 150, 50)

        btn_agua = crear_boton_ico(self.scroll_area_contents, GRAFICO_ICON, "Reporte Agua",
                                   partial(self.generar_reporte_consumo_agua), self.fuente_botones, 600, 90, 150, 50)

        self._labels(lbl_estado)
        self._labels(lbl_plantas)
        self._labels(lbl_img_estado)
        self._labels(lbl_img_planta)
        self._botones(btn_reportes)
        self._botones(btn_reportes_status)

    def generar_plantas_disponibles(self):
        if self.cantidad_plantas > self.cantidad_paneles * 2 + 1:
            self.scroll_area_contents.setFixedSize(800, 600 + self.cantidad_plantas * 20)
            self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # Creación de las plantas dinámicas
        initial_left_pos = self.panel_dinamico_offset[1]
        initial_top_pos = self.panel_dinamico_offset[0]
        cnt_plantas = 0
        for i in self.prolog.plantas:
            cnt_plantas += 1
            if cnt_plantas > self.cantidad_paneles:
                initial_left_pos = 10
                initial_top_pos += self.btn_offset[0]
                cnt_plantas = 1
            btn_planta = crear_boton_ico(self.scroll_area_contents, PLANTA_ICON, i.nombre,
                                         partial(self.abrir_contenido_planta, i), self.fuente_botones, initial_left_pos,
                                         initial_top_pos, 150, 100)
            initial_left_pos += self.btn_offset[1]
            self._botones(btn_planta)

    def setupUi(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.fuente_titulos = crear_fuente("Consolas", 16, es_negrita=True)
        self.fuente_botones = crear_fuente("Consolas", 12, es_negrita=False)
        self.ventana_principal.resize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setFixedSize(self.resolucion[0], self.resolucion[1])
        self.ventana_principal.setWindowTitle("Prolog Smart House")
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
        self.generar_plantas_disponibles()
