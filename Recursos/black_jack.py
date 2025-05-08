from rich import print 
from rich.console import Console
from time import sleep
from rich.text import Text
import os
import random
from Recursos.tragaperras import *

console = Console()


class Jugador():

  def __init__(self):
    VALORES_CARTAS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  
    self.valor_total = 0

  def plantarse(self):
    pass

  def pedir_carta(self,valor):
    pass

class Crupier():
  def __init__(self,):
    VALORES_CARTAS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    self.valor_crupier = 0

  def mostrar_primera_carta(self,valor_carta):
    return  f"""
    ┌───────┐
    │[black on white]{valor_carta}      [/]│
    │[black on white]♠      [/]│
    │[black on white]       [/]│
    │[black on white]   ♠   [/]│
    │[black on white]       [/]│
    │[black on white]      ♠[/]│
    │[black on white]      {valor_carta}[/]│
    └───────┘

    """


  def revelar_carta(self,carta):
    pass

