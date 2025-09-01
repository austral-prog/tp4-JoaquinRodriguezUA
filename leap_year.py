def leap_year():
    año = int(input("Ingrese un año: "))
    if (año%100 == 0) and (año%400 == 0):
        print("El año",año,"es bisiesto")
    elif (año%100 == 0) and (año%400 != 0):
        print("El año",año,"no es bisiesto")
    elif (año%4 == 0):
        print("El año",año,"es bisiesto")
    else:
        print("El año",año,"no es bisiesto")

# leap_year()