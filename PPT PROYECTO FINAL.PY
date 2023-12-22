import random
import math

def is_ganador(jugador, oponente):
    # Determina si el jugador gana a la PC
    return (jugador == 'p' and oponente == 't') or (jugador == 't' and oponente == 'pa') or (jugador == 'pa' and oponente == 'p')

def mostrar_bienvenida():
    # Muestra un mensaje de bienvenida
    print("============================")
    print(" ¡Bienvenido(a) al juego!")
    print("============================")
    print("¡Vamos a divertirnos! Y juguemos con la PC. Piedra - Papel o Tijera")

def jugar():
    # Función para realizar una jugada
    # Mostrar el mensaje de bienvenida solo la primera vez
    if not hasattr(jugar, 'mensaje_mostrado') or not jugar.mensaje_mostrado:
        mostrar_bienvenida()
        jugar.mensaje_mostrado = True

    usuario = input("Elige una opcion: 'p' para piedra, 'pa' para papel, o 't' para tijeras.\n")
    usuario = usuario.lower()
    
    elementos = ['p', 'pa', 't']
    pc = random.choice(elementos)
    
    # Muestra la elección del jugador y la PC
    print(f"Tú has elegido: {usuario}")
    print(f"La PC eligió: {pc}")

    if usuario == pc:
        resultado = 0
        print("Es un empate.")
    elif is_ganador(usuario, pc):
        resultado = 1
        print("¡Ganaste!")
    else:
        resultado = -1
        print("¡Perdiste!")

    return resultado

def el_mejor_jugador(n):
    # Simula el juego varias veces y determina al ganador
    
    def jugar_iteracion():
        # Realiza una iteración del juego.
        return jugar()

    # Realiza el juego varias veces
    resultado_juegos = [jugar_iteracion() for _ in range(n)]
    
    # Cuenta los resultados
    jugador_contar = resultado_juegos.count(1)
    pc_contar = resultado_juegos.count(-1)

    # Determina al ganador
    if jugador_contar > pc_contar:
        print("Has ganado las {} mejores jugadas. ¡Bien hecho!".format(n))
    else:
        print("La PC ha ganado las mejores {} jugadas. ¡Éxito la próxima vez!".format(n))

if __name__ == "__main__":
    el_mejor_jugador(5)
