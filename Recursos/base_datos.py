import sqlite3
from rich.panel import Panel
from rich.console import Console


console = Console()

class Base_de_datos():

    def crear_tabla_usuarios(self):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")
        c.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    saldo REAL DEFAULT 0,
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    contrasena TEXT NOT NULL);""")
        conn.commit()
        conn.close()

    

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


    def sacar_saldo(self,correo):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute('SELECT saldo FROM usuarios WHERE correo = ?',(correo,))
        saldo_usuario = c.fetchall()
        conn.close()
        return saldo_usuario[0][0]
    
    def actualizar_saldo(self,correo, saldo):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute('UPDATE usuarios set saldo = ?  WHERE correo = ?',(saldo,correo))
        conn.commit()
        conn.close()

    def sacar_id(self,correo):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute('SELECT id FROM usuarios WHERE correo = ?',(correo,))
        id_usuario = c.fetchall()
        conn.close()
        return id_usuario[0][0]


    def crear_tabla_historial(self):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")
        c.execute("""CREATE TABLE IF NOT EXISTS historial (
    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    dinero REAL DEFAULT 0,
    id_usuario INTEGER NOT NULL,
    fecha_transaccion DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) 
    );""")
        conn.commit()
        conn.close()

    def actualizar_historial_transacciones(self,dinero_ingresado,correo,fecha):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")
        id = self.sacar_id(correo)
        c.execute("""INSERT IN TO historial (dinero,id_usuario,fecha_transaccion)
                   VALUES (?, ?, ?, ?)""",(dinero_ingresado,id,fecha))

base = Base_de_datos()










