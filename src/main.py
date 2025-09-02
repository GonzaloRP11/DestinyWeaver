import os as sistema
import textwrap as textwrap

def anchoLargoTerminal():
    lineas = sistema.get_terminal_size().lines
    columnas = sistema.get_terminal_size().columns
    return lineas,columnas

def imprimirSeparador(a,f):
    for x in range(f):
        for n in range(a):
            print("*",end=" ")
        print("\n")

def imprimirCabecera():
    lineas,columnas = anchoLargoTerminal()

    if columnas > 100 :
        columnas = 80    

    imprimirSeparador(columnas,2)

def imprimirBienvenida():
    lineas,columnas = anchoLargoTerminal()
    complemento = "*"
    mensajeBienvenida = "¡Bienvenido a Destiny Weaver!"
    print(
            complemento.rjust((columnas//6)) + '\t' +
            mensajeBienvenida.rjust((columnas//5)) + '\t' +
            complemento.rjust((columnas//6)) + '\t' 
        )
    print("\n")
    mensajeDescripcion = "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones.\n Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.\n En este viaje, cada hilo que unes te conecta a un destino único.\n El futuro no está escrito; tú eres el tejedor de tu propia historia."
    mensajeDescEnvuelto = textwrap.fill(mensajeDescripcion,width=(columnas//2))
    lineasMsjDesc = mensajeDescEnvuelto.splitlines()

    for linea in lineasMsjDesc():
        print(linea)
        """print(
                complemento.rjust((columnas//6)) + '\t' +
                linea+
                complemento.rjust((columnas//6)) + '\t' 
            ,end=" ")"""
        
        


def main ():
    imprimirCabecera()
    imprimirBienvenida()

main()