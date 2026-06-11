#ejercicio 1
numeros = []

for x in range (5):
    while True:
        try:
            numero = int(input(f"Ingrese el {x+1} número: "))
            numeros.append(numero)
            break
        except:
            print("Debe ingresar un numero entero")
suma = sum(numeros)
promedio = suma / len(numeros)
("\nNúmeros ingresados:")
for r in numeros.values():
    print(r)
print("Suma:", suma)
print("Promedio:", promedio)
