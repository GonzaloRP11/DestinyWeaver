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
    inicia = (10,0)
    vida,puntos = inicia

    estado = {
        "vida": vida,
        "puntos": puntos,
        "inventario": [],
        "escenas_visitadas":set(),
        "logros": []
    }

    actual = historia["inicio"]
    
    jugando = True

    while jugando:

        if actual == "victoria":
            estado["puntos"] += historia.get("recompensa_victoria", 0)
            print(f"¡VICTORIA {nombre}!")
            print(historia["finales"]["victoria"])
            print(f"Puntos totales: {estado['puntos']}")
            jugando = False
            cantidad_escenas = contarRecursivo(list(estado["escenas_visitadas"]))
            print(f"Escenas visitadas: {cantidad_escenas}")
        elif actual == "derrota":
            print(f"DERROTA {nombre}")
            print(historia["finales"]["derrota"])
            print(f"Puntos alcanzados: {estado['puntos']}")
            jugando = False
            cantidad_escenas = contarRecursivo(list(estado["escenas_visitadas"]))
            print(f"Escenas visitadas: {cantidad_escenas}")
        else:
            if actual in historia["escenas"]:
                actual = ejecutarEscena(actual, historia, estado)

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
        
    for opciones in escena["opciones"]:
        print(f"- {opciones}")

    eleccion = input("¿Qué hacés?: ").strip().lower()

    while eleccion not in escena["opciones"]:
        eleccion = input("Opción inválida. ¿Qué hacés?: ").strip().lower()
    
    siguiente = escena["opciones"][eleccion]

    if eleccion == "abrir":
        if "recompensa_inventario" in escena:
            for item in escena["recompensa_inventario"]:
                estado["inventario"].append(item)
                print(f"Obtenés: {item}")
        
        print(f"Verificando poción. Vida actual: {estado['vida']}.")
        
        if "pocion_de_salud" in estado["inventario"]:
            usar_pocion = input("¿Quieres usar una poción de salud? (si/no): ").strip().lower()
            if usar_pocion == "si":
                estado["vida"] = 10
                estado["inventario"].remove("pocion_de_salud")
                print("Usaste una poción de salud. Vida restaurada al máximo.")
            else:
                print("No usaste la poción de salud.")

    print(f"Vida: {estado['vida']} | Puntos: {estado['puntos']} | Inventario: {estado['inventario']}") 
    
    return siguiente


def ejecutar_batalla(nombre_batalla, historia, estado):
    """Ejecución de batalla"""
    batalla = historia["batallas"][nombre_batalla]

    print("=== ¡COMIENZA LA BATALLA! ===")
    print(batalla["descripcion"])

    vidaMaximaJugador = 10  
    estado["vida"] = vidaMaximaJugador  
    vidaEnemigo = batalla["vida_enemigo"]

    daño = lambda minimo, maximo: random.randint(minimo, maximo)
    dañoMinJugador,dañoMaxJugador = batalla["daño_jugador"]
    dañoMinEnemigo,dañoMaxEnemigo = batalla["daño_enemigo"]

    while estado["vida"] > 0 and vidaEnemigo > 0:
        input("Presioná ENTER para atacar...")
        dañoJugador = daño(dañoMinJugador,dañoMaxJugador)
        dañoEnemigo = daño(dañoMinEnemigo,dañoMaxEnemigo)

        vidaEnemigo -= dañoJugador
        estado["vida"] -= dañoEnemigo

        print(f"Pegás {dañoJugador} | El enemigo te pega {dañoEnemigo}")
        print(f"Tu vida: {estado['vida']} | Vida enemigo: {vidaEnemigo}")

        if estado["vida"] <= 0:
            print("Has sido derrotado.")
            return "derrota"

    if vidaEnemigo <= 0:
        estado["puntos"] += batalla["recompensa"]
        print(f"Ganaste la batalla. +{batalla['recompensa']} puntos.")
        if "Ganador de Batallas" not in estado["logros"]:
            estado["logros"].append("Ganador de Batallas")
            print("¡Logro desbloqueado: Ganador de Batallas!")

    return batalla["siguiente"]


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


def contarRecursivo(lista):
    """Cuenta elementos de una lista usando recursividad."""
    if len(lista) == 0:
        return 0
    return 1 + contarRecursivo(lista[1:])


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
    mensajeComienzoJuego()
    datos = cargarDatos(archivoHistoria)
    nombreJugador = obtenerNombre()
    historia = elegirHistoria(datos)
    jugarHistoria(historia,nombreJugador)

if __name__ == "__main__":
    main()
