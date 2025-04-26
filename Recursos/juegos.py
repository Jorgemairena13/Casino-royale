import random
import time
import os
from Recursos.juegos import *
from Recursos.interfaz import *

# Tus símbolos
SIMBOLOS = ['🍒','🔔','💎','🍀','⭐','7️⃣']

# Función que limpia la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Plantilla completa de la máquina ASCII, con marcadores para los carretes
def render_maquina(r):
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
        clear_screen()
        print(render_maquina(reels))
        time.sleep(delay)
        ultima = reels
    # Muestra el resultado final fijo
    clear_screen()
    print(render_maquina(ultima))
    
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
