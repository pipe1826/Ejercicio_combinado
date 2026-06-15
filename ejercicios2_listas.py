def pedir_numeros(cantidad):
    numeros = []

    for x in range(cantidad):
        while True:
            try:
                numero = int(input(f"Ingrese el {x+1}° número a registrar: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Debe ingresar un número entero.")

    return numeros


def encontrar_mayor_menor(numeros):
    mayor = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    return mayor, menor


def mostrar_resultados(numeros, mayor, menor):
    print("\nLista:", numeros)
    print("Número mayor:", mayor)
    print("Número menor:", menor)
    print("Cantidad de elementos:", len(numeros))


def main():
    numeros = pedir_numeros(8)
    mayor, menor = encontrar_mayor_menor(numeros)
    mostrar_resultados(numeros, mayor, menor)


main()
