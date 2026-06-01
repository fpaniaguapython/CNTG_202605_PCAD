import sqlite3

DB_NAME='db_empleados_optimizado.sqlite3'

def obtener_conexion(nombre_database):
    conn = sqlite3.connect(nombre_database)
    return conn

if __name__=='__main__':
    # Establecer conexión
    conn = obtener_conexion(DB_NAME)

    # Cerrar conexión
    conn.close()