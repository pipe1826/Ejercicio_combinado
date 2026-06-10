estudiantes = {}
while True:
    print("""
    1. Agregar estudiante
    2. Agregar nota
    3. Mostrar estudiantes
    4. Mostrar promedio de un estudiante
    5. Mostrar todos los promedios
    6. Salir""")

    opc = input("Seleccione una opción: ").strip()

    if opc == "1":
        nombre = input("Nombre del estudiante: ").strip().title()
        if nombre in estudiantes:
            print("Error: El estudiante ya existe.")
        else:
            estudiantes[nombre] = []
            print(f"{nombre} agregado correctamente.")
    elif opc == "2":
        nombre = input("Nombre del estudiante: ").strip().title()
        if nombre not in estudiantes:
            print("Error: Estudiante no encontrado.")
        else:
            try:
                nota = float(input("Ingrese la nota: ").strip())

                if 1.0 <= nota <= 7.0:
                    estudiantes[nombre].append(nota)
                    print("Nota agregada correctamente.")
                else:
                    print("Error: La nota debe estar entre 1.0 y 7.0.")

            except ValueError:
                print("Error: Debe ingresar una nota válida.")
    elif opc == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nEstudiantes:")
            for nombre in estudiantes:
                print(nombre)
    elif opc == "4":
        nombre = input("Nombre del estudiante: ").strip().title()

        if nombre not in estudiantes:
            print("Error: Estudiante no encontrado.")
        elif len(estudiantes[nombre]) == 0:
            print("El estudiante no tiene notas.")
        else:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"{nombre} -> Promedio: {promedio:.2f}")
    elif opc == "5":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nPromedios:")
            for nombre, notas in estudiantes.items():
                if len(notas) > 0:
                    promedio = sum(notas) / len(notas)
                    print(f"{nombre} -> {promedio:.2f}")
                else:
                    print(f"{nombre} -> Sin notas")
    elif opc == "6":
        print("Gracias por usar el programa")
        break
    else:
        print("ERROR!, Debe ingresar una opcion entre (1-6)")
    