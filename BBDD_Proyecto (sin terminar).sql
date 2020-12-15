-- 1 Mostrar la Carta inicial más repetida por cada jugador(mostrar nombre jugador y carta).
-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
select t.idpartida, u.username from turnos t 
inner join participante p on p.id_participante=t.idparticipante
inner join jugador j on j.idjugador=p.id_jugador
inner join usuario u on u.idusuario=j.idusuario
where t.apuesta in(select max(t.apuesta) from turnos t group by t.idpartida) group by t.idpartida;	
-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
select t.idpartida, u.username from turnos t 
inner join participante p on p.id_participante=t.idparticipante
inner join jugador j on j.idjugador=p.id_jugador
inner join usuario u on u.idusuario=j.idusuario
where t.apuesta in(select min(t.apuesta) from turnos t group by t.idpartida) group by t.idpartida;	
-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %"
-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %"
SELECT (COUNT(partida.ganador_partida) DIV COUNT(partida.idpartida)) truncate 100 as "porcentaje %" from partida
inner join participante on participante.id_participante = partida.ganador_partida
inner join jugador on participante.id_jugador = jugador.idjugador
where "porcentaje" is not null;
-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.
-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.
-- 8 Cuantas rondas gana la banca en cada partida.
SELECT partida.idpartida, COUNT(turnos.resultado) as "turnos ganados" FROM partida
inner join turnos on partida.idpartida = turnos.idpartida
WHERE turnos.es_banca=1 and turnos.resultado="gana turno"
GROUP BY partida.idpartida;
-- 9 Cuántos usuarios han sido la banca en una partida
SELECT partida.idpartida, COUNT(jugador.idusuario) FROM partida
inner join turnos on turnos.idpartida = partida.idpartida
inner join participante on partida.idpartida = participante.id_partida
inner join jugador on participante.id_jugador = jugador.idjugador
where jugador.idbot is null and turno.es_banca in (SELECT es_banca FROM turnos where es_banca=1)
group by partida.idpartida;

select partida.idpartida, COUNT(DISTINCT turnos.idparticipante) from partida
inner join turnos on partida.idpartida = turnos.idpartida 
where turnos.idparticipante in (select*from turnos where es_banca=1) 
group by partida.idpartida;
-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.
SELECT usuario.username or bot.descripcion as "nombre jugador", MAX(turnos.puntos_final) FROM turnos
inner join participante on participante.id_participante = turnos.idparticipante
inner join jugador on jugador.idjugador = participante.id_jugador
inner join usuario on usuario.idusuario = jugador.idusuario
inner join bot on bot.idbot = jugador.idbot
group by turnos.idparticipante;
-- 11 Calcular la apuesta media por partida.
SELECT AVG(apuesta) from turnos group by turnos.idpartida;
-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.
SELECT*FROM usuario
inner join jugador on jugador.idusuario = usuario.idusuario
inner join participante on participante.id_jugador = jugador.idjugador
inner join turnos on turnos.idparticipante = participante.id_participante
WHERE turnos.id_participante IN(SELECT apuesta from turnos
inner join partida on turnos.idpartida = partida.idpartida
inner join puntuacion on puntuacion.id_partida = partida.idpartida
where puntuacion.puntuacion = turnos.puntos_final)
-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.