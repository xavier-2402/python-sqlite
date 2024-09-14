import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()


def insertar_usuario(nombre, edad):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    conn.close()

def consultar_usuarios():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Insertar usuarios
insertar_usuario('Alice', 30)
insertar_usuario('Bob', 25)

# Consultar y mostrar usuarios
usuarios = consultar_usuarios()
for usuario in usuarios:
    print(usuario)