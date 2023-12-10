# importamos la funcion random para la generacion de numeros aleatorios
import random
import math

def is_ganador(jugador, oponente):
    # Devolver True si el jugador le gana a la pc
    # Condiciones para ganar: p > t, t > pa, pa > p
    if (jugador == 'p' and oponente == 't') or (jugador == 't' and oponente == 'pa') or (jugador == 'pa' and oponente == 'p'):
        return True
    return False

def jugar():
    usuario = input("Elige una opcion: 'p' para piedra, 'pa' para papel, o 't' para tijeras")
    usuario = usuario.lower()
    
    elementos = ['p', 'pa', 't']
    pc = random.choice(elementos)
    
    if usuario == pc:
        return 0, usuario, pc
    
    if is_ganador(usuario, pc):
        return 1, usuario, pc
    
    return -1, usuario, pc

# Para ganar el juego, ceil(n/2) (ie. 2/3, 3/5, 4/7)
def el_mejor_jugador(n):
    jugador_contar = 0
    pc_contar = 0
    para_ganar = math.ceil(n / 2)

    while jugador_contar < para_ganar and pc_contar < para_ganar:
        resultado, usuario, pc = jugar()

        # Empate
        if resultado == 0:
            print("Es un empate. Tú y la PC han elegido {}".format(usuario))
        # Jugador gana a la PC
        elif resultado == 1:
            jugador_contar += 1
            print("Tú has elegido {} y la PC {}. ¡Ganaste!".format(usuario, pc))
        else:
            pc_contar += 1
            print("Tú has elegido {} y la PC {}. ¡Perdiste!".format(usuario, pc))

    if jugador_contar > pc_contar:
        print("Has ganado los mejores de {} juegos. ¡Bien hecho!".format(n))
    else:
        print("La PC ha ganado los mejores de {} juegos. ¡Éxito la próxima vez!".format(n))

if __name__ == "__main__":
    el_mejor_jugador(5)
