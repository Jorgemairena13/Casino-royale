from Recursos.interfaz import *
from Recursos.tragaperras import *
from Recursos.base_datos import *
from Recursos.ruleta import *
from Recursos.black_jack import *



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


def validar_saldo(saldo):
    while True:
        try:
            dinero_apostar = int(prompt('Cuanto dinero quieres apostar?', style=style))
            if dinero_apostar > saldo:
                console.print(Panel("[#fd0000 ]No tienes suficiente saldo.[/]",border_style="#fd0000 "))
            else:
                return dinero_apostar
                
        except :
            print("Introduce un número válido.")

def validar_campo_vacio(campo_validar):
    '''
    Valida que el campo que se le pasa no este vacio
    '''
    if str(campo_validar).strip() == '':
        console.print(Panel('[bold #C70039]No se pueden introducir datos vacios!![/]',border_style='bold #C70039',width = 30))
        return False
    else:
        return True
    
def validar_solo_letras(campo_validar):
    '''
    Valida que el campo que se le pase solo sea numerico
    '''
    campo_validar = campo_validar.replace(" ", "")
    if campo_validar.isalpha():
        return True
    else:
        console.print(Panel('[bold #C70039]Solo se pueden introducir letras!![/]',border_style='bold #C70039',width = 30))
        return False


console = Console()

style = Style.from_dict({
    'prompt': 'bold fg:#ffb027',
    '': 'fg:#ffffff'
})

gestion_db = Base_de_datos()

gestion_db.crear_tabla_usuarios()
gestion_db.crear_tabla_historial()
gestion_db.crear_tabla_tragaperras()
gestion_db.crear_tabla_ruleta()


