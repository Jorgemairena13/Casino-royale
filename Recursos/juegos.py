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
   
╔══════════════════════════════════════════════════════════════════════╗
║                             🎰  SUPER SLOT 🎰                        ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║             ┌────────────┬────────────┬────────────┐                 ║
║             │   ║ {r[0][0]} ║   │   ║ {r[1][0]} ║   │   ║ {r[2][0]} ║   │                 ║
║             │   ║ {r[0][1]} ║   │   ║ {r[1][1]} ║   │   ║ {r[2][1]} ║   │                 ║
║             │   ║ {r[0][2]} ║   │   ║ {r[1][2]} ║   │   ║ {r[2][2]} ║   │                 ║
║             └────────────┴────────────┴────────────┘                 ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║ LINEAS DE PAGO:                          PREMIOS:                    ║
║  3 x 🍒 = 10 créditos                    3 x 💎 = 100 créditos       ║
║  3 x 🔔 = 20 créditos                    3 x 🤑  = 200 créditos      ║
╠══════════════════════════════════════════════════════════════════════╣
║ CRÉDITO: 100                            ÚLTIMAS GANANCIAS: 0         ║
╠══════════════════════════════════════════════════════════════════════╣
║                          [ PULSA SPACE PARA TIRAR ]                  ║
╚══════════════════════════════════════════════════════════════════════╝
"""


    def animar_maquina(self,iteraciones=40, delay=0.01):
        """Anima los carretes dentro del marco ASCII."""
        ultima = None
        premio = 0
        SIMBOLOS = ['🍒','🔔','💎','🍀','🤑','🏆']


        LISTA_SIMBOLOS = [
    [random.choice(SIMBOLOS) for _ in range(3)],  # Rodillo 1
    [random.choice(SIMBOLOS) for _ in range(3)],  # Rodillo 2
    [random.choice(SIMBOLOS) for _ in range(3)],  # Rodillo 3
]
        print(LISTA_SIMBOLOS)
        input()

       
        for _ in range(iteraciones):
            ultima = LISTA_SIMBOLOS
            reels = [random.choice(LISTA_SIMBOLOS) for _ in range(3)]
            limpiar_pantalla()
            print(self.maquina_slots(reels))
            time.sleep(delay)
        # Muestra el resultado final fijo
        limpiar_pantalla()
        print(self.maquina_slots(ultima))

        if ultima[0][1] == ultima[1][1]:
            if ultima[1][0] == '🍒':
                premio = 5
            elif ultima[1][0] == '🔔':
                premio = 10
            elif ultima[1][0] == '💎':
                premio = 50
            elif ultima[1][0] == '🏆':
                premio = 100
            elif ultima[1][0] == '🍀':
                premio = 25
            elif ultima[1][0] == '🤑':
                premio = 100
            print(f"¡GANASTE {premio} CRÉDITOS!")

        elif ultima[1][1] == ultima[2][1]:
            if ultima[1][2] == '🍒':
                premio = 5
            elif ultima[1][2]  == '🔔':
                premio = 10
            elif ultima[1][2]  == '💎':
                premio = 50
            elif ultima[1][2]  == '🏆':
                premio = 100
            elif ultima[1][2]  == '🍀':
                premio = 25
            elif ultima[1][2]  == '🤑':
                premio = 100
            print(f"¡GANASTE {premio} CRÉDITOS!")
        

        
        # Verificar si hay premio
        elif ultima[0][2] == ultima[1][2] == ultima[2][2]:
            
            if ultima[0] == '🍒':
                premio = 10
            elif ultima[0] == '🔔':
                premio = 20
            elif ultima[0] == '💎':
                premio = 100
            elif ultima[0] == '🏆':
                premio = 200
            elif ultima[0] == '🍀':
                premio = 50
            elif ultima[0] == '🤑':
                premio = 200
            
            
            print(f"¡GANASTE {premio} CRÉDITOS!")
        else:
            print("¡Inténtalo de nuevo!")
        
        return premio

