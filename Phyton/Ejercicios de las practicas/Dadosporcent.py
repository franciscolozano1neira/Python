import random

num_dados = int(input("Introduce el número de dados: "))
tiradas = 0
iguales = False
conteo = [0, 0, 0, 0, 0, 0]

while not iguales:
    tiradas += 1
    dados = [random.randint(1, 6) for _ in range(num_dados)]

    for valor in dados:
        conteo[valor - 1] += 1

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
total_apariciones = tiradas * num_dados

for i in range(6):
    porcentaje = round((conteo[i] / total_apariciones) * 100, 2)
    print("El número", i + 1, "ha salido el", porcentaje, "% de las veces")

print("\nHe lanzado", tiradas, "veces los dados para que sean iguales.")

