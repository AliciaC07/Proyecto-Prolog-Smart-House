:- dynamic lugar/3.
:- dynamic planta/2.
:- dynamic electrodomestico/2.
:- dynamic objeto_agua/3.
:- dynamic estado_electrodomestico/4.
:- dynamic objeto/3.
:- dynamic estado_objeto/2.
:- dynamic persona/2.
:- dynamic miembro_casa/1.
:- dynamic invitado/1.
:- dynamic casa_info/3.
:- dynamic unidad_electrica/1.
:- dynamic unidad_agua/1.
:- dynamic consumo_electrodomestico/4.
:- dynamic consumo_agua/4.
:- dynamic estado_objeto_agua/4.
:- dynamic consumo/7.

%casa_info(nombrecasa, ubicacion, [plantas])
% planta(nombre_planta, lista_lugares)
%planta(planta1, [sala1, comedor1, cocina1, bano1, cuarto_lavado1]).

% Los distintos lugares y salas de las casas
% lugar(nombre, temperatura/celsius, lista_objetos).
%lugar(sala1, 28, [television1, television2, bombillo1, bombillo2, computadora1, abanico1,puerta1]).
%lugar(comedor1, 29, [bombillo3, abanico2]).
%lugar(cocina1, 30, [nevera1, estufa1, bombillo4, lavaplatos1,puerta3]).
%lugar(bano1, 30, [bombillo5]).
%lugar(cuarto_lavado1, 30, [lavadora1, lavadora2, bombillo5]).
%lugar(habitacion1, 30, [television3, computadora2, computadora3, abanico3, puerta2]).

% La idea es describir un estado_electrodomestico cualquiera de la casa
% con su consumo en khw.
% estado_electrodomestico(nombre, consumo/khw)
%electrodomestico(nevera1, 662).
%electrodomestico(estufa1, 1000).
%electrodomestico(television1, 263).
%estado_electrodomestico(television1, apagado, date(0,0,0), time(0,0,0)).
%electrodomestico(television2, 263).
%%electrodomestico(television3, 263).
%electrodomestico(bombillo1, 1).
%estado_electrodomestico(bombillo1, apagado, fecha(0,0,0), tiempo(0,0,0)).
electrodomestico(bombillo2, 0.06).
electrodomestico(bombillo3, 0.06).
electrodomestico(bombillo4, 0.06).
electrodomestico(bombillo5, 0.06).
electrodomestico(computadora1, 0.450).
electrodomestico(computadora2, 0.450).
%electrodomestico(computadora3, 0.450).
%electrodomestico(abanico1, 0.9).
%electrodomestico(abanico2, 0.9).
%electrodomestico(abanico3, 0.9).
%electrodomestico(lavadora1, 255).
electrodomestico(lavadora2, 255).
electrodomestico(lavaplatos1, 246).
electrodomestico(bombillo1, 1).
%estado_electrodomestico(bombillo1, apagado, date(0,0,0), time(0,0,0)).

%Objetos de agua
objeto_agua(toilet1,fijo ,6.05).
objeto_agua(fregadero1, continuo ,88.8).
objeto_agua(lavadora1,fijo, 47).
objeto_agua(lavadora2,fijo, 47).
objeto_agua(lavaplatos1,fijo, 12).

%estado_objeto_agua(toilet1, cerrado, fecha(0,0,0), tiempo(0,0,0)).
%estado_objeto_agua(fregadero1, cerrado, fecha(0,0,0), tiempo(0,0,0)).

% estado_electrodomestico(dispositivo, estado/encendido/apagado, fecha, tiempo)
%estado_electrodomestico(nevera1, encendido).
%estado_electrodomestico(estufa1, encendido).
%estado_electrodomestico(television1, encendido).
%estado_electrodomestico(television2, encendido).
%estado_electrodomestico(television3, encendido).
%estado_electrodomestico(bombillo1, encendido).
%estado_electrodomestico(bombillo2, encendido).
%estado_electrodomestico(bombillo3, encendido).
%estado_electrodomestico(bombillo4, encendido).
%estado_electrodomestico(bombillo5, encendido).
%estado_electrodomestico(computadora1, encendido).
%estado_electrodomestico(computadora2, encendido).
%estado_electrodomestico(computadora3, encendido).
%estado_electrodomestico(abanico1, encendido).
%estado_electrodomestico(abanico2, encendido).
%estado_electrodomestico(abanico3, encendido).
%estado_electrodomestico(lavadora1, encendido).
%estado_electrodomestico(lavadora2, encendido).
%estado_electrodomestico(lavaplatos1, encendido).

