def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()

        if len(nombre) < 6:
            print("El nombre debe tener al menos 6 caracteres.")

        elif not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras.")

        else:
            return nombre.title()


def agregar_estudiante(estudiantes):
    nombre = validar_nombre()

    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes.append(nombre)
        print("Estudiante agregado correctamente.")


def buscar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()

    if nombre in estudiantes:
        print(f"{nombre} se encuentra registrado.")
    else:
        print("Estudiante no encontrado.")


def eliminar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().title()

    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print("Estudiante eliminado correctamente.")
    else:
        print("Estudiante no encontrado.")


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\nLista de estudiantes:")

    for i, nombre in enumerate(estudiantes, start=1):
        print(f"{i}. {nombre}")


def menu():
    estudiantes = []

    while True:
        print("""
1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Mostrar estudiantes
5. Salir
""")

        opc = input("Seleccione una opción: ")

        if opc == "1":
            agregar_estudiante(estudiantes)

        elif opc == "2":
            buscar_estudiante(estudiantes)

        elif opc == "3":
            eliminar_estudiante(estudiantes)

        elif opc == "4":
            mostrar_estudiantes(estudiantes)

        elif opc == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida, debe elegir entre 1 y 5.")


menu()