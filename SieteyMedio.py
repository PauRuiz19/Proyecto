#Oros=1, Copas=2, Bastos=3, Espadas=4
import random
mazo=[(1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(10,1,0.5),(11,1,0.5),(12,1,0.5),(1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(10,2,0.5),(11,2,0.5),(12,2,0.5),(1,3,1),(2,3,2),(3,3,3),(4,3,4),(5,3,5),(6,3,6),(7,3,7),(10,3,0.5),(11,3,0.5),(12,3,0.5),(1,4,1),(2,4,2),(3,4,3),(4,4,4),(5,4,5),(6,4,6),(7,4,7),(10,4,0.5),(11,4,0.5),(12,4,0.5)]
modo_juego=int(input("Qué modo de juego quieres jugar?\n1) Modo Juego Manual\n2) Humano contra máquinas\n"))
while modo_juego<1 or modo_juego>2:
    modo_juego=int(input("Opción incorrecta: "))
else:
    if modo_juego==1:
        numero_jugadores=int(input("Cuántos jugadores van a jugar? (mín. 2, máx. 8)\n"))
        while numero_jugadores<2 or numero_jugadores>8:
            numero_jugadores=int(input("Debe estar entre 2 y 8: "))
        else:
            lista_jugadores=[]
            while len(lista_jugadores)<numero_jugadores:
                nuevo_jugador=str(input("Introduce el nombre del jugador: "))
                while nuevo_jugador.isalnum()==False:
                    nuevo_jugador = str(input("Solo puede tener números y letras, no puede tener espacios y debe empezar por una letra: "))
                else:
                    lista_jugadores.append(nuevo_jugador)
        ordenar=[]
        for i in lista_jugadores:
            ordenar.append([i,mazo[random.randint(0,39)]])
        for i in range(len(ordenar)):
            for j in range(0,len(ordenar)-1):
                if ordenar[j][1][0]<ordenar[j+1][1][0]:
                    ordenar[j] , ordenar[j + 1]=ordenar[j+1],ordenar[j]
                elif ordenar[j][1][0]==ordenar[j+1][1][0]:
                    if ordenar[j][1][1]>ordenar[j+1][1][1]:
                        ordenar[j], ordenar[j + 1] = ordenar[j + 1], ordenar[j]
        for i in range(len(lista_jugadores)):
            lista_jugadores[i]=ordenar[i][0]
        lista_jugadores_juego=[]
        for i in range(len(lista_jugadores)):
            #Lista del valor del diccionario: [Lista con las cartas del jugador, Estado mano actual, Estado partida, Prioridad, Puntos acumulados en la mano, Puntos apostados, Puntos restantes, Contador mano actual]
            lista_jugadores_juego.append({lista_jugadores[i]:[[],"jugando","jugando",i,0,0,20,1]})
        print(lista_jugadores_juego)
        cartas_que_han_salido=[]
        for i in range(len(lista_jugadores)):
            carta=random.choice(mazo)
            mazo.remove(carta)
            lista_jugadores_juego[i][lista_jugadores[i]][0].append(carta)
            lista_jugadores_juego[i][lista_jugadores[i]][4]=carta[2]
            cartas_que_han_salido.append(carta)
        for i in range(1,len(lista_jugadores_juego)):
            if lista_jugadores_juego[i][lista_jugadores[i]][1]=="jugando" and lista_jugadores_juego[i][lista_jugadores[i]][2]=="jugando":
                print("Turno de",lista_jugadores[i])
                lista_jugadores_juego[i][lista_jugadores[i]][7]=lista_jugadores_juego[i][lista_jugadores[i]][7]+1
                print("Cartas que han salido:")
                for i in cartas_que_han_salido:
                    if i[1]==1:
                        print(i[0],"de Oros")
                    elif i[1]==2:
                        print(i[0],"de Copas")
                    elif i[1]==3:
                        print(i[0],"de Bastos")
                    elif i[1]==4:
                        print(i[0],"de Espadas")
                print("Puntos totales de cada jugador y puntos apostados:")
                for i in range(len(lista_jugadores_juego)):
                    if i==0:
                        print(lista_jugadores[i] + " (Banca): Puntos totales=", lista_jugadores_juego[i][lista_jugadores[i]][6],", Puntos apostados=", lista_jugadores_juego[i][lista_jugadores[i]][5])
                    else:
                        print(lista_jugadores[i]+": Puntos totales=",lista_jugadores_juego[i][lista_jugadores[i]][6],", Puntos apostados=",lista_jugadores_juego[i][lista_jugadores[i]][5])
                apuesta_valida=False
                #Crecimiento de apuestas:
                #Mano 1 - 5: Apuesta min.: 2 ptos. - Apuesta max.: 5  ptos.
                #Mano 6 - 12: Apuesta min.: 3 ptos. - Apuesta max.: 6 ptos.
                #Mano 13 - 18: Apuesta min.: 4 ptos. - Apuesta max.: 8 ptos.
                #Mano 19 - 25: Apuesta min.: 5ptos. - Apuesta max.: 10ptos.
                #Mano 26 - 30: Apuesta min.: 6ptos. - Apuesta max.: 12ptos.
                if lista_jugadores_juego[i][lista_jugadores[i]][7]>=1 and lista_jugadores_juego[i][lista_jugadores[i]][7]<=5:
                    apuesta_minima=2
                    apuesta_maxima=5
                elif lista_jugadores_juego[i][lista_jugadores[i]][7]>=6 and lista_jugadores_juego[i][lista_jugadores[i]][7]<=12:
                    apuesta_minima=3
                    apuesta_maxima=6
                elif lista_jugadores_juego[i][lista_jugadores[i]][7]>=13 and lista_jugadores_juego[i][lista_jugadores[i]][7]<=18:
                    apuesta_minima=4
                    apuesta_maxima=8
                elif lista_jugadores_juego[i][lista_jugadores[i]][7]>=6 and lista_jugadores_juego[i][lista_jugadores[i]][7]<=12:
                    apuesta_minima=3
                    apuesta_maxima=6
                elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 13 and lista_jugadores_juego[i][lista_jugadores[i]][7] <= 18:
                    apuesta_minima=4
                    apuesta_maxima=8
                elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 19 and lista_jugadores_juego[i][lista_jugadores[i]][7] <= 25:
                    apuesta_minima=5
                    apuesta_maxima=10
                elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 26 and lista_jugadores_juego[i][lista_jugadores[i]][7] <= 30:
                    apuesta_minima=6
                    apuesta_maxima=12
                while apuesta_valida==False:
                    apuesta = int(input("Cuantos puntos quieres apostar? (min. "+str(apuesta_minima)+" , max."+str(apuesta_maxima)))
                    if apuesta<apuesta_minima or apuesta>apuesta_maxima:
                        print("Mínimo=",apuesta_minima,", Máximo=",apuesta_maxima)
                    elif lista_jugadores_juego[i][lista_jugadores[i]][6]-apuesta<0:
                        print("No puedes apostar más puntos de los que tienes")
                    elif lista_jugadores_juego[i][lista_jugadores[i]][6]<apuesta_minima:
                        print("La apuesta mínima es mayor que tus puntos restantes. Debes apostar todos tus puntos")
                        apuesta_minima=lista_jugadores_juego[i][lista_jugadores[i]][6]
                    else:
                        apuesta_valida=True
                else:
                    lista_jugadores_juego[i][lista_jugadores[i]][5]=apuesta
                    lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]-apuesta







    #elif modo_juego==2: