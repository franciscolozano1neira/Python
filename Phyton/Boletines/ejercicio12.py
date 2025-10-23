import random

numTiradas = int(input("Cuantas veces tiras el dado "))
tipDado = int(input("Que dado tiras: (4,6,8,12,20)"))

print("Tirando los dados", numTiradas,"de",tipDado )

for u in range(1,numTiradas+1):
    tirada =random.randint(1,tipDado)
    print("Tirada",u,":",tirada)