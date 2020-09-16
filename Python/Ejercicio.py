##juego 21 con recursividad
import numpy as np
##reglas de juego
#jugadores = 2
    #jugador repartidor
repartidor = []
    #jugador no repartidor
jugador = []
#repartir Cartas
#cartas repartidor
while len(repartidor) !=2:
    repartidor.append(np.random.randint(1,11))
    if len(repartidor) == 2:
        print("cartas del repartidor ", repartidor[1])
#cartas del jugador1
while len(jugador) !=2:
    jugador.append(np.random.randint(1,11))
    if len(jugador) == 2:
        print("cartas del jugador ", jugador)
#mostrar cartas

#funcion aumento 
def aumento(cartas):
    if sum(np.array(cartas)) >= 17:
        print("repartidor tiene: ", sum(np.array(cartas)), " repartidor stop")
        return cartas
    else:
        print("repartidor tiene: ", sum(np.array(cartas)), " repartidor aumenta")
        np.array(cartas.append(np.random.randint(1,11)))        
        return aumento(cartas)
#suma de las cartas del jugador
if sum(jugador) == 21:
    print("jugador tiene: ", jugador + "Gana")
elif sum(jugador) > 21:
    print("jugador tiene: ", jugador + "jugador pierde")
while sum(jugador) < 21:
    Accion = str(input("Carta o no carta? (responda si o no )"))
    if Accion == 'si':        
        jugador.append(np.random.randint(1,11))
        print("tiene un total de: " + str(sum(jugador)) + " con", jugador)
    else:
        print("repartidor tiene: ", repartidor)
        print("jugador tiene: ", jugador)                
        repartidor_aumentado = aumento(repartidor)
        if (sum(np.array(repartidor_aumentado))<21) and (sum(np.array(repartidor_aumentado)) > sum(jugador)):
            print("jugador pierde")
        else:
            print("jugador gana")
            break

#suma de cartas del repartidor
if sum(repartidor) ==21:
    print("repartidor tiene 21 gana repartidor")
elif sum(repartidor) > 21:
    print("repartidor se paso repartidor pierde")

if sum(jugador) > 21:
    print("Jugador1 pierde")
elif sum(jugador) == 21:
    print("21 jugador1 Gana")

#comparar las sumas de los valores de cada jugador
# Si la suma de las cartas del J es mayor que 21 = pierde 
# Si la suma de las cartas del J es menor que 21 = obción pedir o quedarse
    # Si la opción es quedarse, entonces comparar la suma de las cartas del repartidor contra la suma de las cartas del jugador
    # Si la opción es pedir 
        # sumP < 21 and > sum D entonces gana
        # sumP < sum D entonces pierde        