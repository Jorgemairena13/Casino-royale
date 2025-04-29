import random
import time
import os


def limpiar_pantalla():
    os.system('cls')


class Juegos:
    def __init__(self, nombre, apuesta_min, apuesta_max, saldo_inicial):
        self.nombre = nombre                        
        self.apuesta_min = apuesta_min              
        self.apuesta_max = apuesta_max              
        self.saldo_jugador = saldo_inicial          
        self.apuesta_actual = 0                     
        self.resultado = None                       
        self.multiplicador_pago = 0.0               
        self.historial = []                         
         

class Maquina_slots(Juegos):
    def __init__(self, nombre, apuesta_min, apuesta_max, saldo_inicial):
        super().__init__(nombre, apuesta_min, apuesta_max, saldo_inicial)
    
    def mostrar_info(self):
        print(self.nombre)
        print(self.apuesta_min)
        print(self.apuesta_max)
        print(self.saldo_jugador)

    # Plantilla completa de la máquina ASCII, con marcadores para los carretes
    def maquina_slots(self,r):
        return f"""
        ╔═════════════════════════════════════════════════════════════════╗
        ║                         ╭─────────────╮                         ║
        ║         .-~-.           │  SUPER SLOT │           .-~-.         ║
        ║        / / \\ \\          ╰─────────────╯          / / \\ \\        ║
        ║       | |   | |                                 | |   | |       ║
        ╠═══════╧═╧═══╧═╧═════════════════════════════════╧═╧═══╧═╧═══════╣
        ║                                                                 ║
        ║    █████████████████████████████████████████████████████████    ║
        ║    █                                                       █    ║
        ║    █     ┌─────────┐     ┌─────────┐     ┌─────────┐       █    ║
        ║    █     │  ╔═══╗  │     │  ╔═══╗  │     │  ╔═══╗  │       █    ║
        ║    █     │  ║ {r[0]}║  │     │  ║{r[1]} ║  │     │  ║{r[2]} ║  │       █    ║
        ║    █     │  ╚═══╝  │     │  ╚═══╝  │     │  ╚═══╝  │       █    ║
        ║    █     └─────────┘     └─────────┘     └─────────┘       █    ║
        ║    █                                                       █    ║
        ║    █████████████████████████████████████████████████████████    ║
        ║                                                                 ║
        ║    ╔═════════════════════════════════════════════════════╗      ║
        ║    ║         LINEAS DE PAGO:           PREMIOS:          ║      ║
        ║    ║    3 x 🍒 = 10 créditos     3 x 💎 = 100 créditos   ║      ║
        ║    ║    3 x 🔔 = 20 créditos     3 x 7⃣ = 200 créditos   ║      ║
        ║    ╚═════════════════════════════════════════════════════╝      ║
        ║                                                                 ║
        ║                      ┌───────────────┐                          ║
        ║         ┌───────┐    │  TIRAR (SPACE)│     ┌──────────┐         ║
        ║         │CRÉDITO│    └───────┬───────┘     │ÚLTIMAS   │         ║
        ║         │100    │            │             │GANANCIAS │         ║
        ║         └───────┘            │             │0         │         ║
        ║                          ╔═══╧═══╗         └──────────┘         ║
        ║                      ┌───╢   │   ╟───┐                          ║
        ║                      │   ╚═══╧═══╝   │                          ║
        ║                      │      ┌─┐      │                          ║
        ║                      │      │ │      │                          ║
        ║                      │      │ │      │                          ║
        ║                      │      │ │      │                          ║
        ║                      │      └─┘      │                          ║
        ║                      └───────────────┘                          ║
        ╚═════════════════════════════════════════════════════════════════╝
        """

    def animar_maquina(self,iteraciones=30, delay=0.05):
        """Anima los carretes dentro del marco ASCII."""
        ultima = None
        premio = 0
        SIMBOLOS = ['🍒','🔔','💎','🍀','⭐','7⃣']
        

        for _ in range(iteraciones):
            reels = [random.choice(SIMBOLOS) for _ in range(3)]
            limpiar_pantalla()
            print(self.maquina_slots(reels))
            time.sleep(delay)
            ultima = reels
        # Muestra el resultado final fijo
        limpiar_pantalla()
        print(self.maquina_slots(ultima))
        
        # Verificar si hay premio
        if ultima[0] == ultima[1] == ultima[2]:
            
            if ultima[0] == '🍒':
                premio = 10
            elif ultima[0] == '🔔':
                premio = 20
            elif ultima[0] == '💎':
                premio = 100
            elif ultima[0] == '7️⃣':
                premio = 200
            elif ultima[0] == '🍀':
                premio = 50
            elif ultima[0] == '⭐':
                premio = 75
            
            if premio > 0:
                print(f"¡GANASTE {premio} CRÉDITOS!")
        else:
            print("¡Inténtalo de nuevo!")
        
        return premio

