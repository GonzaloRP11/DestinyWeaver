import os as sistema
import textwrap as textwrap
import art as estiloFontArt
import sys
# Añadir la ruta raíz para poder importar desde data y src
sys.path.append(sistema.path.abspath(sistema.path.join(sistema.path.dirname(__file__), '..')))

from importlib.machinery import SourceFileLoader
from data.stories import accionCapituloInicial, dramaCapituloInicial, humorCapituloInicial, terrorCapituloInicial

def anchoLargoTerminal():
    """ Configurar terminal"""
    lineas = sistema.get_terminal_size().lines
    if sistema.get_terminal_size().columns < 80:
        print("Su terminal es demasiado pequeña para jugar.")
        return
    else:
        columnas = sistema.get_terminal_size().columns if (sistema.get_terminal_size().columns >= 100) else 80

    bordeIzquierdo = (columnas//4)
    centro = bordeIzquierdo * 2
    bordeDerecho = bordeIzquierdo

    return lineas,columnas,bordeIzquierdo,centro,bordeDerecho

def borrarLineas(cantLineas):
    """ Borrar lineas de la consola"""
    for _ in range(cantLineas):
        print("\033[F\033[K", end='')


def imprimirSeparador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho):
    """ Impresión de separador"""
    listaAsteriscos = '*' * (columnas - bordeIzquierdo)
    for a in range(2):
        print(listaAsteriscos.center(centro + bordeIzquierdo + bordeDerecho))
   
    
 
def imprimirCabecera(lineas,columnas,bordeIzquierdo,centro,bordeDerecho):
    """Imprimir cabecera al comienzo del juego"""
    imprimirSeparador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)
    imprimirBienvenida(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)

def imprimirParrafo(lineas,columnas,bordeIzquierdo,centro,bordeDerecho,parrafo):
    for oracion in parrafo.splitlines():
        print( 
                
                estiloFontArt.text2art(oracion,font="tiny2").center(bordeIzquierdo+centro+bordeDerecho)
            )
    print("\n")


def imprimirBienvenida(lineas,columnas,bordeIzquierdo,centro,bordeDerecho ):
    """Imprimir mensaje de bienvenida e introducción"""
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

    imprimirParrafo(lineas,columnas,bordeIzquierdo,centro,bordeDerecho,parrafo)
    
def obtenerNombreJugador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho):
    """ Obtiene nombre del jugador """

    letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    nombre = ""

    while len(nombre) < 3:
        nombre = input("Por favor, ingrese un nombre de jugador\n".center(columnas))
        
        # Verificar caracteres válidos usando un bucle for
        valido = True
        for c in nombre:
            if c not in letras_validas:
                valido = False
                break  # si encuentra un caracter que no esta definido rompe el bucle

        if not valido:
            print("Nombre inválido. Solo se permiten letras y números.".center(columnas))
            nombre = "" 

    borrarLineas(3)
    return nombre

def eleccionHistoria(lineas,columnas,bordeIzquierdo,centro,bordeDerecho,nombreJugador):
    mensajeHilos1 = "El murmullo de los hilos se intensifica, como si un telar invisible vibrara en la penumbra. Una voz etérea se filtra en tu mente, clara como un susurro y burlona como una sonrisa escondida: El telar del destino te aguarda, tejedor. ¿Qué historia deseas entrelazar en su tapiz? Ante ti se despliegan cuatro hilos brillando con vida propia:"
    mensajeHilos1 = textwrap.fill(mensajeHilos1,bordeIzquierdo+centro)
    imprimirParrafo(lineas,columnas,bordeIzquierdo,centro,bordeDerecho,mensajeHilos1)
    
    rutaArchivoHilos = sistema.path.abspath(sistema.path.join("data","hilos","hilos.py"))
    hilos = SourceFileLoader("hilos", rutaArchivoHilos).load_module() 

    for diccionario in hilos.hilos:
        print(
              " " * (bordeIzquierdo//2) +
              f"{diccionario['Hilo']}" +
              " " * (len({diccionario['Hilo']}) + bordeDerecho if len({diccionario['Hilo']}) > bordeDerecho else  len({diccionario['Hilo']}) + bordeDerecho) +
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
    """Comeinzo de programa"""
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal()
    imprimirCabecera(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)
    nombreJugador = obtenerNombreJugador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)
    eleccionHistoria(lineas,columnas,bordeIzquierdo,centro,bordeDerecho,nombreJugador)

main()