"""
Ejercicio compuesto de un menú en el que cada opción ejecuta una función diferente.
"""
def pedir_entero(msj: str) -> int:

    while True:
        try:    
            entero = int(input(msj))
            return entero
        except ValueError:
            print("Eso no es un número entero.")

def pedir_nombre(msj: str) -> str:
    finalizar = False
    while not finalizar:
        try:
            nombre = input(msj).strip().lower()
            if nombre == "":
                raise ValueError("No puede estar vacio.")
            for letra in nombre:
                if letra.isdigit():
                    raise ValueError("No puede contener números.")
            
            return nombre
        except ValueError as e:
            print(f"ERROR-> {e}")


def pedir_precio(msj: str) -> float:
    while True:
        try:    
            precio = float(input(msj))
            return precio
        except ValueError:
            print("Eso no es un número decimal.")



def pedir_datos() -> dict:
    nombre = pedir_nombre("Dame tu nombre: ")
    edad = pedir_entero("Dame tu edad: ")

    return nombre, edad




def main():
    numeros = list()
    precios = set()
    datos = dict()

    finalizar = False
    while not finalizar:
        try:
            opcion = input("Elige 'numeros', 'precios', o 'datos' para ir agregándolos a los conjuntos.\n>>> ").strip().lower()
            if opcion == "numeros":
                entero = pedir_entero("Dame un entero: ")
                numeros.append(entero)
            elif opcion == "precios":
                precio = pedir_precio("Introduce un decimal: ")
                precios.add(precio)
            elif opcion == "datos":
                nombre, edad = pedir_datos()
                datos.update({nombre : edad})
            elif opcion == "fin":
                print("Adios!!!")
                finalizar = True
            else:
                raise ValueError("El comando no existe.")
            
            print(numeros)
            print(precios)
            print(datos)
        except ValueError as e:
            print(f"ERROR-> {e}")
        except Exception:
            print("ERROR no controlado")

            
if __name__ == "__main__":
    main()