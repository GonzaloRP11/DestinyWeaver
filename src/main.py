import os as sistema
import textwrap as textwrap

def anchoLargoTerminal():
    lineas = sistema.get_terminal_size().lines
    columnas = sistema.get_terminal_size().columns if (sistema.get_terminal_size().columns >= 100) else 80
    bordeIzquierdo = (columnas//3)
    centro = (columnas//3) + (columnas//3)
    bordeDerecho = (columnas//3)

    return lineas,columnas,bordeIzquierdo,centro,bordeDerecho

def imprimirSeparador(li,col,bz,c,bd):
    bordeIzquierdo = (col//3)
    centro = (col//4)
    bordeDerecho = (col//3)
    

    listaAsteriscos = ['*' for n in range(col)]
    
 

def imprimirCabecera():
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal()  
    imprimirSeparador(lineas,columnas,bordeIzquierdo,centro,bordeDerecho)

def imprimirBienvenida():
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal()

    complemento = "*"
    mensajeBienvenida = "¡Bienvenido a Destiny Weaver!"
    print(
            complemento.ljust(bordeIzquierdo) + 
            mensajeBienvenida.center(0) + 
            complemento.rjust(bordeDerecho) 
        )
    print("\n")
    
    mensajeDescripcion = "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones. Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.\n En este viaje, cada hilo que unes te conecta a un destino único. El futuro no está escrito; tú eres el tejedor de tu propia historia."
    
    parrafo = textwrap.wrap(mensajeDescripcion,(columnas//2))
    complemento = " "
    for linea in parrafo:
        print(
                complemento.ljust(bordeIzquierdo - (centro//3) )+
                linea.center(0)+
                complemento.rjust(bordeDerecho - (centro//3))
             )
    
    

     

def main ():
    imprimirCabecera()
    imprimirBienvenida()

main()