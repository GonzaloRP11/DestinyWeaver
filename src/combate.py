class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, enemigo):
        daño = self.ataque
        enemigo.recibir_danio(daño)

    def recibir_danio(self, daño):
        self.vida -= daño
        print(f"{self.nombre} recibe {daño} daño. Vida restante: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado!")
            return True
        return False
    
    def ejecutar_combate(jugador, enemigo):
        print(f"\n¡Un combate empieza entre {jugador.nombre} y {enemigo.nombre}!\n")
        while jugador.vida > 0 and enemigo.vida > 0:
            # Turno del jugador
            input("Presiona Enter para atacar...")
            jugador.atacar(enemigo)
            if enemigo.vida <= 0:
                print(f"¡{enemigo.nombre} ha sido derrotado!")
                break
            # Turno del enemigo
            enemigo.atacar(jugador)
            if jugador.vida <= 0:
                print(f"{jugador.nombre} ha sido vencido. Fin del combate.")
                break