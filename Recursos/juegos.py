import random
import time
import os

def limpiar_pantalla():
    os.system('cls')


class Juego:
    def __init__(self, nombre: str, apuesta_min: int, apuesta_max: int, saldo_inicial: int = 100):
        self.nombre = nombre                        # Nombre del juego
        self.apuesta_min = apuesta_min              # Apuesta mínima permitida
        self.apuesta_max = apuesta_max              # Apuesta máxima permitida
        self.saldo_jugador = saldo_inicial          # Saldo actual del jugador
        self.apuesta_actual = 0                     # Apuesta de la ronda en curso
        self.resultado = None                       # Resultado de la ronda
        self.multiplicador_pago = 0.0               # Factor de pago de la ronda
        self.historial = []                         # Registro de rondas jugadas
        self.rng = random.Random()                  # Generador de aleatorios
# Tus símbolos
SIMBOLOS = ['🍒','🔔','💎','🍀','⭐','7️⃣']

# Función que limpia la pantalla


# Plantilla completa de la máquina ASCII, con marcadores para los carretes
def maquina_slots(r):
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
    ║    ║    3 x 🔔 = 20 créditos     3 x 7️⃣ = 200 créditos   ║      ║
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

def animar_maquina(iteraciones=30, delay=0.08):
    """Anima los carretes dentro del marco ASCII."""
    ultima = None
    for _ in range(iteraciones):
        reels = [random.choice(SIMBOLOS) for _ in range(3)]
        limpiar_pantalla()
        print(maquina_slots(reels))
        time.sleep(delay)
        ultima = reels
    # Muestra el resultado final fijo
    limpiar_pantalla()
    print(maquina_slots(ultima))
    
    # Verificar si hay premio
    if ultima[0] == ultima[1] == ultima[2]:
        premio = 0
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
    
    return ultima

print(animar_maquina())
input()