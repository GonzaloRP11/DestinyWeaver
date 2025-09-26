import os as sistema
import textwrap as textwrap
import art as estiloFontArt
import sys
import re 
# Añadir la ruta raíz para poder importar desde data y src
sys.path.append(sistema.path.abspath(sistema.path.join(sistema.path.dirname(__file__), '..')))

from importlib.machinery import SourceFileLoader
from data.stories import accionCapituloInicial, dramaCapituloInicial, humorCapituloInicial, terrorCapituloInicial

def anchoLargoTerminal(solicita):
    """ Configurar terminal"""
    lineas = sistema.get_terminal_size().lines
    if sistema.get_terminal_size().columns < 80:
        print("Su terminal es demasiado pequeña para jugar.")
        return
    else:
        columnas = (lambda columna: 80 if columna>=100 else 80) (sistema.get_terminal_size().columns)

    bordeIzquierdo = (columnas//4)
    centro = bordeIzquierdo * 2
    bordeDerecho = bordeIzquierdo

    match solicita:
        case 'bordeizquierdo':
            return bordeIzquierdo
        case 'centro':
            return centro
        case 'bordederecho':
            return bordeDerecho
        case 'lineas':
            return lineas
        case 'columnas':
            return columnas
        case 'bordescentro':
            return bordeIzquierdo,centro,bordeDerecho
        case '*':
            return lineas,columnas,bordeIzquierdo,centro,bordeDerecho
    

def borrarLineas(cantLineas):
    """ Borrar lineas de la consola"""
    for _ in range(cantLineas):
        print("\033[F\033[K", end='')


def imprimirSeparador():
    """ Impresión de separador"""
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('*')
    listaAsteriscos = '*' * (columnas - bordeIzquierdo)
    for a in range(2):
        print(listaAsteriscos.center(centro + bordeIzquierdo + bordeDerecho))
   
    
 
def imprimirCabecera():
    """Imprimir cabecera al comienzo del juego"""
    imprimirSeparador()
    imprimirBienvenida()

def imprimirParrafo(parrafo):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')

    for oracion in parrafo.splitlines():
        print( 
                
                estiloFontArt.text2art(oracion,font="tiny2").center(bordeIzquierdo+centro+bordeDerecho)
            )
    print("\n")


def imprimirBienvenida():
    """Imprimir mensaje de bienvenida e introducción"""
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    complemento = " "
    mensajeBienvenida = "¡Bienvenido a Destiny Weaver!"
    print(
            estiloFontArt.text2art(mensajeBienvenida,font="tiny2").center(bordeIzquierdo+centro+bordeDerecho)
        )
    print("\n")
    
    mensajeDescripcion = (
        "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones.\n"
        "Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.\n"
        "En este viaje, cada hilo que unes te conecta a un destino único.\n"
        "El futuro no está escrito; tú eres el tejedor de tu propia historia."
    )

    parrafo = textwrap.fill(mensajeDescripcion,bordeIzquierdo+centro)

    imprimirParrafo(parrafo)
    
def obtenerNombreJugador():
    """ Obtiene nombre del jugador """
    columnas = anchoLargoTerminal('columnas')
    patron = '^[a-zA-Z]{3,15}$'
    nombre = input("Por favor, ingrese un nombre de jugador\n".center(columnas))
    lineaBorrar = 2
    while re.search(patron,nombre) == None:
        nombre = input("Por favor, ingrese un nombre de jugador\n".center(columnas))
        lineaBorrar += 2
    borrarLineas(lineaBorrar)
    return nombre

def eleccionHistoria(nombreJugador):
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('*')
    mensajeHilos1 = "El murmullo de los hilos se intensifica, como si un telar invisible vibrara en la penumbra. Una voz etérea se filtra en tu mente, clara como un susurro y burlona como una sonrisa escondida: El telar del destino te aguarda, tejedor. ¿Qué historia deseas entrelazar en su tapiz? Ante ti se despliegan cuatro hilos brillando con vida propia:"
    mensajeHilos1 = textwrap.fill(mensajeHilos1,bordeIzquierdo+centro)
    imprimirParrafo(mensajeHilos1)
    
    rutaArchivoHilos = sistema.path.abspath(sistema.path.join("data","hilos","hilos.py"))
    hilos = SourceFileLoader("hilos", rutaArchivoHilos).load_module() 
    max_ancho_hilo = max(len(diccionario['Hilo']) for diccionario in hilos.hilos)  
    
    for diccionario in hilos.hilos:
        espacios_relleno = " " * ((max_ancho_hilo - len(diccionario['Hilo'])) + bordeIzquierdo)
        print(
              " " * (bordeIzquierdo//2) +
              f"{diccionario['Hilo']}" +
                espacios_relleno +
              f"opción:{diccionario['opcion']}")
        
    ejecutar_accion_por_opcion()

def ejecutar_accion_por_opcion():
    while True:
        opcion_input = input("Selecciona una opción: ")
        if opcion_input == "" or not opcion_input.isdigit():
            print("Opción no válida. Por favor, ingresa un número valido.")
            continue
        opcion_elegida = int(opcion_input)
        match opcion_elegida:
            case 1:
                humorCapituloInicial.start()
                break
            case 2:
                accionCapituloInicial.start()
                break
            case 3:
                dramaCapituloInicial.start()
                break
            case 4:
                terrorCapituloInicial.start()
                break
            case _:
                print("Opción no válida. Por favor, intenta nuevamente.")

            
    
def main ():
    """Comienzo de programa"""
    imprimirCabecera()
    nombreJugador = obtenerNombreJugador()
    eleccionHistoria(nombreJugador)

main()