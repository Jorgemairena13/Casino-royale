from Recursos.interfaz import *
from Recursos.tragaperras import *
from Recursos.base_datos import *
from Recursos.ruleta import *
from Recursos.black_jack import *

console = Console()
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = """
                          🎰 🎲 🃏 CASINO ROYALE 🎰 🎲 🃏
    
                    ██████  █████  ███████ ██ ███    ██  ██████  
                   ██      ██   ██ ██      ██ ████   ██ ██    ██ 
                   ██      ███████ ███████ ██ ██ ██  ██ ██    ██ 
                   ██      ██   ██      ██ ██ ██  ██ ██ ██    ██ 
                    ██████ ██   ██ ███████ ██ ██   ████  ██████  
                                                                             

                   ██████   ██████  ██    ██  █████  ██      ███████ 
                   ██   ██ ██    ██  ██  ██  ██   ██ ██      ██      
                   ██████  ██    ██   ████   ███████ ██      █████   
                   ██   ██ ██    ██    ██    ██   ██ ██      ██      
                   ██   ██  ██████     ██    ██   ██ ███████ ███████ 
                                                  
                                                  

    """

banner_alineado = Panel(Align.center(banner), border_style="bright_blue", padding=(1, 4))

def menu_principal():
    limpiar_pantalla()
    console.print(banner_alineado)

    titulo = Text("🎮 SELECCIONE UN JUEGO 🎮", style="bold magenta", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "🎰 Tragamonedas")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "🎲 Ruleta")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "🃏 Black Jack")
    tabla.add_row('')
    tabla.add_row("[cyan]4.[/cyan]", "💰 Gestionar Saldo")
    tabla.add_row('')
    tabla.add_row("[cyan]5.[/cyan]", "📋  Instrucciones")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🚪 Salir")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="bright_blue", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

def menu_tragamonedas():
    limpiar_pantalla()

    titulo = Text("🎰 TRAGAMONEDAS 🎰", style="bold yellow", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💫 Jugar")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📜 Ver historial")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🔙 Volver al menú principal")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="yellow", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

def menu_ruleta():
    limpiar_pantalla()

    titulo = Text("🎲 RULETA 🎲", style="bold red", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💫 Jugar")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📜 Ver historial")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "📊 Ver estadísticas de números")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🔙 Volver al menú principal")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="red", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

def menu_blackjack():
    limpiar_pantalla()

    titulo = Text("🃏 BLACK JACK 🃏", style="bold blue", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💫 Jugar")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🔙 Volver al menú principal")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="bright_blue", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

def menu_gestionar_saldo():
    limpiar_pantalla()

    titulo = Text("💰 GESTIÓN DE SALDO 💰", style="bold green", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💵 Depositar")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📋 Ver historial de transacciones")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🔙 Volver al menú principal")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="green", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))


def mostrar_reglas():
    console.print('''================ REGLAS DEL CASINO ROYALE ================

🃏 BLACKJACK:
-----------------------------------------
1. Objetivo:  
   - Alcanzar 21 puntos o superar la mano del crupier
   - ¡Cuidado con pasarte de 21!

2. Valor de cartas:
   - Numeros: Valor nominal (2-10)
   - J, Q, K: 10 puntos
   - As: 11 u 1 punto (autoajustable)

3. Flujo del juego:
   a) Apuesta inicial
   b) Reparto de 2 cartas visibles (jugador)
   c) Crupier muestra 1 carta
   d) Opciones:
      ✅ [P] Pedir carta
      ✋ [M] Plantarse
   e) Crupier pide hasta 17 puntos

4. Premios:
   ▶ Victoria normal: x2 apuesta
   ▶ Blackjack Natural (21 inicial): x3 apuesta
   ▶ Empate: Recuperas apuesta
   ▶ Derrota: Pierdes apuesta

🎡 RULETA:
-----------------------------------------
TIPOS DE APUESTAS:
+----------------------+-------------+-------+
|       Apuesta        |   Ejemplo   | Pago  |
+----------------------+-------------+-------+
| Número simple (1)    | 17          | 36:1  |
| Color (Rojo/Negro)   | Rojo        | 2:1   |
| Par/Impar            | Par         | 2:1   |
| Docenas (1-12, etc)  | 1ra docena  | 2:1   |
| Filas (1-3)          | Fila 2      | 2:1   |
| Alto/Bajo (1-18/19-36)| Bajo       | 2:1   |
+----------------------+-------------+-------+

REGLAS ESPECIALES:
- Si sale 0 y no apostaste al 0: Pierdes
- Combina múltiples apuestas por ronda
- Usa TAB para autocompletar opciones

🎰 TRAGAPERRAS:
-----------------------------------------
MECÁNICA:
- Apuesta fija: 5€ por tirada
- 3 rodillos con símbolos:
  7 | BAR | Campana | Cereza | Diamante

SISTEMA DE PREMIOS:
♦♦♦ Diamantes: 🤑 x50
☰☰☰ BAR: 💰 x20
🔔🔔🔔 Campanas: x10
🍒🍒🍒 Cerezas: x10
🍒🍒- 2 Cerezas: x2

💰 GESTIÓN GENERAL:
-----------------------------------------
1. SALDO:
   - Consulta en cualquier momento
   - Recarga mínima: 1€
   - Historial detallado

2. CONTROLES:
   - Navegación con números
   - Enter para confirmar
   - Ctrl+C para salir

3. CONSEJOS:
   ▶ Blackjack: Crupier DEBE pedir hasta 17
   ▶ Ruleta: Apuestas múltiples permitidas
   ▶ Tragaperras: ¡Persigue los diamantes!

📜 HISTORIAL:
-----------------------------------------
- Revisa todas tus transacciones
- Estadísticas por juego
- Registro temporal completo
''')
    prompt()
