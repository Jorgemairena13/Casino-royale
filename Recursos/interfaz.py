import os
import time
from Recursos.tragaperras import *

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

banner_alineado = Panel(Align.center(banner),  border_style="bright_blue", padding=(1, 4))


def menu_principal():
    limpiar_pantalla()
    console.print(banner_alineado)

    # Título con estilo
    titulo = Text("🎮 SELECCIONE UN JUEGO 🎮", style="bold magenta", justify="center")

    # Tabla sin bordes con opciones
    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "🎰 Tragamonedas")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "🎲 Ruleta")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "🃏 Black Jack")
    tabla.add_row('')
    tabla.add_row("[cyan]4.[/cyan]", "💰 Gestionar Saldo")
    tabla.add_row('')
    tabla.add_row("[cyan]5.[/cyan]", "ℹ️  Instrucciones")
    tabla.add_row("[cyan]6.[/cyan]", "📊 Estadísticas")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🚪 Salir")

    # Panel con alineación centrada
    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="bright_blue", padding=(1, 4))

    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

def menu_tragamonedas():
    limpiar_pantalla()

    titulo = Text("🎰 TRAGAMONEDAS 🎰", style="bold yellow", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💫 Jugar")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📜 Ver tabla de premios")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "🎯 Seleccionar apuesta")
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
    tabla.add_row("[cyan]2.[/cyan]", "📜 Ver tipos de apuestas")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "🎯 Seleccionar apuesta")
    tabla.add_row('')
    tabla.add_row("[cyan]4.[/cyan]", "📊 Ver estadísticas de números")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🔙 Volver al menú principal")

    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="red", padding=(1, 4))
    console.print(Align.center(panel_menu))
    return console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))


def menu_blackjack():
    limpiar_pantalla()

    titulo = Text("🃏 BLACK JACK 🃏", style="bold blue", justify="center")

    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "💫 Nueva partida")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📜 Ver reglas")
    tabla.add_row('')
    tabla.add_row("[cyan]3.[/cyan]", "🎯 Seleccionar apuesta")
    tabla.add_row('')
    tabla.add_row("[cyan]4.[/cyan]", "📊 Ver estadísticas")
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





