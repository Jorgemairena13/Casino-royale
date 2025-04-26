import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    print("""
    🎰 🎲 🃏 CASINO ROYALE 🎰 🎲 🃏
    ================================
     ____    _    ____ ___ _   _  ___  
    / ___|  / \  / ___|_ _| \ | |/ _ \ 
    | |     / _ \| |    | ||  \| | | | |
    | |___ / ___ \ |___ | || |\  | |_| |
    \____/_/   \_\____|___|_| \_|\___/ 
     ____   _____   ___    _    _     _____ 
    |  _ \ / _ \ \ / / |  | |  / \   | ____|
    | |_) | | | \ V /| |  | | / _ \  |  _|  
    |  _ <| |_| || | | |__| |/ ___ \ | |___ 
    |_| \_\\___/ |_| |_____/_/   \_\|_____|
    ================================
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
        time.sleep(0.5)
        print(".", end='', flush=True)
    print("\n")

