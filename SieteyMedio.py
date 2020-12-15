#Oros=1, Copas=2, Bastos=3, Espadas=4
import random
mazo=[(1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(10,1,0.5),(11,1,0.5),(12,1,0.5),(1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(10,2,0.5),(11,2,0.5),(12,2,0.5),(1,3,1),(2,3,2),(3,3,3),(4,3,4),(5,3,5),(6,3,6),(7,3,7),(10,3,0.5),(11,3,0.5),(12,3,0.5),(1,4,1),(2,4,2),(3,4,3),(4,4,4),(5,4,5),(6,4,6),(7,4,7),(10,4,0.5),(11,4,0.5),(12,4,0.5)]
print("BIENVENIDO A SIETE Y MEDIO")
modo_juego=int(input("Qué modo de juego quieres jugar?\n1) Modo Juego Manual\n2) Humano contra máquinas\n"))
while modo_juego<1 or modo_juego>2:
    modo_juego=int(input("Opción incorrecta: "))
else:
    if modo_juego==1:
        numero_jugadores=int(input("Cuántos jugadores van a jugar? (mín. 2, máx. 8)\n"))
        while numero_jugadores<2 or numero_jugadores>8:
            numero_jugadores=int(input("Debe estar entre 2 y 8: "))
        else:
            #Creamos una lista vacía para ir añadiendo a los jugadores hasta llegar al numero de jugadores que se ha puesto
            lista_jugadores=[]
            num_jugador=1
            while len(lista_jugadores)<numero_jugadores:
                nuevo_jugador=str(input("Introduce el nombre del jugador "+str(num_jugador)+": "))
                lista_nombre=list(nuevo_jugador)
                #Creamos una lista con el nombre introducido para comprobar que el primer elemento no es un número
                while nuevo_jugador.isalnum()==False or lista_nombre[0]=="1" or lista_nombre[0]=="2" or lista_nombre[0]=="3" or lista_nombre[0]=="4" or lista_nombre[0]=="5" or lista_nombre[0]=="6" or lista_nombre[0]=="7" or lista_nombre[0]=="8" or lista_nombre[0]=="9" or lista_nombre[0]=="0":
                    nuevo_jugador = str(input("Solo puede tener números y letras, no puede tener espacios y debe empezar por una letra: "))
                    lista_nombre = list(nuevo_jugador)
                else:
                    lista_jugadores.append(nuevo_jugador)
                    num_jugador = num_jugador + 1
        ordenar=[]
        for i in lista_jugadores:
            carta=random.choice(mazo)
            mazo.remove(carta)
            ordenar.append([i,carta])
        for i in range(len(ordenar)):
            for j in range(0,len(ordenar)-1):
                if ordenar[j][1][0]<ordenar[j+1][1][0]:
                    ordenar[j] , ordenar[j + 1]=ordenar[j+1],ordenar[j]
                elif ordenar[j][1][0]==ordenar[j+1][1][0]:
                    if ordenar[j][1][1]>ordenar[j+1][1][1]:
                        ordenar[j], ordenar[j + 1] = ordenar[j + 1], ordenar[j]
        #En esta nueva lista "ordenar" hemos ido añadiendo una lista con dos elementos, el nombre del jugador y una carta aleatoria, para poder asignar el orden inicial a través del metodo de la burbuja
        for i in ordenar:
            mazo.append(i[1])
        print("Orden inicial y carta repartida para decidir el orden:")
        for i in range(len(ordenar)):
            if ordenar[i][1][1]==1:
                palo="Oros"
            elif ordenar[i][1][1]==2:
                palo="Copas"
            elif ordenar[i][1][1]==3:
                palo="Bastos"
            elif ordenar[i][1][1]==4:
                palo="Espadas"
            if i==0:
                print(str(i)+". "+ordenar[i][0]+" (Banca) - "+str(ordenar[i][1][0])+" de "+palo)
            else:
                print(str(i)+". "+ordenar[i][0]+" - "+str(ordenar[i][1][0])+" de "+palo)
        for i in range(len(lista_jugadores)):
            lista_jugadores[i]=ordenar[i][0]
        lista_jugadores_juego=[]
        for i in range(len(lista_jugadores)):
            #Lista del valor del diccionario: [Lista con las cartas del jugador, Estado mano actual, Estado partida, Prioridad, Puntos acumulados en la mano, Puntos apostados, Puntos restantes, Contador mano actual]
            lista_jugadores_juego.append({lista_jugadores[i]:[[],"jugando","jugando",i,0,0,20,1]})
        cartas_que_han_salido=[]
        #Variable para poder mostrar las cartas que han salido
        #Creamos variable "partida" para crear un bucle del cual se saldra cuando haya un ganador
        partida=True
        while partida==True:
            for i in range(len(lista_jugadores_juego)):
                if lista_jugadores_juego[i][lista_jugadores[i]][2]=="eliminado":
                    continue
                else:
                #Si el jugador no está eliminado recibe una carta
                    carta = random.choice(mazo)
                    mazo.remove(carta)
                    lista_jugadores_juego[i][lista_jugadores[i]][0].append(carta)
                    lista_jugadores_juego[i][lista_jugadores[i]][4] = carta[2]
                    cartas_que_han_salido.append(carta)
            for i in range(1, len(lista_jugadores_juego)+1):
                #Empieza por i=1, y cuando llegue a i=len(lista_jugadores_juego), i será 0 y será el turno de la banca
                if i==len(lista_jugadores_juego):
                    i=0
                if lista_jugadores_juego[i][lista_jugadores[i]][2]=="eliminado":
                    continue
                if lista_jugadores_juego[i][lista_jugadores[i]][1] == "jugando" and lista_jugadores_juego[i][lista_jugadores[i]][2] == "jugando":
                    if i==0:
                        print("*"*5+"Turno de "+lista_jugadores[i]+" (Banca) "+"*"*5)
                    else:
                        print("*"*5+"Turno de "+lista_jugadores[i]+"*"*5)
                    lista_jugadores_juego[i][lista_jugadores[i]][7] = lista_jugadores_juego[i][lista_jugadores[i]][7] + 1
                    if lista_jugadores_juego[i][lista_jugadores[i]][0][0][1]==1:
                        palo="Oros"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 2:
                        palo="Copas"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 3:
                        palo="Bastos"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 4:
                        palo="Espadas"
                    print("Tu carta inicial:",lista_jugadores_juego[i][lista_jugadores[i]][0][0][0],"de",palo)
                    input("Pulsa ENTER para continuar")
                    print("")
                    #Mostramos las cartas que han salido y los puntos totales y apostados de cada jugador
                    print("Cartas que han salido:")
                    for j in cartas_que_han_salido:
                        if j[1] == 1:
                            print(j[0], "de Oros")
                        elif j[1] == 2:
                            print(j[0], "de Copas")
                        elif j[1] == 3:
                            print(j[0], "de Bastos")
                        elif j[1] == 4:
                            print(j[0], "de Espadas")
                    print("-"*50)
                    print("Puntos totales de cada jugador y puntos apostados:")
                    for k in range(len(lista_jugadores_juego)):
                        if k == 0:
                            print(lista_jugadores[k] + " (Banca): Puntos totales=",
                                  lista_jugadores_juego[k][lista_jugadores[k]][6])
                        else:
                            print(lista_jugadores[k] + ": Puntos totales=", lista_jugadores_juego[k][lista_jugadores[k]][6],
                                  ", Puntos apostados=", lista_jugadores_juego[k][lista_jugadores[k]][5])
                    print("-"*50)
                    apuesta_valida = False
                    # Crecimiento de apuestas:
                    # Mano 1 - 5: Apuesta min.: 2 ptos. - Apuesta max.: 5  ptos.
                    # Mano 6 - 12: Apuesta min.: 3 ptos. - Apuesta max.: 6 ptos.
                    # Mano 13 - 18: Apuesta min.: 4 ptos. - Apuesta max.: 8 ptos.
                    # Mano 19 - 25: Apuesta min.: 5ptos. - Apuesta max.: 10ptos.
                    # Mano 26 - 30: Apuesta min.: 6ptos. - Apuesta max.: 12ptos.
                    if lista_jugadores_juego[i][lista_jugadores[i]][7] >= 1 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 5:
                        apuesta_minima = 2
                        apuesta_maxima = 5
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 6 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 12:
                        apuesta_minima = 3
                        apuesta_maxima = 6
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 13 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 18:
                        apuesta_minima = 4
                        apuesta_maxima = 8
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 19 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 25:
                        apuesta_minima = 5
                        apuesta_maxima = 10
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 26 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 30:
                        apuesta_minima = 6
                        apuesta_maxima = 12
                    if i!=0:
                    #Cuando no sea el turno de la banca (i!=0), el jugador deberá realizar una apuesta con un rango predefinido
                        while apuesta_valida == False:
                        #Bucle del cual se saldra solo si el jugador realiza una apuesta válida
                            if lista_jugadores_juego[i][lista_jugadores[i]][6] < apuesta_minima:
                            #Si se da el caso que al jugador le queden menos puntos que la apuesta mínima este deberá apostar todos sus puntos y cambiaremos las variables que fijan el rango de apuestas
                                print("La apuesta mínima es mayor que tus puntos restantes. Debes apostar todos tus puntos")
                                apuesta_minima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                                apuesta_maxima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                            apuesta = int(input("Cuantos puntos quieres apostar? (min. " + str(apuesta_minima) + " , max." + str(apuesta_maxima) + ") "))
                            if apuesta < apuesta_minima or apuesta > apuesta_maxima:
                                print("Mínimo=", apuesta_minima, ", Máximo=", apuesta_maxima)
                            elif lista_jugadores_juego[i][lista_jugadores[i]][6] - apuesta < 0:
                                print("No puedes apostar más puntos de los que tienes")
                            else:
                                apuesta_valida = True
                        lista_jugadores_juego[i][lista_jugadores[i]][5] = apuesta
                        lista_jugadores_juego[i][lista_jugadores[i]][6] = lista_jugadores_juego[i][lista_jugadores[i]][6] - apuesta
                    while lista_jugadores_juego[i][lista_jugadores[i]][1]=="jugando":
                    #Bucle para que el jugador decida si pedir cara o plantarse, del cual se sale si el jugador se planta o se pasa de 7,5 (estado_mano=eliminado)
                        print("Puntos acumulados en la mano=",lista_jugadores_juego[i][lista_jugadores[i]][4])
                        opcion=int(input("Qué quieres hacer?\n1) Pedir Carta\n2) Plantarme\n"))
                        while opcion<1 or opcion>2:
                            opcion=int(input("Opción incorrecta!\n"))
                        else:
                            if opcion==2:
                                lista_jugadores_juego[i][lista_jugadores[i]][1]="plantado"
                            elif opcion==1:
                            #Se coge carta random y se elimina del mazo
                                carta=random.choice(mazo)
                                cartas_que_han_salido.append(carta)
                                mazo.remove(carta)
                                if carta[1] == 1:
                                    palo = "Oros"
                                elif carta[1] == 2:
                                    palo = "Copas"
                                elif carta[1] == 3:
                                    palo = "Bastos"
                                elif carta[1] == 4:
                                    palo = "Espadas"
                                print("Carta que ha salido:",carta[0],"de",palo)
                                lista_jugadores_juego[i][lista_jugadores[i]][0].append(carta)
                                lista_jugadores_juego[i][lista_jugadores[i]][4]=lista_jugadores_juego[i][lista_jugadores[i]][4]+carta[2]
                                if lista_jugadores_juego[i][lista_jugadores[i]][4]>7.5:
                                    print("Te has pasado de 7,5!")
                                    lista_jugadores_juego[i][lista_jugadores[i]][1]="eliminado"
                                    input("Presiona ENTER para continuar")
            banca_cambiada=False
            #Varible para guardar si un jugador saca 7,5 y la banca no, deberá cambiarse el orden
            if lista_jugadores_juego[0][lista_jugadores[0]][1]=="eliminado":
            #Si la banca se pasa
                for i in range(1,len(lista_jugadores_juego)):
                    if lista_jugadores_juego[i][lista_jugadores[i]][1]=="eliminado":
                    #Si el jugador se también se ha pasado, perderá el turno y los puntos apostados
                        lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                    else:
                        if lista_jugadores_juego[i][lista_jugadores[i]][4]==7.5:
                        #Si el jugador tiene 7,5 se le paga el doble
                            if lista_jugadores_juego[0][lista_jugadores[0]][6]<lista_jugadores_juego[i][lista_jugadores[i]][5] and lista_jugadores_juego[0][lista_jugadores[0]][6]!=0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]+lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6]==0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+3*lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]-lista_jugadores_juego[i][lista_jugadores[i]][5]
                            if banca_cambiada==False:
                            #Si es el primer jugador que ha sacado 7,5 en la ronda, guardaremos variables para cambiar la banca al finalizar la ronda
                                nueva_posicion=lista_jugadores_juego[0]
                                nueva_posicion2=lista_jugadores[0]
                                nueva_banca=i
                                banca_cambiada=True
                        else:
                        #Si el jugador no se ha pasado y no tiene 7,5
                            if lista_jugadores_juego[0][lista_jugadores[0]][6]<lista_jugadores_juego[i][lista_jugadores[i]][5] and lista_jugadores_juego[0][lista_jugadores[0]][6]!=0:
                            #Caso en el que la banca tenga menos puntos que los apostados por el jugador pero no 0 se le pagará lo apostado más los puntos restantes de la banca
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]+lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6]==0:
                            #Si la banca se ha quedado sin puntos se le devolverá al jugador lo apostado
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+2*lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]-lista_jugadores_juego[i][lista_jugadores[i]][5]
            elif lista_jugadores_juego[0][lista_jugadores[0]][4]==7.5:
            #Si la banca saca 7,5 ganará a todos los jugadores
                for i in range(1,len(lista_jugadores_juego)):
                    lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
            else:
            #Si la banca no se ha pasado se hara la comparación con todos los jugadores
                for i in range(1,len(lista_jugadores_juego)):
                    if lista_jugadores_juego[i][lista_jugadores[i]][1]=="eliminado":
                    #Si el jugador se ha pasado sumaremos sus puntos apostados a los puntos de la máquina
                        lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                    elif lista_jugadores_juego[0][lista_jugadores[0]][4]>=lista_jugadores_juego[i][lista_jugadores[i]][4]:
                        lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                    else:
                    #Si el jugador tiene más puntos en la mano que la banca
                        if lista_jugadores_juego[i][lista_jugadores[i]][4]==7.5:
                        #Si el jugador tiene 7,5
                            if lista_jugadores_juego[0][lista_jugadores[0]][6]<lista_jugadores_juego[i][lista_jugadores[i]][5] and lista_jugadores_juego[0][lista_jugadores[0]][6]!=0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]+lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6]==0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+3*lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]-lista_jugadores_juego[i][lista_jugadores[i]][5]
                            if banca_cambiada==False:
                                nueva_posicion = lista_jugadores_juego[0]
                                nueva_posicion2 = lista_jugadores[0]
                                nueva_banca = i
                                banca_cambiada = True
                        else:
                            if lista_jugadores_juego[0][lista_jugadores[0]][6]<lista_jugadores_juego[i][lista_jugadores[i]][5] and lista_jugadores_juego[0][lista_jugadores[0]][6]!=0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]+lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6]==0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6]=lista_jugadores_juego[i][lista_jugadores[i]][6]+2*lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6]=lista_jugadores_juego[0][lista_jugadores[0]][6]-lista_jugadores_juego[i][lista_jugadores[i]][5]
            if banca_cambiada==True:
            #Si la banca debe cambiarse se cambiará el orden, y la banca pasará al último lugar
                lista_jugadores_juego[nueva_banca], lista_jugadores_juego[0] = lista_jugadores_juego[0], lista_jugadores_juego[nueva_banca]
                lista_jugadores[nueva_banca], lista_jugadores[0] = lista_jugadores[0], lista_jugadores[nueva_banca]
                lista_jugadores_juego.remove(nueva_posicion)
                lista_jugadores.remove(nueva_posicion2)
                lista_jugadores_juego.append(nueva_posicion)
                lista_jugadores.append(nueva_posicion2)
            for i in range(len(lista_jugadores_juego)):
            #for para actualizar los puntos apostados, las cartas, los puntos en la mano y el estado de la mano
                lista_jugadores_juego[i][lista_jugadores[i]][5]=0
                lista_jugadores_juego[i][lista_jugadores[i]][0]=[]
                lista_jugadores_juego[i][lista_jugadores[i]][4]=0
                lista_jugadores_juego[i][lista_jugadores[i]][1] = "jugando"
            for i in range(len(lista_jugadores_juego)):
            #for para comprobar si hay algún jugador con 0 puntos, cambiar su estado a "eliminado" y moverlo al último lugar de la lista
                if lista_jugadores_juego[i][lista_jugadores[i]][6]==0:
                    lista_jugadores_juego[i][lista_jugadores[i]][1]="eliminado"
                    lista_jugadores_juego[i][lista_jugadores[i]][2]="eliminado"
                    eliminado=lista_jugadores_juego[i]
                    eliminado2=lista_jugadores[i]
                    lista_jugadores_juego.remove(eliminado)
                    lista_jugadores.remove(eliminado2)
                    lista_jugadores_juego.append(eliminado)
                    lista_jugadores.append(eliminado2)

            for i in range(len(cartas_que_han_salido)):
            #for para añadir las cartas repartidas de nuevo al mazo
                mazo.append(cartas_que_han_salido[i])
            cartas_que_han_salido=[]
            for i in range(len(lista_jugadores_juego)):
            #for para actualizar la prioridad de los jugadores
                lista_jugadores_juego[i][lista_jugadores[i]][3]=i
            contador=0
            for i in range(len(lista_jugadores_juego)):
            #for para comprobar cuantos jugadores quedan jugando
                if lista_jugadores_juego[i][lista_jugadores[i]][2]=="jugando":
                    contador=contador+1
            if contador<=1 or lista_jugadores_juego[0][lista_jugadores[0]][7]==30:
            #Si hay solo 1 jugador jugando o hemos llegado a la mano 30 se saldrá del bucle
                partida=False
            else:
                #Mostraremos un resumen del orden y la puntuación de cada jugador
                print("Orden y puntuación de cada jugador:")
                for i in range(len(lista_jugadores_juego)):
                    if i==0:
                        print(str(i)+". "+lista_jugadores[i]+" (Banca) - "+str(lista_jugadores_juego[i][lista_jugadores[i]][6])+" puntos")
                    elif lista_jugadores_juego[i][lista_jugadores[i]][2]=="eliminado":
                        print(str(i) + ". " + lista_jugadores[i] + " - " + str(lista_jugadores_juego[i][lista_jugadores[i]][6]) + " puntos (eliminado)")
                    else:
                        print(str(i) + ". " + lista_jugadores[i] + " - " + str(lista_jugadores_juego[i][lista_jugadores[i]][6]) + " puntos")
                input("Presiona ENTER para continuar")

        punt_maxima=0
        for i in range(len(lista_jugadores_juego)):
        #for para saber quien es el ganador
            if lista_jugadores_juego[i][lista_jugadores[i]][6]>punt_maxima:
                punt_maxima=lista_jugadores_juego[i][lista_jugadores[i]][6]
                ganador=lista_jugadores[i]
        print("Ha ganado",ganador,"!!!")











    elif modo_juego==2:
        #Lo único que cambiará en el modo Humano vs máquinas será el cómo apuestan las máquinas y cuando pedirán carta
        numero_jugadores = int(input("Cuántos jugadores van a jugar? (incluido jugador humano) (mín. 2, máx. 8)\n"))
        while numero_jugadores < 2 or numero_jugadores > 8:
            numero_jugadores = int(input("Debe estar entre 2 y 8: "))
        else:
            lista_jugadores = []
            num_jugador = 0
            while len(lista_jugadores) < numero_jugadores:
                if num_jugador==0:
                    nuevo_jugador = str(input("Introduce el nombre del jugador: "))
                    lista_nombre = list(nuevo_jugador)
                    while nuevo_jugador.isalnum() == False or lista_nombre[0] == "1" or lista_nombre[0] == "2" or lista_nombre[0] == "3" or lista_nombre[0] == "4" or lista_nombre[0] == "5" or lista_nombre[0] == "6" or lista_nombre[0] == "7" or lista_nombre[0] == "8" or lista_nombre[0] == "9" or lista_nombre[0] == "0":
                        nuevo_jugador = str(input("Solo puede tener números y letras, no puede tener espacios y debe empezar por una letra: "))
                        lista_nombre = list(nuevo_jugador)
                else:
                    nuevo_jugador = "BOT"+str(num_jugador)
                lista_jugadores.append(nuevo_jugador)
                num_jugador = num_jugador + 1

        ordenar = []
        for i in lista_jugadores:
            carta = random.choice(mazo)
            mazo.remove(carta)
            ordenar.append([i, carta])
        for i in range(len(ordenar)):
            for j in range(0, len(ordenar) - 1):
                if ordenar[j][1][0] < ordenar[j + 1][1][0]:
                    ordenar[j], ordenar[j + 1] = ordenar[j + 1], ordenar[j]
                elif ordenar[j][1][0] == ordenar[j + 1][1][0]:
                    if ordenar[j][1][1] > ordenar[j + 1][1][1]:
                        ordenar[j], ordenar[j + 1] = ordenar[j + 1], ordenar[j]
        for i in ordenar:
            mazo.append(i[1])
        print("Orden inicial y carta repartida para decidir el orden:")

        for i in range(len(ordenar)):
            if ordenar[i][1][1] == 1:
                palo = "Oros"
            elif ordenar[i][1][1] == 2:
                palo = "Copas"
            elif ordenar[i][1][1] == 3:
                palo = "Bastos"
            elif ordenar[i][1][1] == 4:
                palo = "Espadas"
            if i == 0:
                print(str(i) + ". " + ordenar[i][0] + " (Banca) - " + str(ordenar[i][1][0]) + " de " + palo)
            else:
                print(str(i) + ". " + ordenar[i][0] + " - " + str(ordenar[i][1][0]) + " de " + palo)
        for i in range(len(lista_jugadores)):
            lista_jugadores[i] = ordenar[i][0]
        lista_jugadores_juego = []
        for i in range(len(lista_jugadores)):
            # Lista del valor del diccionario: [Lista con las cartas del jugador, Estado mano actual, Estado partida, Prioridad, Puntos acumulados en la mano, Puntos apostados, Puntos restantes, Contador mano actual, BOT o humano]
            if lista_jugadores[i]!="BOT1" and lista_jugadores[i]!="BOT2" and lista_jugadores[i]!="BOT3" and lista_jugadores[i]!="BOT4" and lista_jugadores[i]!="BOT5" and lista_jugadores[i]!="BOT6" and lista_jugadores[i]!="BOT7":
                lista_jugadores_juego.append({lista_jugadores[i]: [[], "jugando", "jugando", i, 0, 0, 20, 1,"humano"]})
            else:
                lista_jugadores_juego.append({lista_jugadores[i]: [[], "jugando", "jugando", i, 0, 0, 20, 1,"bot"]})
        cartas_que_han_salido = []
        partida = True
        while partida == True:
            for i in range(len(lista_jugadores_juego)):
                if lista_jugadores_juego[i][lista_jugadores[i]][2] == "eliminado":
                    continue
                else:
                    carta = random.choice(mazo)
                    mazo.remove(carta)
                    lista_jugadores_juego[i][lista_jugadores[i]][0].append(carta)
                    lista_jugadores_juego[i][lista_jugadores[i]][4] = carta[2]
                    cartas_que_han_salido.append(carta)
            for i in range(1, len(lista_jugadores_juego) + 1):
                if i == len(lista_jugadores_juego):
                    i = 0
                if lista_jugadores_juego[i][lista_jugadores[i]][2] == "eliminado":
                    continue
                if lista_jugadores_juego[i][lista_jugadores[i]][1] == "jugando" and \
                        lista_jugadores_juego[i][lista_jugadores[i]][2] == "jugando":
                    if i == 0:
                        print("*" * 5 + "Turno de " + lista_jugadores[i] + " (Banca) " + "*" * 5)
                    else:
                        print("*" * 5 + "Turno de " + lista_jugadores[i] + "*" * 5)
                    lista_jugadores_juego[i][lista_jugadores[i]][7] = lista_jugadores_juego[i][lista_jugadores[i]][7] + 1
                    if lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 1:
                        palo = "Oros"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 2:
                        palo = "Copas"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 3:
                        palo = "Bastos"
                    elif lista_jugadores_juego[i][lista_jugadores[i]][0][0][1] == 4:
                        palo = "Espadas"
                    print("Tu carta inicial:", lista_jugadores_juego[i][lista_jugadores[i]][0][0][0], "de", palo)
                    input("Pulsa ENTER para continuar")
                    print("")
                    print("Cartas que han salido:")
                    for j in cartas_que_han_salido:
                        if j[1] == 1:
                            print(j[0], "de Oros")
                        elif j[1] == 2:
                            print(j[0], "de Copas")
                        elif j[1] == 3:
                            print(j[0], "de Bastos")
                        elif j[1] == 4:
                            print(j[0], "de Espadas")
                    print("-"*50)
                    print("Puntos totales de cada jugador y puntos apostados:")
                    for k in range(len(lista_jugadores_juego)):
                        if k == 0:
                            print(lista_jugadores[k] + " (Banca): Puntos totales=",
                                  lista_jugadores_juego[k][lista_jugadores[k]][6])
                        else:
                            print(lista_jugadores[k] + ": Puntos totales=",
                                  lista_jugadores_juego[k][lista_jugadores[k]][6],
                                  ", Puntos apostados=", lista_jugadores_juego[k][lista_jugadores[k]][5])
                    print("-"*50)
                    apuesta_valida = False
                    # Crecimiento de apuestas:
                    # Mano 1 - 5: Apuesta min.: 2 ptos. - Apuesta max.: 5  ptos.
                    # Mano 6 - 12: Apuesta min.: 3 ptos. - Apuesta max.: 6 ptos.
                    # Mano 13 - 18: Apuesta min.: 4 ptos. - Apuesta max.: 8 ptos.
                    # Mano 19 - 25: Apuesta min.: 5ptos. - Apuesta max.: 10ptos.
                    # Mano 26 - 30: Apuesta min.: 6ptos. - Apuesta max.: 12ptos.
                    if lista_jugadores_juego[i][lista_jugadores[i]][7] >= 1 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 5:
                        apuesta_minima = 2
                        apuesta_maxima = 5
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 6 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 12:
                        apuesta_minima = 3
                        apuesta_maxima = 6
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 13 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 18:
                        apuesta_minima = 4
                        apuesta_maxima = 8
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 19 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 25:
                        apuesta_minima = 5
                        apuesta_maxima = 10
                    elif lista_jugadores_juego[i][lista_jugadores[i]][7] >= 26 and \
                            lista_jugadores_juego[i][lista_jugadores[i]][7] <= 30:
                        apuesta_minima = 6
                        apuesta_maxima = 12
                    if i != 0:
                        if lista_jugadores_juego[i][lista_jugadores[i]][8]=="humano":
                        #Si el jugador es bot su apuesta será random entre el rango de apuesta
                            while apuesta_valida == False:
                                if lista_jugadores_juego[i][lista_jugadores[i]][6] < apuesta_minima:
                                    print( "La apuesta mínima es mayor que tus puntos restantes. Debes apostar todos tus puntos")
                                    apuesta_minima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                                    apuesta_maxima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                                apuesta = int(input("Cuantos puntos quieres apostar? (min. " + str(apuesta_minima) + " , max." + str(apuesta_maxima) + ") "))
                                if apuesta < apuesta_minima or apuesta > apuesta_maxima:
                                    print("Mínimo=", apuesta_minima, ", Máximo=", apuesta_maxima)
                                elif lista_jugadores_juego[i][lista_jugadores[i]][6] - apuesta < 0:
                                    print("No puedes apostar más puntos de los que tienes")
                                else:
                                    apuesta_valida = True
                        else:
                            if lista_jugadores_juego[i][lista_jugadores[i]][6] < apuesta_minima:
                                apuesta_minima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                                apuesta_maxima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                            apuesta=random.randint(apuesta_minima,apuesta_maxima)
                            print("Apuesta de "+lista_jugadores[i]+": "+str(apuesta)+" puntos")
                            input("Presiona ENTER para continuar")
                        lista_jugadores_juego[i][lista_jugadores[i]][5] = apuesta
                        lista_jugadores_juego[i][lista_jugadores[i]][6] = lista_jugadores_juego[i][lista_jugadores[i]][6] - apuesta
                    while lista_jugadores_juego[i][lista_jugadores[i]][1] == "jugando":
                        print("Puntos acumulados en la mano=", lista_jugadores_juego[i][lista_jugadores[i]][4])
                        if lista_jugadores_juego[i][lista_jugadores[i]][8]=="humano":
                            opcion = int(input("Qué quieres hacer?\n1) Pedir Carta\n2) Plantarme\n"))
                            while opcion < 1 or opcion > 2:
                                opcion = int(input("Opción incorrecta!\n"))
                        else:
                            if lista_jugadores_juego[i][lista_jugadores[i]][4]<lista_jugadores_juego[0][lista_jugadores[0]][4]:
                            #Si el bot tiene menos puntos en la mano que la banca siempre pedirá carta
                                opcion=1
                            else:
                                cartas_no_pasarte=0
                                for j in range(len(mazo)):
                                #Si al sumar el valor en el juego de la carta más los puntos en la mano no se pasa de 7,5 se sumará 1 al contador
                                    if lista_jugadores_juego[i][lista_jugadores[i]][4]+mazo[j][2]<=7.5:
                                        cartas_no_pasarte=cartas_no_pasarte+1
                                #Probabilidad de no pasarte
                                probabilidad=cartas_no_pasarte/len(mazo)
                                if probabilidad>0.65:
                                #Si la probabilidad es mayor de 65% siempre pedirá carta
                                    opcion=1
                                elif probabilidad>=0.50 and probabilidad<=0.65:
                                #Si la probabilidad está entre 50% y 65% siempre pedirá carta
                                    opcion=1
                                elif probabilidad<0.50:
                                #Si la probabilidad es menor de 50% siempre se plantará
                                    opcion=2
                        if opcion == 2:
                            lista_jugadores_juego[i][lista_jugadores[i]][1] = "plantado"
                            if lista_jugadores_juego[i][lista_jugadores[i]][8]=="bot":
                                print(lista_jugadores[i],"se ha plantado")
                                input("Presiona ENTER para continuar")
                        elif opcion == 1:
                            carta = random.choice(mazo)
                            cartas_que_han_salido.append(carta)
                            mazo.remove(carta)
                            if carta[1] == 1:
                                palo = "Oros"
                            elif carta[1] == 2:
                                palo = "Copas"
                            elif carta[1] == 3:
                                palo = "Bastos"
                            elif carta[1] == 4:
                                palo = "Espadas"
                            if lista_jugadores_juego[i][lista_jugadores[i]][8]=="bot":
                                print(lista_jugadores[i],"ha pedido carta")
                            print("Carta que ha salido:", carta[0], "de", palo)
                            input("Presiona ENTER para continuar")
                            lista_jugadores_juego[i][lista_jugadores[i]][0].append(carta)
                            lista_jugadores_juego[i][lista_jugadores[i]][4] = \
                            lista_jugadores_juego[i][lista_jugadores[i]][4] + carta[2]
                            if lista_jugadores_juego[i][lista_jugadores[i]][4] > 7.5:
                                if lista_jugadores_juego[i][lista_jugadores[i]][8]=="humano":
                                    print("Te has pasado de 7,5!")
                                else:
                                    print(lista_jugadores[i],"se ha pasado de 7,5")
                                lista_jugadores_juego[i][lista_jugadores[i]][1] = "eliminado"
                                input("Presiona ENTER para continuar")
            banca_cambiada = False
            if lista_jugadores_juego[0][lista_jugadores[0]][1] == "eliminado":
                for i in range(1, len(lista_jugadores_juego)):
                    if lista_jugadores_juego[i][lista_jugadores[i]][1] == "eliminado":
                        lista_jugadores_juego[0][lista_jugadores[0]][6] = lista_jugadores_juego[0][lista_jugadores[0]][6] + lista_jugadores_juego[i][lista_jugadores[i]][5]
                    else:
                        if lista_jugadores_juego[i][lista_jugadores[i]][4] == 7.5:
                            if lista_jugadores_juego[0][lista_jugadores[0]][6] <lista_jugadores_juego[i][lista_jugadores[i]][5] and lista_jugadores_juego[0][lista_jugadores[0]][6] != 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] =lista_jugadores_juego[i][lista_jugadores[i]][6] + lista_jugadores_juego[i][lista_jugadores[i]][5] + lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = 0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6] == 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] =lista_jugadores_juego[i][lista_jugadores[i]][6] + lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] =lista_jugadores_juego[i][lista_jugadores[i]][6] + 3 * lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] =lista_jugadores_juego[0][lista_jugadores[0]][6] - lista_jugadores_juego[i][lista_jugadores[i]][5]
                            if banca_cambiada == False:
                                nueva_posicion = lista_jugadores_juego[0]
                                nueva_posicion2 = lista_jugadores[0]
                                nueva_banca = i
                                banca_cambiada = True
                        else:
                            if lista_jugadores_juego[0][lista_jugadores[0]][6] < \
                                    lista_jugadores_juego[i][lista_jugadores[i]][5] and \
                                    lista_jugadores_juego[0][lista_jugadores[0]][6] != 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5] + \
                                lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = 0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6] == 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + 2 * \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = \
                                lista_jugadores_juego[0][lista_jugadores[0]][6] - \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
            elif lista_jugadores_juego[0][lista_jugadores[0]][4] == 7.5:
                for i in range(1, len(lista_jugadores_juego)):
                    lista_jugadores_juego[0][lista_jugadores[0]][6] = lista_jugadores_juego[0][lista_jugadores[0]][6] + \
                                                                      lista_jugadores_juego[i][lista_jugadores[i]][5]
            else:
                for i in range(1, len(lista_jugadores_juego)):
                    if lista_jugadores_juego[i][lista_jugadores[i]][1] == "eliminado":
                        lista_jugadores_juego[0][lista_jugadores[0]][6] = lista_jugadores_juego[0][lista_jugadores[0]][
                                                                              6] + \
                                                                          lista_jugadores_juego[i][lista_jugadores[i]][
                                                                              5]
                    elif lista_jugadores_juego[0][lista_jugadores[0]][4] >= \
                            lista_jugadores_juego[i][lista_jugadores[i]][4]:
                        lista_jugadores_juego[0][lista_jugadores[0]][6] = lista_jugadores_juego[0][lista_jugadores[0]][
                                                                              6] + \
                                                                          lista_jugadores_juego[i][lista_jugadores[i]][
                                                                              5]
                    else:
                        if lista_jugadores_juego[i][lista_jugadores[i]][4] == 7.5:
                            if lista_jugadores_juego[0][lista_jugadores[0]][6] < \
                                    lista_jugadores_juego[i][lista_jugadores[i]][5] and \
                                    lista_jugadores_juego[0][lista_jugadores[0]][6] != 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5] + \
                                lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = 0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6] == 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + 3 * \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = \
                                lista_jugadores_juego[0][lista_jugadores[0]][6] - \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                            if banca_cambiada == False:
                                nueva_posicion = lista_jugadores_juego[0]
                                nueva_posicion2 = lista_jugadores[0]
                                nueva_banca = i
                                banca_cambiada = True
                        else:
                            if lista_jugadores_juego[0][lista_jugadores[0]][6] < \
                                    lista_jugadores_juego[i][lista_jugadores[i]][5] and \
                                    lista_jugadores_juego[0][lista_jugadores[0]][6] != 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5] + \
                                lista_jugadores_juego[0][lista_jugadores[0]][6]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = 0
                            elif lista_jugadores_juego[0][lista_jugadores[0]][6] == 0:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                            else:
                                lista_jugadores_juego[i][lista_jugadores[i]][6] = \
                                lista_jugadores_juego[i][lista_jugadores[i]][6] + 2 * \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
                                lista_jugadores_juego[0][lista_jugadores[0]][6] = \
                                lista_jugadores_juego[0][lista_jugadores[0]][6] - \
                                lista_jugadores_juego[i][lista_jugadores[i]][5]
            if banca_cambiada == True:
                lista_jugadores_juego[nueva_banca], lista_jugadores_juego[0] = lista_jugadores_juego[0], \
                                                                               lista_jugadores_juego[nueva_banca]
                lista_jugadores[nueva_banca], lista_jugadores[0] = lista_jugadores[0], lista_jugadores[nueva_banca]
                lista_jugadores_juego.remove(nueva_posicion)
                lista_jugadores.remove(nueva_posicion2)
                lista_jugadores_juego.append(nueva_posicion)
                lista_jugadores.append(nueva_posicion2)
            for i in range(len(lista_jugadores_juego)):
                lista_jugadores_juego[i][lista_jugadores[i]][5] = 0
                lista_jugadores_juego[i][lista_jugadores[i]][0] = []
                lista_jugadores_juego[i][lista_jugadores[i]][4] = 0
                lista_jugadores_juego[i][lista_jugadores[i]][1] = "jugando"
            for i in range(len(lista_jugadores_juego)):
                if lista_jugadores_juego[i][lista_jugadores[i]][6] == 0:
                    lista_jugadores_juego[i][lista_jugadores[i]][1] = "eliminado"
                    lista_jugadores_juego[i][lista_jugadores[i]][2] = "eliminado"
                    eliminado = lista_jugadores_juego[i]
                    eliminado2 = lista_jugadores[i]
                    lista_jugadores_juego.remove(eliminado)
                    lista_jugadores.remove(eliminado2)
                    lista_jugadores_juego.append(eliminado)
                    lista_jugadores.append(eliminado2)

            for i in range(len(cartas_que_han_salido)):
                mazo.append(cartas_que_han_salido[i])
            cartas_que_han_salido = []
            for i in range(len(lista_jugadores_juego)):
                lista_jugadores_juego[i][lista_jugadores[i]][3] = i
            contador = 0
            for i in range(len(lista_jugadores_juego)):
                if lista_jugadores_juego[i][lista_jugadores[i]][2] == "jugando":
                    contador = contador + 1
            if contador <= 1 or lista_jugadores_juego[0][lista_jugadores[0]][7] == 30:
                partida = False
            else:
                print("Orden y puntuación de cada jugador:")
                for i in range(len(lista_jugadores_juego)):
                    if i == 0:
                        print(str(i) + ". " + lista_jugadores[i] + " (Banca) - " + str(
                            lista_jugadores_juego[i][lista_jugadores[i]][6]) + " puntos")
                    elif lista_jugadores_juego[i][lista_jugadores[i]][2] == "eliminado":
                        print(str(i) + ". " + lista_jugadores[i] + " - " + str(
                            lista_jugadores_juego[i][lista_jugadores[i]][6]) + " puntos (eliminado)")
                    else:
                        print(str(i) + ". " + lista_jugadores[i] + " - " + str(
                            lista_jugadores_juego[i][lista_jugadores[i]][6]) + " puntos")
                input("Presiona ENTER para continuar")
        punt_maxima = 0
        for i in range(len(lista_jugadores_juego)):
            if lista_jugadores_juego[i][lista_jugadores[i]][6] > punt_maxima:
                punt_maxima = lista_jugadores_juego[i][lista_jugadores[i]][6]
                ganador = lista_jugadores[i]
        print("Ha ganado", ganador, "!!!")