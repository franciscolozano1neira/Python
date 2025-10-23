import random
#14
"""

num1 = int(input("Introduce el primer valor:"))
num2 = int(input("Introduce el segundo valor:"))

for _ in range(num1,num2):
    numeroA=random.randint(num1,num2)
print(numeroA)
print(random.randint(num1,num2))
"""
#15
"""
num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))

a = min(num1, num2)
b = max(num1, num2)

numeroA = random.randint(a, b)
print("Número aleatorio entre ",a,"y",b,":", numeroA)
"""

import math
#21

num = int(input("Introduce un número entero: "))

es_primo = True

if num <= 1:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número ",num, "es primo.")
else:
    print(f"El número",num, "no es primo.")






