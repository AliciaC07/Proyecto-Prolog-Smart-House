from PyQt5 import QtCore, QtWidgets, QtGui


def crear_fuente(familia, tamano, es_negrita):
    """
    Funcion auxiliar PyQT5 que nos permite crear una fuente
    para texto, dado su familia, tamaño y si viene en negrita.
    :param familia: Familia de la fuente, como un string.
    :param tamano: Tamaño de la fuente.
    :param es_negrita: Es negrita o no.
    :return: La fuente creada, como QFont()
    """
    font = QtGui.QFont()
    font.setPointSize(tamano)
    font.setFamily(familia)
    font.setBold(es_negrita)
    return font


def crear_label(widget_padre, texto, fuente, top, left):
    label = QtWidgets.QLabel(widget_padre)
    label.setFont(fuente)
    label.setText(texto)
    label.move(top, left)
    label.adjustSize()
    return label


def crear_img(widget_padre, dir_img, top, left):
    label_img = QtWidgets.QLabel(widget_padre)
    pixel_map = QtGui.QPixmap(dir_img)
    label_img.setPixmap(pixel_map)
    label_img.move(top, left)
    label_img.adjustSize()
    return label_img


def crear_boton(widget_padre, texto, funcion, fuente, top, left, width, height):
    btn = QtWidgets.QPushButton(widget_padre)
    btn.setFont(fuente)
    btn.setText(texto)
    btn.setGeometry(QtCore.QRect(top, left, width, height))
    btn.clicked.connect(funcion)


def crear_boton_ico(widget_padre, img_src, texto, funcion, fuente, top, left, width, height):
    btn = QtWidgets.QPushButton(widget_padre)
    btn.setFont(fuente)
    btn.setText(texto)
    btn.setGeometry(QtCore.QRect(top, left, width, height))
    btn.setIcon(QtGui.QIcon(img_src))
    btn.setIconSize(QtCore.QSize(32, 32))
    btn.clicked.connect(funcion)
    return btn


def set_img_to_label(label, img):
    pixel_map = QtGui.QPixmap(img)
    label.setPixmap(pixel_map)
    label.adjustSize()


def hacer_nada(self):
    print("Hago nada!!!")