def main():
    limpiar_pantalla()
    console.print(banner_alineado)

    # Título con estilo
    titulo = Text("🎮 BIENVENIDO A CASINO ROYALE 🎮", style="bold magenta", justify="center")

    # Tabla con opciones
    tabla = Table.grid(padding=(0, 2))
    tabla.add_row("[cyan]1.[/cyan]", "🔑 Iniciar Sesión")
    tabla.add_row('')
    tabla.add_row("[cyan]2.[/cyan]", "📝 Registrarse")
    tabla.add_row('')
    tabla.add_row("[cyan]0.[/cyan]", "🚪 Salir")

    # Panel con alineación centrada
    panel_menu = Panel(Align.center(tabla), title=titulo, border_style="bright_blue", padding=(1, 4))
    console.print(Align.center(panel_menu))

    opcion = console.input(Align.center("[bold green]Ingrese su elección: [/bold green]"))

    while True:
        if opcion == '1':
            limpiar_pantalla()
            console.print(banner_alineado)
            console.print(Panel("[bold cyan]INICIAR SESIÓN[/]", border_style="cyan", width=30))
            correo = prompt("Correo: ", style=style)
            contrasena = prompt("Contraseña: ", style=style)
            
            validar_entrada = gestion_db.iniciar_sesion(correo, contrasena)
            
            if validar_entrada:
                console.print(Panel(f'[bold #24fc69]¡Bienvenido![/]', 
                                border_style='#24fc69', 
                                expand=False, 
                                width=30))
                prompt("Pulsa enter para continuar")
                break
            else:
                continue
            prompt()  
        elif opcion == '2':
            limpiar_pantalla()
            console.print(banner_alineado)
            console.print(Panel("[bold cyan]REGISTRO DE USUARIO[/]", border_style="cyan", width=30))
            
            while True:
                        nombre = prompt("Nombre: ", style=style)
                        if validar_campo_vacio(nombre) and validar_solo_letras(nombre):
                            break
                        else:
                            continue
            
            while True:
                        correo = prompt("Correo: ", style=style)
                        if validar_campo_vacio(correo) and validar_solo_letras(correo):
                            break
                        else:
                            continue
            
            while True:
                try:
                    fecha = prompt("Fecha de nacimiento [dd/mm/aaaa]: ", style=style)
                    datetime.strptime(fecha, '%d/%m/%Y')
                    break
                except:
                    console.print("[bold red]Fecha inválida[/]")
                    continue
            
            

            while True:
                        contrasena = prompt("Contraseña: ", style=style)
                        if validar_campo_vacio(contrasena) and validar_solo_letras(contrasena):
                            break
                        else:
                            continue

            
            while True:
                        try:
                            saldo = prompt("Saldo inicial: ", style=style)
                            break
                                
                        except:
                            console.print(Panel('[bold #C70039]No se puede introducir otra cosa que no sea un numero!![/]',border_style='bold #C70039',width = 30))
                            continue
            
            if gestion_db.agregar_usuario(nombre, saldo, correo, fecha, contrasena):
                console.print(Panel(f'[bold #24fc69]¡Registro exitoso![/]', 
                                border_style='#24fc69', 
                                expand=False, 
                                width=30))
                prompt("Pulsa enter para continuar")
                break
            else:
                console.print(Panel("[bold red]El correo ya está registrado[/]", 
                                border_style="red", 
                                width=30))
                prompt("Pulsa enter para continuar")
                continue
                
        elif opcion == '0':
            console.print(Panel("[bold yellow]¡Gracias por jugar![/]", 
                            border_style="yellow", 
                            width=30))
        
    while True:
        
        saldo = gestion_db.sacar_saldo(correo)
        opcion = menu_principal()
        
        if opcion == "1":
            while True:

                opcion_tragamonedas = menu_tragamonedas()
                if opcion_tragamonedas == "0":
                    break
                elif opcion_tragamonedas == "1":
                    
                    salida = ''
                    while salida == '':
                        saldo -= 5
                        slots = MaquinaTragaperras()
                        premio = slots
                        premio = slots.animar_maquina(saldo)
                        gestion_db.actualizar_partidas_tragaperras(correo,premio)
                        saldo += premio
                        
                        print(premio)
                        print(f'Tu saldo es de {saldo}')
                        salida = prompt('Enter para tirar otra tecla para salir!!',style=style)
                    gestion_db.actualizar_saldo(correo,saldo)

                elif opcion_tragamonedas == '2':
                    id=gestion_db.sacar_id(correo)
                    gestion_db.mostrar_partidas_tragaperras(id)
                    prompt()
                     
                
        elif opcion == "2":
            while True:
                opcion_ruleta = menu_ruleta()
                
                if opcion_ruleta == "0":
                    break
                elif opcion_ruleta == '1':
                    ruleta = Ruleta()
                    
                    dinero_apostado = validar_saldo(saldo)

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
                        numeros = prompt('Escribe los numeros que quieres apostar separados por espacios: ',style=style)
                        # Pasamos los numeros a enteros para comprobar despues
                        for numero in numeros.split():
                            if numero.isdigit():
                                lista_numeros_sueltos.append(int(numero))
                            else:
                                console.print(f"[#ff0000 ][!] '{numero}' no es un número válido.[/]")
                    for numero in lista_numeros_sueltos:
                        console.print(numero,end="")
                        
                    # Le mostramos las apuestas que a hecho   
                    for apuesta in apuestas_usuario:
                        console.print(Panel(apuesta,border_style='#9a27ff '),width=30)
                    print(" ") # Espacio
                    console.print(Panel('Numeros apostados',width=30,border_style='#9a27ff '))
                    for numero in lista_numeros_sueltos:
                        console.print(numero,end="")
                    print(" ") # Espacio

                    # Le pedimos confimacion
                    validar_apuesta = prompt('Estan correctas la apuestas?[S/N]: ',style=style).upper()
                    if validar_apuesta == "S":
                        # Numeros ramdom para las vueltas de la ruleta
                        iteraciones = random.randint(50, 150)

                        # Animamos la ruleta y guardamos el resultado
                        numero_ganador = ruleta.animar_ruleta(iteraciones)
                        premio = ruleta.buscar_apuesta(dinero_apostado,apuestas_usuario,lista_numeros_sueltos,numero_ganador)
                         # Le pasamos el dinero y las apuestas del usuario
                        console.print(Panel(f'[#6fff90]Has ganado {premio} € y has apostado {dinero_apostado}€ y el numero ganador es {numero_ganador}[/]',width=30,border_style='#6fff90'))
                        id = gestion_db.sacar_id(correo)
                        gestion_db.actualizar_partidas_ruleta(id,dinero_apostado,numero_ganador,premio)
                        saldo+=premio
                        gestion_db.actualizar_saldo(correo,saldo)
                        prompt()
                    else:
                        break
                elif opcion_ruleta == '2':
                    id = gestion_db.sacar_id(correo)
                    gestion_db.mostrar_datos_ruleta(id)
                    prompt()

                elif opcion_ruleta == '3':
                    gestion_db.mostrar_estadisticas_ruleta()
                    prompt()
                    prompt()    
                   
        elif opcion == "3":
            while True:
                opcion_blackjack = menu_blackjack()
                if opcion_blackjack == "0":
                    break
                elif opcion_blackjack == "1":
                    # Le pedimos el dinero de la apuesta que quiere hacer
                    console.print(Panel(f'Tu saldo es de {saldo}',width=30))
                    
                    apuesta_black= validar_saldo(saldo)

                    # Creamos un objeto juego
                    juego = Black_jack(apuesta_black)
                    limpiar_pantalla()

                    # Le mostramos el saldo que tiene
                    console.print(Panel(f'Tu saldo es de {saldo}'))
                    # Iniciamos el juego y sacamos el saldo que vamos a delver
                    ganado_black = juego.iniciar_juego()
                    console.print(Panel(f'Has ganado {ganado_black}'))
                    saldo += ganado_black
                    gestion_db.actualizar_saldo(correo,saldo)
                    prompt()

                    # Le preguntamos si quiere jugar otra vez
                    jugar_otra_vez = prompt("\n¿Quieres jugar otra partida? (s/n): ",style=style).lower()
                    while jugar_otra_vez == 's':

                        # Le mostramos el saldo disponible
                        console.print(Panel(f'Tu saldo es de {saldo}',width=30))
                        # Le pedimos la apuesta
                        apuesta_black= validar_saldo(saldo)

                        # Hacemos lo mismo que cuando juega por primera vez
                        juego = Black_jack(apuesta_black)
                        ganado_black = juego.iniciar_juego()
                        console.print(Panel(f'Has ganado {ganado_black}'))
                        saldo += ganado_black
                        gestion_db.actualizar_saldo(correo,saldo)
                        jugar_otra_vez = prompt("\n¿Quieres jugar otra partida? (s/n): ",style=style).lower()
                        
                        
                    console.print(Panel("[#fdf500]¡Gracias por jugar! ¡Hasta la próxima![#fdf500]",border_style="#fdf500"))
                    limpiar_pantalla()
                    
                
                
        elif opcion == "4":
            while True:
                opcion_saldo = menu_gestionar_saldo()
                if opcion_saldo == "0":
                    break
                elif opcion_saldo == "1":
                    saldo_actualizar = int(prompt("Cuanto saldo quieres añadir?\n",style=style))
                    saldo += saldo_actualizar
                    gestion_db.actualizar_saldo(correo,saldo)
                    gestion_db.actualizar_historial_transacciones(saldo_actualizar,correo)
                    console.print(Panel(f"[#fdf500]Tu saldo es de {saldo}[/]\n",border_style="#fdf500 ",width=40))
                    prompt("\nPresione Enter para volver al menú principal...",style=style)

                elif opcion_saldo == '2':
                    resultados = gestion_db.mostrar_historial(correo)
                    for dato in resultados:
                        print(dato[0],dato[1],dato[2])
                    prompt()
        elif opcion == '5':
            mostrar_reglas()

        elif opcion == "0":
            limpiar_pantalla()
            console.print("""[#2848ff]
            🎰 ¡Gracias por jugar en CASINO ROYALE! 🎰
            ========================================
                    ¡Vuelva pronto![/] 👋
            """)
            break

if __name__ == "__main__":
    main()
