numeros = []

for x in range(8):
    while True:
        try:
            numero = int(input(f"Ingrese el {x+1} número a registrar: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Error: Debe ingresar un número entero.")

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

print("\nLista:", numeros)
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Cantidad de elementos:", len(numeros))