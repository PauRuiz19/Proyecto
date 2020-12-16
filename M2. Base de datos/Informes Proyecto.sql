-- 1 Mostrar la Carta inicial más repetida por cada jugador(mostrar nombre jugador y carta).
select u.username, c.idcartas from usuario u 
inner join jugador j on u.idusuario=j.idusuario
inner join participante p on j.idjugador=p.id_jugador
inner join turnos t on p.id_participante=t.idparticipante
inner join cartas c on t.carta_inicial=c.idcartas
where c.idcartas in (select max(count(t.carta_inicial)) from usuario u 
inner join jugador j on u.idusuario=j.idusuario
inner join participante p on j.idjugador=p.id_jugador
inner join turnos t on p.id_participante=t.idparticipante
inner join cartas c on t.carta_inicial=c.idcartas) group by t.idparticipante;
-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
select nombre,max(apuesta),idpartida
from
(
select 
case 
when username is not null then usuario.username 
else descripcion 
end
as nombre,max(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username
) tabla
where (apuesta,idpartida) in (

select 
max(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by max(turnos.apuesta) desc
)
group by idpartida;
-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
select nombre,min(apuesta),idpartida
from
(
select 
case 
when username is not null then usuario.username 
else descripcion 
end
as nombre,min(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username
) tabla
where (apuesta,idpartida) in (

select 
min(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by min(turnos.apuesta) desc
)
group by idpartida;
-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %"
select u.username, pa.nombre_sala, round(count(t.idturnos)/max(t.numero_turno)*100,2) as "Porcentaje rondas ganadas" from usuario u
inner join jugador j on u.idusuario=j.idusuario
inner join participante p on j.idjugador=p.id_jugador
inner join turnos t on p.id_participante=t.idparticipante
inner join partida pa on t.idpartida=pa.idpartida
where t.puntos_final-t.puntos_inicio>0 group by t.idpartida, t.idparticipante
union
select b.descripcion, pa.nombre_sala, round(count(t.idturnos)/max(t.numero_turno)*100,2) as "Porcentaje rondas ganadas" from bot b
inner join jugador j on b.idbot=j.idbot
inner join participante p on j.idjugador=p.id_jugador
inner join turnos t on p.id_participante=t.idparticipante
inner join partida pa on t.idpartida=pa.idpartida
where t.puntos_final-t.puntos_inicio>0 group by t.idpartida, t.idparticipante;
-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %"
SELECT (COUNT(partida.ganador_partida)/COUNT(partida.idpartida))*100 as "porcentaje %" from partida
inner join participante on participante.id_participante = partida.ganador_partida
inner join jugador on participante.id_jugador = jugador.idjugador 
where jugador.idjugador in(select idjugador from jugador where idbot is not null);
-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.
SELECT jugador.*, TIMEDIFF(partida.hora_fin,partida.hora_inicio) as duracion from jugador
inner join participante on jugador.idjugador = participante.id_jugador
inner join partida on partida.ganador_partida = participante.id_participante
inner join turnos on partida.idpartida = turnos.idpartida
where turnos.puntos_final in(select MAX(COUNT(idturnos)) from turnos)) > (SELECT AVG(puntos_final) FROM turnos where puntos_final in(select MAX(COUNT(idturnos)) from turnos);
-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.
select t.idpartida, count(t.idturnos) as Rondas, c.tipo from turnos t
inner join cartas c on t.carta_inicial=c.idcartas
where t.es_banca=0 and t.puntos_final-t.puntos_inicio>0 
group by t.idpartida;
-- 8 Cuantas rondas gana la banca en cada partida.
select turnos.idpartida, count(turnos.idturnos) as "Turnos ganados de la banca" from turnos where turnos.es_banca=0 and turnos.puntos_final-turnos.puntos_inicio<0 group by turnos.idpartida; 
-- 9 Cuántos usuarios han sido la banca en cada partida
select turnos.idpartida, COUNT(DISTINCT turnos.idparticipante) as "Nº usuarios banca"from turnos
where turnos.idparticipante in (select turnos.idparticipante from turnos where es_banca=1 group by turnos.idpartida) 
group by turnos.idpartida;
-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.
select 
-- 11 Calcular la apuesta media por partida.
select t.idpartida, round(avg(t.apuesta),2) as "Apuesta media" from turnos t group by t.idpartida;
-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.
SELECT*FROM usuario
inner join jugador on jugador.idusuario = usuario.idusuario
inner join participante on participante.id_jugador = jugador.idjugador
inner join turnos on turnos.idparticipante = participante.id_participante
WHERE turnos.id_participante IN(SELECT apuesta from turnos
inner join partida on turnos.idpartida = partida.idpartida
inner join puntuacion on puntuacion.id_partida = partida.idpartida
where puntuacion.puntuacion = turnos.puntos_final);
-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
select t.idpartida ,count(t.carta_inicial) as "Cartas que se han dado", sum(c.valor) as "Valor total de las cartas" from turnos t inner join cartas c on t.carta_inicial=c.idcartas group by t.idpartida;
-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.