% La idea es describir el objeto con un identificador, nombre
% y el identificador del lugar donde esta ubicado.
% lugar(identificador, nombre, id_lugar).
%objeto(puerta1,puerta,sala1).
%objeto(puerta2, puerta, habitacion1).
%objeto(puerta3, cocina1).
%objeto(puerta4, bano1).
%objeto(puerta5, cuarto_lavado1).
%objeto(venatana1, ventana, habitacion1).
%objeto(ventana2, ventana, sala1).
%objeto(ventana3, cocina1).

% La idea es describir si el objeto esta abierto o cerrado.
% estado_objeto(identificador, estado/abierto/cerrado)
%estado_objeto(puerta1, abierto).
%estado_objeto(puerta2, abierto).
%estado_objeto(puerta3, abierto).
%estado_objeto(puerta4, cerrado).
%estado_objeto(puerta5, cerrado).
%estado_objeto(ventana1, cerrado).
%estado_objeto(ventana2, abierto).
%estado_objeto(ventana3, cerrado).

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


cerrar_ventanas_casa():-
    objeto(Objeto, ventana, _), estado_objeto(Objeto, abierto),
    retract(estado_objeto(Objeto, abierto)),
    assertz(estado_objeto(Objeto, cerrado)).

cerrar_puertas_casa():-
    objeto(Objeto, puerta, _), estado_objeto(Objeto, abierto),
    retract(estado_objeto(Objeto, abierto)),
    assertz(estado_objeto(Objeto, cerrado)).

cerrar_ventanas_lugar(Lugar):-
        ubicacion_persona(Lugar,_), objeto(Objeto, ventana, Lugar),estado_objeto(Objeto, abierto),
        retract(estado_objeto(Objeto, abierto)),
        assertz(estado_objeto(Objeto, cerrado)).

cerrar_puertas_lugar(Lugar):-
        ubicacion_persona(Lugar,_), objeto(Objeto, puerta, Lugar),estado_objeto(Objeto, abierto),
        retract(estado_objeto(Objeto, abierto)),
        assertz(estado_objeto(Objeto, cerrado)).

% - cerrar_puerta(NombrePuerta)
% - Cierra una puerta especifica, dado un nombre.
% - Si la puerta esta cerrada inicialmente,
% - la regla fallará. De lo contrario, se abrirá.
cerrar_puerta(Puerta):-
    retract(estado_objeto(Puerta, _)),
    assertz(estado_objeto(Puerta, cerrado)).

% - abrir_puerta(NombrePuerta)
% - Abre  una puerta especifica, dado un nombre.
% - Si la puerta esta abierta inicialmente,
% - la regla fallará. De lo contrario, se abrirá.
abrir_puerta(Puerta):-
    retract(estado_objeto(Puerta, _)),
    assertz(estado_objeto(Puerta, abierto)).


% - cerrar_ventana(NombreVentana)
% - Cierra una ventana especifica, dado un nombre.
% - Si la ventana esta cerrada inicialmente,
% - la regla fallará. De lo contrario, se abrirá.
cerrar_ventana(Ventana):-
    retract(estado_objeto(Ventana, _)),
    assertz(estado_objeto(Ventana, cerrado)).

% - abrir_ventana(NombreVentana)
% - Abre una ventana, dado un nombre.
% - Si la ventana esta abierta inicialmente,
% - la regla fallará. De lo contrario, se abrirá.
abrir_ventana(Ventana):-
    retract(estado_objeto(Ventana, _)),
    assertz(estado_objeto(Ventana, abierto)).

% - fecha_tiempo_actual(Fecha, Tiempo)
% - Esta regla produce tanto como la fecha y tiempo
% - actual del computador, como date(DD,MM,YY) y time(HH,MM,SS).
fecha_tiempo_actual(Fecha, Tiempo):-
    get_time(Stamp),
    stamp_date_time(Stamp, Datetime, local),
    date_time_value(time, Datetime, Tiempo),
    date_time_value(date, Datetime, Fecha).

% - calc_fecha_dias(date, Dias)
% - dada una fecha, la convierte a dias gregorianos,
% - para facilitar el calculo de fechas.
calc_fecha_dias(date(Y,M,D),Dias):-
    Dias is (((Y*1461)/4)+((M*153)/5)+D).

diferencia_fechas(date(Y,M,D), date(Y2, M2, D2), Diff):-
    calc_fecha_dias(date(Y,M,D), Dias1),
    calc_fecha_dias(date(Y2, M2, D2), Dias2),
    Resta is abs(Dias2-Dias1),
    Diff is round(Resta).

