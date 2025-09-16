historial = [
    {
            "nombre_jugador":"",
            "contenido":"",
            "opciones":[],
            "respuesta_jugador":""
    }
]

def start():
    print("\nLlegas a una plaza llena de gente, donde un conflicto entre dos personas está a punto de explotar.")
    print("Un hombre y una mujer discuten acaloradamente por un incidente pasado.")
    print("¿Qué decides hacer?")
    print("1. Intervenir e intentar calmar la situación")
    print("2. Mantenerte al margen, observando en silencio")
    opcion = input("> ")

    if opcion == '1':
        print("\nTe acercas con calma y hablas con ambos.")
        print("Logras que se escuchen y comprendan, lo que ayuda a resolver el conflicto.")
        print("La gente aplaude tu valentía y honestidad.")
        print("Recibes una pequeña joya como agradecimiento, simbolizando tu bondad.")
    elif opcion == '2':
        print("\nDecides no involucrarte y simplemente observar desde lejos.")
        print("La discusión termina por sí sola, dejando un aire de tensión.")
    else:
        print("Decisión inválida. La historia termina aquí.")
