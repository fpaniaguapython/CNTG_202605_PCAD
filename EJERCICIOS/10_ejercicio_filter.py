'''
Crear una tupla con 3 tuplas. Cada una de estas tuplas tiene:
(Una lista con dos números, el nombre de una persona)
(([15,3],'Raúl'),(),())
Filtrar los elementos que cumplan con la siguientes reglas:
1. Aquellos cuyo nombre contenga la letra A
2. Aquellos cuyo primer número sea > 10
3. Aquellos cuya suma de los dos números sea par.
4. Aquellos cuyo primer número sea > 12
'''
datos = (
    ([15,3],'Jesús'),
    ([8,3],'Ana'),
    ([12,4],'Gustavo')
    )
datos[1][1] # Ana
datos[1][0][0] # 8

# 1
def has_a(empleado):
    return 'a' in empleado[1].lower()
empleados_con_a = filter(has_a, datos)
for empleado in empleados_con_a:
    print(empleado)

# 2
def antiguedad_mayor_10(empleado):
    return empleado[0][0]>10

empleados_mayor_10 = filter(antiguedad_mayor_10, datos)

# 3
def suma_par(empleado):
    suma = empleado[0][0]+empleado[0][1]
    #suma = sum(empleado[0])
    return suma%2==0

empleados_pares = filter(suma_par, datos)

# 4
empleados_mayor_12 = filter(lambda empleado : empleado[0][0]>12, datos)

