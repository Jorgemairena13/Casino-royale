from rich import print 
from rich.console import Console
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
    self.tablero_ruleta = '''
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
    from rich import print 
from rich.console import Console
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
    # Definiciones correctas de los colores
    self.rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    self.negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

  def mostrar_ruleta(self,n):  
    '''Muestra la ruleta y el tablero de la ruleta'''
    # Tablero para que el usuario vea a que se puede apostar
    self.tablero_ruleta = '''
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                     RULETA CASINO                             ┃
    ┣━━━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┫
    ┃       ┃  3  ┃  6  ┃  9  ┃ 12  ┃ 15  ┃ 18  ┃ 21  ┃ 24  ┃ 27  ┃ 30  ┃ 33  ┃ 36  ┃     
    ┃       ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃    
    ┣━━━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
    ┃   0   ┃  2  ┃  5  ┃  8  ┃ 11  ┃ 14  ┃ 17  ┃ 20  ┃ 23  ┃ 26  ┃ 29  ┃ 32  ┃ 35  ┃     
    ┃  🟢   ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃     
    ┣━━━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
    ┃       ┃  1  ┃  4  ┃  7  ┃ 10  ┃ 13  ┃ 16  ┃ 19  ┃ 22  ┃ 25  ┃ 28  ┃ 31  ┃ 34  ┃     
    ┃       ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ 🔴  ┃ 🔴  ┃ ⚫  ┃ 🔴  ┃ ⚫  ┃ ⚫  ┃ ⚫ ┃     
    ┣━━━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┫
    ┃  1-12 PRIMERA DOCENA  ┃  13-24 SEGUNDA DOCENA  ┃  25-36 TERCERA DOCENA        ┃
    ┣━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃    1-18   ┃    PAR    ┃    🔴    ┃   IMPAR   ┃   19-36   ┃     ⚫             ┃
    ┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┛
    '''
    # Determinar el color de cada número para la ruleta gráfica
    def color_format(num):
        if num == 0 :
            return "white on green"  
        elif num in self.rojos:
            return "white on red"    
        else:
            return "white on black"  
    
    # Ruleta con todos los índices correctamente coloreados
    ruleta2 = f"""[bold #6fff90]
                  ▓▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▓               
              ▓▓▓▓█▓▓▓████[{color_format(n[0])}]0{n[0]}[/]▓▓▓████▓▓▓▓▓           
            ▒▓▓████▓▓[{color_format(n[36])}]{n[36]}[/]▓███▓▓[{color_format(n[1])}]{n[1]}[/]▓████▓▓▓███▓      
          ▒▓▓█▓▓▓▓█[{color_format(n[35])}]0{n[35]}[/]██▓▓▓███▓▓▓██[{color_format(n[2])}]{n[2]}[/]█▓▓▓████▓▓▓▒   
        ▒▓████[{color_format(n[34])}]{n[34]}[/]▓▓▓▓███▓▓▓██▓▓▓██▓▓▓█[{color_format(n[3])}]{n[3]}[/]██▓▓▓▓▓█▓   
      ▓▒▓▓▓[{color_format(n[33])}]{n[33]}[/]█████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓[{color_format(n[4])}]0{n[4]}[/]▓▓█████▓
      ▓▒▓[{color_format(n[32])}]{n[32]}[/]▓▓█████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓█[{color_format(n[5])}]{n[5]}[/]████▓
      ▓▓█[{color_format(n[31])}]0{n[31]}[/]█▓▓▓▓▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█████▓▓▓▓▓  
    ▒▓█████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███▓▓▓▓[{color_format(n[6])}]0{n[6]}[/]▓▓▓▒ 
    ▒▓▓▓[{color_format(n[30])}]{n[30]}[/]█████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█████▒ 
    ▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████[{color_format(n[7])}]{n[7]}[/]███▓▒
    ▓████[{color_format(n[29])}]{n[29]}[/]▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒
    ▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓[{color_format(n[8])}]{n[8]}[/]▓███▓
    ▓████[{color_format(n[28])}]{n[28]}[/]████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓███▓
    ▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓[{color_format(n[9])}]{n[9]}[/]▓███▓
    ▓▓███[{color_format(n[27])}]0{n[27]}[/]▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
    ▓▓███▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓[{color_format(n[10])}]0{n[10]}[/]▓▓▓▓▓
    ▓▓███[{color_format(n[26])}]{n[26]}[/]▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
    ▓████▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▓[{color_format(n[11])}]{n[11]}[/]▓▓▓▓▒
    ▒▓██▓[{color_format(n[25])}]{n[25]}[/]▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓███████▓▒
    ▒▓▓▓▓▓████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓[{color_format(n[12])}]{n[12]}[/]████▒ 
    ▒▒████[{color_format(n[24])}]{n[24]}[/]███▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████▓▓▓▓▓▒▓ 
      ▒▓███▓▓▓▓▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓███[{color_format(n[13])}]{n[13]}[/]███▓▓▒  
      ▓▓▓▓▓▓[{color_format(n[23])}]{n[23]}[/]▓████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓▓▓███▓▒   
        ▒▓▓███▓▓▓▓███▓▓▓██▓▓███▓▓▓██▓█▓▓[{color_format(n[14])}]{n[14]}[/]▓▓▓▒     
          ▒▓▓██[{color_format(n[22])}]{n[22]}[/]▓▓▓▓███▓▓▓███▓▓▓███▓▓▓████▓▓▒▒      
          ▒▓▓██▓▓▓[{color_format(n[21])}]{n[21]}[/]▓███▓▓▓███▓▓▓███▓▓▓[{color_format(n[15])}]{n[15]}[/]████▓▓   
            ▒▓▓▓▓███[{color_format(n[20])}]{n[20]}[/]▓▓▓▓███▓▓▓███[{color_format(n[16])}]0{n[16]}[/]█▓▓▓██▓▒         
              ▓▒▓▓██▓▓▓[{color_format(n[19])}]{n[19]}[/]▓█[{color_format(n[18])}]{n[18]}[/]██▓[{color_format(n[17])}]{n[17]}[/]▓▓▓███▓▓          
                  ▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒   [/]            
    """
    return ruleta2 + self.tablero_ruleta
    


  def animar_ruleta(self,iteraciones,delay = 0.1):
    n = self.n.copy()

    # Bola que se vera en la ruleta
    bola = '[on #ff6fde ] ⚪ [/]'

    # Longitud de la ruleta
    longitud = len(n)

    # Bucle que itera un numero de iteraciones random
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
    
    # Posición final donde cae la bola
    posicion_final = (iteraciones - 1) % longitud
    
    # Restauramos el último valor para que se muestre correctamente
    n[posicion_final] = self.n[posicion_final]
    
    # Mostramos la ruleta final con el resultado
    limpiar_pantalla()
    console.print(self.mostrar_ruleta(n))
    
    # Resaltamos el resultado
    resultado = self.n[posicion_final]
    console.print(f"[bold yellow]¡La bola ha caído en el número {resultado}![/]")
    
    # Devolvemos el número donde cayó la bola
    return resultado

      
  def buscar_apuesta(self,dinero,apuestas_jugador,numeros_sueltos,resultado_rule):

    
    dinero_devolver = 0


    # Comparamos para ver si el numero del jugar es igual al numero que a salido
    for numero in numeros_sueltos:
        if resultado_rule == numero:
            dinero_devolver += dinero * 36 
            
        
    # Comprobamos que no haya salido el 0 para terminar sin nada
    if resultado_rule == 0 and 0 not in numeros_sueltos:
        return 0
    
    # Listas que vamos a usar para comparar con el resultado del jugador y lo que salga en la ruleta
    
    # Lista de colores
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    

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


    # Logica de las apuestas

    # Logica si hace apuestas a los colores
    if apuestas_jugador[0] == "0": # Si es cero significa que no ha puesto nada
      pass

    elif apuestas_jugador[0] == "Rojo": # Si a puesto rojo
      if resultado_rule in rojos: # Comprobamos que el numero que haya salido sea rojo
        dinero_devolver = dinero * 2

    elif apuestas_jugador[0] == "Negro": # Si a puesto negro
      if resultado_rule in negros: # Comprobamos que el numero que haya salido sea negro
        dinero_devolver = dinero * 2

    # Logica de la apuesta si es par o impar
    if apuestas_jugador[1] == "0":
      pass
    elif apuestas_jugador[1] == "Par":
      if resultado_rule % 2 == 0:
        dinero_devolver += dinero * 2
    elif apuestas_jugador[1] == "Impar":
      if resultado_rule % 2 != 0:
        dinero_devolver += dinero * 2

    # Logica de las docenas
    if apuestas_jugador[2] == "0":
      pass
    elif apuestas_jugador[2] == "1 docena":
      if resultado_rule in primera_docena:
        dinero_devolver += dinero * 3
    elif apuestas_jugador[2] == "2 docena":
      if resultado_rule in segunda_docena:
        dinero_devolver += dinero * 3
    elif apuestas_jugador[2] == "3 docena":
      if resultado_rule in tercera_docena:
        dinero_devolver += dinero * 3

    # Logica de la alta y la baja
    if apuestas_jugador[3] == "0":
      pass
    elif apuestas_jugador[3] == "Alta":
      if resultado_rule in alta:
        dinero_devolver += dinero * 2
    elif apuestas_jugador[3] == "Baja":
      if resultado_rule in baja:
        dinero_devolver += dinero * 2
    
    # Logica de las filas
    if apuestas_jugador[4] == "0":
      pass
    elif apuestas_jugador[4] == "Fila 1":
      if resultado_rule in fila_1:
        dinero_devolver += dinero * 3
    elif apuestas_jugador[4] == "Fila 2":
      if resultado_rule in fila_2:
        dinero_devolver += dinero * 3
    elif apuestas_jugador[4] == "Fila 3":
      if resultado_rule in fila_3:
        dinero_devolver += dinero * 3

    return dinero_devolver
   




