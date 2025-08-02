#Ejercicio 2, Nina Nájera, Jorge Palacios
def esta_balanceada(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    print("------------------------------------------------------------------")
    print(f"Expresión en el txt: {expresion}")

    for i, char in enumerate(expresion):
        if char in '([{':
            pila.append(char)
            print(f"Paso {i+1}: '{char}' agregado a la pila {pila}")
        elif char in ')]}':
            if pila and pila[-1] == pares[char]:
                pila.pop()
                print(f"Paso {i+1}: '{char}' pasa, se saca de la pila {pila}")
            else:
                print(f"Paso {i+1}: '{char}' no pasa o pila vacía {pila}")
                return False
        else:
            print(f"Paso {i+1}: '{char}' se ignora")

    if not pila:
        print("Resultado: Balanceada")
        return True
    else:
        print(f"Resultado: No balanceada, se queda en pila {pila}")
        return False

def procesar_archivo(txt):
    with open(txt, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea = linea.strip()
        esta_balanceada(linea)

if __name__ == "__main__":
    procesar_archivo("expresiones.txt")