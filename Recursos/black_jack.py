from rich import print 
from rich.console import Console
from time import sleep
from rich.text import Text
import os
import random
console = Console()
#class Black_jack():
carta = """
   
  [black on white]|A      |[/]
  [black on white]|  ♠    |[/]
  [black on white]|      A|[/]
  [black on white]|       |[/]
  [black on white]|_______|[/]

  
   _______
  |[black on white]A      [/]|
  |[black on white]  ♠    [/]|
  |[black on white]      A[/]|
  |[black on white]       [/]|
  |_______|

"""
console.print(carta)
carta = Text()
carta.append("┌───────┐\n", style="bold black on white")
carta.append("| A ♠   |\n", style="bold black on white")
carta.append("|       |\n", style="bold black on white")
carta.append("|   A   |\n", style="bold black on white")
carta.append("└───────┘\n", style="bold black on white")

# Mostrar la carta
console.print(carta)
console.print(carta)