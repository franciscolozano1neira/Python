"""
from random import randint

lista = list()

for i in range(10):
    numeros = randint(1, 10)
    lista.append(numeros)
print("\n",lista,end="")
"""

digitos = [
    ["###", "# #", "# #", "# #", "###"],
    ["  #", "  #", "  #", "  #", "  #"],
    ["###", "  #", "###", "#  ", "###"],
    ["###", "  #", "###", "  #", "###"],
    ["# #", "# #", "###", "  #", "  #"],
    ["###", "#  ", "###", "  #", "###"],
    ["###", "#  ", "###", "# #", "###"],
    ["###", "  #", "  #", "  #", "  #"],
    ["###", "# #", "###", "# #", "###"],
    ["###", "# #", "###", "  #", "###"],

]
numero = input("introduce un numero: ")

for lista in range(5):
    for digito in numero:
        print(digitos[int(digito)][lista], end=" ")
    print()

