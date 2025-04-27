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

class Base_de_datos():
    
    

    def agregar_usuario(self,nombre,saldo,correo,fecha_nacimiento,contrase):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        # Buscamos el correo
        c.execute('SELECT correo FROM usuarios WHERE correo = ?', (correo,))

        # Si encuentra algo es que esta registrado asi que devolvemos falso
        if c.fetchone() is not None:
            # Mensaje de que esta registrado
            
            return False
        # Si no los registramos en la base de datos
        c.execute("""
                INSERT INTO usuarios (nombre, saldo, correo, fecha_nacimiento, contrasena) 
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, saldo, correo, fecha_nacimiento, contrase))
        conn.commit()
        conn.close()
        return True
            

    def agregar_partida(self):
        pass

    def iniciar_sesion(self,correo,contrasena):
        try:
            conn = sqlite3.connect('casino_royale.db')
            c = conn.cursor()
            c.execute('SELECT contrasena FROM usuarios WHERE correo = ?',(correo,))
            lista_contrasena_usuario = c.fetchall()
            conn.close()

            if not lista_contrasena_usuario :
                console.print(Panel("[bold #ff0000]Correo no registrado[/]", border_style="#ff0000", width=30))
                return False
            contrasena_usuario = lista_contrasena_usuario[0][0]

            if contrasena_usuario == contrasena:
                console.print(Panel(f'[bold #24fc69]Inicio de sesion correcto[/]',border_style='#24fc69',expand=False,width=30))
                return True
            else:
                console.print(Panel("[bold #ff0000]Contraseña incorrrecta[/]", border_style="#ff0000"))
                return False
            
            
            
        except sqlite3.Error as e:
            console.print(Panel(f'[bold red]Error: {str(e)}[/]', border_style="red", width=30))
            return False

    
    

    
conn = sqlite3.connect('casino_royale.db')
c = conn.cursor()
c.execute("""UPDATE usuarios
SET correo = 'jorge@'
WHERE id = 1 """)
conn.commit()
conn.close()








