import random

num_dados = int(input("Introduce el número de dados: "))
tiradas = 0
iguales = False

while not iguales:
    tiradas += 1
    dados = [random.randint(1, 6) for _ in range(num_dados)]

    for i in range(len(dados)):
        if i < len(dados) - 1:
            print(dados[i], end=" - ")
        else:
            print(dados[i])

    iguales = True
    for i in range(1, len(dados)):
        if dados[i] != dados[0]:
            iguales = False
            break

print("He lanzado", tiradas, "veces los dados para que sean iguales.")