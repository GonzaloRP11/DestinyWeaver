import os
import json
import re
import random

def cargarDatos(archivoHistoria):
    try:
        with open(archivoHistoria, "r", encoding="utf-8") as fHistorias:
            return json.load(fHistorias)
    except (FileNotFoundError,FileExistsError) as error:
        print("Error:\t",error)

def elegirHistoria(datos):
    historias = datos["historias"]

    print("=== HISTORIAS DISPONIBLES ===")

    descripciones = [nombre for nombre in historias]

    for desc in descripciones:
        print(f"- {desc}")

    eleccion = str(input("Elegí una historia y escribí su descripción: ").strip().lower())
    while eleccion not in historias:
        print("Historia inválida, intentá otra vez.")
        eleccion = str(input("Elegí una historia y escribí su descripción: ").strip().lower())
    return historias[eleccion]


def obtenerNombre():
    patron = '^[a-zA-Z]{3,15}$'
    nombre = str(input("Ingresa tu nombre (solo letras y una longitud mínimo 3 máximo 15):\t"))
    while re.search(patron,nombre) == None:
        nombre = str(input("Ingresa tu nombre (solo letras y una longitud mínimo 3 máximo 15):\t"))
    return nombre

def jugarHistoria(historia,nombre):
    inicia = (20,0)
    vida,puntos = inicia

    estado = {
        "vida": vida,
        "puntos": puntos,
        "inventario": []
    }

    actual = historia["inicio"]
    
    jugando = True

    while jugando:

        # Verifico estado del juego
        if actual == "victoria":
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
            # ¿Es escena?
            if actual in historia["escenas"]:
                actual = ejecutar_escena(actual, historia, estado)

            # ¿Es batalla?
            elif actual in historia["batallas"]:
                actual = ejecutar_batalla(actual, historia, estado)

            else:
                print("Error: estado desconocido", actual)
                return
            
def ejecutar_escena(nombreEscena, historia, estado):
    escena = historia["escenas"][nombreEscena]

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

    # Si ganás
    estado["puntos"] += batalla["recompensa"]
    print(f"Ganaste la batalla. +{batalla['recompensa']} puntos.")

    return batalla["siguiente"]

def  mensajeComienzoJuego():
    print("=== COMIENZO DE JUEGO ===")
    print("Instrucciones:",end="\n")
    print("- Escribí una de las opciones mostradas.",end="\n")
    print("- Si la escena tiene batalla, seguí los pasos.",end="\n")
    print("- Podés ganar o perder según tus decisiones.",end="\n")
    print("Elegí una aventura para comenzar.",end="\n")


def main():
    archivoHistoria = os.path.join(os.path.dirname(__file__),"historias.json")
    mensajeComienzoJuego()
    datos = cargarDatos(archivoHistoria)
    nombreJugador = obtenerNombre()
    historia = elegirHistoria(datos)
    jugarHistoria(historia,nombreJugador)

main()