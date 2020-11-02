import csv
import os.path

def guardarDatos(archivo, campos):
    cargar = "si"
    lista_empleados = []
    while cargar == "si":
        empleado = {}
        for campo in campos:
            validar = True
            while validar:
                valor = input(f"Ingrese {campo} del empleado: ")
                if campo == 'Legajo' or campo == 'Total Vacaciones':
                    try:
                        valor = int(valor)
                        validar = False
                    except ValueError:
                        validar = True
                        print(f'El campo {campo} debe ser un numero')
                else:
                    validar = False
                empleado[campo] = valor     
        lista_empleados.append(empleado)

        cargar = input("Desea seguir agregando empleados? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        print(archivo_existe)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista_empleados)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def inicio():
    print("Ingrese el nombre del archivo")
    archivo = input("")
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    VACACIONES = 'dias.csv'

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            guardarDatos(archivo, CAMPOS)
        if opcion == "2":
            cargarArchivo(archivo,VACACIONES)
        else:
            print("Por favor elija una opcion valida")

inicio()