import sqlite3
from rich.panel import Panel
from rich.console import Console
from datetime import datetime

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

    def actualizar_historial_transacciones(self,dinero_ingresado,correo):
        # Conectamos a la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        # Ejecutamos para que las claves foraneas funcionen
        c.execute("PRAGMA foreign_keys = ON;")
        
        # Sacamos el id del usuario
        id = self.sacar_id(correo)
        
        # El momento de la trasaccion que es en el momento de ahora
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insertamos valores en la tabla
        c.execute("""INSERT INTO historial (dinero,id_usuario,fecha_transaccion)
                   VALUES (?, ?, ?)""",(dinero_ingresado,id,fecha))
        # Guardamos los cambios y cerramos conexion
        conn.commit()
        conn.close()

    def mostrar_historial(self,correo):
         # Conectamos a la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        # Ejecutamos para que las claves foraneas funcionen
        c.execute("PRAGMA foreign_keys = ON;")
        # Sacamos el id del usuario
        id = self.sacar_id(correo)
        c.execute('''SELECT usuarios.nombre, historial.dinero,historial.fecha_transaccion 
                  FROM historial
                  JOIN usuarios 
                  ON historial.id_usuario = usuarios.id 
                  WHERE usuarios.id = ?
                  ORDER BY historial.fecha_transaccion
                  ''',(id,))
        historial=c.fetchall()

        conn.close()
        return historial
    
    def crear_tabla_tragaperras(self):
        # Conectamos la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        # Claves foranes activas
        c.execute("PRAGMA foreign_keys = ON;")
        c.execute("""CREATE TABLE IF NOT EXISTS tragaperras (
    id_tirada INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    premio INTEGER DEFAULT 0,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
    )""")
        conn.commit()
        conn.close()
    
    def actualizar_partidas_tragaperras(self,correo,premio):
        id = self.sacar_id(correo)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Conectamos a la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        # Ejecutamos para que las claves foraneas funcionen
        c.execute("PRAGMA foreign_keys = ON;")

        # Insertamos datos
        c.execute("""INSERT INTO tragaperras (id_usuario,premio,fecha)
                   VALUES (?, ?, ?)""",(id,premio,fecha))

        conn.commit()
        conn.close()



base = Base_de_datos()










