import sqlite3


conn = sqlite3.connect('casino_royale.db')
c = conn.cursor()

# Tabla de usuarios con datos esenciales

def agregar_usuario(nombre,saldo,correo,fecha_nacimiento,contrase):
    c.execute("""
    INSERT INTO usuarios (nombre, saldo,correo,fecha_nacimiento,contrasena ) 
    VALUES (?, ?,?,?,?)
    """, (nombre, saldo,correo,fecha_nacimiento,contrase))

def agregar_juego():
    pass

conn.commit()








