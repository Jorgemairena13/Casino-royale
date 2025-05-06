import random
import time
import os
from rich.text import Text
from rich import print 
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from rich.table import Table
from prompt_toolkit.completion import FuzzyWordCompleter
from rich.console import Console
from datetime import datetime
from time import sleep


console = Console()





def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

class MaquinaTragaperras:
    def __init__(self):
        # Definimos los símbolos ASCII y sus valores correspondientes
        # Todos los ASCII art tienen exactamente 15 líneas y 30 caracteres de ancho
        self.SIMBOLOS = {
            "CEREZA": {
                "ascii": [
                    "                              ",
                    "            [#27ff58]███[/]               ",
                    "         [#27ff58]███████████[/]          ",
                    "      [#27ff58]██████████████[/]          ",
                    "     [#27ff58]██  ██ █████████[/]         ",
                    "    [#27ff58]██   █     ███████[/]        ",
                    "    [#27ff58]██   █        ██[/]          ",
                    "   [#27ff58]██    ██[/]                   ",
                    "   [#ff0000]█████████ ██  ███[/]          ",
                    "[#ff0000]███████████ ████████[/]          ",
                    "[#ff0000]██████████████████████[/]        ",
                    "[#ff0000]██████████████████████[/]        ",
                    "[#ff0000]████████████████████[/]          ",
                    "  [#ff0000]████    █████████[/]           ",
                    "          [#ff0000]████[/]                "
                ],
                "emoji": "🍒",
                "valor": 10,
                "peso": 40
            },
            "CAMPANA": {
                "ascii": [
                    "                              ",
                    "            [#FFFF00]██[/]                ",
                    "           [#FFFF00]████[/]               ",
                    "          [#FFFF00]█████[/]               ",
                    "         [#FFFF00]███████[/]              ",
                    "[#FFFF00]█████████████████████████[/]     ",
                    "[#FFFF00]█████████████████████████[/]     ",
                    "  [#FFFF00]████████████████████[/]        ",
                    "     [#FFFF00]███████████████[/]          ",
                    "     [#FFFF00]███████████████[/]          ",
                    "     [#FFFF00]███████████████[/]          ",
                    "     [#FFFF00]███████████████[/]          ",
                    "     [#FFFF00]█████     █████[/]          ",
                    "     [#FFFF00]██           ██[/]          ",
                    "                              "
                ],
                "emoji": "🔔",
                "valor": 20,
                "peso": 30
            },
            "DIAMANTE": {
                "ascii": [
                    "                              ",
                    "                              ",
                    "   [#28e1ff] ██████████████[/]            ",
                    "   [#28e1ff]████████████████[/]           ",
                    " [#28e1ff]████████████████████[/]         ",
                    "  [#28e1ff]██████████████████[/]          ",
                    "    [#28e1ff]██████████████[/]            ",
                    "      [#28e1ff]██████████[/]              ",
                    "       [#28e1ff]████████[/]               ",
                    "         [#28e1ff]████[/]                 ",
                    "                              ",
                    "                              ",
                    "                              ",
                    "                              ",
                    "                              "
                ],
                "emoji": "💎",
                "valor": 100,
                "peso": 20
            },
            "TREBOL": {
                "ascii": [
                    "                              ",
                    "       [#008000]████[/]                   ",
                    "    [#008000]███████████[/]               ",
                    "    [#008000]███████████[/]               ",
                    "     [#008000]██████████[/]               ",
                    "  [#008000]███████████████[/]             ",
                    "[#008000]█████████████████████[/]         ",
                    "[#008000]██████████████████████[/]        ",
                    "[#008000]████████████████████[/]          ",
                    " [#008000]███████ █████████[/]            ",
                    "  [#008000]████  ███ ███████[/]           ",
                    "       [#008000]███    ███[/]             ",
                    "       [#008000]██[/]                     ",
                    "                              ",
                    "                              "
                ],
                "emoji": "🍀",
                "valor": 50,
                "peso": 30
            },
            "DINERO": {
                "ascii": [
                    "                              ",
                    "   [#FFD700]█[#ff2626]███████████████[#FFD700]█[/][/][/]          ",
                    "   [#FFD700]█[#ff2626]███████████████[#FFD700]█[/][/][/]          ",
                    "  [#FFD700]█[#ff2626]███████████████[#FFD700]█[/][/][/]           ",
                    "           [#FFD700]█[#ff2626]█████[#FFD700]█[/][/][/]            ",
                    "          [#FFD700]█[#ff2626]█████[#FFD700]█[/][/][/]             ",
                    "         [#FFD700]█[#ff2626]██████[#FFD700]█[/][/][/]             ",
                    "        [#FFD700]█[#ff2626]██████[#FFD700]█[/][/][/]              ",
                    "        [#FFD700]█[#ff2626]█████[#FFD700]█[/][/][/]               ",
                    "       [#FFD700]█[#ff2626]█████[#FFD700]█[/][/][/]                ",
                    "      [#FFD700]█[#ff2626]██████[#FFD700]█[/][/][/]                ",
                    "     [#FFD700]█[#ff2626]██████[#FFD700]█[/][/][/]                 ",
                    "     [#FFD700]█[#ff2626]█████[#FFD700]█[/][/][/]                  ",
                    "                              ",
                    "                              "
                ],
                "emoji": "🤑",
                "valor": 200,
                "peso": 15
            },
            "TROFEO": {
                "ascii": [
                    "                              ",
                    "[#f8ff26]    ███████████████[/]           ",
                    "[#f8ff26]████████████████████████[/]      ",
                    "[#f8ff26]██  ███████████████  ███[/]      ",
                    "[#f8ff26]███  █████████████  ███[/]       ",
                    " [#f8ff26]███  ███████████  ███[/]        ",
                    "  [#f8ff26]███████████████████[/]         ",
                    "        [#f8ff26]███████[/]               ",
                    "         [#f8ff26]█████[/]                ",
                    "         [#f8ff26]█████[/]                ",
                    "        [#f8ff26]████████[/]              ",
                    "      [#f8ff26]███████████[/]             ",
                    "      [#f8ff26]███████████[/]             ",
                    "                              ",
                    "                              "
                ],
                "emoji": "🏆",
                "valor": 200,
                "peso": 10
            }
        }
        
        # Convertimos el diccionario a listas para facilitar su uso
        self.simbolos_lista = list(self.SIMBOLOS.values())
        self.pesos = [s["peso"] for s in self.simbolos_lista]

    def maquina_slots(self, r, credito, ultima_tirada):
        """Dibuja la máquina tragaperras con los carretes dados."""
        simbolo_alto = 15  # Altura fija para todos los símbolos
        margen = "     "   # Espacio entre símbolos
        
        # Marco superior fijo
        marco_superior = """
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                  💥  MÁQUINA TRAGAPERRAS DEL BAR  💥                                       ║
║════════════════════════════════════════════════════════════════════════════════════════════════════════════║
║                                                                                                            ║
║                                     🎰  GIRANDO LOS CARRETES... 🎰                                         ║
║                                                                                                            ║
║════════════════════════════════════════════════════════════════════════════════════════════════════════════║
║                                                                                                            ║"""
        
        # Construimos las líneas centrales con los símbolos
        lineas_centrales = []
        for i in range(simbolo_alto):
            linea = "║   "  # Margen izquierdo dentro del marco
            for col in range(3):
                # Accedemos a la línea i del símbolo en la posición central indice 1
                linea += r[col][1]["ascii"][i] + margen
            linea += "║" # Margen derecho
            lineas_centrales.append(linea)
        
        # Marco inferior con la información de premios
        marco_inferior = f"""
║════════════════════════════════════════════════════════════════════════════════════════════════════════════║
║                                             💰 PREMIOS 💰                                                  ║
║           3 x 🍒 = 10 créditos        3 x 🔔 = 20 créditos         3 x 💎 = 100 créditos                   ║
║           3 x 🍀 = 50 créditos        3 x 7 = 200 créditos         3 x 🏆 = 200 créditos                   ║
║════════════════════════════════════════════════════════════════════════════════════════════════════════════║
║ 💳 CRÉDITOS: {credito:<5}                                                  🎯 Último resultado: {ultima_tirada:<4}              ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                              🎲  [ PULSA ENTER PARA TIRAR DE NUEVO ]  🎲                                   ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
        
        return marco_superior + "\n" + "\n".join(lineas_centrales) + marco_inferior

    def animar_maquina(self, saldo_pasar, iteraciones=40, delay=0.01):
        """Anima los carretes dentro del marco ASCII."""
        ultima = None
        premio = 0
        
        # Bucle con las iteraciones para animar la maquina
        for _ in range(iteraciones):
            # Generamos carretes aleatorios basados en los pesos
            reels = [[random.choices(self.simbolos_lista, weights=self.pesos, k=1)[0] for _ in range(3)] for _ in range(3)]

            limpiar_pantalla()
            # Mostramos la maquina de slots 
            console.print(self.maquina_slots(reels, saldo_pasar, premio))

            # Guardamos la lista de la última iteración
            ultima = reels

            # Damos una pausa
            time.sleep(delay)
        
        # Muestra el resultado final fijo
        limpiar_pantalla()
        console.print(self.maquina_slots(ultima, saldo_pasar, premio))
        
        # Evaluamos los premios basados en los símbolos centrales
        simbolo1 = ultima[0][1]
        simbolo2 = ultima[1][1]
        simbolo3 = ultima[2][1]
        
        # Si los 3 son iguales damos más premio
        if simbolo1 == simbolo2 == simbolo3:
            premio = simbolo1["valor"]
            console.print(f"¡GANASTE {premio} CRÉDITOS!")
            
        # Comparamos que los 2 de la izquierda sean iguales
        elif simbolo1 == simbolo2:
            premio = simbolo1["valor"] // 2  # La mitad del valor
            console.print(f"¡GANASTE {premio} CRÉDITOS!")
            
        # Comparamos los 2 del lado derecho si son iguales
        elif simbolo2 == simbolo3:
            premio = simbolo2["valor"] // 2  # La mitad del valor
            console.print(f"¡GANASTE {premio} CRÉDITOS!")
        else:
            console.print("¡Inténtalo de nuevo!")
        
        return premio