diferencia_tiempo(time(H,Mn,S), time(H2,Mn2,S2), Horas):-
    Ht is abs(H-H2),
    Mnt is abs((Mn-Mn2)/60),
    St is abs((S2-S)/3600),
    Horas is (Ht + Mnt + St).

fechas_horas(date(Y,M,D), time(H,Mn,S), date(Y2,M2,D2), time(H2,Mn2,S2), Res):-
    diferencia_fechas(date(Y,M,D), date(Y2,M2,D2), Dias),
    diferencia_tiempo(time(H,Mn,S), time(H2, Mn2, S2), Horas),
    Diashoras is (Dias*24),
    Res is (Diashoras + Horas).

% consumo(nombre, consumo, fecha_inicial, tiempo_inicial, fecha_final, tiempo_final, duracion)

encender_electrodomestico(Electrodomestico):-
    retract(estado_electrodomestico(Electrodomestico,_,_,_)),
    fecha_tiempo_actual(Fecha, Tiempo),
    assertz(estado_electrodomestico(Electrodomestico, encendido, Fecha, Tiempo)).

calcular_consumo_electrodomestico(Electrodomestico, Horas_encendido, Res):-
    electrodomestico(Electrodomestico, Consumo),
    Res is (Horas_encendido * Consumo).

abrir_objeto_agua(Objeto_agua):-
    retract(estado_objeto_agua(Objeto_agua,_,_,_)),
    fecha_tiempo_actual(Fecha, Tiempo),
    assertz(estado_objeto_agua(Objeto_agua, abierto, Fecha, Tiempo)),!.

calcular_consumo_agua(Objeto_agua, Horas_uso, Res):-
    objeto_agua(Objeto_agua, continuo,Consumo),
    Res is (Horas_uso * Consumo),!.

usar_objeto_agua(Objeto_agua):-
    objeto_agua(Objeto_agua, fijo, Consumo),
    fecha_tiempo_actual(Fecha_actual, Tiempo_actual),
    assertz(consumo(Objeto_agua, Consumo, Fecha_actual, Tiempo_actual, Fecha_actual, Tiempo_actual, 0)).

cierre_objeto_agua(Objeto_agua):-
    estado_objeto_agua(Objeto_agua, _, Fecha_vieja, Tiempo_viejo),
    fecha_tiempo_actual(Fecha_actual, Tiempo_actual),
    fechas_horas(Fecha_actual, Tiempo_actual, Fecha_vieja, Tiempo_viejo, Horas),
    calcular_consumo_agua(Objeto_agua, Horas, Consumo),
    assertz(consumo(Objeto_agua, Consumo, Fecha_vieja, Tiempo_viejo, Fecha_actual, Tiempo_actual, Horas)),
    retract(estado_objeto_agua(Objeto_agua,_,_,_)),
    assertz(estado_objeto_agua(Objeto_agua, cerrado, Fecha_actual, Tiempo_actual)),!.


apagar_electrodomestico(Electrodomestico):-
    estado_electrodomestico(Electrodomestico,_, Fecha_vieja, Tiempo_viejo),
    fecha_tiempo_actual(Fecha_actual, Tiempo_actual),
    fechas_horas(Fecha_actual, Tiempo_actual, Fecha_vieja, Tiempo_viejo, Horas),
    calcular_consumo_electrodomestico(Electrodomestico, Horas, Consumo),
    assertz(consumo(Electrodomestico, Consumo, Fecha_vieja, Tiempo_viejo, Fecha_actual, Tiempo_actual, Horas)),
    retract(estado_electrodomestico(Electrodomestico,_,_,_)),
    assertz(estado_electrodomestico(Electrodomestico, apagado, Fecha_actual, Tiempo_actual)).

listado_consumo_de_aparato_por_fechas(Aparato, Filtro_fecha, Res):-
    findall(Consumo, consumo(Aparato, Consumo, Filtro_fecha, _, Filtro_fecha, _, _), Res).

calculo_consumo_electrodomesticos(Electrodomestico, ConsumoElectrico, Fecha_filtrado):-
    electrodomestico(Electrodomestico, _),
    listado_consumo_de_aparato_por_fechas(Electrodomestico, Fecha_filtrado, Listado),
    sum_list(Listado, ConsumoElectrico).

calcula_consumo_agua(Objeto_agua, ConsumoAgua, Fecha_filtrado):-
    objeto_agua(Objeto_agua, _, _),
        listado_consumo_de_aparato_por_fechas(Objeto_agua, Fecha_filtrado, Listado),
    sum_list(Listado, ConsumoAgua).
