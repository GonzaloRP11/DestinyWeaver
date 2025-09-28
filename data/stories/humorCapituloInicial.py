historial = [
    {
            "nombre_jugador":"",
            "contenido":"""El Tirón del Hilo Amarillo
                            Al tocar el Hilo de la Comedia, un amarillo brillante y juguetón, sientes un cosquilleo en el estómago que pronto se convierte en una risa ahogada. El ambiente sombrío de la penumbra se ilumina con una luz absurda.

                            La voz etérea se transforma en un barítono exageradamente teatral, como el de un presentador de circo que ha bebido demasiado café: ¡Ah, el hilo del bufón! El más resistente de todos, pues la risa es la armadura que nadie espera. ¡Vamos, tejedor! El mundo es un chiste, y tú tienes el remate.

                            El hilo te jala con suavidad, llevándote hacia una escena. No es una batalla, sino un dilema en la plaza central de una ciudad abarrotada. Un guardia particularmente solemne está a punto de arrestar a un anciano por una infracción ridícula: llevar un pato en la cabeza durante un día de mercado.

                            El pato, por cierto, parece disfrutar la atención.

                            La situación es tensa, pero inherentemente ridícula. Sientes cómo la energía de la Comedia te da dos herramientas para intervenir:

                            La Palabra Absurda: Intentar resolver la situación con la lógica más ridícula y enredada posible, distrayendo al guardia con un torrente de preguntas sin sentido sobre la legalidad del pato y su sombrero. Esto podría confundir al guardia, pero también podría enfurecerlo al hacerlo sentir estúpido.

                            El Tropiezo Épico: Crear una distracción física y grandiosa: tropezar de manera espectacular con un carrito de manzanas, provocando una avalancha controlada de frutas que desviaría la atención del guardia y permitiría al anciano y su pato escapar en el caos. Esto podría liberar al anciano, pero te dejaría a ti como el centro de la vergüenza pública.

                            ¿Cómo tejerás este momento?

                            A) Utilizar la Palabra Absurda (Confundir al guardia).

                            B) Provocar el Tropiezo Épico (Crear un caos controlado).""",
            "opciones":['A','B'],
            "respuesta_jugador":""
    }
]

def start():
    while True:
        print("\n¡Bienvenido al festival más colorido y divertido de toda la ciudad!\n")
        print("El lugar está lleno de risas, música, y puestos con comida y juegos.")
        print("De repente, un payaso con una nariz gigante, lentes muy grandes y una sonrisa traviesa se acerca.")
        print("\"¡Hola! ¿Te apetece participar en nuestro famoso concurso de chistes? ¡Gana una sorpresa y la gloria!\"")
        print("¿Qué decides hacer?")
        print("1. Aceptar y contar tu mejor chiste")
        print("2. Rechazar y seguir disfrutando del festival")
        print("3. Preguntar si puedes hacer un truco de magia primero")
        print("4. Pedirle al payaso que te deje hacer un espectáculo de payasos tú solo")
        opcion = input("> ")

        if opcion == '1':
            print("\n¡Genial! Subes al escenario con confianza y miras al público expectante.")
            print("Tomas un respiro y cuentas un chiste clásico pero efectivo...")
            print("\nTu chiste es:")
            print("\"¿Por qué no confía el átomo? Porque hace todo con mucho 'fuerza'\"")
            print("El público ríe a carcajadas, algunos aplauden y otros repiten el chiste.")
            print("El payaso te entrega una corona de flores y un saco de caramelos.")
            print("¡Eres la estrella del día!")
            print("¿Quieres intentar otro truco de humor ahora? (sí/no)")
            respuesta = input("> ").lower()
            if respuesta == 'sí' or respuesta == 'si':
                print("\nDecides seguir haciendo reír a todos con tus talentos ocultos.")
                print("Haces muecas, imitaciones y chistes improvisados que encantan a todos.")
            else:
                print("\nDecides tomarte un descanso y disfrutar del show de otros artistas.")
        elif opcion == '2':
            print("\nDecides que la diversión está en mirar y disfrutar sin arriesgar nada.")
            print("Uno de los payasos hace acrobacias y una caricatura gigante dibuja retratos en minutos.")
            print("¿Te entretienes probando las delicias o jugando en los puestos?")
            print("Dejas que la alegría te envuelva sin necesidad de participar.")
        elif opcion == '3':
            print("\nPreguntas si puedes hacer un truco de magia. El payaso se ríe y acepta.")
            print("Sacas una bufanda y la haces desaparecer en tus manos. ¡Magia de baratillo, pero graciosa!")
            print("El público aplaude y el payaso te da una medalla de 'Mejor Mago del Festival'.")
            print("¿Quieres intentar otro truco o seguir comiendo regalos del puesto de comida?")
        elif opcion == '4':
            print("\nPides hacer un espectáculo con tus propios trucos de payaso.")
            print("¡Te pones un vestido gracioso y empiezas a contar chistes y hacer muecas.")
            print("La gente ríe y te aplaude en un concierto de risas.")
            print("Al terminar, te entregan un premio simbólico y muchos aplausos.")
        else:
            print("\nDecisión inválida. La fiesta continúa, y tú decides simplemente observar y disfrutar.")

        print("\n¿Quieres volver a jugar esta historia de humor y alegría? (sí/no)")
        volver = input("> ").lower()
        if volver != 'sí' and volver != 'si':
            print("¡Gracias por compartir risas en el festival! ¡Hasta luego!")
            break