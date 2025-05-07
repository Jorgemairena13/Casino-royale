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
                
                if opcion_ruleta == "0":
                    break
                elif opcion_ruleta == '1':
                    ruleta = Ruleta()

                    while True:
                        try:
                            dinero = int(prompt('Cuanto dinero quieres apostar?', style=style))
                            if dinero > saldo:
                                print("No tienes suficiente saldo.")
                            else:
                                break
                        except :
                            print("Introduce un número válido.")

                    # Lista que pasaremos a la funcion con la apuesta del usuario
                    apuestas_usuario = []

                    # Lista autocompletado
                    colores = ['Negro','Rojo']
                    colores_auto = FuzzyWordCompleter(colores)
                    # Pedimos si quiere apostar a color
                    color = prompt('Quieres apostar a algun color?\n',style=style,completer=colores_auto)
                    # Comprobamos que haya apostado a color
                    if color in colores:
                        apuestas_usuario.append(color)
                    else:
                        apuestas_usuario.append("0")

                    # Apuesta a par o impar
                    par_impar_lista = ['Par','Impar']
                    par_impar_auto = FuzzyWordCompleter(par_impar_lista)
                    par_impar = prompt('Quieres apostar a par o impar?\n',style=style,completer = par_impar_auto).capitalize()
                    if par_impar in par_impar_lista:
                        apuestas_usuario.append(par_impar)
                    else:
                        apuestas_usuario.append("0")
                    

                    # Apuesta a las docenas
                    docenas_lista = ['1 docena','2 docena','3 docena']
                    docenas_auto = FuzzyWordCompleter(docenas_lista)
                    docenas = prompt('Quieres apostar a la docenas?\n',style=style,completer=docenas_auto)
                    if docenas in docenas_lista:
                        apuestas_usuario.append(docenas)
                    else:
                        apuestas_usuario.append("0")
                    
                    # Lista para el auto completado y para comprobar
                    alta_baja_lista = ['Alta','Baja']
                    # Auto completado
                    alta_baja_auto = FuzzyWordCompleter(alta_baja_lista)

                    # Le pedimos al ususario la apuesa
                    alta_baja = prompt('Quieres apostar al baja o la alta?\n',style=style,completer=alta_baja_auto)
                    # Comprobamos que este en la lista
                    if alta_baja in alta_baja_lista:
                        # Añadimos a la lista
                        apuestas_usuario.append(alta_baja)
                    else:
                        apuestas_usuario.append("0")

                    # Apuestas a las filas del tablero
                    completar_fila =['Fila 1','Fila 2','Fila 3']
                    apuesta_fila = FuzzyWordCompleter(completar_fila)
                    fila = prompt('Quieres aposar a alguna fila? Numero del 1 al 3 segun la fila?\n',style=style,completer=apuesta_fila).capitalize()
                    if fila in completar_fila:
                        apuestas_usuario.append(fila)
                    else:
                        apuestas_usuario.append("0")

                    # Apuestas a los nuemeros sueltos
                    numeros_sueltos = prompt('Quieres apostar a numeros sueltos??[S/N]\n',style=style).upper()

                    lista_numeros_sueltos = []
                    if numeros_sueltos == 'S':
                        numeros = prompt('Escribe los numeros que quieres apostar separados por espacios: ')
                        # Pasamos los numeros a enteros para comprobar despues
                        for numero in numeros.split():
                            lista_numeros_sueltos.append(int(numero))
                    
                        
                    # Le mostramos las apuestas que a hecho   
                    for apuesta in apuestas_usuario:
                        print(apuesta)
                    print(" ") # Espacio

                    # Le pedimos confimacion
                    validar_apuesta = prompt('Estan  correctas la apuestas?[S/N]').upper()
                    if validar_apuesta == "S":
                        resultado = ruleta.buscar_apuesta(dinero,apuestas_usuario,lista_numeros_sueltos)
                         # Le pasamos el dinero y las apuestas del usuario
                        console.print(Panel(f'Has ganado {resultado} €',width=30))
                        saldo+=resultado
                        gestion_db.actualizar_saldo('jorge@',saldo)
                        prompt()
                    else:
                        break
                    
                   
        elif opcion == "3":
            while True:
                opcion_blackjack = menu_blackjack()
                if opcion_blackjack == "0":
                    break
                
                
        elif opcion == "4":
            while True:
                opcion_saldo = menu_gestionar_saldo()
                if opcion_saldo == "0":
                    break
                
                
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
