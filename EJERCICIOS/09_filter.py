lista_personas = [('Ramón',100),('Teresa',200),('Jesús',50)]
lista_personas.append(('Julia',5000))

for persona in lista_personas:
    print(persona[0])

def is_mayor_100(persona):
    return persona[1]>100

lista_personas_mayor_100 = filter(is_mayor_100, lista_personas)    
lista_personas_mayor_100=list(lista_personas_mayor_100)
for persona in lista_personas_mayor_100:
    print(persona)

    

