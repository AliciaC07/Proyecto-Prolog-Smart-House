:-dynamic estado_objeto/2.
:-dynamic persona/2.
:-dynamic miembro_casa/1.
:-dynamic ubicacion_persona/2.
:-dynamic lugar/3.

% La idea es describir un electrodomestico cualquiera de la casa
% con su consumo en khw. Como se puede tener varios electrodomesticos,
% describirlos como un identificador fuese lo correcto.
% electrodomestico(identificador, nombre, consumo/khw, identificador_lugar)
electrodomestico(1, nevera, 662, 4).
electrodomestico(2, estufa, 1000, 4).
electrodomestico(3, television, 263, 1).
electrodomestico(4, bombillo, 0.06, 1).
electrodomestico(5, computadora, 0.450, 1).
electrodomestico(6, nevera, 662, 5).
electrodomestico(7, nevera, 700, 5).
electrodomestico(8, abanico, 0.9, 1).
electrodomestico(9, lavadora, 255, 7).
electrodomestico(10, lavaplatos, 246, 4).

% La idea es describir si el electrodomestico esta encendido o no.
% Con esto, se puede calcular el consumo de khw, que se tiene actual.
% estado_electrodomestico(identificador, estado/on/off)
estado_electrodomestico(1, on).
estado_electrodomestico(2, on).
estado_electrodomestico(3, on).
estado_electrodomestico(4, on).
estado_electrodomestico(5, on).
estado_electrodomestico(6, on).
estado_electrodomestico(7, on).
estado_electrodomestico(8, on).
estado_electrodomestico(9, off).

%Escificar los objetos para el consumo de agua
%objeto_agua(identificador, nombre, consumo(litros de agua))
objeto_agua(1, toilet, 6.05).
objeto_agua(2, fregadero, 88.8).
objeto_agua(3, lavadora, 47).
objeto_agua(4, lavaplatos, 12).

% La idea es describir el lugar con un identificador y el nombre
% donde esta ubicado.
% lugar(identificador, nombre, temperatura/celsius).
lugar(1, sala, 28).
lugar(2, comedor, 29).
lugar(3, comedor, 30).
lugar(4, cocina, 31.3).
lugar(5, cocina, 32.5).
lugar(6, baño, 30).
lugar(7, cuarto_lavado, 31).

% La idea es describir el objeto con un identificador, nombre
% y el identificador del lugar donde esta ubicado.
% lugar(identificador, nombre, id_lugar).
objeto(1, puerta, 1).
objeto(2, puerta, 1).
objeto(3, puerta, 1).
objeto(4, puerta, 1).

% La idea es describir si el objeto esta abierto o cerrado.
% estado_objeto(identificador, estado/abierto/cerrado)
estado_objeto(1, abierto).
estado_objeto(2, abierto).
estado_objeto(3, abierto).
estado_objeto(4, abierto).

%Se tiene la persona de la familia
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
ubicacion_persona(1, roberto).
ubicacion_persona(3, nicole).
ubicacion_persona(1, papotico).

% Pregunta tipo monitoreo:
% Calcular cuantos KW/H esta consumiendo la casa actualmente
calcular_consumo_actual(Consumo_Total):-
    findall(Consumo, (lugar(IdLugar, _, _),electrodomestico(IdElec, _, Consumo, IdLugar),estado_electrodomestico(IdElec, on)), Consumos),
    sum_list(Consumos, Consumo_Total).


cerrar_puertas():-
    ubicacion_persona(IdLugar),objeto(IdObjeto, _, IdLugar),estado_objeto(IdObjeto, abierto),
    retract(estado_objeto(IdObjeto, abierto)),
    assertz(estado_objeto(IdObjeto, cerrado)).