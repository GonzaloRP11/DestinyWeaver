import os as sistema
import textwrap as textwrap
import sys
import re 
import requests
import json

# Añadir la ruta raíz para poder importar desde data y src
sys.path.append(sistema.path.abspath(sistema.path.join(sistema.path.dirname(__file__), '..')))

from importlib.machinery import SourceFileLoader
from data.stories import accionCapituloInicial, dramaCapituloInicial, humorCapituloInicial, terrorCapituloInicial


opcionesMenu = ('1', '2', '3', '4')

limitesAncho = (70, 90, 110, 100)  # (minimo, pequeño, mediano, grande)

mensajesError = [
    "Opción inválida. Intente nuevamente",
    "Su terminal es demasiado pequeña para jugar",
    "Error al cargar los hilos"
]

numerosValidos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

posicionInicial = (0, 0)  # (x, y)

caracteresEspeciales = ['*', '-', '|', '+']

rangoTemperatura = (0.0, 1.0)  # (minimo, maximo)

generosHistoria = ['Humor', 'Acción', 'Drama', 'Terror']

def anchoLargoTerminal(solicita):
    """ Configurar terminal
        Ajusta automáticamente el ancho más adecuado para texto.
    """
    # Obtener tamaño de terminal con fallback por si no está disponible
    size = sistema.get_terminal_size() if sistema.isatty(0) else sistema.terminal_size((100, 25))
    columnas, lineas = size.columns, size.lines

    # Validación de tamaño mínimo 
    minimo, pequeno, mediano, grande = limitesAncho
    if columnas < minimo:
        print(f"{mensajesError[1]} (mínimo {minimo} columnas).")
        sys.exit()

    # Determinar ancho de trabajo óptimo 
    if columnas < pequeno:
        ancho = minimo
    elif columnas < mediano:
        ancho = pequeno
    else:
        ancho = grande  
    
    
    bordes = (ancho//4)
    centro = ancho // 2

    match solicita.lower():
        case 'bordes':
            return bordes
        case 'centro':
            return centro
        case 'ancho':
            return ancho
        case '*':
            return lineas,columnas,bordes,centro,ancho
        case '_':
            print("Parámetro no reconocido. Use: 'bordeizquierdo', 'centro', 'bordederecho', 'lineas', 'columnas', 'bordescentro' o '*'.")
            return None

def guardarHistorialJson(nombreArchivo, datos):
    """Guarda el historial completo del juego en un archivo .json"""
    with open(nombreArchivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    print(f"\nEl historial del juego se guardó en '{nombreArchivo}'.")


def borrarLineas(cantLineas):
    """ Borrar lineas de la consola"""
    for _ in range(cantLineas):
        print("\033[F\033[K", end='')

def imprimirSeparador():
    """ Impresión de separador"""
    ancho = anchoLargoTerminal('ancho')
    caracterSeparador = caracteresEspeciales[0] 
    listaArtetiscos = caracterSeparador * ancho
    for i in range(0,2):
        print(listaArtetiscos) 
 
def imprimirCabecera():
    """Imprimir cabecera al comienzo del juego"""
    imprimirSeparador()
    imprimirBienvenida()

def formatearOpciones(texto):
    bordes = anchoLargoTerminal('bordes')
    ancho = anchoLargoTerminal('ancho')
    indent = " " * (bordes//4)

    """
    Separa las opciones A - , B -, C - en líneas nuevas
    y ajusta el ancho del texto sin perder formato.
    """
    # Insertar salto de línea antes de letras que marcan opciones
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
    bordes= anchoLargoTerminal('bordes')
    ancho = anchoLargoTerminal('ancho')

    indent = " " * (bordes//4)
    for linea in parrafo.splitlines():
        linea.lstrip()
        print("\n".join(textwrap.wrap(linea, width=ancho, initial_indent=indent, subsequent_indent=indent)))
    print()
    
def imprimirBienvenida():
    """Imprimir mensaje de bienvenida e introducción"""
    ancho = anchoLargoTerminal('ancho')
    mensajesBienvenida = [
        "¡Bienvenido a Destiny Weaver!",
        "Has llegado al borde de un mundo inexplorado, un lugar forjado por historias y el poder de las elecciones.",
        "Al dar tu primer paso, te sumerges en un tejido de destinos que se irá formando con cada una de tus decisiones.",
        "En este viaje, cada hilo que unes te conecta a un destino único.",
        "El futuro no está escrito; tú eres el tejedor de tu propia historia."
    ]
    
    print(mensajesBienvenida[0].center(ancho))
    print("\n")
    
    mensajeDescripcion = "\n".join(mensajesBienvenida[1:])

    imprimirParrafo(mensajeDescripcion)
    
def obtenerNombreJugador():
    """ Obtiene nombre del jugador """
    ancho = anchoLargoTerminal('ancho')
    limitesNombre = (3, 15)  # (minimo, maximo)
    minimo, maximo = limitesNombre
    patron = f'^[a-zA-Z]{{{minimo},{maximo}}}$'
    nombre = input("Por favor, ingrese un nombre de jugador\n".center(ancho))
    contadorLineas = (2, 2)  # (inicial, incremento)
    lineaBorrar = contadorLineas[0]
    while re.search(patron,nombre) == None:
        nombre = input("Por favor, ingrese un nombre de jugador\n".center(ancho))
        lineaBorrar += contadorLineas[1]
    borrarLineas(lineaBorrar)
    return nombre

def eleccionHistoria(nombreJugador):
    bordes = anchoLargoTerminal('bordes')
    mensajeHilos1 = "El murmullo de los hilos se intensifica, como si un telar invisible vibrara en la penumbra. Una voz etérea se filtra en tu mente, clara como un susurro y burlona como una sonrisa escondida: El telar del destino te aguarda, tejedor. ¿Qué historia deseas entrelazar en su tapiz? Ante ti se despliegan cuatro hilos brillando con vida propia:"
    imprimirParrafo(mensajeHilos1)
    
    try:
        rutaArchivoHilos = sistema.path.abspath(sistema.path.join("data","hilos","hilos.py"))
        hilos = SourceFileLoader("hilos", rutaArchivoHilos).load_module() 
        maxAnchoHilo = max(len(diccionario['Hilo']) for diccionario in hilos.hilos)  
        
        for diccionario in hilos.hilos:
            espaciosRelleno = " " * ((maxAnchoHilo - len(diccionario['Hilo'])) + bordes)
            print(
                  " " * (bordes//4) +
                  f"{diccionario['Hilo']}" +
                    espaciosRelleno +
                  f"opción:{diccionario['opcion']}",end="\n")
        print("\n")
    except FileNotFoundError:
        print(f"Error: {mensajesError[2]}. Verifica que 'data/hilos/hilos.py' exista.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al cargar los hilos: {e}")
        sys.exit(1)
    else:
        ejecutarAccionPorOpcion(nombreJugador)

def ejecutarHiloHumor():
    bordes = anchoLargoTerminal('bordes')
    imprimirParrafo(humorCapituloInicial.historial[0]["contenido"])
    patron = r'^[A-Za-z]$'
    estadoJuego = (0, True)  # (indice, continuar)
    indice, continuar = estadoJuego
    while continuar:
        opcionesValidas = [opcion.split('-')[0].strip().upper() for opcion in humorCapituloInicial.historial[indice]["opciones"]]
        respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
        print("\n")
        
        """Verificar si el usuario quiere salir"""
        if indice > 0:
            if respuestaJugador == "SALIR":
                print(" " * (bordes//4) + "Gracias por jugar. ¡Hasta la próxima!.\n")
                guardarHistorialJson("historial_humor.json", humorCapituloInicial.historial)
                break

        while (not re.match(patron, respuestaJugador)) or respuestaJugador not in opcionesValidas: 
        #while  respuestaJugador not in opcionesValidas: 
            print(f"{mensajesError[0]}\n")
            respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
            print("\n")
            if respuestaJugador == "SALIR":
                continuar = False
                print(" " * (bordes//4) + "\nFin de la historia. ¡Hasta la próxima!")
                sys.exit()
            
        
        humorCapituloInicial.historial[indice].update({'respuestaJugador':respuestaJugador})
        #Interacción inicial con la ia para que entienda el contexto
        responseNarrativa = requests.post(
                                            'http://localhost:11434/api/generate',
                                            json={
                                                'model': 'phi3:mini',
                                                'prompt': f'''  Contexto: {humorCapituloInicial.historial[indice]['contenido']}
                                                                Acciones válidas: {humorCapituloInicial.historial[indice]['opciones']}
                                                                Acción anterior del jugador: {humorCapituloInicial.historial[indice]['respuestaJugador']}
                                                                Escribe la continuidad de la historia desde ese punto, tomando en cuenta la acción del jugador, pero sin repetirla ni mencionarla explícitamente.
                                                                Requisitos estrictos:
                                                                No incluyas la palabra "Historia:" ni ningún encabezado.
                                                                No agregues opciones nuevas.
                                                                No menciones la variable del jugador ni la acción anterior de forma directa.
                                                                La narración debe tener entre 3 y 5 oraciones, nunca más de 5.
                                                                El tono debe ser narrativo, coherente y en tercera persona, utilizando el nombre del jugador {humorCapituloInicial.historial[indice]['nombreJugador']} solo cuando sea natural.
                                                                Devuelve solo el texto narrativo, sin explicaciones ni formato adicional.
                                                                Este formato es obligatorio. No lo ignores.''',
                                                'options': {
                                                                "num_predict": 400,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                "temperature": 0.15,   # baja verbosidad
                                                                "top_p": 0.7,
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
                                        'prompt': f'''Historia:{contenidoNarrativa}. Genera una lista de como máximo 3 opciones, cada una de ellas  como máximo puede contener 5 palabras y debe describir la accióna seguir por el jugador.
                                                    Cada opción debe cumplir estrictamente estas reglas:
                                                    Máximo de 4 palabras por oración.
                                                    Formato obligatorio: Letra inicial + espacio + guion medio + espacio + descripción de la acción.
                                                    Ejemplo de formato: A - Avanzar por el bosque.
                                                    Devuelve solo la lista, sin texto adicional, sin explicaciones y sin saltarte ninguna regla.
                                                    Este formato es obligatorio. No lo ignores.''',
                                        'options': {
                                                                    "num_predict": 150,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                    "temperature": 0.15,   # baja verbosidad
                                                                    "top_p": 0.7,
                                                                    "stop_sequence": ["\n", "Historia:", "Opción:"]
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
        imprimirOpciones(formatearOpciones(bufferOpciones))

        listaOpciones = [opcion for opcion in (bufferOpciones).split('\n')]

        #Actualiza diccionario para almacenar los datos ya obtenidos hasta el momento
        humorCapituloInicial.historial.append(
            {
                "nombreJugador":humorCapituloInicial.historial[indice]['nombreJugador'],
                "contenido": contenidoNarrativa,
                "opciones":listaOpciones,
                "respuestaJugador":"",
            }
        )
        indice += 1
        
def ejecutarHiloAccion():
    bordes = anchoLargoTerminal('bordes')
    imprimirParrafo(accionCapituloInicial.historial[0]["contenido"])
    patron = r'^[A-Za-z]$'
    estadoJuego = (0, True)  # (indice, continuar)
    indice, continuar = estadoJuego
    while continuar:
        opcionesValidas = [opcion.split('-')[0].strip().upper() for opcion in accionCapituloInicial.historial[indice]["opciones"]]
        respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
        print("\n")
        
        """Verificar si el usuario quiere salir"""
        if indice > 0:
            if respuestaJugador == "SALIR":
                print(" " * (bordes//4) + "Gracias por jugar. ¡Hasta la próxima!.\n")
                guardarHistorialJson("historial_accion.json", accionCapituloInicial.historial)
                break

        while (not re.match(patron, respuestaJugador)) or respuestaJugador not in opcionesValidas: 
        #while  respuestaJugador not in opcionesValidas: 
            print(f"{mensajesError[0]}\n")
            respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
            print("\n")
            if respuestaJugador == "SALIR":
                continuar = False
                print(" " * (bordes//4) + "\nFin de la historia. ¡Hasta la próxima!")
                sys.exit()
            
        
        accionCapituloInicial.historial[indice].update({'respuestaJugador':respuestaJugador})
        #Interacción inicial con la ia para que entienda el contexto
        responseNarrativa = requests.post(
                                            'http://localhost:11434/api/generate',
                                            json={
                                                'model': 'phi3:mini',
                                                'prompt': f'''  Contexto: {accionCapituloInicial.historial[indice]['contenido']}
                                                                Acciones válidas: {accionCapituloInicial.historial[indice]['opciones']}
                                                                Acción anterior del jugador: {accionCapituloInicial.historial[indice]['respuestaJugador']}
                                                                Escribe la continuidad de la historia desde ese punto, tomando en cuenta la acción del jugador, pero sin repetirla ni mencionarla explícitamente.
                                                                Requisitos estrictos:
                                                                No incluyas la palabra "Historia:" ni ningún encabezado.
                                                                No agregues opciones nuevas.
                                                                No menciones la variable del jugador ni la acción anterior de forma directa.
                                                                La narración debe tener entre 3 y 5 oraciones, nunca más de 5.
                                                                El tono debe ser narrativo, coherente y en tercera persona, utilizando el nombre del jugador {accionCapituloInicial.historial[indice]['nombreJugador']} solo cuando sea natural.
                                                                Devuelve solo el texto narrativo, sin explicaciones ni formato adicional.
                                                                Este formato es obligatorio. No lo ignores.''',
                                                'options': {
                                                                "num_predict": 400,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                "temperature": 0.15,   # baja verbosidad
                                                                "top_p": 0.7,
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
                                        'prompt': f'''Historia:{contenidoNarrativa}. Genera una lista de como máximo 3 opciones, cada una de ellas  como máximo puede contener 5 palabras y debe describir la accióna seguir por el jugador.
                                                    Cada opción debe cumplir estrictamente estas reglas:
                                                    Máximo de 4 palabras por oración.
                                                    Formato obligatorio: Letra inicial + espacio + guion medio + espacio + descripción de la acción.
                                                    Ejemplo de formato: A - Avanzar por el bosque.
                                                    Devuelve solo la lista, sin texto adicional, sin explicaciones y sin saltarte ninguna regla.
                                                    Este formato es obligatorio. No lo ignores.''',
                                        'options': {
                                                                    "num_predict": 150,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                    "temperature": 0.15,   # baja verbosidad
                                                                    "top_p": 0.7,
                                                                    "stop_sequence": ["\n", "Historia:", "Opción:"]
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
        imprimirOpciones(formatearOpciones(bufferOpciones))

        listaOpciones = [opcion for opcion in (bufferOpciones).split('\n')]

        #Actualiza diccionario para almacenar los datos ya obtenidos hasta el momento
        accionCapituloInicial.historial.append(
            {
                "nombreJugador":accionCapituloInicial.historial[indice]['nombreJugador'],
                "contenido": contenidoNarrativa,
                "opciones":listaOpciones,
                "respuestaJugador":"",
            }
        )
        indice += 1       

def ejecutarHiloTerror():
    bordes = anchoLargoTerminal('bordes')
    imprimirParrafo(terrorCapituloInicial.historial[0]["contenido"])
    patron = r'^[A-Za-z]$'
    estadoJuego = (0, True)  # (indice, continuar)
    indice, continuar = estadoJuego
    while continuar:
        opcionesValidas = [opcion.split('-')[0].strip().upper() for opcion in terrorCapituloInicial.historial[indice]["opciones"]]
        respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
        print("\n")
        
        """Verificar si el usuario quiere salir"""
        if indice > 0:
            if respuestaJugador == "SALIR":
                print(" " * (bordes//4) + "Gracias por jugar. ¡Hasta la próxima!.\n")
                guardarHistorialJson("historial_terror.json", terrorCapituloInicial.historial)
                break

        while (not re.match(patron, respuestaJugador)) or respuestaJugador not in opcionesValidas: 
        #while  respuestaJugador not in opcionesValidas: 
            print(f"{mensajesError[0]}\n")
            respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
            print("\n")
            if respuestaJugador == "SALIR":
                continuar = False
                print(" " * (bordes//4) + "\nFin de la historia. ¡Hasta la próxima!")
                sys.exit()
            
        
        terrorCapituloInicial.historial[indice].update({'respuestaJugador':respuestaJugador})
        #Interacción inicial con la ia para que entienda el contexto
        responseNarrativa = requests.post(
                                            'http://localhost:11434/api/generate',
                                            json={
                                                'model': 'phi3:mini',
                                                'prompt': f'''  Contexto: {terrorCapituloInicial.historial[indice]['contenido']}
                                                                Acciones válidas: {terrorCapituloInicial.historial[indice]['opciones']}
                                                                Acción anterior del jugador: {terrorCapituloInicial.historial[indice]['respuestaJugador']}
                                                                Escribe la continuidad de la historia desde ese punto, tomando en cuenta la acción del jugador, pero sin repetirla ni mencionarla explícitamente.
                                                                Requisitos estrictos:
                                                                No incluyas la palabra "Historia:" ni ningún encabezado.
                                                                No agregues opciones nuevas.
                                                                No menciones la variable del jugador ni la acción anterior de forma directa.
                                                                La narración debe tener entre 3 y 5 oraciones, nunca más de 5.
                                                                El tono debe ser narrativo, coherente y en tercera persona, utilizando el nombre del jugador {terrorCapituloInicial.historial[indice]['nombreJugador']} solo cuando sea natural.
                                                                Devuelve solo el texto narrativo, sin explicaciones ni formato adicional.
                                                                Este formato es obligatorio. No lo ignores.''',
                                                'options': {
                                                                "num_predict": 400,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                "temperature": 0.15,   # baja verbosidad
                                                                "top_p": 0.7,
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
                                        'prompt': f'''Historia:{contenidoNarrativa}. Genera una lista de como máximo 3 opciones, cada una de ellas  como máximo puede contener 5 palabras y debe describir la accióna seguir por el jugador.
                                                    Cada opción debe cumplir estrictamente estas reglas:
                                                    Máximo de 4 palabras por oración.
                                                    Formato obligatorio: Letra inicial + espacio + guion medio + espacio + descripción de la acción.
                                                    Ejemplo de formato: A - Avanzar por el bosque.
                                                    Devuelve solo la lista, sin texto adicional, sin explicaciones y sin saltarte ninguna regla.
                                                    Este formato es obligatorio. No lo ignores.''',
                                        'options': {
                                                                    "num_predict": 150,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                    "temperature": 0.15,   # baja verbosidad
                                                                    "top_p": 0.7,
                                                                    "stop_sequence": ["\n", "Historia:", "Opción:"]
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
        imprimirOpciones(formatearOpciones(bufferOpciones))

        listaOpciones = [opcion for opcion in (bufferOpciones).split('\n')]

        #Actualiza diccionario para almacenar los datos ya obtenidos hasta el momento
        terrorCapituloInicial.historial.append(
            {
                "nombreJugador":terrorCapituloInicial.historial[indice]['nombreJugador'],
                "contenido": contenidoNarrativa,
                "opciones":listaOpciones,
                "respuestaJugador":"",
            }
        )
        indice += 1       

def ejecutarHiloDrama():
    bordes = anchoLargoTerminal('bordes')
    imprimirParrafo(dramaCapituloInicial.historial[0]["contenido"])
    patron = r'^[A-Za-z]$'
    estadoJuego = (0, True)  # (indice, continuar)
    indice, continuar = estadoJuego
    while continuar:
        opcionesValidas = [opcion.split('-')[0].strip().upper() for opcion in dramaCapituloInicial.historial[indice]["opciones"]]
        respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
        print("\n")
        
        """Verificar si el usuario quiere salir"""
        if indice > 0:
            if respuestaJugador == "SALIR":
                print(" " * (bordes//4) + "Gracias por jugar. ¡Hasta la próxima!.\n")
                guardarHistorialJson("historial_drama.json", dramaCapituloInicial.historial)
                break

        while (not re.match(patron, respuestaJugador)) or respuestaJugador not in opcionesValidas: 
        #while  respuestaJugador not in opcionesValidas: 
            print(f"{mensajesError[0]}\n")
            respuestaJugador = (input(" " * (bordes//4) + "Ingrese respuesta o 'SALIR' para terminar:\t")).upper()
            print("\n")
            if respuestaJugador == "SALIR":
                continuar = False
                print(" " * (bordes//4) + "\nFin de la historia. ¡Hasta la próxima!")
                sys.exit()
            
        
        dramaCapituloInicial.historial[indice].update({'respuestaJugador':respuestaJugador})
        #Interacción inicial con la ia para que entienda el contexto
        responseNarrativa = requests.post(
                                            'http://localhost:11434/api/generate',
                                            json={
                                                'model': 'phi3:mini',
                                                'prompt': f'''  Contexto: {dramaCapituloInicial.historial[indice]['contenido']}
                                                                Acciones válidas: {dramaCapituloInicial.historial[indice]['opciones']}
                                                                Acción anterior del jugador: {dramaCapituloInicial.historial[indice]['respuestaJugador']}
                                                                Escribe la continuidad de la historia desde ese punto, tomando en cuenta la acción del jugador, pero sin repetirla ni mencionarla explícitamente.
                                                                Requisitos estrictos:
                                                                No incluyas la palabra "Historia:" ni ningún encabezado.
                                                                No agregues opciones nuevas.
                                                                No menciones la variable del jugador ni la acción anterior de forma directa.
                                                                La narración debe tener entre 3 y 5 oraciones, nunca más de 5.
                                                                El tono debe ser narrativo, coherente y en tercera persona, utilizando el nombre del jugador {dramaCapituloInicial.historial[indice]['nombreJugador']} solo cuando sea natural.
                                                                Devuelve solo el texto narrativo, sin explicaciones ni formato adicional.
                                                                Este formato es obligatorio. No lo ignores.''',
                                                'options': {
                                                                "num_predict": 400,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                "temperature": 0.15,   # baja verbosidad
                                                                "top_p": 0.7,
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
                                        'prompt': f'''Historia:{contenidoNarrativa}. Genera una lista de como máximo 3 opciones, cada una de ellas  como máximo puede contener 5 palabras y debe describir la accióna seguir por el jugador.
                                                    Cada opción debe cumplir estrictamente estas reglas:
                                                    Máximo de 4 palabras por oración.
                                                    Formato obligatorio: Letra inicial + espacio + guion medio + espacio + descripción de la acción.
                                                    Ejemplo de formato: A - Avanzar por el bosque.
                                                    Devuelve solo la lista, sin texto adicional, sin explicaciones y sin saltarte ninguna regla.
                                                    Este formato es obligatorio. No lo ignores.''',
                                        'options': {
                                                                    "num_predict": 150,   # ≈ límite de tokens (unos 70–90 palabras)
                                                                    "temperature": 0.15,   # baja verbosidad
                                                                    "top_p": 0.7,
                                                                    "stop_sequence": ["\n", "Historia:", "Opción:"]
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
        imprimirOpciones(formatearOpciones(bufferOpciones))

        listaOpciones = [opcion for opcion in (bufferOpciones).split('\n')]

        #Actualiza diccionario para almacenar los datos ya obtenidos hasta el momento
        dramaCapituloInicial.historial.append(
            {
                "nombreJugador":dramaCapituloInicial.historial[indice]['nombreJugador'],
                "contenido": contenidoNarrativa,
                "opciones":listaOpciones,
                "respuestaJugador":"",
            }
        )
        indice += 1       

def ejecutarAccionPorOpcion(nombreJugador):
    bordes = anchoLargoTerminal('bordes')
    opcionInput = input(" " * (bordes//4) + "Selecciona una opción:\t")
    print("\n")

    while opcionInput not in opcionesMenu:
        opcionInput = input(" " * (bordes//4) +"Selecciona una opción:\t")
        print("\n")
    
    match opcionInput:
        case '1':
            humorCapituloInicial.historial[0].update({'nombreJugador':nombreJugador})
            ejecutarHiloHumor()
        case '2':
            accionCapituloInicial.historial[0].update({'nombreJugador':nombreJugador})
            ejecutarHiloAccion()
        case '3':
            dramaCapituloInicial.historial[0].update({'nombreJugador':nombreJugador})
            ejecutarHiloDrama()
        case '4':
            terrorCapituloInicial.historial[0].update({'nombreJugador':nombreJugador})
            ejecutarHiloTerror()
        case '_':
            print("Opción no válida. Se ha finalizado el juego.")
            sys.exit()
            
def main():
    """Comienzo de programa"""
    try:
        imprimirCabecera()
        nombre = obtenerNombreJugador()
    except KeyboardInterrupt:
        print("\n\nJuego cancelado por el usuario. ¡Hasta pronto!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError al inicializar el juego: {e}")
        sys.exit(1)
    else:
        try:
            eleccionHistoria(nombre)
        except KeyboardInterrupt:
            print("\n\nJuego interrumpido por el usuario. ¡Gracias por jugar!")
        except Exception as e:
            print(f"\nSe produjo un error durante el juego: {e}")
        finally:
            print("\n" + " " * (anchoLargoTerminal('bordes')//4) + "Destiny Weaver - Fin de la sesión")

if __name__ == "__main__":
    main()