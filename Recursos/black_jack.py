import random
from time import sleep

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
        
    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def valor_numerico(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11  # Por defecto el As vale 11, luego se puede cambiar a 1 si es necesario
        else:
            return int(self.valor)
    
    def mostrar_carta(self):
        simbolo = '♠' if self.palo == 'Picas' else '♥' if self.palo == 'Corazones' else '♦' if self.palo == 'Diamantes' else '♣'
        return f"""
        ┌───────┐
        │{self.valor:<2}     │
        │{simbolo}      │
        │       │
        │   {simbolo}   │
        │       │
        │      {simbolo}│
        │     {self.valor:>2}│
        └───────┘
        """

class Baraja:
    def __init__(self):
        VALORES_CARTAS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        PALOS = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
        self.cartas = [Carta(valor, palo) for valor in VALORES_CARTAS for palo in PALOS]
        self.mezclar()
        
    def mezclar(self):
        random.shuffle(self.cartas)
        
    def dar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            print("¡La baraja está vacía!")
            return None

class Jugador:
    def __init__(self):
        self.mano = []
        self.valor_total = 0
        self.plantado = False
        
        
    def pedir_carta(self, carta):
        self.mano.append(carta)
        self.calcular_valor()
        return carta
    
    def calcular_valor(self):
        # Primero calculamos el valor sin considerar los Ases
        valor = sum(carta.valor_numerico() for carta in self.mano)
        
        # Contamos cuántos Ases hay en la mano
        ases = sum(1 for carta in self.mano if carta.valor == 'A')
        
        # Ajustamos el valor si tenemos Ases y nos pasamos de 21
        while valor > 21 and ases > 0:
            valor -= 10  # Convertimos un As de 11 a 1
            ases -= 1
            
        self.valor_total = valor
        return self.valor_total
    
    def plantarse(self):
        self.plantado = True
    
    def mostrar_mano(self):
        print("Tu mano:")
        for carta in self.mano:
            print(carta.mostrar_carta())
        print(f"Valor total: {self.valor_total}")

class Crupier(Jugador):
    def __init__(self):
        super().__init__()
    
    def mostrar_primera_carta(self):
        if len(self.mano) > 0:
            return self.mano[0].mostrar_carta()
        return ""
    
    def mostrar_mano_inicial(self):
        print("Carta visible del crupier:")
        print(self.mostrar_primera_carta())
        print("Segunda carta oculta")
    
    def jugar_turno(self, baraja):
        print("Turno del crupier:")
        print("Mano completa del crupier:")
        for carta in self.mano:
            print(carta.mostrar_carta())
            
        # El crupier pide carta hasta tener 17 o más
        while self.valor_total < 17:
            print("El crupier pide carta...")
            sleep(1)  # Pausa para crear suspense
            nueva_carta = self.pedir_carta(baraja.dar_carta())
            print(f"El crupier recibe: {nueva_carta}")
            print(nueva_carta.mostrar_carta())
            print(f"Valor total del crupier: {self.valor_total}")
            
            if self.valor_total > 21:
                print("¡El crupier se ha pasado!")
                break
        
        if self.valor_total <= 21:
            print(f"El crupier se planta con {self.valor_total}")

class Black_jack:
    def __init__(self,saldo):
        self.baraja = Baraja()
        self.jugador = Jugador()
        self.crupier = Crupier()
        self.saldo = saldo
    def iniciar_juego(self):
        print("¡Bienvenido al Black Jack!")
        print("Repartiendo cartas iniciales...")
        
        # Dar dos cartas al jugador
        self.jugador.pedir_carta(self.baraja.dar_carta())
        self.jugador.pedir_carta(self.baraja.dar_carta())
        
        # Dar dos cartas al crupier
        self.crupier.pedir_carta(self.baraja.dar_carta())
        self.crupier.pedir_carta(self.baraja.dar_carta())
        
        # Mostrar las cartas
        self.jugador.mostrar_mano()
        self.crupier.mostrar_mano_inicial()
        
        # Verificar BlackJack natural
        if self.jugador.valor_total == 21:
            print("¡Has ganado!")
            self.saldo *= 3
            return self.saldo
        
        # Turno del jugador
        self.turno_jugador()
        
        # Si el jugador no se ha pasado es el turno del crupier
        if self.jugador.valor_total <= 21:
            self.crupier.jugar_turno(self.baraja)
            
        # Determinar ganador
        return self.determinar_ganador()
    
    def turno_jugador(self):
        while not self.jugador.plantado and self.jugador.valor_total < 21:
            accion = input("\n¿Qué deseas hacer? (p = pedir carta, m = plantarse): ").lower()
            
            if accion == 'p':
                nueva_carta = self.jugador.pedir_carta(self.baraja.dar_carta())
                print(f"Has recibido: {nueva_carta}")
                print(nueva_carta.mostrar_carta())
                self.jugador.mostrar_mano()
                
                if self.jugador.valor_total > 21:
                    print("¡Te has pasado de 21! Has perdido.")
                    break
            elif accion == 'm':
                self.jugador.plantarse()
                print("Te has plantado con", self.jugador.valor_total)
            else:
                print("Opción no válida. Intenta de nuevo.")
    
    def determinar_ganador(self):
        print("\n--- Resultado final ---")
        print(f"Tu puntuación: {self.jugador.valor_total}")
        print(f"Puntuación del crupier: {self.crupier.valor_total}")
        
        # Determinar ganador
        if self.jugador.valor_total > 21:
            print("Has perdido por pasarte de 21.")
            self.saldo = 0
            return self.saldo
        elif self.crupier.valor_total > 21:
            print("¡El crupier se ha pasado! ¡Has ganado!")
            self.saldo *= 2
            return self.saldo
        elif self.jugador.valor_total > self.crupier.valor_total:
            print("¡Has ganado!")
            self.saldo *= 2
            return self.saldo
        elif self.jugador.valor_total < self.crupier.valor_total:
            print("El crupier gana.")
            self.saldo = 0
            return self.saldo
        else:
            print("¡Empate!")
            # El saldo no cambia, recupera la apuesta
            return self.saldo



