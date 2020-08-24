# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from src.visual.PrologRepositorio import PrologRepositorio
import src.visual.configuracion as config


class CasaInfo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 350)
        Dialog.setFixedSize(658, 350)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 150, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(280, 150, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(280, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(280, 210, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lbl_nombre = QtWidgets.QLabel(Dialog)
        self.lbl_nombre.setGeometry(QtCore.QRect(100, 120, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_direccion = QtWidgets.QLabel(Dialog)
        self.lbl_direccion.setGeometry(QtCore.QRect(100, 150, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_direccion.setFont(font)
        self.lbl_direccion.setObjectName("lbl_direccion")
        self.lbl_latitud = QtWidgets.QLabel(Dialog)
        self.lbl_latitud.setGeometry(QtCore.QRect(100, 180, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_latitud.setFont(font)
        self.lbl_latitud.setObjectName("lbl_latitud")
        self.lbl_longitud = QtWidgets.QLabel(Dialog)
        self.lbl_longitud.setGeometry(QtCore.QRect(100, 210, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_longitud.setFont(font)
        self.lbl_longitud.setObjectName("lbl_longitud")
        self.lbl_unidad_agua = QtWidgets.QLabel(Dialog)
        self.lbl_unidad_agua.setGeometry(QtCore.QRect(410, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_unidad_agua.setFont(font)
        self.lbl_unidad_agua.setObjectName("lbl_unidad_agua")
        self.lbl_unidad_electricidad = QtWidgets.QLabel(Dialog)
        self.lbl_unidad_electricidad.setGeometry(QtCore.QRect(410, 150, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_unidad_electricidad.setFont(font)
        self.lbl_unidad_electricidad.setObjectName("lbl_unidad_electricidad")
        self.lbl_costo_agua = QtWidgets.QLabel(Dialog)
        self.lbl_costo_agua.setGeometry(QtCore.QRect(410, 180, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_costo_agua.setFont(font)
        self.lbl_costo_agua.setObjectName("lbl_costo_agua")
        self.lbl_costo_luz = QtWidgets.QLabel(Dialog)
        self.lbl_costo_luz.setGeometry(QtCore.QRect(410, 210, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_costo_luz.setFont(font)
        self.lbl_costo_luz.setObjectName("lbl_costo_luz")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(10, 260, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.chk_box_eco = QtWidgets.QCheckBox(Dialog)
        self.chk_box_eco.setGeometry(QtCore.QRect(20, 300, 601, 17))
        self.chk_box_eco.setObjectName("chk_box_eco")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.prolog = PrologRepositorio()
        info = self.prolog.get_info_casa()
        self.lbl_nombre.setText(str(info[0]))
        self.lbl_direccion.setText(str(info[1]))
        self.lbl_latitud.setText("N/A")
        self.lbl_longitud.setText("N/A")
        self.lbl_unidad_agua.setText(str(info[4]))
        self.lbl_costo_agua.setText(str(info[5]))
        self.lbl_unidad_electricidad.setText(str(info[6]))
        self.lbl_costo_luz.setText(str(info[7]))
        self.init_view()
        self.chk_box_eco.stateChanged.connect(self.cambiar_estado)

    def init_view(self):
        self.chk_box_eco.setChecked(config.MODO_ECO)

    def cambiar_estado(self, state):
        if state == QtCore.Qt.Checked:
            config.MODO_ECO = True
        else:
            config.MODO_ECO = False
        print(config.MODO_ECO)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Prolog Smart House v1.0"))
        self.label_3.setText(_translate("Dialog", "Datos Principales:"))
        self.label_4.setText(_translate("Dialog", "Nombre:"))
        self.label_8.setText(_translate("Dialog", "Dirección:"))
        self.label_9.setText(_translate("Dialog", "Latitud:"))
        self.label_10.setText(_translate("Dialog", "Longitud:"))
        self.label_5.setText(_translate("Dialog", "Unidad Agua:"))
        self.label_6.setText(_translate("Dialog", "Unidad Electricidad:"))
        self.label_7.setText(_translate("Dialog", "Costo Agua:"))
        self.label_11.setText(_translate("Dialog", "Costo Luz:"))
        self.lbl_nombre.setText(_translate("Dialog", "Nombre de la casa"))
        self.lbl_direccion.setText(_translate("Dialog", "Direccion de la casa"))
        self.lbl_latitud.setText(_translate("Dialog", "Latitud de la casa"))
        self.lbl_longitud.setText(_translate("Dialog", "Longitud de la casa"))
        self.lbl_unidad_agua.setText(_translate("Dialog", "Unidad Agua de la casa"))
        self.lbl_unidad_electricidad.setText(_translate("Dialog", "Unidad Agua de la casa"))
        self.lbl_costo_agua.setText(_translate("Dialog", "Unidad Agua de la casa"))
        self.lbl_costo_luz.setText(_translate("Dialog", "Unidad Agua de la casa"))
        self.label_20.setText(_translate("Dialog", "Opciones:"))
        self.chk_box_eco.setText(_translate("Dialog", "Modo ECO (Cuando no haya personas en un lugar, la casa cerrará automáticamente todo lo que consuma en ese lugar."))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
