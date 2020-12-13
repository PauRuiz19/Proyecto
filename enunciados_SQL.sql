-- 1 Mostrar la Carta inicial más repetida por cada jugador(mostrar nombre jugador y carta).
SELECT * FROM turnos
INNER JOIN participante ON idparticipante = id_participante
INNER JOIN jugador ON id_jugador = idjugador
INNER JOIN usuario ON jugador.idusuario = usuario.idusuario
ORDER BY carta_inicial,username
-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
SELECT * FROM turnos
INNER JOIN participante ON idparticipante = id_participante
INNER JOIN jugador ON id_jugador = idjugador
INNER JOIN usuario ON jugador.idusuario = usuario.idusuario
ORDER BY apuesta DESC LIMIT 1

SELECT * FROM turnos
INNER JOIN participante ON idparticipante = id_participante
INNER JOIN jugador ON id_jugador = idjugador
INNER JOIN usuario ON jugador.idusuario = usuario.idusuario
ORDER BY apuesta DESC
-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
SELECT * FROM turnos
INNER JOIN participante ON idparticipante = id_participante
INNER JOIN jugador ON id_jugador = idjugador
INNER JOIN usuario ON jugador.idusuario = usuario.idusuario
WHERE apuesta is not NULL
ORDER BY apuesta LIMIT 1
-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %"
-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %"
-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.
-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.
-- 8 Cuantas rondas gana la banca en cada partida.
-- 9 Cuántos usuarios han sido la banca en la partida
SELECT DISTINCT username FROM turnos
INNER JOIN participante ON idparticipante = id_participante
INNER JOIN jugador ON id_jugador = idjugador
INNER JOIN usuario ON jugador.idusuario = usuario.idusuario
WHERE es_banca = 1
-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.
-- 11 Calcular la apuesta media por partida.
-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.
-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.