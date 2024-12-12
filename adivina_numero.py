



import os
from random import randint
CONFIG_DEFECTO = {"min": 0, "max": 50, "intentos": 5}

def borrar_consola():
    """ Limpiar la consola.
        * Esta función ya está terminada y funciona correctamente!
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")



def menu():
    return """***Bienvenido a 'ADIVINA EL NÚMERO'***
   --------------------------------
   1>> Jugar.
   2>> Opciones.
   3>> Salir.
           """

def generar_numero_aleatorio(min: int, max: int) -> int:
    numero_aleatorio = randint(min, max)
    return numero_aleatorio


def pedir_entero() -> int:
    while True:
        try:    
            entero = int(input("Introduce número a adivinar: "))
            return entero
        except ValueError:
            print("Eso no es un número válido.")


def validar_entero(entero: int) -> bool:
    try:
        if rango_num_aleatorio >= entero >= 0:
            return True
        else:
            raise ValueError("No está dentro del rango permitido.")
    except ValueError as e:
        print(f"ERROR. {e}")

def dar_pista(numero: int, resolver: int) -> str:
    if resolver > numero - 5 and resolver < numero + 5:
        print("")
    elif resolver > numero - 10 and resolver < numero + 5:


def calcular_intentos() -> str:
    pass



def jugar(configuracion: dict):
    numero = generar_numero_aleatorio(configuracion["min"], configuracion["max"])
    numeros = set()

    while len(numeros) < configuracion["intentos"] and resolver != numero:
        try:
            resolver = pedir_entero()

            if resolver in numeros:
                print("Error")
            else:
                numeros.add(resolver)

            if resolver == numero:
                print(f"Has acertado el numero {numero} oculto.")
            else:
                pistas!!!
                print(f"Has fallado te quedan {configuracion["intentos"] - len(numeros)} intentos.")
            
        except Exception:
            print("ERROR inesperado.")



def opciones(configuracion: dict):
    pass


def main():
    finalizar = False
    borrar_consola()

    configuracion = CONFIG_DEFECTO

    while not finalizar:
        try:
            print(menu())
            opcion = input("-->").strip().lower()
            if opcion == "1" or opcion == "jugar":
                jugar(configuracion)
            elif opcion == "2" or opcion == "opciones":
                opciones(configuracion)
            elif opcion == "3" or opcion == "salir":
                borrar_consola()
                print("¡Hasta la proxima!")
                finalizar = True
            else:
                raise ValueError("Debes elegir una de las tres opciones.")
        except ValueError as e:
            borrar_consola()
            print(f"ERROR -> {e}")

if __name__ == "__main__":
    main()