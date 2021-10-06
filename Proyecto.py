from genericpath import exists
import os

CARPETA = 'contactos/' #carpetas de contactos
EXTENSION = '.txt' #extension de archivos

#contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #revisar si la carpeta existe o no
    crear_directorio()


    #muestra menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Sellecione una opcion: \r\n')
        opcion = int(opcion)

        #ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5 :
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except expression as identifier:
        print('No existe ese contacto')

    #reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n informacion del contacto: \r\n' )
        for linea in contacto:
            print(linea.rstrip())
        print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    #Reiniciar la app
    app()


def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
            #imprime los separadores
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar.')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #restos de los campos
            nombre_contacto = input('Agrega nuevo nombre: \r\n')
            telefono_contacto = input('Agrega nuevo telefono: \r\n')
            categoria_contacto = input('Agrega la nueva categoria contacto: \r\n')

            #instanciar
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Contacto: ' + contacto.categoria + '\r\n')

            #renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar mensaje de exito

            print('Contacto editado correctamente \r\n')  


    else:
        print('Ese contacto no existe')
      #Reiniciar aplicacion
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre contacto: \r\n')

    #revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            
            #restos de los campos
            telefono_contacto = input('Agregar el telefono: \r\n')
            categoria_contacto = input('Categoria contacto: \r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Contacto: ' + contacto.categoria + '\r\n')

            #mostrar mensaje de exito
            print('Contacto creado correctamente \r\n')  
    else:
        print('Ese contacto ya existe')   


    #reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta
        os.makedirs(CARPETA)
    else:
        print('la carpeta ya existe')


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()