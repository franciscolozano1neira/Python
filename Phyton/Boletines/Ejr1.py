"""
#ejer1
for x in range(11):
    print(x,end=",")
print("\b")#quita el ultimo elemento de la rista

#ejr2
for z in range (0,102,2):
    print(z,end=",")
print("\b")
#ejer3

num = int(input("Introduce un valor"))

print("Los 5 primeros multiplos del",  num ," es:")

for k in range (1,6):
    print(num*k , end=",")
print("\b")
#ejer4
for t in range(1,10000):
    if t%7==0:
        print(t,end=",")
print("\b")

#ejer5
num1 = int(input("Introduce un valor: "))
if num1 %2 ==0:
    print("el numero:", num1 ," es par")
else:
    print("el numero:", num1,"es impar")

#ejer6
num2 = int(input("Introduce un valor: "))
if num2 %3 ==0:
    print("el numero", num2,"si es divisible entre 3")
else:
    print("El numero", num2,"no es divisible entre 3")
"""
import random

#ejer12

numDeTiradas = int(input("Cuantas veces tiras el dado"))
numCaras = int(input("¿De cuántas caras son los dados? (ej: 4, 6, 8, 12, 20)"))

print("tirando los dados",numDeTiradas,"de ",numCaras)

for u in range(1,numDeTiradas + 1):
    tirada = random.randint(1,numCaras)
    print("dado",u,": " ,tirada )
