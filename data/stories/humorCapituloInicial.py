historial = [
    {
            "nombre_jugador":"",
            "contenido":"",
            "opciones":[],
            "respuesta_jugador":""
    }
]

def start():
    print("\n¡Te encuentras en un colorido festival en medio de la ciudad! La música, risas y luces iluminan el lugar.\n")
    print("De repente, un payaso con una nariz gigante se acerca y te desafía:")
    print("\"¿Aceptas un concurso de chistes? ¡Gana y te llevarás una sorpresa!\"")
    print("¿Qué decides hacer?")
    print("1. Aceptar el desafío y contar tu mejor chiste")
    print("2. Rechazar cortésmente y seguir disfrutando del festival")
    opcion = input("> ")

    if opcion == '1':
        print("\nPuedes sentir el nerviosismo, pero decides intentar.")
        print("Tu mejor chiste es:\n")
        print("¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.")
        print("El público estalla en risas, y el payaso te da una sonrisa gigante.")
        print("¡Has ganado una sonrisa y una pequeña bolsa con dulces!")
    elif opcion == '2':
        print("\nDecides no participar y seguir paseando por el festival.")
        print("Disfrutas de los músicos, los bailarines y la alegría en cada rincón.")
    else:
        print("Decisión inválida. La festividad sigue su curso sin ti.")
