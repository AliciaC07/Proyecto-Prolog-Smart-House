# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from src.modelo.Lugar import Lugar
from src.modelo.Objetos import Objeto
from src.modelo.Planta import Planta
from src.visual.PrologRepositorio import PrologRepositorio
from src.visual.app.ShHome import ShHome


class Ui_ventanaPrincipalDesigner(object):
    def __init__(self):
        self.prolog = PrologRepositorio()
        self.ventana_app = None
        self.app = None

    def setupUi(self, ventanaPrincipalDesigner):
        ventanaPrincipalDesigner.setObjectName("ventanaPrincipalDesigner")
        ventanaPrincipalDesigner.resize(983, 906)
        self.centralwidget = QtWidgets.QWidget(ventanaPrincipalDesigner)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTituloVentana = QtWidgets.QLabel(self.centralwidget)
        self.labelTituloVentana.setGeometry(QtCore.QRect(270, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTituloVentana.setFont(font)
        self.labelTituloVentana.setObjectName("labelTituloVentana")
        self.labelNombreCasa_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelNombreCasa_2.setGeometry(QtCore.QRect(10, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelNombreCasa_2.setFont(font)
        self.labelNombreCasa_2.setObjectName("labelNombreCasa_2")
        self.inputNombreCasa = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNombreCasa.setGeometry(QtCore.QRect(150, 80, 211, 21))
        self.inputNombreCasa.setObjectName("inputNombreCasa")
        self.labelPlanta = QtWidgets.QLabel(self.centralwidget)
        self.labelPlanta.setGeometry(QtCore.QRect(10, 230, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPlanta.setFont(font)
        self.labelPlanta.setObjectName("labelPlanta")
        self.btnAgregarPlanta = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarPlanta.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.btnAgregarPlanta.setObjectName("btnAgregarPlanta")
        self.btnRemoverPlanta = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoverPlanta.setGeometry(QtCore.QRect(230, 260, 71, 23))
        self.btnRemoverPlanta.setObjectName("btnRemoverPlanta")
        self.lwPlantas = QtWidgets.QListWidget(self.centralwidget)
        self.lwPlantas.setGeometry(QtCore.QRect(10, 290, 451, 192))
        self.lwPlantas.setObjectName("lwPlantas")
        self.labelLugares = QtWidgets.QLabel(self.centralwidget)
        self.labelLugares.setGeometry(QtCore.QRect(530, 225, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelLugares.setFont(font)
        self.labelLugares.setObjectName("labelLugares")
        self.btnAgregarLugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarLugar.setGeometry(QtCore.QRect(680, 260, 75, 23))
        self.btnAgregarLugar.setObjectName("btnAgregarLugar")
        self.lwLugares = QtWidgets.QTableWidget(self.centralwidget)
        self.lwLugares.setGeometry(QtCore.QRect(530, 290, 301, 192))
        self.lwLugares.setMaximumSize(QtCore.QSize(301, 16777215))
        self.lwLugares.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.lwLugares.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lwLugares.setObjectName("lwLugares")
        self.lwLugares.setColumnCount(2)
        self.lwLugares.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lwLugares.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lwLugares.setHorizontalHeaderItem(1, item)
        self.lwLugares.horizontalHeader().setCascadingSectionResizes(False)
        self.lwLugares.horizontalHeader().setSortIndicatorShown(False)
        self.lwLugares.horizontalHeader().setStretchLastSection(True)
        self.lwLugares.verticalHeader().setCascadingSectionResizes(False)
        self.lwLugares.verticalHeader().setStretchLastSection(False)
        self.btnRemoverLugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoverLugar.setGeometry(QtCore.QRect(760, 260, 71, 23))
        self.btnRemoverLugar.setObjectName("btnRemoverLugar")
        self.btnAgregarObjeto = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarObjeto.setGeometry(QtCore.QRect(310, 580, 71, 23))
        self.btnAgregarObjeto.setObjectName("btnAgregarObjeto")
        self.lwObjetos = QtWidgets.QTableWidget(self.centralwidget)
        self.lwObjetos.setGeometry(QtCore.QRect(10, 610, 451, 191))
        self.lwObjetos.setObjectName("lwObjetos")
        self.lwObjetos.setColumnCount(2)
        self.lwObjetos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lwObjetos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lwObjetos.setHorizontalHeaderItem(1, item)
        self.lwObjetos.horizontalHeader().setStretchLastSection(True)
        self.lwObjetos.verticalHeader().setCascadingSectionResizes(False)
        self.btnRemoverObjeto = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoverObjeto.setGeometry(QtCore.QRect(390, 580, 71, 23))
        self.btnRemoverObjeto.setObjectName("btnRemoverObjeto")
        self.labelObjetos = QtWidgets.QLabel(self.centralwidget)
        self.labelObjetos.setGeometry(QtCore.QRect(10, 545, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelObjetos.setFont(font)
        self.labelObjetos.setObjectName("labelObjetos")
        self.labelCustomizacionHogar = QtWidgets.QLabel(self.centralwidget)
        self.labelCustomizacionHogar.setGeometry(QtCore.QRect(10, 180, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCustomizacionHogar.setFont(font)
        self.labelCustomizacionHogar.setObjectName("labelCustomizacionHogar")
        self.labelGeneral = QtWidgets.QLabel(self.centralwidget)
        self.labelGeneral.setGeometry(QtCore.QRect(10, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelGeneral.setFont(font)
        self.labelGeneral.setObjectName("labelGeneral")
        self.labelFamilia = QtWidgets.QLabel(self.centralwidget)
        self.labelFamilia.setGeometry(QtCore.QRect(530, 540, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFamilia.setFont(font)
        self.labelFamilia.setObjectName("labelFamilia")
        self.btnAgregarFamiliar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarFamiliar.setGeometry(QtCore.QRect(680, 580, 75, 23))
        self.btnAgregarFamiliar.setObjectName("btnAgregarFamiliar")
        self.lwFamiliares = QtWidgets.QListWidget(self.centralwidget)
        self.lwFamiliares.setGeometry(QtCore.QRect(530, 610, 301, 192))
        self.lwFamiliares.setObjectName("lwFamiliares")
        self.btnRemoverFamiliar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoverFamiliar.setGeometry(QtCore.QRect(760, 580, 71, 23))
        self.btnRemoverFamiliar.setObjectName("btnRemoverFamiliar")
        self.btnFinalizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnFinalizar.setGeometry(QtCore.QRect(850, 770, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnFinalizar.setFont(font)
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.inputFamiliar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFamiliar.setGeometry(QtCore.QRect(530, 580, 141, 20))
        self.inputFamiliar.setObjectName("inputFamiliar")
        self.labelUbicacion = QtWidgets.QLabel(self.centralwidget)
        self.labelUbicacion.setGeometry(QtCore.QRect(10, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelUbicacion.setFont(font)
        self.labelUbicacion.setObjectName("labelUbicacion")
        self.inputUbicacion = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUbicacion.setGeometry(QtCore.QRect(150, 110, 211, 21))
        self.inputUbicacion.setObjectName("inputUbicacion")
        self.inputUnidad = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUnidad.setGeometry(QtCore.QRect(130, 580, 81, 21))
        self.inputUnidad.setObjectName("inputUnidad")
        self.cbxLugares = QtWidgets.QComboBox(self.centralwidget)
        self.cbxLugares.setGeometry(QtCore.QRect(530, 260, 141, 22))
        self.cbxLugares.setObjectName("cbxLugares")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxLugares.addItem("")
        self.cbxObjetos = QtWidgets.QComboBox(self.centralwidget)
        self.cbxObjetos.setGeometry(QtCore.QRect(10, 580, 111, 22))
        self.cbxObjetos.setObjectName("cbxObjetos")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxObjetos.addItem("")
        self.cbxPlanta = QtWidgets.QComboBox(self.centralwidget)
        self.cbxPlanta.setGeometry(QtCore.QRect(10, 260, 131, 22))
        self.cbxPlanta.setObjectName("cbxPlanta")
        self.cbxPlanta.addItem("")
        self.cbxPlanta.addItem("")
        self.labelUbicacion_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelUbicacion_2.setGeometry(QtCore.QRect(450, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelUbicacion_2.setFont(font)
        self.labelUbicacion_2.setObjectName("labelUbicacion_2")
        self.labelUbicacion_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelUbicacion_3.setGeometry(QtCore.QRect(450, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelUbicacion_3.setFont(font)
        self.labelUbicacion_3.setObjectName("labelUbicacion_3")
        self.cbxUnidadacuatica = QtWidgets.QComboBox(self.centralwidget)
        self.cbxUnidadacuatica.setGeometry(QtCore.QRect(530, 80, 181, 22))
        self.cbxUnidadacuatica.setObjectName("cbxUnidadacuatica")
        self.cbxUnidadacuatica.addItem("")
        self.cbxUnidadacuatica.addItem("")
        self.cbxUnidadacuatica.addItem("")
        self.cbxUnidadelectrica = QtWidgets.QComboBox(self.centralwidget)
        self.cbxUnidadelectrica.setGeometry(QtCore.QRect(530, 110, 181, 22))
        self.cbxUnidadelectrica.setObjectName("cbxUnidadelectrica")
        self.cbxUnidadelectrica.addItem("")
        self.cbxUnidadelectrica.addItem("")
        self.cbxUnidadelectrica.addItem("")
        self.inputUnidadAgua = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUnidadAgua.setGeometry(QtCore.QRect(220, 580, 81, 21))
        self.inputUnidadAgua.setObjectName("inputUnidadAgua")
        ventanaPrincipalDesigner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventanaPrincipalDesigner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 26))
        self.menubar.setObjectName("menubar")
        ventanaPrincipalDesigner.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventanaPrincipalDesigner)
        self.statusbar.setObjectName("statusbar")
        ventanaPrincipalDesigner.setStatusBar(self.statusbar)
        # aqui empiezan los cambios
        self.retranslateUi(ventanaPrincipalDesigner)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipalDesigner)
        self.btnAgregarPlanta.clicked.connect(self.SetPlantas)
        self.btnRemoverPlanta.clicked.connect(self.RemovePlantas)
        self.btnAgregarLugar.clicked.connect(self.SetLugares)
        self.btnRemoverLugar.clicked.connect(self.RemoveLugares)
        self.btnAgregarObjeto.clicked.connect(self.SetObjetos)
        self.btnRemoverObjeto.clicked.connect(self.RemoveObjeto)
        self.btnAgregarFamiliar.clicked.connect(self.SetFamilias)
        self.btnRemoverFamiliar.clicked.connect(self.RemoveFamiliares)
        self.btnFinalizar.clicked.connect(self.InsertarEstructura)
        self.lwLugares.setSelectionBehavior(QTableWidget.SelectRows)
        self.lwObjetos.setSelectionBehavior(QTableWidget.SelectRows)

    contadorplanta = 1
    contadorLugar = 1
    contadorObjeto = 1
    plantas = []
    lugares = []
    fam = []
    tiposObjetos = {'Nevera': 'Electrodomestico', 'Estufa': 'Electrodomestico','Abanico': 'Electrodomestico','Bombillo': 'Electrodomestico'
               ,'Lavadora': 'Electrodomestico','Nevera': 'Electrodomestico','Toilet': 'Agua','Lavaplatos': 'Agua','Puerta': 'Contundente','Ventana': 'Contundente'}

    def retranslateUi(self, ventanaPrincipalDesigner):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipalDesigner.setWindowTitle(_translate("ventanaPrincipalDesigner", "Home Designer"))
        self.labelTituloVentana.setText(_translate("ventanaPrincipalDesigner", "Configuración  Inicial de su Casa"))
        self.labelNombreCasa_2.setText(_translate("ventanaPrincipalDesigner", "Nombre de su casa:"))
        self.labelPlanta.setText(_translate("ventanaPrincipalDesigner", "Plantas"))
        self.btnAgregarPlanta.setText(_translate("ventanaPrincipalDesigner", "Agregar"))
        self.btnRemoverPlanta.setText(_translate("ventanaPrincipalDesigner", "Remover"))
        self.labelLugares.setText(_translate("ventanaPrincipalDesigner", "Lugares"))
        self.btnAgregarLugar.setText(_translate("ventanaPrincipalDesigner", "Agregar"))
        item = self.lwLugares.horizontalHeaderItem(0)
        item.setText(_translate("ventanaPrincipalDesigner", "Lugar"))
        item = self.lwLugares.horizontalHeaderItem(1)
        item.setText(_translate("ventanaPrincipalDesigner", "Planta"))
        self.btnRemoverLugar.setText(_translate("ventanaPrincipalDesigner", "Remover"))
        self.btnAgregarObjeto.setText(_translate("ventanaPrincipalDesigner", "Agregar"))
        item = self.lwObjetos.horizontalHeaderItem(0)
        item.setText(_translate("ventanaPrincipalDesigner", "Objeto"))
        item = self.lwObjetos.horizontalHeaderItem(1)
        item.setText(_translate("ventanaPrincipalDesigner", "Lugar"))
        self.btnRemoverObjeto.setText(_translate("ventanaPrincipalDesigner", "Remover"))
        self.labelObjetos.setText(_translate("ventanaPrincipalDesigner", "Objetos"))
        self.labelCustomizacionHogar.setText(_translate("ventanaPrincipalDesigner", "Customización del Hogar"))
        self.labelGeneral.setText(_translate("ventanaPrincipalDesigner", "General"))
        self.labelFamilia.setText(_translate("ventanaPrincipalDesigner", "Familia"))
        self.btnAgregarFamiliar.setText(_translate("ventanaPrincipalDesigner", "Agregar"))
        self.btnRemoverFamiliar.setText(_translate("ventanaPrincipalDesigner", "Remover"))
        self.btnFinalizar.setText(_translate("ventanaPrincipalDesigner", "Finalizar"))
        self.inputFamiliar.setPlaceholderText(_translate("ventanaPrincipalDesigner", "Ingresar nombre del familiar"))
        self.labelUbicacion.setText(_translate("ventanaPrincipalDesigner", "Ubicación:"))

        self.inputUnidad.setPlaceholderText(_translate("ventanaPrincipalDesigner", "Electricidad"))

        self.inputNombreCasa.setPlaceholderText(_translate("ventanaPrincipalDesigner", "Nombre de la Casa"))
        self.inputUbicacion.setPlaceholderText(_translate("ventanaPrincipalDesigner", "Ubicacion"))
        self.cbxLugares.setItemText(0, _translate("ventanaPrincipalDesigner", "<Seleccione>"))
        self.cbxLugares.setItemText(1, _translate("ventanaPrincipalDesigner", "Sala"))
        self.cbxLugares.setItemText(2, _translate("ventanaPrincipalDesigner", "Comedor"))
        self.cbxLugares.setItemText(3, _translate("ventanaPrincipalDesigner", "Cocina"))
        self.cbxLugares.setItemText(4, _translate("ventanaPrincipalDesigner", "Habitacion"))
        self.cbxLugares.setItemText(5, _translate("ventanaPrincipalDesigner", "Bano"))
        self.cbxLugares.setItemText(6, _translate("ventanaPrincipalDesigner", "Garaje"))
        self.cbxObjetos.setItemText(0, _translate("ventanaPrincipalDesigner", "<Seleccione>"))
        self.cbxObjetos.setItemText(1, _translate("ventanaPrincipalDesigner", "Nevera"))
        self.cbxObjetos.setItemText(2, _translate("ventanaPrincipalDesigner", "Estufa"))
        self.cbxObjetos.setItemText(3, _translate("ventanaPrincipalDesigner", "Abanico"))
        self.cbxObjetos.setItemText(4, _translate("ventanaPrincipalDesigner", "Bombillo"))
        self.cbxObjetos.setItemText(5, _translate("ventanaPrincipalDesigner", "Puerta"))
        self.cbxObjetos.setItemText(6, _translate("ventanaPrincipalDesigner", "Ventana"))
        self.cbxObjetos.setItemText(7, _translate("ventanaPrincipalDesigner", "Lavadora"))
        self.cbxObjetos.setItemText(8, _translate("ventanaPrincipalDesigner", "Toilet"))
        self.cbxObjetos.setItemText(9, _translate("ventanaPrincipalDesigner", "Lavaplatos"))
        self.cbxPlanta.setItemText(0, _translate("ventanaPrincipalDesigner", "<Seleccione>"))
        self.cbxPlanta.setItemText(1, _translate("ventanaPrincipalDesigner", "Planta"))
        self.labelUbicacion_2.setText(_translate("ventanaPrincipalDesigner", "Agua:"))
        self.labelUbicacion_3.setText(_translate("ventanaPrincipalDesigner", "Electricidad:"))
        self.cbxUnidadacuatica.setItemText(0,
                                           _translate("ventanaPrincipalDesigner", "<Seleccione la unidad de medida>"))
        self.cbxUnidadacuatica.setItemText(1, _translate("ventanaPrincipalDesigner", "KWatt"))
        self.cbxUnidadacuatica.setItemText(2, _translate("ventanaPrincipalDesigner", "Watt"))
        self.cbxUnidadelectrica.setItemText(0,
                                            _translate("ventanaPrincipalDesigner", "<Seleccione la unidad de medida>"))
        self.cbxUnidadelectrica.setItemText(1, _translate("ventanaPrincipalDesigner", "Galones"))
        self.cbxUnidadelectrica.setItemText(2, _translate("ventanaPrincipalDesigner", "Litros"))

        self.cbxUnidadacuatica.setItemText(0,
                                           _translate("ventanaPrincipalDesigner", "<Seleccione la unidad de medida>"))
        self.cbxUnidadacuatica.setItemText(1, _translate("ventanaPrincipalDesigner", "Galones"))
        self.cbxUnidadacuatica.setItemText(2, _translate("ventanaPrincipalDesigner", "Litros"))
        self.cbxUnidadelectrica.setItemText(0,
                                            _translate("ventanaPrincipalDesigner", "<Seleccione la unidad de medida>"))
        self.cbxUnidadelectrica.setItemText(1, _translate("ventanaPrincipalDesigner", "KWatt"))
        self.cbxUnidadelectrica.setItemText(2, _translate("ventanaPrincipalDesigner", "Watt"))
        self.inputUnidadAgua.setPlaceholderText(_translate("ventanaPrincipalDesigner", "Agua"))

    def SetPlantas(self):
        if self.lwPlantas.__len__() < 4:
            if self.cbxPlanta.currentText() != "<Seleccione>":
                planta = Planta(self.cbxPlanta.currentText() + str(self.contadorplanta))
                self.lwPlantas.addItem(self.cbxPlanta.currentText() + str(self.contadorplanta))
                self.plantas.append(planta)
                self.contadorplanta += self.contadorplanta + random.randint(2, 10)
            else:
                error = QtWidgets.QErrorMessage()
                error.setWindowModality(QtCore.Qt.WindowModal)
                error.showMessage("Asegurese de que se seleccione una planta")
                error.setWindowTitle("Error")
                error.exec_()

    def RemovePlantas(self):
        listItems = self.lwPlantas.selectedItems()
        if not listItems: return
        for item in listItems:
            self.lwPlantas.takeItem(self.lwPlantas.row(item))
            itemplanta = item.text()
            for aux in self.plantas:
                if aux.nombre == item.text():
                    self.plantas.remove(aux)

        self.contadorplanta = self.contadorplanta - 1

    def SetLugares(self):
        listItems = self.lwPlantas.selectedItems()
        if listItems.__len__() < 1:
            error = QtWidgets.QErrorMessage()
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage("Asegurese de que se seleccione una planta")
            error.setWindowTitle("Error")
            error.exec_()
        else:
            if self.cbxLugares.currentText() != "<Seleccione>":
                lugar = Lugar(self.cbxLugares.currentText() + str(self.contadorLugar), self.cbxLugares.currentText())
                rowPosition = self.lwLugares.rowCount()
                self.lwLugares.insertRow(rowPosition)  # insert new row
                self.lwLugares.setItem(rowPosition, 0, QTableWidgetItem(lugar.nombre))
                itemplanta = ""
                if not listItems: return
                for item in listItems:
                    itemplanta = item.text()
                    for aux in self.plantas:
                        if aux.nombre == item.text():
                            aux.lugares.append(lugar)
                self.lwLugares.setItem(rowPosition, 1, QTableWidgetItem(itemplanta))
                self.contadorLugar += self.contadorLugar + random.randint(2, 10)
            else:
                error = QtWidgets.QErrorMessage()
                error.setWindowModality(QtCore.Qt.WindowModal)
                error.showMessage("Asegurese de que se seleccione un lugar para insertar")
                error.setWindowTitle("Error")
                error.exec_()

    def RemoveLugares(self):
        listItems = self.lwLugares.selectedItems()
        listItemsPlanta = self.lwPlantas.selectedItems()
        itemplanta = ""
        itemlugar = listItems[0].text()
        if not listItems: return
        for itemp in listItemsPlanta:
            itemplanta = itemp.text()

            self.lwLugares.removeRow(self.lwLugares.currentRow())

            for aux in self.plantas:
                if aux.nombre == itemplanta:
                    for aux1 in aux.lugares:
                        if aux1.nombre == itemlugar:
                            aux.lugares.remove(aux1)

            self.contadorLugar = self.contadorLugar - 1

    def GetAllPlantas(self, plantaselected, lugarselected):

        for aux in self.plantas:
            if aux.nombre == plantaselected:
                for aux1 in aux.lugares:
                    if aux1.nombre == lugarselected:
                        return aux1

    def SetObjetos(self):
        listItemsPlanta = self.lwPlantas.selectedItems()
        listItems = self.lwLugares.selectedItems()

        if listItems.__len__() < 1 and listItemsPlanta.__len__() < 1:
            error = QtWidgets.QErrorMessage()
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage("Asegurese de que se seleccione un lugar y su planta antes de borrar el objeto")
            error.setWindowTitle("Error")
            error.exec_()
        else:


            if self.cbxObjetos.currentText() != "<Seleccione>":
                if self.tiposObjetos[self.cbxObjetos.currentText()] == "Contundente":
                    self.inputUnidad.setDisabled(True)
                    self.inputUnidad.setText(str(0))
                    self.inputUnidadAgua.setDisabled(True)
                    self.inputUnidadAgua.setText(str(0))
                elif self.tiposObjetos[self.cbxObjetos.currentText()] == "Electrodomestico":
                    self.inputUnidadAgua.setDisabled(True)
                    self.inputUnidadAgua.setText(str(0))
                tipoO = []
                if self.cbxObjetos.currentText() == "Lavadora":
                    tipoO = ['Agua','Electrodomestico']
                else:
                    tipoO.append(self.tiposObjetos[self.cbxObjetos.currentText()])

                objeto = Objeto(self.cbxObjetos.currentText() + str(self.contadorObjeto), tipoO,
                                self.inputUnidad.text(), self.inputUnidadAgua.text())
                rowPosition = self.lwObjetos.rowCount()
                self.lwObjetos.insertRow(rowPosition)  # insert new row
                self.lwObjetos.setItem(rowPosition, 0, QTableWidgetItem(objeto.nombre))
                itemplanta = ""
                itemlugar = listItems[0].text()
                if not listItemsPlanta: return
                for itemp in listItemsPlanta:
                    itemplanta = itemp.text()

                    self.lwLugares.row(listItems[0])

                    lugars = self.GetAllPlantas(itemplanta, itemlugar)
                    lugars.objetos.append(objeto)
                    self.lwObjetos.setItem(rowPosition, 1, QTableWidgetItem(itemlugar))
            else:
                error = QtWidgets.QErrorMessage()
                error.setWindowModality(QtCore.Qt.WindowModal)
                error.showMessage("Asegurese de que se seleccione un objeto y su tipo antes de agregar el objeto")
                error.setWindowTitle("Error")
                error.exec_()

            self.contadorObjeto += self.contadorObjeto + random.randint(2, 10)
            self.inputUnidad.clear()
            self.inputUnidadAgua.clear()
            self.inputUnidadAgua.setDisabled(False)

    def RemoveObjeto(self):
        listItems = self.lwObjetos.selectedItems()
        listItemsLugares = self.lwLugares.selectedItems()
        if listItems.__len__() < 1 and listItemsLugares.__len__() < 1:
            error = QtWidgets.QErrorMessage()
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage("Asegurese de que se seleccione un lugar y su planta antes de borrar el objeto")
            error.setWindowTitle("Error")
            error.exec_()
        else:
            ob = listItems[0].text()
            self.lwObjetos.removeRow(self.lwObjetos.currentRow())
            for aux in self.plantas:
                for itemsl in aux.lugares:
                    if itemsl.nombre == listItemsLugares[0].text():
                        for aux1 in itemsl.objetos:
                            if aux1.nombre == ob:
                                itemsl.objetos.remove(aux1)

            self.contadorObjeto = self.contadorObjeto - 1

    def SetFamilias(self):
        self.lwFamiliares.addItem(self.inputFamiliar.text())
        self.fam.append(self.inputFamiliar.text())
        self.inputFamiliar.clear()

    def RemoveFamiliares(self):
        listItems = self.lwFamiliares.selectedItems()
        if not listItems: return
        for item in listItems:
            self.lwFamiliares.takeItem(self.lwFamiliares.row(item))
            for aux in self.fam:
                if aux == item.text():
                    self.fam.remove(aux)

    # def validar(self):
    #     if self.cbxLugares.currentText() != "<Seleccionar>" and self.inputFamiliar.text() != "":
    #         return True
    #     return False

    def validar(self):
        for aux in self.plantas:
            if aux.lugares.__len__() < 1:
                print("debe de introducir lugares")
                return False
        return True

    def validar2(self):
        for aux in self.plantas:
            for aux1 in aux.lugares:
                if aux1.objetos.__len__() < 1:
                    print("debe de introducir objetos")
                    return False
        return True

    def abrir_casa(self):
        self.ventana_app = QtWidgets.QMainWindow()
        self.app = ShHome()
        self.app.setupUi(self.ventana_app)
        self.ventana_app.show()

    def InsertarEstructura(self):
        if self.validar() and self.validar2() and self.inputNombreCasa.text() != "" and self.inputUbicacion.text() != "" and self.cbxUnidadacuatica.currentText() != "<Seleccione la unidad de medida>" and self.cbxUnidadelectrica.currentText() != "<Seleccione la unidad de medida>":
            for aux in self.plantas:
                self.prolog.InsertPlanta(aux)
            for aux in self.fam:
                self.prolog.InsertPersons(aux)
            self.prolog.InsertInfoHouse(self.inputNombreCasa.text(), self.inputUbicacion.text(), self.plantas,
                                        self.cbxUnidadelectrica.currentText(), self.cbxUnidadacuatica.currentText())
            self.prolog.plantas = self.plantas
            self.clearAll()
            self.centralwidget.close()
            self.ventana_suprema.close()
            self.abrir_casa()
        else:
            error = QtWidgets.QErrorMessage()
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage("Asegurese de que llene todas las informaciones correspondientes")
            error.setWindowTitle("Error")
            error.exec_()

    def clearAll(self):
        self.lugares = []
        self.plantas = []
        self.fam = []
        self.lwLugares.clearContents()
        self.lwObjetos.clearContents()
        for aux in range(self.lwLugares.rowCount()):
            self.lwLugares.removeRow(aux)
        for aux in range(self.lwObjetos.rowCount()):
            self.lwObjetos.removeRow(aux)
        self.lwPlantas.clear()
        self.lwFamiliares.clear()
        for aux in range(self.lwLugares.rowCount()):
            self.lwLugares.removeRow(aux)
        for aux in range(self.lwObjetos.rowCount()):
            self.lwObjetos.removeRow(aux)
        self.inputUnidad.clear()
        self.inputUnidadAgua.clear()
        self.inputFamiliar.clear()
        self.inputUbicacion.clear()
        self.inputNombreCasa.clear()
        self.cbxUnidadelectrica.setCurrentIndex(0)
        self.cbxUnidadacuatica.setCurrentIndex(0)

        self.cbxPlanta.setCurrentIndex(0)
        self.cbxObjetos.setCurrentIndex(0)
        self.cbxLugares.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ventanaPrincipalDesigner = QtWidgets.QMainWindow()
    ui = Ui_ventanaPrincipalDesigner()
    ui.setupUi(ventanaPrincipalDesigner)
    ventanaPrincipalDesigner.show()
    sys.exit(app.exec_())
