import os as sistema
import textwrap as textwrap
#import art as estiloFontArt
import sys
import re 
import requests
import json

# Añadir la ruta raíz para poder importar desde data y src
sys.path.append(sistema.path.abspath(sistema.path.join(sistema.path.dirname(__file__), '..')))

from importlib.machinery import SourceFileLoader
from data.stories import accionCapituloInicial, dramaCapituloInicial, humorCapituloInicial, terrorCapituloInicial

def anchoLargoTerminal(solicita):
    """ Configurar terminal
        Ajusta automáticamente el ancho más adecuado para texto.
    """
    # Obtener tamaño de terminal con fallback por si no está disponible
    size = sistema.get_terminal_size() if sistema.isatty(0) else sistema.terminal_size((100, 25))
    columnas, lineas = size.columns, size.lines
    # Validación de tamaño mínimo
    if columnas < 70:
        print("Su terminal es demasiado pequeña para jugar (mínimo 70 columnas).")
        return None

    # Determinar ancho de trabajo óptimo
    if columnas < 90:
        ancho = 70
    elif columnas < 110:
        ancho = 90
    else:
        ancho = 100  
    
    #lineas = sistema.get_terminal_size().lines
    #if sistema.get_terminal_size().columns < 80:
    #    print("Su terminal es demasiado pequeña para jugar.")
    #    return
    #else:
    #columnas = (lambda columna: 80 if columna>=100 else 80) (sistema.get_terminal_size().columns)

    bordeIzquierdo = (ancho//4)
    centro = ancho // 2
    bordeDerecho = ancho - bordeIzquierdo

    match solicita.lower():
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
        case 'ancho':
            return ancho
        case '*':
            return lineas,columnas,bordeIzquierdo,centro,bordeDerecho
        case '_':
            print("Parámetro no reconocido. Use: 'bordeizquierdo', 'centro', 'bordederecho', 'lineas', 'columnas', 'bordescentro' o '*'.")
            return None

def borrarLineas(cantLineas):
    """ Borrar lineas de la consola"""
    for _ in range(cantLineas):
        print("\033[F\033[K", end='')


def imprimirSeparador():
    """ Impresión de separador"""
    ancho = anchoLargoTerminal('ancho')
    listaArtetiscos = '*' * ancho
    for i in range(0,2):
        print(listaArtetiscos)
    
 
def imprimirCabecera():
    """Imprimir cabecera al comienzo del juego"""
    imprimirSeparador()
    imprimirBienvenida()

def formatear_opciones(texto):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    ancho = anchoLargoTerminal('ancho')
    indent = " " * (bordeIzquierdo//4)

    """
    Separa las opciones (a), b), c)... o a., b., etc.) en líneas nuevas
    y ajusta el ancho del texto sin perder formato.
    """
    # Insertar salto de línea antes de letras que marcan opciones
    # Ej: "a) ", "b. ", "C) "
    texto = re.sub(r"(?<!\n)(?=\s*[a-zA-Z][\)\.] )", "\n", texto)

    # Ajustar el ancho de cada línea
    lineas = []
    for linea in texto.splitlines():
        envueltas = textwrap.wrap(linea.strip(),
                                  width=ancho,
                                  initial_indent=indent,
                                  subsequent_indent=indent)
        if envueltas:
            lineas.extend(envueltas)
        else:
            lineas.append("")  # conservar líneas vacías
    
    return "\n".join(lineas)

def imprimirOpciones(texto):
    for linea in texto.splitlines():
        print(linea)
      
    

def imprimirParrafo(parrafo):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    ancho = anchoLargoTerminal('ancho')

    indent = " " * (bordeIzquierdo//4)
    for linea in parrafo.splitlines():
        linea.lstrip()
        print("\n".join(textwrap.wrap(linea, width=ancho, initial_indent=indent, subsequent_indent=indent)))
    print()
    #print("\n".join(textwrap.wrap(parrafo, width=ancho, initial_indent=indent, subsequent_indent=indent)))
   #print()



def imprimirBienvenida():
    """Imprimir mensaje de bienvenida e introducción"""
    #bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    ancho = anchoLargoTerminal('ancho')
    mensajeBienvenida = "¡Bienvenido a Destiny Weaver!"
    print(
            #estiloFontArt.text2art(mensajeBienvenida,font="tiny2").center(centro)
            mensajeBienvenida.center(ancho)
        )
    print("\n")
    
    mensajeDescripcion = (
        "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones.\n"
        "Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.\n"
        "En este viaje, cada hilo que unes te conecta a un destino único.\n"
        "El futuro no está escrito; tú eres el tejedor de tu propia historia."
    )
    imprimirParrafo(mensajeDescripcion)

    
def obtenerNombreJugador():
    """ Obtiene nombre del jugador """
    #columnas = anchoLargoTerminal('columnas')
    ancho = anchoLargoTerminal('ancho')
    patron = '^[a-zA-Z]{3,15}$'
    nombre = input("Por favor, ingrese un nombre de jugador\n".center(ancho))
    lineaBorrar = 2
    while re.search(patron,nombre) == None:
        nombre = input("Por favor, ingrese un nombre de jugador\n".center(ancho))
        lineaBorrar += 2
    borrarLineas(lineaBorrar)
    return nombre

def eleccionHistoria(nombreJugador):
    lineas,columnas,bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('*')
    mensajeHilos1 = "El murmullo de los hilos se intensifica, como si un telar invisible vibrara en la penumbra. Una voz etérea se filtra en tu mente, clara como un susurro y burlona como una sonrisa escondida: El telar del destino te aguarda, tejedor. ¿Qué historia deseas entrelazar en su tapiz? Ante ti se despliegan cuatro hilos brillando con vida propia:"
    imprimirParrafo(mensajeHilos1)
    
    rutaArchivoHilos = sistema.path.abspath(sistema.path.join("data","hilos","hilos.py"))
    hilos = SourceFileLoader("hilos", rutaArchivoHilos).load_module() 
    max_ancho_hilo = max(len(diccionario['Hilo']) for diccionario in hilos.hilos)  
    
    for diccionario in hilos.hilos:
        espacios_relleno = " " * ((max_ancho_hilo - len(diccionario['Hilo'])) + bordeIzquierdo)
        print(
              " " * (bordeIzquierdo//4) +
              f"{diccionario['Hilo']}" +
                espacios_relleno +
              f"opción:{diccionario['opcion']}",end="\n")
        
    ejecutar_accion_por_opcion(nombreJugador)

def ejecutarHiloHumor(nombreJugador):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    parrafo = textwrap.fill(humorCapituloInicial.historial[0]["contenido"],bordeIzquierdo+centro)
    imprimirParrafo(parrafo)
    respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    while respuestaJugador not in humorCapituloInicial.historial[0]["opciones"]:
        respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    
    humorCapituloInicial.historial[0].update(
                                                {
                                                    'nombre_jugador':nombreJugador,
                                                    'respuesta_jugador':respuestaJugador
                                                }
                                            )
    

def ejecutarHiloAccion(nombreJugador):
    imprimirParrafo(accionCapituloInicial.historial[0]["contenido"])
    patron = r'^[A-Za-z]$'
    respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    while (not re.match(patron, respuestaJugador)): 
        respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    
    accionCapituloInicial.historial[0].update(
                                                {
                                                    'nombre_jugador':nombreJugador,
                                                    'respuesta_jugador':respuestaJugador
                                                }
                                            )
    #Interacción inicial con la ia para que entienda el contexto
    responseNarrativa = requests.post(
                                        'http://localhost:11434/api/generate',
                                        json={
                                            'model': 'phi3:mini',
                                            #'prompt': f'Historia:{accionCapituloInicial.historial[0]['contenido']},respuesta_jugador:{accionCapituloInicial.historial[0]['respuesta_jugador']},brindar continuidad de historia para el jugador. Tene en cuenta no devolver la respuesta del jugador ni nuevas opciones ni tampoco la palabra historia dos puntos. El nombre del jugador es {nombreJugador}.La narración no debe superar las 5 oraciones estrictamente.',
                                            'prompt': f'''  Contexto: {accionCapituloInicial.historial[0]['contenido']}
                                                            Acción anterior del jugador: {accionCapituloInicial.historial[0]['respuesta_jugador']}
                                                            Escribe la continuidad de la historia desde ese punto, tomando en cuenta la acción del jugador, pero sin repetirla ni mencionarla explícitamente.
                                                            Requisitos estrictos:
                                                            No incluyas la palabra “Historia:” ni ningún encabezado.
                                                            No agregues opciones nuevas.
                                                            No menciones la variable del jugador ni la acción anterior de forma directa.
                                                            La narración debe tener entre 3 y 5 oraciones, nunca más de 5.
                                                            El tono debe ser narrativo, coherente y en tercera persona, utilizando el nombre del jugador {nombreJugador} solo cuando sea natural.
                                                            Devuelve solo el texto narrativo, sin explicaciones ni formato adicional.
                                                            Este formato es obligatorio. No lo ignores.''',
                                            'options': {
                                                            "num_predict": 150,   # ≈ límite de tokens (unos 70–90 palabras)
                                                            "temperature": 0.5,   # baja verbosidad
                                                            "top_p": 0.8,
                                                             "stop_sequence": ["\n", "Opción", "Respuesta", "Historia:", "Jugador:"]
                                                    }
                                        },
                                        stream=True
                
    )
   #Procesa la respuesta de la ia en un buffer
    contenidoNarrativa = ""
    for line in responseNarrativa.text.strip().split('\n'):
        if line:
            data = json.loads(line)
            contenidoNarrativa += data['response']
    #Imprime en pantalla la narrativa generada
    imprimirParrafo(contenidoNarrativa)
    
    #Envia a la ia la narrativa generada para obtener un listado de opciones del juego
    responseOpciones = requests.post(
                                'http://localhost:11434/api/generate',
                                json={
                                    'model': 'phi3:mini',
                                    'prompt': f'''Historia:{contenidoNarrativa}. Genera una lista de opciones breves para que el jugador elija cómo continuar o finalizar la historia.
                                                Cada opción debe cumplir estrictamente estas reglas:
                                                Máximo una oración de hasta 5 palabras.
                                                Formato obligatorio: Letra inicial + guion medio + descripción de la acción.
                                                Ejemplo de formato: A - Avanzar por el bosque.
                                                Devuelve solo la lista, sin texto adicional, sin explicaciones y sin saltarte ninguna regla.
                                                Este formato es obligatorio. No lo ignores.''',
                                   'options': {
                                                            "num_predict": 100,   # ≈ límite de tokens (unos 70–90 palabras)
                                                            "temperature": 0.5,   # baja verbosidad
                                                            "top_p": 0.8,
                                                             "stop_sequence": ["\n", "Opción", "Respuesta", "Historia:", "Jugador:"]
                                                    }
                                }
                            )
    #Procesa opciones generadas por la ia en base a la narrativa
    bufferOpciones = ""
    for line in responseOpciones.iter_lines():
        if line:
            data = json.loads(line)
            bufferOpciones += data['response']
    
    #Imprime las opciones en pantalla
    imprimirOpciones(formatear_opciones(bufferOpciones))

    listaOpciones = [opcion for opcion in (bufferOpciones).split('\n')]

    #Actualiza diccionario para almacenar los datos ya obtenidos hasta el momento
    accionCapituloInicial.historial.append(
        {
             "nombre_jugador":nombreJugador,
            "contenido": contenidoNarrativa,
            "opciones":listaOpciones,
            "respuesta_jugador":""
        }
    )       


def ejecutarHiloTerror(nombreJugador):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    parrafo = textwrap.fill(terrorCapituloInicial.historial[0]["contenido"],bordeIzquierdo+centro)
    imprimirParrafo(parrafo)
    respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    while respuestaJugador not in terrorCapituloInicial.historial[0]["opciones"]:
        respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    
    terrorCapituloInicial.historial[0].update(
                                                {
                                                    'nombre_jugador':nombreJugador,
                                                    'respuesta_jugador':respuestaJugador
                                                }
                                            )

def ejecutarHiloDrama(nombreJugador):
    bordeIzquierdo,centro,bordeDerecho = anchoLargoTerminal('bordescentro')
    parrafo = textwrap.fill(dramaCapituloInicial.historial[0]["contenido"],bordeIzquierdo+centro)
    imprimirParrafo(parrafo)
    respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    while respuestaJugador not in dramaCapituloInicial.historial[0]["opciones"]:
        respuestaJugador = (input("Ingrese respuesta:\t")).upper()
    
    dramaCapituloInicial.historial[0].update(
                                                {
                                                    'nombre_jugador':nombreJugador,
                                                    'respuesta_jugador':respuestaJugador
                                                }
                                            )
    

def ejecutar_accion_por_opcion(nombreJugador):
    bordeIzquierdo =anchoLargoTerminal('bordeizquierdo')
    opciones = ['1','2','3','4']
    opcion_input = input(" " * (bordeIzquierdo//4) + "Selecciona una opción:\t")

    while opcion_input not in opciones:
        opcion_input = input(" " * (bordeIzquierdo//4) +"Selecciona una opción:\t")
    
    match opcion_input:
        case '1':
            ejecutarHiloHumor(nombreJugador)
        case '2':
            ejecutarHiloAccion(nombreJugador)
        case '3':
            ejecutarHiloDrama(nombreJugador)
        case '4':
            ejecutarHiloTerror(nombreJugador)
        case '_':
            print("Opción no válida. Se ha finalizado el juego.")
            sys.exit()

            
    
def main ():
    """Comienzo de programa"""
    imprimirCabecera()
    nombreJugador = obtenerNombreJugador()
    eleccionHistoria(nombreJugador)

main()