from src.combate import Personaje

historial = [
    {
            "nombre_jugador":"",
            "contenido":"",
            "opciones":[],
            "respuesta_jugador":""
    }
]

inventario = {
    'pocion': 1,
    'espada': 1
}

def start():
    while True:
        print("\n¡Bienvenido a un mundo lleno de desafíos y aventuras!\n")
        print("Eres un héroe recién llegado a la ciudad de Eldoria, un lugar donde la paz y el caos conviven en tensión.")
        print("El sol brilla sobre las calles, pero en el aire hay una sensación inquietante de que algo malo va a ocurrir.\n")
        print(f"Tu inventario inicial: Pociones={inventario['pocion']}, Espadas={inventario['espada']}\n")

        print("Mientras caminas por la plaza principal, un mensajero aparece en tu camino, agitado y con el rostro pálido.")
        print("\"¡Héroe! La amenaza que acecha a nuestra ciudad está más cerca de lo que pensábamos,\" dice.")
        print("El mensajero entrega un pergamino con un mensaje urgente en letras temblorosas.")
        print("\"El ejército oscuro avanza desde las montañas. Necesitamos que decidas tu próximo paso:\"")
        print("¿Qué deseas hacer?")
        print("1. Ir al bosque en busca de una criatura peligrosa que puede ser clave para detener a los invasores.")
        print("2. Entrar en la ciudad y buscar información en los mercados y calles.")
        print("3. Ir al cuartel general para prepararte, entrenar y fortalecer tus habilidades.")
        print("4. Ignorar la amenaza por ahora, y seguir tu propio camino confiado en tu suerte.")

        opcion = input("> ")

        if opcion == '1':
            print("\nDecides adentrarte en las sombras del bosque. La vegetación densa y el silencio inquietante te rodean.")
            print("De repente, sonidos de ramas rotas y pasos rápidos te alertan de un ataque inminente.")
            print("Un grupo de goblins aparece, liderados por un goblin más grande y feroz.")
            enemigo = Personaje("Goblin Líder", 60, 14)
            jugador = Personaje("Héroe", 100, 20)

            Personaje.ejecutar_combate(jugador, enemigo)
            if jugador.vida > 0:
                print("\nTras vencer, encuentras un relicario brillante enterrado en el suelo. Tiene símbolos antiguos que parecen resonar con el peligro que se acerca.")
                print("Este relicario podría tener un poder que ayuda a detener a la amenaza o desbloquear antiguos secretos.")
                # Se puede agregar lógica adicional para usar el relicario en la historia
            else:
                print("Has sido derrotado en el combate. La amenaza crece en la oscuridad... fin de tu historia.")

        elif opcion == '2':
            print("\nDecides entrar en la ciudad. Las calles está llenas de vida, aunque una sensación de tensión se respira.")
            print("Mientras examines los puestos, un anciano te llama desde su puesto.")
            print("\"Joven héroe, he escuchado rumores de movimientos extraños en las afueras. Si quieres obtener información, ayúdame a detener a unos ladrones que asaltan en las callejuelas.\"")
            print("¿Quieres ayudar al anciano? (sí/no)")
            ayuda = input("> ").lower()
            if ayuda == 'sí' or ayuda == 'si':
                print("\nAyudas al anciano a atrapar a unos ladrones que estaban saqueando su puesto y el de otros comerciantes.")
                print("En agradecimiento, te entrega un amuleto que, según dice, protege contra las fuerzas oscuras.")
                inventario['amuleto'] = inventario.get('amuleto', 0) + 1
                print(f"Ahora tienes un amuleto en tu inventario. Total: {inventario['amuleto']}")
            else:
                print("\nDecides seguir investigando en los mercados. Pronto, un guardia te advierte que lo que se acerca es mucho peor.")
                print("No tienes mucho tiempo para prepararte.")

        elif opcion == '3':
            print("\nVas al cuartel, donde los soldados te reciben con respeto y determinación.")
            print("El comandante te entrega un conjunto de equipos y te explica que se preparan para una ofensiva.")
            print("También te ofrece la opción de usar una poción de fortaleza antes de la misión.")
            if inventario['pocion'] > 0:
                print(f"Tienes {inventario['pocion']} poción(es). ¿Quieres usar una ahora? (sí/no)")
                usar = input("> ").lower()
                if usar == 'sí' or usar == 'si':
                    inventario['pocion'] -= 1
                    print("Usas una poción de fortaleza. Tu vida aumenta en 20 puntos.")
                else:
                    print("Decides no usar la poción y te entrenas con lo que tienes.")
            else:
                print("No tienes pociones disponibles en tu inventario, pero aún puedes entrenar con las armas y habilidades que ya posees.")

            print("\nLuego de prepararte, el comandante te informa que es momento de partir hacia las tierras que amenazan la ciudad.")
            print("Tu misión es infiltrarte en las líneas enemigas y sabotear sus operaciones desde adentro.")
            print("¿Quieres aceptar esta misión secreta? (si/no)")
            mision_secreta = input("> ").lower()

            if mision_secreta == 'sí' or mision_secreta == 'si':
                print("\nDecides aceptar la misión y te equipas para la infiltración.")
                print("Te entregan un equipo especial y un mapa detallado de las posiciones enemigas.")
                print("Con sigilo y precisión, logras atravesar las líneas y sabotear las máquinas de guerra de los invasores.")
                print("Tu éxito protege a la ciudad y fortalece las fuerzas de resistencia.")
                print("¡Eres un héroe en las sombras!")
            else:
                print("\nDecides que la estrategia frontal puede ser más segura. Reúnes a las fuerzas y lanzan un ataque directo.")
                print("La batalla es dura, pero lograron defender la ciudad. Aunque no lograste infiltrarte, tu presencia explica mucho.")
                print("Tu heroísmo se reconoce en toda Eldoria.")

        elif opcion == '4':
            print("\nDecides ignorar la amenaza y seguir tu propio camino, confiando en tu suerte.")
            print("Al principio, esto parece lo más prudente y te permite explorar rincones desconocidos.")
            print("Sin embargo, pronto te enteras de que la amenaza creció en tu ausencia, afectando a muchas personas.")
            print("¿Llevado por la culpa o la reflexión, decides regresar para ayudar en lo que puedas?")
            print("1. Sí, vuelvo para apoyar a la gente y luchar contra la amenaza.")
            print("2. Continúo mi camino, confiando en que encontré mi destino en otros lugares.")
            decision = input("> ")

            if decision == '1':
                print("\nRegresas decidido a hacer lo correcto. Te unes a las fuerzas locales y luchas con valentía.")
                print("Con esfuerzo y estrategia, logras contribuir a detener la invasión.")
                print("Aunque llegaste tarde, tu determinación hace una gran diferencia.")
            elif decision == '2':
                print("\nSigues tu camino, dejando atrás la amenaza. Quizás fue una decisión egoísta, pero sientes que debes seguir buscando tu propio destino.")
                print("La historia continúa, y quizás en el futuro regreses a enfrentarte a nuevas amenazas.")
            else:
                print("Decisión no válida. Sin una elección clara, decides seguir tu camino sin mirar atrás.")
                print("La historia queda en tus manos para seguir desarrollándose según tus decisiones.")
   
        print("\n¿Quieres volver a jugar esta historia de acción? (sí/no)")
        volver = input("> ").lower()
        if volver != 'si' or volver != 'sí':
            break

