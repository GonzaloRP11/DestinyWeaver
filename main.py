import os
import json
import re
import random

def cargarDatos(archivoHistoria):
    """Carga el archivo historias.json"""
    try:
        with open(archivoHistoria, "r", encoding="utf-8") as fHistorias:
            return json.load(fHistorias)
    except (FileNotFoundError) as error:
        print("Error:\t",error)

def elegirHistoria(datos):
    """Impresión de historias y elección del usuario"""
    historias = datos["historias"]

    print("=== HISTORIAS DISPONIBLES ===")

    descripciones = [nombre for nombre in historias]

    for desc in descripciones:
        print(f"- {desc}")

    eleccion = str(input("Elegí una historia y escribí su descripción: ").strip().lower())
    while eleccion not in historias:
        print("Historia inválida, intentá otra vez.")
        eleccion = str(input("Elegí una historia y escribí su descripción: ").strip().lower())
    
    #Mostrar mapa de la aventura que se jugará
    mostrarMapa(eleccion)

    return historias[eleccion]


def validarNombre(nombre):
    patron = '^[a-zA-Z]{3,15}$'
    return re.search(patron, nombre) != None


def obtenerNombre():
    """Obtener nombre de jugador"""
    nombre = str(input("Ingresa tu nombre (solo letras y una longitud mínimo 3 máximo 15):\t"))
    while not validarNombre(nombre):
        nombre = str(input("Ingresa tu nombre (solo letras y una longitud mínimo 3 máximo 15):\t"))
    return nombre

def jugarHistoria(historia,nombre):
    """Inicio del juego"""
    inicia = (20,0)
    vida,puntos = inicia

    estado = {
        "vida": vida,
        "puntos": puntos,
        "inventario": [],
        "escenas_visitadas":set()
    }

    actual = historia["inicio"]
    
    jugando = True

    while jugando:

        # Verifico si es final victoria o derrota
        if actual == "victoria":
            estado["puntos"] += historia.get("recompensa_victoria")
            print(f"¡VICTORIA {nombre}!")
            print(historia["finales"]["victoria"])
            print(f"Puntos totales: {estado['puntos']}")
            jugando = False
        elif actual == "derrota":
            print(f"DERROTA {nombre}")
            print(historia["finales"]["derrota"])
            print(f"Puntos alcanzados: {estado['puntos']}")
            jugando = False
        else:
            # procesa escena
            if actual in historia["escenas"]:
                actual = ejecutarEscena(actual, historia, estado)

            # procesa batalla
            elif actual in historia["batallas"]:
                actual = ejecutar_batalla(actual, historia, estado)

            else:
                print("Error: estado desconocido", actual)
                return
            
def ejecutarEscena(nombreEscena, historia, estado):

    escena = historia["escenas"][nombreEscena]
    estado["escenas_visitadas"].add(nombreEscena)

    print("---------------------------------")
    print(escena["descripcion"])
    print("---------------------------------")

    # Mostrar opciones
    for opciones in escena["opciones"]:
        print(f"- {opciones}")

    eleccion = input("¿Qué hacés?: ").strip().lower()

    while eleccion not in escena["opciones"]:
        eleccion = input("¿Qué hacés?: ").strip().lower()
    
    siguiente = escena["opciones"][eleccion]

    if "recompensa_inventario" in escena:
        for item in escena["recompensa_inventario"]:
            estado["inventario"].append(item)
            print(f"Obtenés: {item}")

    return siguiente


def ejecutar_batalla(nombre_batalla, historia, estado):
    """Ejecución de batalla"""
    batalla = historia["batallas"][nombre_batalla]

    print("=== ¡COMIENZA LA BATALLA! ===")
    print(batalla["descripcion"])

    vidaJugador = batalla["vida_jugador"]
    vidaEnemigo = batalla["vida_enemigo"]

    daño = lambda minimo, maximo: random.randint(minimo, maximo)
    dañoMinJugador,dañoMaxJugador = batalla["daño_jugador"]
    dañoMinEnemigo,dañoMaxEnemigo = batalla["daño_enemigo"]

    while vidaJugador > 0 and vidaEnemigo > 0:
        input("Presioná ENTER para atacar...")

        dañoJugador = daño(dañoMinJugador,dañoMaxJugador)
        dañoEnemigo = daño(dañoMinEnemigo,dañoMaxEnemigo)

        vidaEnemigo -= dañoJugador
        vidaJugador -= dañoEnemigo

        print(f"Pegás {dañoJugador} | El enemigo te pega {dañoEnemigo}")
        print(f"Tu vida: {vidaJugador} | Vida enemigo: {dañoEnemigo}")

        if vidaJugador <= 0:
            return "derrota"

    # Suma de puntos si se gana
    estado["puntos"] += batalla["recompensa"]
    print(f"Ganaste la batalla. +{batalla['recompensa']} puntos.")

    return batalla["siguiente"]



def mostrarMapa(nombreHistoria):
    mapas = {
                "aventura_clasica": [
                    ["bosque", "sendero"],
                    ["cueva"]
                ],
                "estacion_espacial": [
                    ["laboratorio", "pasillo"],
                    ["sala"]
                ],
                "mazmorra_magica": [
                    ["celda", "pasillo"],
                    ["pared", "camara"]
                ]
            }
    
    print("\n=== MAPA DE LA AVENTURA ===")
    matriz = mapas.get(f"{nombreHistoria}")

    # Recorremos la matriz (lista de listas)
    for fila in matriz:
        print(" | ".join(fila))
    print("===========================\n")

def obtenerMapa(nombreHistoria):
    mapas = {
        "aventura_clasica": [
            ["bosque", "sendero"],
            ["cueva"]
        ],
        "estacion_espacial": [
            ["laboratorio", "pasillo"],
            ["sala"]
        ],
        "mazmorra_magica": [
            ["celda", "pasillo"],
            ["pared", "camara"]
        ]
    }
    return mapas.get(nombreHistoria)

def mostrarMapa(nombreHistoria):
    matriz = obtenerMapa(nombreHistoria)
    print("\n=== MAPA DE LA AVENTURA ===")
    for fila in matriz:
        print(" | ".join(fila))
    print("===========================\n")


def  mensajeComienzoJuego():
    print("=== COMIENZO DE JUEGO ===")
    print("Instrucciones:",end="\n")
    print("- Escribí una de las opciones mostradas.",end="\n")
    print("- Si la escena tiene batalla, seguí los pasos.",end="\n")
    print("- Podés ganar o perder según tus decisiones.",end="\n")
    print("Elegí una aventura para comenzar.",end="\n")
    print("==========================",end="\n")


def main():
    archivoHistoria = os.path.join(os.path.dirname(__file__),"historias.json")
    #Mensaje comienzo de juego
    mensajeComienzoJuego()
    #Cargar historias del archivo json
    datos = cargarDatos(archivoHistoria)
    #Obtener nombre del jugador
    nombreJugador = obtenerNombre()
    #Elegir historia a jugar y mostrar mapa
    historia = elegirHistoria(datos)
    #Ejecutar historia
    jugarHistoria(historia,nombreJugador)

if __name__ == "__main__":
    main()
