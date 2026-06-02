import sqlite3
DB_NAME='db_empleados_optimizado.sqlite3'

class Empleado:
    def __init__(self, nombre, apellidos, categoria_programacion, ciudad, salario, id=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.categoria_programacion = categoria_programacion
        self.ciudad = ciudad
        self.salario = salario


def obtener_conexion(nombre_database):
    conn = sqlite3.connect(database=nombre_database)
    return conn
# CRUD (Create, Read, Update, Delete)
def create(conn : sqlite3.Connection, empleado : Empleado):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO empleados(nombre, \
                   apellidos, categoria_programacion, ciudad, salario) \
                   VALUES (?, ?, ?, ?, ?)', (empleado.nombre, empleado.apellidos,
                                             empleado.categoria_programacion,
                                             empleado.ciudad,
                                             empleado.salario))
    conn.commit()
    cursor.close()

if __name__=='__main__':
    # Establecer conexión
    conn = obtener_conexion(DB_NAME)
    # Create 
    empleado = Empleado('Empleado 1', 'Apellidos 1', 'Ingeniero de Software', 'Vigo', 25_000)
    create(conn, empleado)
    # Cerrar conexión
    conn.close()