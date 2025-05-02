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
    n = self.n.copy()
    bola = '[on #ff6fde ] ⚪ [/]'
    longitud = len(n)

    for i in range(iteraciones):
        limpiar_pantalla()

        indice = i % longitud
        anterior = (i - 1) % longitud

        n[anterior] = self.n[anterior]  # restaurar el anterior
        n[indice] = bola                # colocar la bola en el nuevo índice

        console.print(self.mostrar_ruleta(n))
        sleep(delay)

    return  self.n[(anterior + 1) % len(self.n)]

      
    




