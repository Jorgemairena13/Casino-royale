import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    print("""
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
                                                  
                                                  

    """)

def mostrar_saldo(saldo):
    print(f"\n💰 Saldo actual: ${saldo:.2f} 💰\n")

def menu_principal():
    limpiar_pantalla()
    mostrar_banner()
    print("""
    🎮 SELECCIONE UN JUEGO 🎮
    ========================
    1. 🎰 Tragamonedas
    2. 🎲 Ruleta
    3. 🃏 Black Jack
    4. 💰 Gestionar Saldo
    5. ℹ️  Instrucciones
    6. 📊 Estadísticas
    0. 🚪 Salir
    """)
    return input("Ingrese su elección: ")

def menu_tragamonedas():
    limpiar_pantalla()
    print("""
    🎰 TRAGAMONEDAS 🎰
    ==================
    1. 💫 Jugar
    2. 📜 Ver tabla de premios
    3. 🎯 Seleccionar apuesta
    0. 🔙 Volver al menú principal
    """)
    return input("Ingrese su elección: ")

def menu_ruleta():
    limpiar_pantalla()
    print("""
    🎲 RULETA 🎲
    ============
    1. 💫 Jugar
    2. 📜 Ver tipos de apuestas
    3. 🎯 Seleccionar apuesta
    4. 📊 Ver estadísticas de números
    0. 🔙 Volver al menú principal
    """)
    return input("Ingrese su elección: ")

def menu_blackjack():
    limpiar_pantalla()
    print("""
    🃏 BLACK JACK 🃏
    ===============
    1. 💫 Nueva partida
    2. 📜 Ver reglas
    3. 🎯 Seleccionar apuesta
    4. 📊 Ver estadísticas
    0. 🔙 Volver al menú principal
    """)
    return input("Ingrese su elección: ")

def menu_gestionar_saldo():
    limpiar_pantalla()
    print("""
    💰 GESTIÓN DE SALDO 💰
    =====================
    1. 💵 Depositar
    2. 💸 Retirar
    3. 📋 Ver historial de transacciones
    0. 🔙 Volver al menú principal
    """)
    return input("Ingrese su elección: ")

def mostrar_mensaje_carga(mensaje):
    print(f"\n{mensaje}", end='')
    for _ in range(3):
        time.sleep(0.01)
        print(".", end='', flush=True)
    print("\n")

import random
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

SIMBOLOS = ['🍒','🔔','💎','🍀','🤑','🏆']
APARICIONES = [40,25,15,25,10,5]

def animar_bajada(iteraciones=20, delay=1):
    reels = [[random.choices(SIMBOLOS, weights=APARICIONES)[0] for _ in range(3)] for _ in range(3)]

    for _ in range(iteraciones):
        limpiar_pantalla()

        # Simula que cada rodillo baja: "rotación"
        for i in range(3):
            reels[i] = [random.choices(SIMBOLOS, weights=APARICIONES)[0]] + reels[i][:2]

        # Imprimir línea por línea
        print("╔════════════════════════════╗")
        print("║     🎰  MÁQUINA SLOT  🎰     ║")
        print("╠════════════════════════════╣")
        for fila in range(3):
            print("║  ", end="")
            for col in range(3):
                print(f" {reels[col][fila]} ", end=" ")
            print(" ║")
        print("╚════════════════════════════╝")

        time.sleep(delay)

animar_bajada()
