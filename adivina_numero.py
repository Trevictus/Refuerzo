



import os
from random import randint
rango_num_aleatorio = 50

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

def generar_numero_aleatorio() -> int:
    numero_aleatorio = randint(0, rango_num_aleatorio)
    return numero_aleatorio


def pedir_entero() -> int:
    while True:
        try:    
            entero = int(input(">>> "))
            return entero
        except ValueError:
            print("Eso no es un número entero.")


def validar_entero(entero: int) -> bool:
    try:
        if rango_num_aleatorio >= entero >= 0:
            return True
        else:
            raise ValueError("No está dentro del rango permitido.")
    except ValueError as e:
        print(f"ERROR. {e}")

def dar_pista() -> str:
    pass


def calcular_intentos() -> str:
    pass


def jugar():
    pass


def opciones():
    pass


def main():
    finalizar = False
    borrar_consola()
    while not finalizar:
        try:
            print(menu())
            opcion = input("-->").strip().lower()
            if opcion == "1" or opcion == "jugar":
                jugar()
            elif opcion == "2" or opcion == "opciones":
                opciones()
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