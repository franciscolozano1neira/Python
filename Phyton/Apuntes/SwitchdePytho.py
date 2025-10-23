#Funciona como un switch

opc=input("p para jugar, c para conficurar, x para salir:")
match opc:
    case "p" | "P"| "J"|"j":# asi se pondrian multiples valores con el or = |
        print("Has elegid jugar")
    case "c":
        print("Has elegido configurar")
    case "x":
        print("Has elegido salir. Xao xao xao")
    case _:
        print("Opcion no valida")#este caso seria el por defecto
print("Fin del menu")
