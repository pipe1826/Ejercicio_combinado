#ejercicio 1
def pedir_numeros(cantidad):
    numeros = []
    for x in range(cantidad):
        while True:
            try:
                numero = int(input(f"Ingrese el {x+1}° número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Debe ingresar un número entero.")

    return numeros
def calcular_suma_y_promedio(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio

def mostrar_resultados(numeros, suma, promedio):
    print("\nNúmeros ingresados:", numeros)
    print("Suma:", suma)
    print("Promedio:", promedio)

def main():
    numeros = pedir_numeros(5)
    suma, promedio = calcular_suma_y_promedio(numeros)
    mostrar_resultados(numeros, suma, promedio)

main()