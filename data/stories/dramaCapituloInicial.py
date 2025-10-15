historial = [
    {
            "nombre_jugador":"",
            "contenido":"""El Peso del Hilo Plateado
                            Al tomar el Hilo de la Melancolía, un color plateado opaco y frío, no sientes un tirón, sino un hundimiento suave, como si la gravedad se hubiera centrado en tu pecho. El aire se vuelve más denso, cargado del dulce aroma de las flores marchitas y la música lejana de un violín triste.

                            La voz etérea baja su tono a un susurro resignado, teñido de una belleza dolorosa: Ah, el hilo de los ecos. Un tejido de recuerdos y lamentos. La tristeza te enseña el valor de lo perdido, tejedor, pero ten cuidado de no ahogarte en el pasado.

                            El hilo te envuelve con una frialdad reconfortante y te presenta una escena: Te encuentras en un jardín abandonado, bajo un cielo crepuscular y perpetuo. En el centro, hay una estatua de mármol cubierta de hiedra. La estatua representa a alguien que amaste o admiraste profundamente, y que ya no está. A sus pies, yace un cofre de madera gastado.

                            Sientes una necesidad profunda de interactuar con el símbolo de esta pérdida. El Hilo de la Melancolía te ofrece dos formas de honrar o enfrentar este dolor:

                            Abrir el Cofre: Destapar el cofre, que sabes que contiene el último recuerdo tangible de la persona (una carta, un objeto pequeño). Esto podría traer una claridad dolorosa y quizás la paz de la aceptación, pero corres el riesgo de quedar paralizado por la intensidad del recuerdo.

                            Limpiar la Estatua: Retirar la hiedra y la suciedad de la estatua, revelando el rostro y la inscripción. Es un acto de respeto y homenaje, un reconocimiento de que la persona permanece en tu memoria. Esto te daría un sentido de propósito y continuidad, pero podría ocultar la necesidad de avanzar.

                            ¿Cómo tejerás tu vínculo con el pasado?

                            A) Abrir el Cofre (Enfrentar el recuerdo).

                            B) Limpiar la Estatua (Honrar la memoria).""",
            "opciones":['A','B'],
            "respuesta_jugador":""
    }
]

'''
def start():
    while True:
        print("\nLlegas a una plaza silenciosa, donde una tensión silenciosa llena el aire.")
        print("Dos personas están en medio de un conflicto intenso, gritando y gesticulando con pasión.")
        print("Decides si quieres intervenir, escuchar y tratar de calmingarlos, o simplemente observar.")
        print("¿Qué deseas hacer?")
        print("1. Intervenir y tratar de mediar en la situación")
        print("2. Observar en silencio y dejar que las cosas se resuelvan por sí mismas")
        print("3. Buscar a alguien que pueda ayudarte primero")
        opcion = input("> ")

        if opcion == '1':
            print("\nTe acercas con calma y hablas con ambas partes.")
            print("Con palabras suaves, logras que escuchen y comprendan, evitando una pelea mayor.")
            print("La multitud te mira y algunos aplauden por tu valentía.")
            print("Como agradecimiento, un anciano te entrega una joya antigua que simboliza paz.")
            print("¿Quieres aceptar el regalo y seguir ayudando en la plaza? (sí/no)")
            respuesta = input("> ").lower()
            if respuesta == 'sí' or respuesta == 'si':
                print("\nDecides usar ese dinero para mejorar tu equipamiento o ayudar a otros necesitados.")
                print("Tu acto de heroísmo se extiende, y la ciudad te mira con respeto.")
            else:
                print("\nPrefieres dejar la joya y seguir caminos diferentes, pero la paz que has ayudado a sembrar te llena de satisfacción.")
        elif opcion == '2':
            print("\nDecides no involucrarte y simplemente observar la escena desde una distancia segura.")
            print("La discusión se intensifica, pero finalmente, los dos se calman y se retiran, dejando un ambiente cargado.")
            print("Reflexionas sobre lo que viste, pensando si debiste actuar, pero decides que quizás era mejor dejar que las cosas siguieran su curso.")
        elif opcion == '3':
            print("\nBuscas a un anciano que siempre está en la plaza, conocido por su sabiduría.")
            print("Le expones la situación y te aconseja que la paciencia y la empatía son clave.")
            print("Sigues su consejo, y con su ayuda, logras calmar a ambas partes con palabras llenas de comprensión.")
            print("Eso genera un respeto mayor entre todos en la plaza.")
            print("¿Quieres seguir ayudando en la plaza o seguir tu camino ahora?")
            print("1. Seguir ayudando")
            print("2. Irte y dejar que la plaza vuelva a la calma")
            decisión = input("> ")
            if decisión == '1':
                print("\nTienes la oportunidad de poner en práctica todo lo aprendido y dejar tu huella positiva en la comunidad.")
            else:
                print("\nAgradeces a la sabiduría del anciano y sigues tu camino, dejando atrás un ejemplo de paz.")
        else:
            print("\nDecisión inválida. La situación se resuelve sola, y vuelves a tu camino, reflexionando sobre la importancia de la pacificación.")

        print("\n¿Quieres volver a vivir esta historia de drama y reflexión? (sí/no)")
        volver = input("> ").lower()
        if volver != 'sí' and volver != 'si':
            print("¡Gracias por vivir esta historia de drama! ¡Hasta la próxima!")
            break
'''