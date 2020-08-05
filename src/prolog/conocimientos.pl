:- dynamic lugar/3.
:- dynamic planta/2.
:- dynamic electrodomestico/2.
:- dynamic objeto_agua/2.
:- dynamic estado_electrodomestico/2.
:- dynamic objeto/2.
:- dynamic estado_objeto/2.
:- dynamic persona/2.
:- dynamic miembro_casa/1.
:- dynamic invitado/1.

% planta(nombre_planta, lista_lugares)
planta(planta1, [sala1, comedor1, cocina1, bano1, cuarto_lavado1]).

% Los distintos lugares y salas de las casas
% lugar(nombre, temperatura/celsius, lista_objetos).
lugar(sala1, 28, [television1, television2, bombillo1, bombillo2, computadora1, abanico1]).
lugar(comedor1, 29, [bombillo3, abanico2]).
lugar(cocina1, 30, [nevera1, estufa1, bombillo4, lavaplatos1]).
lugar(bano1, 30, [bombillo5]).
lugar(cuarto_lavado1, 30, [lavadora1, lavadora2, bombillo5]).
lugar(habitacion1, 30, [television3, computadora2, computadora3, abanico3]).


% La idea es describir un estado_electrodomestico cualquiera de la casa
% con su consumo en khw.
% estado_electrodomestico(identificador, nombre, consumo/khw, identificador_lugar)
electrodomestico(nevera1, 662).
electrodomestico(estufa1, 1000).
electrodomestico(television1, 263).
electrodomestico(television2, 263).
electrodomestico(television3, 263).
electrodomestico(bombillo1, 0.06).
electrodomestico(bombillo2, 0.06).
electrodomestico(bombillo3, 0.06).
electrodomestico(bombillo4, 0.06).
electrodomestico(bombillo5, 0.06).
electrodomestico(computadora1, 0.450).
electrodomestico(computadora2, 0.450).
electrodomestico(computadora3, 0.450).
electrodomestico(abanico1, 0.9).
electrodomestico(abanico2, 0.9).
electrodomestico(abanico3, 0.9).
electrodomestico(lavadora1, 255).
electrodomestico(lavadora2, 255).
electrodomestico(lavaplatos1, 246).

%Objetos de agua
objeto_agua(toilet1, 6.05).
objeto_agua(fregadero1, 88.8).
objeto_agua(lavadora1, 47).
objeto_agua(lavadora2, 47).
objeto_agua(lavaplatos1, 12).

% estado_electrodomestico(dispositivo, estado/encendido/apagado)
estado_electrodomestico(nevera1, encendido).
estado_electrodomestico(estufa1, encendido).
estado_electrodomestico(television1, encendido).
estado_electrodomestico(television2, encendido).
estado_electrodomestico(television3, encendido).
estado_electrodomestico(bombillo1, encendido).
estado_electrodomestico(bombillo2, encendido).
estado_electrodomestico(bombillo3, encendido).
estado_electrodomestico(bombillo4, encendido).
estado_electrodomestico(bombillo5, encendido).
estado_electrodomestico(computadora1, encendido).
estado_electrodomestico(computadora2, encendido).
estado_electrodomestico(computadora3, encendido).
estado_electrodomestico(abanico1, encendido).
estado_electrodomestico(abanico2, encendido).
estado_electrodomestico(abanico3, encendido).
estado_electrodomestico(lavadora1, encendido).
estado_electrodomestico(lavadora2, encendido).
estado_electrodomestico(lavaplatos1, encendido).

% La idea es describir el objeto con un identificador, nombre
% y el identificador del lugar donde esta ubicado.
% lugar(identificador, nombre, id_lugar).
objeto(puerta1, sala1).
objeto(puerta2, habitacion1).
objeto(puerta3, cocina1).
objeto(puerta4, bano1).
objeto(puerta5, cuarto_lavado1).
objeto(venatana1, habitacion1).
objeto(ventana2, sala1).
objeto(ventana3, cocina1).

% La idea es describir si el objeto esta abierto o cerrado.
% estado_objeto(identificador, estado/abierto/cerrado)
estado_objeto(puerta1, abierto).
estado_objeto(puerta2, abierto).
estado_objeto(puerta3, abierto).
estado_objeto(puerta4, cerrado).
estado_objeto(puerta5, cerrado).
estado_objeto(ventana1, cerrado).
estado_objeto(ventana2, abierto).
estado_objeto(ventana3, cerrado).

%Especificacion de las personas que entran a la casa.
%persona(nombre_persona, estado(despierto,fuera,durmiendo))
persona(roberto, despierto).
persona(nicole, despierto).
persona(papotico, despierto).

%especifica si es un miembro de la casa o no
%miembro_casa(persona)
miembro_casa(roberto).
miembro_casa(nicole).

%Especifica si es un invitado y no un miembro de la casa
%invitado(persona)
invitado(papotico).

%Ubicacion de la persona en la casa
%ubicacion_persona(lugar, persona)
ubicacion_persona(sala1, roberto).
ubicacion_persona(comedor1, nicole).
ubicacion_persona(sala1, papotico).

calcula_consumo([], 0).
calcula_consumo([H|T], Total):-
    electrodomestico(H, Consumo),
    calcula_consumo(T, TotalFuturo),
    Total is (TotalFuturo + Consumo).

calcular_consumo_electrico(Lugar, Consumo):-
    lugar(Lugar, _, Objetos),
    calcula_consumo(Objetos, Consumo).
