from src.combate import Personaje

historial = [
    {
            "nombre_jugador":"",
            "contenido":"",
            "opciones":[],
            "respuesta_jugador":""
    }
]

def start(inventario):
    print("\n¡Comienzas en un mundo de acción! Una misión importante te espera...\n")
    print("Te encuentras en una plaza, hay dos caminos: uno lleva a un bosque, otro a una ciudad.")
    print("¿Qué deseas hacer?")
    print("1. Explorar el bosque")
    print("2. Entrar a la ciudad")
    opcion = input("> ")

    if opcion == '1':
        print("\nCaminas hacia el bosque y encuentras un enemigo: ¡Goblin!")
        enemigo = Personaje("Goblin", 30, 8)
        jugador = Personaje("Héroe", 100, 15)
        Personaje.ejecutar_combate(jugador, enemigo)
    elif opcion == '2':
        print("\nEntras en la ciudad y te encuentras con un mercader que te ofrece una poción.")
        inventario['pocion'] += 1
        print("Tu inventario de pociones ha aumentado a:", inventario['pocion'])
    else:
        print("Decisión inválida. La historia termina aquí.")
