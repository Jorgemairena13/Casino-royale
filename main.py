from Recursos.interfaz import *
from Recursos.juegos import *
from Recursos.base_datos import *


def main():
    
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            while True:
                opcion_tragamonedas = menu_tragamonedas()
                if opcion_tragamonedas == "0":
                    break
                mostrar_mensaje_carga("Cargando tragamonedas")
                
        elif opcion == "2":
            while True:
                opcion_ruleta = menu_ruleta()
                if opcion_ruleta == "0":
                    break
                mostrar_mensaje_carga("Preparando la ruleta")
                
        elif opcion == "3":
            while True:
                opcion_blackjack = menu_blackjack()
                if opcion_blackjack == "0":
                    break
                mostrar_mensaje_carga("Preparando la mesa de Black Jack")
                
        elif opcion == "4":
            while True:
                opcion_saldo = menu_gestionar_saldo()
                if opcion_saldo == "0":
                    break
                mostrar_mensaje_carga("Accediendo a su cuenta")
                
        elif opcion == "5":
            limpiar_pantalla()
            print("""
            📖 INSTRUCCIONES 📖
            ==================
            🎰 TRAGAMONEDAS:
            - Seleccione su apuesta
            - Pulse para girar
            - ¡Consiga 3 símbolos iguales para ganar!

            🎲 RULETA:
            - Elija el tipo de apuesta
            - Seleccione sus números
            - ¡Espere a que la bola se detenga!

            🃏 BLACK JACK:
            - Apueste antes de recibir cartas
            - Intente llegar a 21 sin pasarse
            - Gane al crupier para duplicar su apuesta
            """)
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "6":
            limpiar_pantalla()
            print("""
            📊 ESTADÍSTICAS 📊
            =================
            🏆 Mayores Ganancias:
            - Tragamonedas: $0
            - Ruleta: $0
            - Black Jack: $0

            📈 Racha de victorias:
            - Tragamonedas: 0
            - Ruleta: 0
            - Black Jack: 0
            """)
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "0":
            limpiar_pantalla()
            print("""
            🎰 ¡Gracias por jugar en CASINO ROYALE! 🎰
            ========================================
                    ¡Vuelva pronto! 👋
            """)
            break

if __name__ == "__main__":
    main()
