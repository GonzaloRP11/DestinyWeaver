historial = [
    {
            "nombre_jugador":"",
            "contenido":"",
            "opciones":[],
            "respuesta_jugador":""
    }
]

def start():
    print("\nTe adentras en una antigua cabaña en medio del bosque, con tablas crujientes y ventanas rotas.")
    print("El ambiente es frio y lleno de susurros extraños que parecen venir de las sombras.")
    print("De repente, las luces parpadean y una figura espectral se materializa frente a ti.")
    print("\"¿Por qué has venido?\" - susurra la figura con una voz etérea.")
    print("¿Qué decides hacer?")
    print("1. Hacerle frente y hablar con la entidad")
    print("2. Correr sin mirar atrás y buscar una salida")
    opcion = input("> ")

    if opcion == '1':
        print("\nCon temor, le preguntas quién es y qué quiere.")
        print("La entidad te revela un secreto ancestral que podría cambiar tu destino.")
        print("Te ofrece un relicario si logras responder su acertijo. ¿Lo aceptas?")
        print("¿Sí o No?")
        respuesta = input("> ").lower()
        if respuesta == 'sí' or respuesta == 'si':
            print("\nRespondes con valentía y logras responder correctamente.")
            print("La entidad te entrega el relicario y desaparece en el humo.")
            print("A partir de ahora, tienes un objeto mágico que podría salvarte en futuras aventuras.")
        else:
            print("\nProcedías con cautela, pero la entidad se enfurece y te expulsa del lugar.")
    elif opcion == '2':
        print("\nCorres desesperado por la oscuridad del bosque, con el corazón latiendo con fuerza.")
        print("Finalmente, encuentras un claro y logras salir de la cabaña, pero el miedo se queda contigo.")
        print("Alivio, pero con una sensación de que algo aún te acecha.")
    else:
        print("Decisión inválida. La historia termina aquí.")
