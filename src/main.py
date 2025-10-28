import os as sistema
import textwrap as textwrap
import art as estiloFontArt
import sys
import re 
# Añadir la ruta raíz para poder importar desde data y src
sys.path.append(sistema.path.abspath(sistema.path.join(sistema.path.dirname(__file__), '..')))

from importlib.machinery import SourceFileLoader
from data.stories import accionCapituloInicial, dramaCapituloInicial, humorCapituloInicial, terrorCapituloInicial

# Matriz de configuración de historias disponibles
# Cada fila contiene: [numero_opcion, nombre_display, modulo, descripcion]
matrizHistorias = [
    [1, "Humor", "humorCapituloInicial", "Una aventura llena de risas y situaciones cómicas"],
    [2, "Acción", "accionCapituloInicial", "Suspenso, emoción y desafíos constantes"],
    [3, "Drama", "dramaCapituloInicial", "Emociones profundas y decisiones difíciles"],
    [4, "Terror", "terrorCapituloInicial", "Terror psicológico y misterios oscuros"]
]

# Matriz de opciones de menu y modulos
# Cada fila contiene: [opcion_numerica, modulo_correspondiente]
matrizOpcionesModulos = [
    [1, humorCapituloInicial],
    [2, accionCapituloInicial],
    [3, dramaCapituloInicial],
    [4, terrorCapituloInicial]
]

# Matriz de mensajes de error
# Cada fila contiene: [tipo_error, mensaje]
matrizMensajesError = [
    ['terminal_pequeña', 'Su terminal es demasiado pequeña para jugar.'],
    ['error_terminal', 'Error al obtener el tamaño de la terminal. Usando valores por defecto.'],
    ['archivo_no_encontrado', 'Error: No se encontró el archivo de hilos. Verifique que el archivo data/hilos/hilos.py existe.'],
    ['error_carga', 'Error al cargar el módulo de hilos'],
    ['error_inesperado', 'Error inesperado en la selección de historia'],
    ['opcion_invalida', 'Opción no válida. Por favor, ingresa un número valido.'],
    ['juego_cancelado', 'Juego cancelado por el usuario.'],
    ['error_modulo', 'Error: El módulo de historia seleccionado no tiene la función start']
]

def obtenerMensajeError(tipo_error):
    """Busca y retorna un mensaje de error desde matrizMensajesError"""
    for error in matrizMensajesError:
        if error[0] == tipo_error:
            return error[1]
    return "Error desconocido"

def anchoLargoTerminal(solicita):
    """ Configurar terminal"""
    try:
        lineas = sistema.get_terminal_size().lines
        if sistema.get_terminal_size().columns < 80:
            print(obtenerMensajeError('terminal_pequeña'))
            return
        else:
            columnas = (lambda columna: 80 if columna>=100 else 80) (sistema.get_terminal_size().columns)
    except (OSError, AttributeError) as e:
        print(obtenerMensajeError('error_terminal'))
        lineas = 24
        columnas = 80

    bordeIzquierdo = (columnas//4)
    centro = bordeIzquierdo * 2
    bordeDerecho = bordeIzquierdo

    # Matriz de dimensiones de la terminal
    # Cada fila representa: [tipo, valor]
    matrizDimensiones = [
        ['lineas', lineas],
        ['columnas', columnas],
        ['bordeizquierdo', bordeIzquierdo],
        ['centro', centro],
        ['bordederecho', bordeDerecho]
    ]

    # Tupla con todas las dimensiones de la terminal
    dimensiones_completas = (lineas, columnas, bordeIzquierdo, centro, bordeDerecho)
    
    # Tupla con los bordes y el centro
    bordes_centro = (bordeIzquierdo, centro, bordeDerecho)

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
            return bordes_centro
        case '*':
            return dimensiones_completas
    

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
    # Desempaqueta tupla de bordes
    bordes = anchoLargoTerminal('bordescentro')
    bordeIzquierdo, centro, bordeDerecho = bordes

    for oracion in parrafo.splitlines():
        print( 
                
                estiloFontArt.text2art(oracion,font="tiny2").center(bordeIzquierdo+centro+bordeDerecho)
            )
    print("\n")


def imprimirBienvenida():
    """Imprimir mensaje de bienvenida e introducción"""
    # Desempaqueta tupla de bordes
    bordes = anchoLargoTerminal('bordescentro')
    bordeIzquierdo, centro, bordeDerecho = bordes
    
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
    try:
        columnas = anchoLargoTerminal('columnas')
        patron = '^[a-zA-Z]{3,15}$'
        nombre = input("Por favor, ingrese un nombre de jugador\n".center(columnas))
        lineaBorrar = 2
        while re.search(patron,nombre) == None:
            nombre = input("Por favor, ingrese un nombre de jugador\n".center(columnas))
            lineaBorrar += 2
        borrarLineas(lineaBorrar)
        return nombre
    except (KeyboardInterrupt, EOFError):
        print("\n\nEntrada cancelada por el usuario.")
        return "Jugador"
    except Exception as e:
        print(f"Error inesperado al obtener nombre: {e}")
        return "Jugador"

def mostrarInformacionHistoria(opcion):
    """Muestra información detallada de una historia usando la matriz matrizHistorias"""
    for historia in matrizHistorias:
        if historia[0] == opcion:
            # historia[1] = nombre, historia[2] = modulo, historia[3] = descripcion
            print(f"Historia: {historia[1]}")
            print(f"Descripción: {historia[3]}\n")
            break

def eleccionHistoria(nombreJugador):
    try:
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
    except FileNotFoundError:
        print(obtenerMensajeError('archivo_no_encontrado'))
    except ImportError as e:
        print(f"{obtenerMensajeError('error_carga')}: {e}")
    except Exception as e:
        print(f"{obtenerMensajeError('error_inesperado')}: {e}")

def ejecutar_accion_por_opcion():
    while True:
        try:
            opcion_input = input("Selecciona una opción: ")
            if opcion_input == "" or not opcion_input.isdigit():
                print(obtenerMensajeError('opcion_invalida'))
                continue
            opcion_elegida = int(opcion_input)
            
            # Usa matriz para buscar la opcion y ejecuta el modulo correspondiente
            opcion_encontrada = False
            for fila in matrizOpcionesModulos:
                if fila[0] == opcion_elegida:
                    fila[1].start()  # Ejecuta el modulo en la segunda columna
                    opcion_encontrada = True
                    break
            
            if opcion_encontrada:
                break
            else:
                print("Opción no válida. Por favor, intenta nuevamente.")
                
        except (KeyboardInterrupt, EOFError):
            print("\n\n" + obtenerMensajeError('juego_cancelado'))
            break
        except AttributeError as e:
            print(f"{obtenerMensajeError('error_modulo')}: {e}")
            break
        except Exception as e:
            print(f"Error inesperado al ejecutar la opción: {e}")
            break

            
    
def main ():
    """Comienzo de programa"""
    try:
        imprimirCabecera()
        nombreJugador = obtenerNombreJugador()
        eleccionHistoria(nombreJugador)
    except KeyboardInterrupt:
        print("\n\n¡Gracias por jugar Destiny Weaver! ¡Hasta la próxima!")
    except Exception as e:
        print(f"\nError crítico en el juego: {e}")
        print("El juego se cerrará para evitar daños mayores.")
    finally:
        print("\nDestiny Weaver ha finalizado.")

main()