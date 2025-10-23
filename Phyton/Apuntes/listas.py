"""esto es lo mas parecido a un arry pero sin llamarse asi en phyton"""

lista=[]
lista2= list()
lista3 =[1,12,32,46,15,162,17,18,91,10]
lista4=["Adrian Mauricio","Kevin","Bianca"]

"""
lista4 =[34, "pepe", False,7654.3,[1,2,3]]
print(lista4)
Recorrer una lista

for elemento in lista3:
    print(elemento)
    
for elemento1 in lista4:
        print(elemento1)"""

"""Esto te muestra la posicion detnro de una list

for posicion in range(0,len(lista4)):
        print(posicion,"-", lista4[posicion])

Añadir cosas a las listas
lista4.append("Nuevo elemento")
print(lista4)

Creamos la lista 5 y la añadimos la lista3 + la siguiente consecucion de numeros
lista5 = lista3 + [23,45]
print(lista5)

Creamos la lista6 y la añadimos la lista 5 mas la lista 4
lista6 = lista5 + lista4
print(lista6)

Borrar elementos por posicion 
print(lista3.pop(1))
print(lista3)

o por elemento concreto que borrar tee borra el primer elemento que se llame asi sea un numero o txt
lista3.remove(7)
print(lista)

Metodo sort modifica la lista original aqui si se toca la lista original solo funciona si los datos son del mismo tipo no puede ordenar string con int
lista3.sort()
print(lista3)

ordenar de forma descendente
lista3.sort(reverse=True)
print(lista3)"""

"""El metodo extend funciona igual que el operador + 
lista3.extend(lista4)
print(lista3)"""
"""Este metodo añade el valor 14 al final del la lista
lista3.append(14)
print(lista3)
Este metodo inseta el objeto 15 en antes de la posicion 2
lista3.insert(2,15)
Esta vez añadimos el 17 en una posicion empezando a contar desde el final de la lista
lista3.insert(-1,17)
Este metodo devuelve cuantas veces aparece el numero entre parentesis
print(lista3.count(1))
Este metodo me permite ver donde se localiza el elemento entre parentesis cuiadado si el numero no esta dara error
print(lista3.index(12))"""

texto=str(lista3)
print(lista3)
texto2="Hola mundo"
lista8=list(texto2)
print(lista8)
texto =texto.replace("[","")
texto =texto.replace("]","")
print(texto)

"""Array de dos dimensiones"""

matriz = [[1,2,3],[4,5,6],[7,8,9]]
"""Este da el 4"""
print(matriz[1][0])
"""Este da el 9"""
print(matriz[2][2])

print(lista3)
"""Desde la posicion 0 hasta la 5 sin ella"""
print(lista3[:5])
"""Desde la posicion 2 a la 5 sin la 5 incluida"""
print(lista3[2:5])
"""Salto de dos en dos"""
print(lista3[5::2])
"""salto de dos en dos al reves desdde la ultima posicion solicitada hasta el final"""
print(lista3[4::-2])
"""Le da la vuela a la lista """
print(lista3[::-1])





