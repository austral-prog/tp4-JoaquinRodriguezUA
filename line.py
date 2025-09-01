import math

def line():
    ca = float(input("Ingrese el coeficiente A: "))
    cb = float(input("Ingrese el coeficiente B: "))
    cx1 = float(input("Ingrese el coeficiente X1: "))
    cx2 = float(input("Ingrese el coeficiente X2: "))
    
    p1 = (cx1, (ca*cx1+cb))
    p2 = (cx2, (ca*cx2+cb))

    distancia = math.dist(p1,p2)

    print("El coeficiente A de su ecuación de la recta es:", ca)
    print("El coeficiente B de su ecuación de la recta es:", cb)
    print("El coeficiente X1 de su ecuación de la recta es:", cx1)
    print("El coeficiente X2 de su ecuación de la recta es:", cx2)
    print("")
    print("Para la siguiente ecuación:")
    print("\tY = "+str(ca)+"X + "+str(cb)+"")
    print("")
    print("Dados los siguientes puntos:")
    print("\tP1", p1)
    print("\tP2", p2)
    print("")
    print("La distancia entre ellos es:", distancia)
