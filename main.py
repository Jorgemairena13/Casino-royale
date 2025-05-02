from Recursos.interfaz import *
from Recursos.tragaperras import *
from Recursos.base_datos import *
from Recursos.ruleta import *


import sqlite3
from os import system
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

style = Style.from_dict({
    'prompt': 'bold fg:#ffb027',
    '': 'fg:#ffffff'
})

gestion_db = Base_de_datos()

gestion_db.crear_tabla()


def main():
    #Validamos el inicio de sesion
    
    # while True:

    #     opcion = prompt('1. Si estas registrado\n2. Para registrarte\n',style=style)
    #     if opcion =='1':

    #             # Pedimos el email
    #             email = prompt("Introduce tu correo de inicio de sesion: ",style=style)

    #             # Pedimos la contraseña
    #             contrasena = prompt('Introduce tu contraseña: ',style=style)

    #             # Validamos la sesion
    #             validar_entrada = gestion_db.iniciar_sesion(email,contrasena)

    #             if validar_entrada:
    #                 console.print(Panel(f'[bold #24fc69]Has iniciado sesion correctamente[/]',border_style='#24fc69',expand=False,width=30))
    #                 prompt("Pulsa enter para continuar")
    #                 break
    #             else:
                    
    #                 continue
    #     elif opcion == '2':
    #             # Pedimos los datos de registro
    #             nombre = prompt('Introduce el tu nombre: ',style=style)
    #             correo = prompt('Correo de inicio de sesion: ',style=style)
    #             while True:
    #                         try:
    #                             fecha = prompt('Introduce la fecha de nacimiento [dd/mm/aa]: ', style=style)
    #                             # Combrobamos que este vacia por si no quiere editar los datos
    #                             datetime.strptime(fecha, '%d/%m/%Y')
    #                             break
    #                         except:
    #                             console.print("[bold red]Fecha inválida[/]")
    #                             continue
    #             contrase = prompt('Intreduce tu contraseña: ',style=style)
    #             saldo = float(prompt('Saldo para iniciar la cuenta: ',style=style))

    #             if gestion_db.agregar_usuario(nombre,saldo,correo,fecha,contrase):
    #                 break
                    
    #             else:
    #                 continue
                
    
    while True:
        saldo = gestion_db.sacar_saldo('jorge@')
        opcion = menu_principal()
        
        if opcion == "1":
            while True:

                opcion_tragamonedas = menu_tragamonedas()
                if opcion_tragamonedas == "0":
                    break
                elif opcion == "1":
                    mostrar_mensaje_carga("Cargando tragamonedas")
                    salida = ''
                    while salida == '':
                        saldo -= 5
                        slots = MaquinaTragaperras()
                        premio = slots
                        premio = slots.animar_maquina(saldo)
                        saldo += premio
                        print(premio)
                        print(f'Tu saldo es de {saldo}')
                        salida = prompt('Enter para tirar otra otra cosa para salir!!')
                    gestion_db.actualizar_saldo('jorge@',saldo)
                     
                
        elif opcion == "2":
            while True:
                opcion_ruleta = menu_ruleta()
                mostrar_mensaje_carga("Preparando la ruleta")
                if opcion_ruleta == "0":
                    break
                elif opcion_ruleta == '1':
                    ruleta = Ruleta()
                    iteraciones = random.randint(100, 300)
                    
                    resultado = ruleta.animar_ruleta(39)
                    print(resultado)
                    prompt()

                
                
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
            prompt("\nPresione Enter para volver al menú principal...")
            
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
            prompt("\nPresione Enter para volver al menú principal...")
            
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
