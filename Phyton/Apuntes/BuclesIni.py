#Bucles (if/else)/for/while/match(switch)
"""
edad = input("Dame tu edad:")

if edad == "66":
    print("Estas jubilado")
else:
    print("no se....")
    print("De verdad que no lo se ")
print("Fin del progama")
"""
#pass es una instruccion vacia sirve para rellenar bloques sin necesidad de que tengan contenido
"""
edad = 33
if edad > 150:
    print("Estas vivo???")
elif edad >68:
    print("Deberias de estar jubilado")
elif (edad > 50) and (edad < 58):
    print("te falta poco")
else:
    print("aun te queda ")
print("Fin del progama")

# Operadores logicos and/or/not


acertado = False
if not acertado:
    print("Opcion1")
else:
    print("Opcion2")

"""
#For mas facil
# rango va del 0 hasta el 4 el valor final nunca se incluye el inicial si
"""
for n in range(0,5):
    print(n)
for c in "Hola mundo":
    print(c)
for s in "Hola mundo":
    print(s, end="")
# esto va de 0 hasta 30 sin el 30 incluido de saltos de dos en dos sino se pone tercer campo va de 1 en 1
for x in range(0,30,2):
    print(x)
for m in range(0, 40, 2):
    print(m, end="," )
    for m in range(40 , 0 , -2):
        print(m, end=",")
        """
"""
edad = int(input("Dame tu edad:"))
print("Te faltan ", 67-edad,"Años para poder jubilarte")
"""