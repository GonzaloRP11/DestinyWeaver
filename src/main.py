import os as sistema
import textwrap as textwrap
from colorama import fore,Style



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

def imprimirSeparador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho):
    """ Impresión de separador"""
    listaAsteriscos = '*' * centro
    for a in range(2):
        print(listaAsteriscos.center(centro + bordeIzquierdo))
   
    
 
def imprimirCabecera(lineas,columnas,bordeIzquierdo,centro,bordeDerecho):
    """Imprimir cabecera al comienzo del juego"""
    imprimirSeparador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)
    imprimirBienvenida(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)

def imprimirBienvenida(lineas,columnas,bordeIzquierdo,centro,bordeDerecho ):
    """Imprimir mensaje de bienvenida e introducción"""
    complemento = " "
    mensajeBienvenida = "¡Bienvenido a Destiny Weaver!"
    print(
            mensajeBienvenida.center(centro + bordeIzquierdo)
        )
    print("\n")
    
    mensajeDescripcion = "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones. Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.\n En este viaje, cada hilo que unes te conecta a un destino único. El futuro no está escrito; tú eres el tejedor de tu propia historia."
    
    parrafo = textwrap.fill(mensajeDescripcion,centro)

    for oracion in parrafo.splitlines():
        print( " ".ljust(bordeIzquierdo // 2) +
                oracion +
               " ".rjust(bordeDerecho)
            )

def obtenerNombreJugador():
    nombre = ""
    while len(nombre) < 3:
        nombre = input("Por favor, ingrese un nombre de jugador")
    

#Comienzo del programa
def main ():
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal()
    imprimirCabecera(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)
    obtenerNombreJugador()

main()