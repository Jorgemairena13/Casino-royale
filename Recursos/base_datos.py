import sqlite3
from rich.panel import Panel
from rich.console import Console
from datetime import datetime
from Recursos.tragaperras import *
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

    def mostrar_partidas_tragaperras(self,id_usuario):
        # Conexión a la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()

        # Activar claves foráneas
        c.execute("PRAGMA foreign_keys = ON;")

        # Obtener todas las partidas de tragaperras
        c.execute("""
            SELECT t.id_tirada, u.nombre, t.premio, t.fecha
            FROM tragaperras t
            JOIN usuarios u ON t.id_usuario = u.id
            WHERE t.id_usuario = ?
            ORDER BY t.fecha DESC
        """, (id_usuario,))
        
        partidas = c.fetchall()

        if partidas:
            table = Table(title="Historial de Tragaperras")

            table.add_column("Tirada #", style="cyan", justify="center")
            table.add_column("Usuario", style="magenta", justify="center")
            table.add_column("Premio (€)", style="green", justify="center")
            table.add_column("Fecha", style="yellow", justify="center")

            for partida in partidas:
                table.add_row(
                    str(partida[0]),
                    partida[1],
                    f"{partida[2]}€",
                    partida[3]
                )

            console.print(table)
        else:
            console.print("[bold red]No hay partidas de tragaperras registradas en la base de datos.[/bold red]")

        conn.close()


#
    def crear_tabla_ruleta(self):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")

        # Crear tabla con clave foránea
        c.execute("""
            CREATE TABLE IF NOT EXISTS ruleta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                dinero_apostado INTEGER NOT NULL,
                num_ganador INTEGER NOT NULL,
                premio INTEGER DEFAULT 0,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        """)

        conn.commit()
        conn.close()


    def actualizar_partidas_ruleta(self, usuario, apuesta, ganador, premio):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")

        c.execute("""
            INSERT INTO ruleta (id_usuario, dinero_apostado, num_ganador, premio)
            VALUES (?, ?, ?, ?)
        """, (usuario, apuesta, ganador, premio))

        conn.commit()
        conn.close()

    def mostrar_datos_ruleta(self,id):
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON;")

        # Obtenemos datos combinados de ruleta y usuarios
        c.execute("""
            SELECT ruleta.id, usuarios.nombre, ruleta.dinero_apostado, ruleta.num_ganador, ruleta.premio
            FROM ruleta
            JOIN usuarios ON ruleta.id_usuario = usuarios.id
            WHERE usuarios.id = ?
        """,(id,))
        
        partidas = c.fetchall()
        
        if partidas:
            table = Table(title="Historial de Partidas",border_style='red')

            table.add_column("Tirada #", style="cyan", justify="center")
            table.add_column("Usuario", style="magenta", justify="center")
            table.add_column("Apuesta (€)", style="green", justify="center")
            table.add_column("Número ganador", style="yellow", justify="center")
            table.add_column("Premio (€)", style="bold green", justify="center")

            for partida in partidas:
                table.add_row(
                    str(partida[0]),
                    partida[1],
                    f"{partida[2]}€",
                    str(partida[3]),
                    f"{partida[4]}€"
                )

            console.print(table)
        else:
            console.print("[bold red]No hay partidas registradas en la base de datos.[/bold red]")

        conn.close()

    def mostrar_estadisticas_ruleta(self):
        # Conexión a la base de datos
        conn = sqlite3.connect('casino_royale.db')
        c = conn.cursor()

        # Activar claves foráneas
        c.execute("PRAGMA foreign_keys = ON;")

        # Obtener estadísticas de números
        c.execute("""
            SELECT num_ganador, COUNT(*) as frecuencia
            FROM ruleta
            GROUP BY num_ganador
            ORDER BY frecuencia DESC
            LIMIT 10
        """)
        
        estadisticas = c.fetchall()

        if estadisticas:
            table = Table(title="Top 10 Números más Frecuentes en la Ruleta")

            table.add_column("Número", style="cyan", justify="center")
            table.add_column("Frecuencia", style="magenta", justify="center")
            table.add_column("Color", style="yellow", justify="center")

            for numero, frecuencia in estadisticas:
                # Determinar el color del número
                if numero == 0:
                    color = "Verde"
                elif numero in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
                    color = "Rojo"
                else:
                    color = "Negro"

                table.add_row(
                    str(numero),
                    str(frecuencia),
                    color
                )

            console.print(table)

            # Mostrar estadísticas adicionales
            c.execute("SELECT COUNT(*) FROM ruleta")
            total_tiradas = c.fetchone()[0]
            
            console.print("\n[bold]Estadísticas Generales:[/bold]")
            console.print(f"Total de tiradas registradas: {total_tiradas}")
            
            # Calcular porcentajes
            for numero, frecuencia in estadisticas:
                porcentaje = (frecuencia / total_tiradas) * 100
                console.print(f"Número {numero}: {porcentaje:.2f}% de las tiradas")

        else:
            console.print("[bold red]No hay suficientes datos para mostrar estadísticas.[/bold red]")

        conn.close()

    

    