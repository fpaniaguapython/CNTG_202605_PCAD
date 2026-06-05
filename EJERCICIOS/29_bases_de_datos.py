import sqlite3
from unittest import case

DB_NAME='db_empleados_optimizado.sqlite3'

class Empleado:
    def __init__(self, nombre, apellidos, categoria_profesional, ciudad, salario, id=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.categoria_profesional = categoria_profesional
        self.ciudad = ciudad
        self.salario = salario


def obtener_conexion(nombre_database):
    conn = sqlite3.connect(database=nombre_database)
    return conn
######
# CRUD (Create, Read, Update, Delete)
######

######
# CRUD - CREATE
######
def create(conn : sqlite3.Connection, empleado : Empleado):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO empleados(nombre, \
                   apellidos, categoria_profesional, ciudad, salario) \
                   VALUES (?, ?, ?, ?, ?)', (empleado.nombre, empleado.apellidos,
                                             empleado.categoria_profesional,
                                             empleado.ciudad,
                                             empleado.salario))
    conn.commit()
    cursor.close()

######
# CRUD - READ
######
def read(conn : sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()
    cursor.close()
    return empleados

def read_by_id(conn : sqlite3.Connection, id : int):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados WHERE id=?', (id,))
    empleado = cursor.fetchone()
    cursor.close()
    return empleado

######
# CRUD - UPDATE
######
def update(conn : sqlite3.Connection, empleado : Empleado):
    cursor = conn.cursor()
    cursor.execute('UPDATE empleados SET nombre=?, apellidos=?, \
                   categoria_profesional=?, ciudad=?, salario=? \
                   WHERE id=?', (empleado.nombre, empleado.apellidos,
                                 empleado.categoria_profesional,
                                 empleado.ciudad,
                                 empleado.salario, empleado.id))
    conn.commit()
    cursor.close()

######
# CRUD - DELETE
######
def delete(conn : sqlite3.Connection, id : int):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM empleados WHERE id=?', (id,))
    conn.commit()
    cursor.close()


def get_opcion():
    print('1. Crear empleado')
    print('2. Leer empleados')
    print('3. Actualizar empleado')
    print('4. Eliminar empleado')
    print('5. Salir')
    return int(input('Seleccione una opción: '))

if __name__=='__main__':
    # Establecer conexión
    conn = obtener_conexion(DB_NAME)
    while True:
        opcion = get_opcion()
        match opcion:
            case 1:
                # Crear empleado
                nombre = input('Nombre: ')
                apellidos = input('Apellidos: ')
                categoria_profesional = input('Categoría profesional: ')
                ciudad = input('Ciudad: ')
                salario = float(input('Salario: '))
                empleado = Empleado(nombre, apellidos, categoria_profesional, ciudad, salario)
                create(conn, empleado)
            case 2:
                # Leer empleados
                empleados = read(conn)
                for emp in empleados:
                    print(emp)
            case 3:
                # Actualizar empleado
                id = int(input('ID del empleado a actualizar: '))
                empleado = read_by_id(conn, id)
                if empleado:
                    print('Empleado encontrado:')
                    print(empleado)
                    nombre = input('Nuevo nombre: ')
                    apellidos = input('Nuevos apellidos: ')
                    categoria_profesional = input('Nueva categoría profesional: ')
                    ciudad = input('Nueva ciudad: ')
                    salario = float(input('Nuevo salario: '))
                    empleado_actualizado = Empleado(nombre, apellidos, categoria_profesional, ciudad, salario, id)
                    update(conn, empleado_actualizado)
                else:
                    print('Empleado no encontrado')
            case 4:
                # Eliminar empleado
                id = int(input('ID del empleado a eliminar: '))
                delete(conn, id)
            case 5:
                print('Saliendo...')
                break
    
    # Cerrar conexión
    conn.close()