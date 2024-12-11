
import os

PALOS = ('Corazones', 'Picas', 'Tréboles', 'Diamantes')

CARTAS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

VALORES = {'As':(1, 11), '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

PUNTOS_OBJETIVO = 21
CARTAS_AL_INICIO = 1


def borrar_consola():
    """ Limpiar la consola.
        * Esta función ya está terminada y funciona correctamente!
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pulse_tecla_para_continuar():
    """ Mostrar el mensaje Presione una tecla para continuar y hacer una pausa hasta que se realice la acción.
        * Esta función ya está terminada y funciona correctamente!
    """
    os.system("pause")


def crear_baraja() -> set:
    """ Crear la baraja de 52 cartas (debe retornar un conjunto de tuplas (carta, palo) construida desde PALOS y CARTAS)
    """
    baraja = set()
    for palo in PALOS:
        for carta in CARTAS:
            baraja.add((palo, carta))

    return baraja

def reparte_carta(baraja: set) -> tuple:
    """ Reparte una carta de la baraja (debe extraer una carta del conjunto 'baraja' y retornarla... esta carta debe eliminarse de la baraja)
        * Captura las posibles Excepciones... si se produce, debe mostrar un mensaje de error "*Error* la baraja no tiene cartas" y retornar None
    """
    try:
        carta = baraja.pop()

        return carta
    except KeyError:
        print("*Error* la baraja no tiene cartas")
    return None
        

def dame_carta(baraja: set, cartas_jugador: list) -> bool:
    """ Pide una carta, la guarda en la lista del jugador y retorna True o retorna False si la baraja se ha quedado sin cartas.
        * Utiliza aquí la función reparte_carta() y controla el resultado que te da.
    """
    cartas_jugador = []
    if reparte_carta(baraja):
        cartas_jugador.append(reparte_carta(baraja))
        return True
    else:
        return False


def contesta_a_pregunta(mensaje: str) -> bool:
    """ Hace una pregunta de si o no (retorna True si la respuesta es afirmativa)
        * Las respuestas válidas serán 's', 'si', 'n' o 'no'.
        * Si la respuesta no es válida mostrará el mensaje "*Error* respuesta no válida (s, si, n, no)") y volverá a preguntar.
    """
    finalizar = False
    while not finalizar:
        try:
            mensaje = input(">>> ").strip().lower()
            if mensaje == 's' or mensaje == 'si':
                return True
            elif mensaje == 'n' or mensaje == 'no':
                return False
            else:
                raise ValueError("*Error* respuesta no válida (s, si, n, no)")
        except ValueError as e:
            print(f"ERROR. {e}")
            


def pedir_carta(baraja: set, cartas_jugador: list) -> bool:
    """ Pregunta si quiere una carta o se planta ("¿Quieres una carta? (s/n) ")
        * Utiliza aquí la función contesta_a_pregunta y si retorna True, realiza una llamada a dame_carta() retornando el resultado de su ejecución.
        * Si contesta no, solo debes retornar False.
    """



def actualizar_puntos_comodines(cartas_jugador: list, puntos: int) -> int:
    """ Actualizar los puntos con las cartas que tengan más de un valor
        * Esta función ya está terminada y funciona correctamente!
    """
    for carta in cartas_jugador:       
        if puntos < puntos - valor_carta(carta[0]) + valor_carta(carta[0], False) <= PUNTOS_OBJETIVO:
            puntos = puntos - valor_carta(carta[0]) + valor_carta(carta[0], False)
    return puntos


def valor_carta(carta: tuple, valor_minimo = True) -> int:
    """ Retornar el valor de una carta, si tiene más de uno retornará el valor mínimo o máximo dependiendo de valor_minimo
        * Si el tipo de VALORES[carta] es una tupla y tiene 2 elementos, retorna el valor mínimo de los elementos si valor_minimo es True, sino retorna el valor máximo
        * Si el tipo de VALORES[carta] no es una tupla, retorna simplemente su valor.
        * La constante VALORES es un diccionario!!!
    """



def calcular_puntos(cartas_jugador: list) -> tuple[bool, int]:
    """ Calcular los puntos de las cartas del jugador
        * Acumula en la variable puntos el valor de los puntos totales de las cartas del jugador (utiliza en el bucle for la función valor_carta() que te devolverá el valor mínimo de la carta)
        * Después de sumar los puntos de las cartas con valores mínimos, actualiza esos mismos puntos realizando la llamada a la función actualizar_puntos_comodines()
        * Retornar la tupla con el valor True/False si los puntos superan los PUNTOS_OBJETIVO y el valor de puntos
    """



def mostrar_cartas(jugador: str, puntos: int, cartas_jugador: list):
    """ Mostrar los puntos y cartas de un jugador
        * Imprime por consola en la primera línea el nombre del Jugador (variable jugador)
        * En la siguiente línea tantos guiones (-) como sea el tamaño de la variable jugador.
        * A continuación el número de puntos (con un tabluador antes, es decir, usa \t).
        * Debajo de los puntos, en las siguientes filas, muestra la carta y palo de cada una de las cartas de cartas_jugador (también está identado con un tabulador).

        * Por ejemplo, si se trata de jugador = "Jugador 1", puntos = 6 y cartas_jugador = [('2', 'Tréboles'), ('4', 'Corazones')]:

        Jugador 1
        ---------
                6 puntos >>
                2 de Tréboles
                4 de Corazones
    """



def mostrar_resultado(cartas_jugador1, puntosJ1, cartas_jugador2, puntosJ2):
    """ Mostrar el resultado final del juego:
        * limpia la pantalla.
        * muestra las cartas de cada jugador (utiliza mostrar_cartas())
        * Imprime un salto de línea (usa print vacío)
        * Si los puntos de ambos jugadores han superado los puntos objetivo, imprimirá "¡Los dos os habéis pasado!"
        * Sino, si los puntos del jugador 2 ha superado los puntos objetivo, imprimirá "¡Jugador 1 GANA!"
        * Sino, si los puntos del jugador 1 ha superado los puntos objetivo, imprimirá "¡Jugador 2 GANA!"
        * Sino, si los puntos del jugador 1 son superiores a los puntos del jugador 2, imprimirá "¡Jugador 1 GANA!"
        * Sino, si los puntos del jugador 2 son superiores a los puntos del jugador 1, imprimirá "¡Jugador 2 GANA!"
        * Sino, imprimirá "¡Habéis empatado!"
        * Imprime un salto de línea (usa print vacío)
        * Realiza una pausa hasta que se pulse una tecla, es decir, llama a la función pulse_una_tecla_para_continuar()
        * limpia la pantalla.
    """



def jugar(baraja: set):
    """ Jugar al black jack entre dos jugadores
        * Crea las siguientes variables:
           - ronda (asígnale el valor 1)
           - cartas_jugador1 (lista vacía)
           - cartas_jugador2 (lista vacía)
           - puntosJ1 (asígnale el valor  0)
           - puntosJ2 (asígnale el valor  0)
        * Realiza un bucle y reparte tantas cartas como indique la constante CARTAS_INICIO a cada jugador (usa la función dame_carta)
        * Utiliza el retorno de dame_carta NEGADO para asignar el valor de las variables finJ! y finJ2.
        * Haz un bucle Mientras finJ1 o finJ2 tengan un valor False
           - Dentro del bucle:
              * suma 1 a la variable ronda.
              * limpia la pantalla.
              * Imprime en que ronda estamos ("RONDA: 2") y después un salto de línea (usa "\n").
              * Si el jugador 1 no se ha plantado, es decir, si finJ1 es False... utiliza la función calcular_puntos con las cartas del jugador 1 y la tupla que retorna asignala a finJ1 y puntosJ1.
              * Si el jugador 2 no se ha plantado, es decir, si finJ2 es False... utiliza la función calcular_puntos con las cartas del jugador 2 y la tupla que retorna asignala a finJ2 y puntosJ2.
              * Si el jugador 1 no se ha plantado, es decir, si finJ1 es False... mostrar las cartas del jugador 1 y pedir otra carta (el resultado NEGADO de su ejecución se volverá a asignar 
              a finJ1).
              * Si el jugador 2 no se ha plantado, es decir, si finJ2 es False... mostrar las cartas del jugador 2 y pedir otra carta (el resultado NEGADO de su ejecución se volverá a asignar a finJ2).
            - Fuera del bucle While... mostrar el resultado final de la partida
    """



def main():
    """
    Crear una baraja y asignarla a la variable baraja.
    Hacer un bucle que ejecute la función jugar() y después preguntar "¿Quieres jugar otra partida? (s/n) " (función contestar_a_pregunta)
    (el resultado es que jugará partidas hasta que responda no o n a la pregunta)
    """
    

if __name__ == "__main__":
    main()