estudiantes = []
while True:
    print("""
    1. Agregar estudiante
    2. Buscar estudiante
    3. Eliminar estudiante
    4. Mostrar estudiantes
    5. Salir""")
    
    opc = input("Elige una opción na realizar: ")

    if opc == "1":
        nombre = input("Ingrese el nombre del alumno: ").strip().title()
        if nombre in estudiantes:
            print("El estudiante ya está registrado.")
        else:
            estudiantes.append(nombre)
            print("Estudiante agregado correctamente.")

    elif opc == "2":
        nombre = input("Ingrese el nombre del alumno que desea encontrar: ").strip().title()
        if nombre in estudiantes:
            print(f"{nombre} se encuentra registrado.")
        else:
            print("Estudiante no encontrado.")
    elif opc == "3":
        nombre = input("Ingrese el nombre a eliminar: ").strip().title()
        if nombre in estudiantes:
            estudiantes.remove(nombre)
            print("Estudiante eliminado correctamente.")
        else:
            print("Estudiante no encontrado.")
    elif opc == "4":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante)
    elif opc == "5":
        print("Gracias por usar el programa")
        break
    else:
        print("ERROR!, debe elegir una opcion entre (1- 5)")
