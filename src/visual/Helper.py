from src.visual.resource_locator import *
from src.visual.PrologRepositorio import PrologRepositorio

ELECTRODOMESTICO_AGUA = 1
ELECTRODOMESTICO = 2
AGUA = 3
CONTUNDENTE = 4

prolog = PrologRepositorio()


def determinar_tipo_objeto(objeto):
    if prolog.es_electrodomestico(objeto) and prolog.es_objeto_agua(objeto):
        return ELECTRODOMESTICO_AGUA
    elif prolog.es_electrodomestico(objeto):
        return ELECTRODOMESTICO
    elif prolog.es_objeto_agua(objeto):
        return AGUA
    else:
        return CONTUNDENTE


def determinar_icono_objeto(objeto):
    if objeto.naturaleza == "Nevera":
        return NEVERA_ICON
    if objeto.naturaleza == "Estufa":
        return ESTUFA_ICON
    if objeto.naturaleza == "Abanico":
        return ABANICO_ICON
    if objeto.naturaleza == "Bombillo":
        return BOMBILLO_ENCENDIDO_ICON
    if objeto.naturaleza == "Puerta":
        return PUERTA_ICON
    if objeto.naturaleza == "Ventana":
        return VENTANA_ICON
    if objeto.naturaleza == "Lavadora":
        return LAVADORA_ICON
    if objeto.naturaleza == "Toilet":
        return TOILET_ICON
    if objeto.naturaleza == "Lavaplatos":
        return LAVAPLATOS_ICON
    if objeto.naturaleza == "Lavamanos":
        return LAVAMANOS_ICON


def objeto_naturaleza_tipo(objeto):
    if objeto.naturaleza == "Nevera":
        return ELECTRODOMESTICO
    elif objeto.naturaleza == "Estufa":
        return ELECTRODOMESTICO
    elif objeto.naturaleza == "Abanico":
        return ELECTRODOMESTICO
    elif objeto.naturaleza == "Bombillo":
        return ELECTRODOMESTICO
    elif objeto.naturaleza == "Puerta":
        return CONTUNDENTE
    elif objeto.naturaleza == "Ventana":
        return CONTUNDENTE
    elif objeto.naturaleza == "Lavadora":
        return ELECTRODOMESTICO_AGUA
    elif objeto.naturaleza == "Toilet":
        return AGUA
    elif objeto.naturaleza == "Lavaplatos":
        return ELECTRODOMESTICO_AGUA


def determinar_icono_lugar(lugar):
    if lugar.tipo == "Sala":
        return SALA_ICON
    if lugar.tipo == "Comedor":
        return COMEDOR_ICON
    if lugar.tipo == "Habitacion":
        return HABITACION_ICON
    if lugar.tipo == "Bano":
        return DUCHA_ICON
    if lugar.tipo == "Garaje":
        return GARAJE_ICON
    if lugar.tipo == "Cocina":
        return COCINA_ICON
