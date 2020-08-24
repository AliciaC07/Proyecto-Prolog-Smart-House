# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detalleobjeto.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from functools import partial

from PyQt5 import QtCore, QtWidgets

from src.modelo.Objetos import Objeto
from src.visual.Helper import determinar_icono_objeto
from src.visual.PrologRepositorio import PrologRepositorio
from src.visual.QtHelper import set_img_to_label


class ShDetalleObjetoElectrico(object):

    def __init__(self, objeto):
        self.objeto = objeto
        self.prologRepository = PrologRepositorio()

    def setupUi(self, dialogo_objeto):
        dialogo_objeto.setObjectName("dialogo_objeto")
        dialogo_objeto.resize(501, 285)
        self.label = QtWidgets.QLabel(dialogo_objeto)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialogo_objeto)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialogo_objeto)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label_3.setObjectName("label_3")
        self.btn_encender = QtWidgets.QPushButton(dialogo_objeto)
        self.btn_encender.setGeometry(QtCore.QRect(130, 220, 101, 41))
        self.btn_encender.setObjectName("btn_encender")
        self.btn_apagar = QtWidgets.QPushButton(dialogo_objeto)
        self.btn_apagar.setGeometry(QtCore.QRect(20, 220, 101, 41))
        self.btn_apagar.setObjectName("btn_apagar")
        self.img_objeto = QtWidgets.QLabel(dialogo_objeto)
        self.img_objeto.setGeometry(QtCore.QRect(310, 40, 161, 131))
        self.img_objeto.setText("")
        self.img_objeto.setObjectName("img_objeto")
        self.label_4 = QtWidgets.QLabel(dialogo_objeto)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialogo_objeto)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dialogo_objeto)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lbl_nombre = QtWidgets.QLabel(dialogo_objeto)
        self.lbl_nombre.setGeometry(QtCore.QRect(130, 20, 81, 16))
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_tipo = QtWidgets.QLabel(dialogo_objeto)
        self.lbl_tipo.setGeometry(QtCore.QRect(130, 50, 61, 16))
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.lbl_estado = QtWidgets.QLabel(dialogo_objeto)
        self.lbl_estado.setGeometry(QtCore.QRect(130, 80, 61, 16))
        self.lbl_estado.setObjectName("lbl_estado")
        self.lbl_consumo_electrico = QtWidgets.QLabel(dialogo_objeto)
        self.lbl_consumo_electrico.setGeometry(QtCore.QRect(130, 140, 121, 16))
        self.lbl_consumo_electrico.setObjectName("lbl_consumo_electrico")
        self.lbl_consumo_agua = QtWidgets.QLabel(dialogo_objeto)
        self.lbl_consumo_agua.setGeometry(QtCore.QRect(130, 170, 111, 16))
        self.lbl_consumo_agua.setObjectName("lbl_consumo_agua")

        self.retranslateUi(dialogo_objeto)
        QtCore.QMetaObject.connectSlotsByName(dialogo_objeto)
        self.iniciar()
        self.llenar_datos()
        self.btn_encender.clicked.connect(partial(self.encender))
        self.btn_apagar.clicked.connect(partial(self.apagar))

        # Aparte hay que crear el boton de uso para electrodomesticos que son de un uso:
        # por ejemplo:
        # Si es continuo, pues no hay que agregar el boton.
        # pero si es de un uso, hay que agregarlo.
        print(self.objeto.nombre)

    def encender(self):
        self.btn_apagar.setDisabled(False)
        self.btn_encender.setDisabled(True)
        self.lbl_consumo_agua.setStyleSheet("color: green")
        self.lbl_consumo_electrico.setStyleSheet("color: green")
        self.prologRepository.encender_electrodomestico(self.objeto)
        self.lbl_estado.setText(self.prologRepository.obtener_estado_electrodomestico(self.objeto))

    def apagar(self):
        self.btn_apagar.setDisabled(True)
        self.btn_encender.setDisabled(False)
        self.lbl_consumo_agua.setStyleSheet("color: red")
        self.lbl_consumo_electrico.setStyleSheet("color: red")
        self.prologRepository.apagar_electrodomestico(self.objeto)
        self.lbl_estado.setText(self.prologRepository.obtener_estado_electrodomestico(self.objeto))

    def iniciar(self):
        if self.prologRepository.obtener_estado_electrodomestico(self.objeto) == "apagado":
            self.btn_apagar.setDisabled(True)
            self.btn_encender.setDisabled(False)
            self.lbl_consumo_agua.setStyleSheet("color: red")
            self.lbl_consumo_electrico.setStyleSheet("color: red")
        else:
            self.btn_apagar.setDisabled(False)
            self.btn_encender.setDisabled(True)
            self.lbl_consumo_agua.setStyleSheet("color: green")
            self.lbl_consumo_electrico.setStyleSheet("color: green")

    def llenar_datos(self):
        self.lbl_nombre.setText(self.objeto.nombre)
        self.lbl_estado.setText(self.prologRepository.obtener_estado_electrodomestico(self.objeto))
        self.lbl_tipo.setText(self.objeto.naturaleza)
        self.lbl_consumo_electrico.setText(str(self.objeto.unidad + ' ' + self.prologRepository.get_unidad_electrica()))
        self.lbl_consumo_agua.setText("N/A")
        set_img_to_label(self.img_objeto, determinar_icono_objeto(self.objeto))

    def retranslateUi(self, dialogo_objeto):
        _translate = QtCore.QCoreApplication.translate
        dialogo_objeto.setWindowTitle(_translate("dialogo_objeto", "Detalle Objeto"))
        self.label.setText(_translate("dialogo_objeto", "Nombre:"))
        self.label_2.setText(_translate("dialogo_objeto", "Tipo:"))
        self.label_3.setText(_translate("dialogo_objeto", "Consumo:"))
        self.btn_encender.setText(_translate("dialogo_objeto", "Encender"))
        self.btn_apagar.setText(_translate("dialogo_objeto", "Apagar"))
        self.label_4.setText(_translate("dialogo_objeto", "Electrico:"))
        self.label_5.setText(_translate("dialogo_objeto", "Agua:"))
        self.label_6.setText(_translate("dialogo_objeto", "Estado:"))
        self.lbl_nombre.setText(_translate("dialogo_objeto", "Valor Nombre"))
        self.lbl_tipo.setText(_translate("dialogo_objeto", "Tipo Nombre"))
        self.lbl_estado.setText(_translate("dialogo_objeto", "Valor Estado"))
        self.lbl_consumo_electrico.setText(_translate("dialogo_objeto", "Valor Consumo Electrico"))
        self.lbl_consumo_agua.setText(_translate("dialogo_objeto", "Valor Consumo Agua"))


if __name__ == "__main__":
    import sys
    objeto = Objeto("bombillo1", ["electrodomestico"], 0.06, 0, "Bombillo")
    app = QtWidgets.QApplication(sys.argv)
    dialogo_objeto = QtWidgets.QDialog()
    ui = ShDetalleObjetoElectrico(objeto)
    ui.setupUi(dialogo_objeto)
    dialogo_objeto.show()
    sys.exit(app.exec_())
