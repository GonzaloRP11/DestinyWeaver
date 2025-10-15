historial = [
    {
            "nombre_jugador":"",
            "contenido":""" La Fragilidad del Hilo Azul Oscuro
                           
                            Al rozar el Hilo del Miedo, de un azul tan profundo que casi parece negro, sientes un escalofrío que no es de frío, sino de anticipación. Una punzada de terror ancestral te recorre la espina dorsal, un recordatorio de todo lo que has querido evitar.

                            La voz etérea se reduce a un siseo helado y penetrante, como el viento que se cuela por una grieta: El miedo... La herramienta más afilada de todas. Te obliga a ver las sombras antes de que te consuman. Pero, ¿te esconderás, o lo usarás para ver?

                            El hilo se enrolla suavemente en tu muñeca y te arrastra hacia una visión: Te encuentras en un pasillo largo y silencioso. El aire es denso y huele a polvo viejo y hierro oxidado. Al final del pasillo, una puerta entreabierta deja escapar una luz parpadeante y un sonido apenas audible: una respiración que no es humana.

                            Tu corazón late con fuerza. El Miedo te ofrece dos rutas, cada una una prueba de tu voluntad:

                            La Evasión Silenciosa: Retroceder lentamente por donde viniste, utilizando el pánico como un radar para detectar el menor sonido, la menor vibración. Tu objetivo es desaparecer sin hacer ruido, dejando lo desconocido en paz. Esto garantizaría tu seguridad inmediata, pero te dejaría con la duda que te perseguirá por siempre.

                            La Confrontación Furtiva: Acercarte a la puerta, pegándote a la pared y avanzando centímetro a centímetro, usando el terror no para huir, sino para agudizar tus sentidos al máximo, preparándote para un vistazo rápido o un ataque sorpresa. Esto podría revelar la naturaleza de la amenaza, pero te pondría en peligro inminente.

                            ¿Cómo tejerás tu respuesta ante la sombra de lo desconocido?

                            A) Retroceder con Evasión Silenciosa (Buscar seguridad).

                            B) Acercarte con Confrontación Furtiva (Buscar la verdad).""",
            "opciones":[],
            "respuesta_jugador":""
    }
]

'''
inventario = {
    'pocion': 1,           # Pociones para recuperar vida si decides enfrentarte a algo o escapar
    'amuleta': 0,          # Objeto que puedes usar para protección contra fantasmas o entidades oscuras
    'linterna': 1,         # Útil para iluminar en la oscuridad
    'amuletos_mago': 1     # Un objeto mágico que puede protegerte o ayudarte a resolver acertijos relacionados con espíritus
}

def start():
    while True:
        print("\nCaminas por un bosque oscuro, donde la luna apenas ilumina el sendero.")
        print("El aire está pesado, y escuchas susurros que parecen provenir de las sombras.")
        print("De repente, una figura espectral aparece ante ti, flotando con ojos que brillan en la oscuridad.")
        print("\"¿Por qué has venido aquí?\" - susurra la figura con una voz fría y etérea.")
        print("¿Qué decides hacer?")
        print("1. Hacerle frente y preguntarle quién es")
        print("2. Huir lo más rápido que puedas")
        print("3. Intentar comunicarte y ganar su confianza")
        print("4. Sacar la linterna para intentar ver mejor")
        opcion = input("> ")

        if opcion == '1':
            print("\nTe acercas con valor y preguntas quién es.")
            print("La figura te revela un secreto ancestral, una historia de un espíritu atrapado en ese bosque.")
            print("Te ofrece un trato: si logras resolver su acertijo, te dará un poder.")
            print("¿Aceptarás el desafío? (sí/no)")
            respuesta = input("> ").lower()
            if respuesta == 'sí' or respuesta == 'si':
                print("\nRespondes con valor y logras resolver su acertijo.")
                print("El espíritu te concede un poder místico que puede usarse en futuras aventuras.")
            else:
                print("\nDecides no arriesgarte y la figura se enfurece, desapareciendo en una nube de humo.")
                print("El silencio vuelve, pero algo oscuro aún acecha en el bosque.")
        elif opcion == '2':
            print("\nCorres sin mirar atrás, esquivando raíces y ramas.")
            print("A lo lejos, ves una figura espectral que comienza a perseguirte.")
            if inventario['amuleta'] > 0:
                print("Recuerdas que tienes un amuleto mágico para protección.")
                print("¿Quieres usar el amuleto ahora? (sí/no)")
                usar_amulet = input("> ").lower()
                if usar_amulet == 'sí' or usar_amulet == 'si':
                    print("Usas el amuleto y la figura se desvanece en una nube de humo, protegéndote.")
                else:
                    print("Decides no usar el amuleto y la figura te alcanza, dejando una sensación de frío extremo.")
            else:
                print("Sin objetos mágicos, la figura te alcanza y tu visión se vuelve oscura.")
                print("Perdiste en el bosque oscuro.")
                break
        elif opcion == '3':
            print("\nIntentas comunicarte con calma y ganar su confianza.")
            print("El espíritu te cuenta una historia trágica y te pide ayuda para descansar en paz.")
            if inventario['amuletos_mago'] > 0:
                print("Sacando tu amuleto mágico, enfocas su energía hacia el espíritu.")
                print("El espíritu se calma, y puedes liberar su energía para protegerte en el futuro.")
                inventario['amuletos_mago'] -= 1
                print("Has usado el amuleto mágico. Quedas con un poder protector.")
            else:
                print("Sin objetos mágicos, solo con tus palabras logras calmarlo, pero no le das nada que le ayude.")
        elif opcion == '4':
            if inventario['linterna'] > 0:
                print("\nSacando tu linterna, iluminas el lugar.")
                print("La luz revela una figura espectral menor que te intenta engañar con ilusiones.")
                print("Con la linterna apunto a la figura y su energía se disipa en la luz.")
                inventario['linterna'] -= 1
                print("Has usado la linterna y ahora tienes que buscar otra fuente de luz para seguir.")
            else:
                print("\nNo tienes linterna. La oscuridad te envuelve, y la figura espectral te sorprende.")
                print("Perdiste en la oscuridad.")
                break
        else:
            print("\nDecisión inválida. La figura espectral desaparece en la penumbra, dejándote solo en el bosque.")

        print("\n¿Quieres volver a vivir esta historia de terror? (sí/no)")
        volver = input("> ").lower()
        if volver != 'sí' and volver != 'si':
            print("¡Gracias por explorar este mundo oscuro! ¡Hasta luego!")
            break
'''