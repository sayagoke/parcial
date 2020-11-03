import csv
import os.path

def modificar(archivo, campos):
    lista_Empleados = cargarLista(archivo, campos)
    try:
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)
            file_guarda.writerows(lista_Empleados)
            print(f"se guardo correctamente {archivo}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def sobreescribir(archivo, campos):
    lista_Empleados = cargarLista(archivo, campos)
    try:
        with open(archivo, 'w', newline='') as file:
            archivo_guarda = csv.DictWriter(file, fieldnames=campos)

            archivo_guarda.writeheader()

            archivo_guarda.writerows(lista_Empleados)
            print(f"Se guardo exitosamente {archivo}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

def cargarLista(archivo, campos):
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

        cargar = input("Desea seguir agregando empleados? Si/No ")
    return lista_empleados

def opcionArchivo(archivo,campos):
    archivo_creado = os.path.isfile(archivo)
    
    if archivo_creado:
        print(f"Ya existe el archivo, ¿desea Modificar o Sobreescribir? m/s")
        accion = input("")
        if accion == "s":
            sobreescribir(archivo, campos)
            return
        if accion == "m":
            modificar(archivo, campos)
            return
        else:
            print('ingrese una opcion valida')
    else:
        sobreescribir(archivo, campos)
        return

def guardarDatos(archivo, campos):
    cargarLista
    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista_empleados)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def cargarArchivo(archivo,vacaciones):
    aux_empleados = open(archivo)
    aux_vacaciones = open(vacaciones)
    empleados_csv = csv.reader(aux_empleados)
    vacaciones_csv = csv.reader(aux_vacaciones)

    #Saltear Encabezados
    next(empleados_csv)
    next(vacaciones_csv)

    empleados = next(empleados_csv, None)
    vacaciones = next(vacaciones_csv, None)

    validar = True
    while validar:
        valor = input(f"Ingrese el numero de legajo: ")
        try:
            valor = int(valor)
            validar = False
        except ValueError:
            validar = True
            print(f'El legajo debe ser un numero')

    contador_dias = 0
    while vacaciones:
        if int(vacaciones[0]) == valor:
            contador_dias += 1
        vacaciones = next(vacaciones_csv, None)
    
    while empleados:
        if int(empleados[0]) == valor:
            total_vacaciones = int(empleados[3])
            dias_restantes = total_vacaciones - int(contador_dias)
            print(f'Legajo {valor}: {empleados[1]} {empleados[2]}, le restan {dias_restantes} dias de vacaciones')    
  
        empleados = next(empleados_csv, None)

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
        elif opcion == "1":
            opcionArchivo(archivo, CAMPOS)
        elif opcion == "2":
            cargarArchivo(archivo,VACACIONES)
        else:
            print("Por favor elija una opcion valida")

inicio()