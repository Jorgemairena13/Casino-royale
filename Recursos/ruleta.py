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
import os

import random
console = Console()

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Ruleta():
  def __init__(self):
    self.n = [
        00,  32, 15, 19, 4,  21, 2,  25, 17, 34, 6,  27, 13, 36, 11, 30, 8,  23,
        10, 5,  24, 16, 33, 1,  20, 14, 31, 9,  22, 18, 29, 7,  28, 12, 35, 3,  26
    ]

  def mostrar_ruleta(self,n):  
    '''Muestra la ruleta y el tablero de la ruleta'''
    # Tablero para que el usuario vea a que se puede apostar
    tablero_ruleta = '''
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                              RULETA CASINO                              ┃
    ┣━━━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┫
    ┃       ┃  3  ┃  6  ┃  9  ┃ 12  ┃ 15  ┃ 18  ┃ 21  ┃ 24  ┃ 27  ┃ 30  ┃ 33  ┃
    ┃       ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃
    ┣━━━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
    ┃    0  ┃  2  ┃  5  ┃  8  ┃ 11  ┃ 14  ┃ 17  ┃ 20  ┃ 23  ┃ 26  ┃ 29  ┃ 32  ┃
    ┃   🟢  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃
    ┣━━━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
    ┃       ┃  1  ┃  4  ┃  7  ┃ 10  ┃ 13  ┃ 16  ┃ 19  ┃ 22  ┃ 25  ┃ 28  ┃ 31  ┃
    ┃       ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃
    ┣━━━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┫
    ┃  1-12 PRIMERA DOCENA  ┃  13-24 SEGUNDA DOCENA  ┃  25-36 TERCERA DOCENA  ┃
    ┣━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃    1-18   ┃    PAR    ┃    🔴    ┃   IMPAR   ┃   19-36   ┃     ⚫       ┃
    ┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━━━━┛
    '''
    # Ruleta con todo los indice metidos
    ruleta2 = f"""[bold #6fff90]
                  ▓▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▓               
              ▓▓▓▓█▓▓▓████[white on green]0{n[0]}[/]▓▓▓████▓▓▓▓▓           
            ▒▓▓████▓▓[white on black]{n[36]}[/]▓███▓▓[white on red]{n[1]}[/]▓████▓▓▓███▓      
          ▒▓▓█▓▓▓▓█[white on red]0{n[35]}[/]██▓▓▓███▓▓▓██[white on black]{n[2]}[/]█▓▓▓████▓▓▓▒   
        ▒▓████[white on black]{n[34]}[/]▓▓▓▓███▓▓▓██▓▓▓██▓▓▓█[white on red]{n[3]}[/]██▓▓▓▓▓█▓   
      ▓▒▓▓▓[white on red]{n[33]}[/]█████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓[white on black]0{n[4]}[/]▓▓█████▓
      ▓▒▓[white on black]{n[32]}[/]▓▓█████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓█[white on red]{n[5]}[/]████▓
      ▓▓█[white on red]0{n[31]}[/]█▓▓▓▓▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█████▓▓▓▓▓  
    ▒▓█████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███▓▓▓▓[white on black]0{n[6]}[/]▓▓▓▒ 
    ▒▓▓▓[white on red]{n[30]}[/]█████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█████▒ 
    ▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████[white on black]{n[7]}[/]███▓▒
    ▓████[white on black]{n[29]}[/]▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒
    ▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓[white on red]{n[8]}[/]▓███▓
    ▓████[white on red]{n[28]}[/]████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓███▓
    ▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓[white on red]{n[9]}[/]▓███▓
    ▓▓███[white on red]0{n[27]}[/]▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
    ▓▓███▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓[white on black]0{n[10]}[/]▓▓▓▓▓
    ▓▓███[white on black]{n[26]}[/]▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
    ▓████▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▓[white on black]{n[11]}[/]▓▓▓▓▒
    ▒▓██▓[white on red]{n[25]}[/]▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓███████▓▒
    ▒▓▓▓▓▓████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓[white on black]{n[12]}[/]████▒ 
    ▒▒████[white on red]{n[24]}[/]███▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████▓▓▓▓▓▒▓ 
      ▒▓███▓▓▓▓▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓███[white on black]{n[13]}[/]███▓▓▒  
      ▓▓▓▓▓▓[white on black]0{n[23]}[/]▓████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓▓▓███▓▒   
        ▒▓▓███▓▓▓▓███▓▓▓██▓▓███▓▓▓██▓█▓▓[white on red]{n[14]}[/]▓▓▓▒     
          ▒▓▓██[white on black]{n[22]}[/]▓▓▓▓███▓▓▓███▓▓▓███▓▓▓████▓▓▒▒      
          ▒▓▓██▓▓▓[white on red]{n[21]}[/]▓███▓▓▓███▓▓▓███▓▓▓[white on black]{n[15]}[/]████▓▓   
            ▒▓▓▓▓███[white on black]{n[20]}[/]▓▓▓▓███▓▓▓███[white on red]0{n[16]}[/]█▓▓▓██▓▒         
              ▓▒▓▓██▓▓▓[white on black]0{n[19]}[/]▓█[white on red]{n[18]}[/]██▓[white on black]{n[17]}[/]▓▓▓███▓▓          
                  ▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒   [/]            
    """
    return ruleta2 + tablero_ruleta
    


  def animar_ruleta(self,iteraciones,delay = 0.1):
    # Hacemos una copia para no alterar la lista original
    n = self.n.copy()

    # Bola que se vera en la ruleta
    bola = '[on #ff6fde ] ⚪ [/]'

    # Longitud de la ruleta
    longitud = len(n)

  # Bucle que itera un numero de iteraciones ramdom
    for i in range(iteraciones):
        limpiar_pantalla()

        # Calculamos el indice 
        indice = i % longitud

        # Calculamos el anterior
        anterior = (i - 1) % longitud

        # Restauramos el anterior
        n[anterior] = self.n[anterior]  

        # Indice para colocar la bola
        n[indice] = bola                

        # Mostramos la ruleta con la bola
        console.print(self.mostrar_ruleta(n))

        # Tiempo de espera para que parezca que se mueve
        sleep(delay)
    # Devolvemos el anterior mas 1 para saber donde a caido la bola 
    return  self.n[(anterior + 1) % len(self.n)]

      
  def buscar_apuesta(self,dinero,apuestas_jugador,numeros_sueltos):
    

    # Numeros ramdom para las vueltas de la ruleta
    iteraciones = random.randint(100, 300)

    # Animamos la ruleta y guardamos el resultado
    resultado_rule = self.animar_ruleta(iteraciones= 39)
    
    for numero in numeros_sueltos:
      if resultado_rule == numero:
        dinero_devolver = dinero * 35
    
    
    


    # Listas que vamos a usar para comparar con el resultado del jugador y lo que salga en la ruleta
    
    # Lista de colores
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    verde = [0] 

    # Par o impar
    pares = [n for n in range(1, 37) if n % 2 == 0]
    impares = [n for n in range(1, 37) if n % 2 != 0]

    
    # Docenas
    primera_docena = list(range(1, 13))     
    segunda_docena = list(range(13, 25))    
    tercera_docena = list(range(25, 37))    

    # A nuemros altos o bajos
    baja = list(range(1, 19))   
    alta = list(range(19, 37))  

    # Las filas del tablero
    fila_1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    fila_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    fila_3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]


    return dinero_devolver
   




