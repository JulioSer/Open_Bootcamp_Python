import datetime

año = int(input('Introduce un año: '))

print("PRIMER MÉTODO USANDO DATETIME")
x = datetime.datetime(año,12,31)
numeroDias = x.strftime("%j")
print("El año", año, "tiene", numeroDias, "días")
if numeroDias == "366":
    print("El año ", año, "es bisiesto")
else:
    print("El año", año, "no es bisiesto" ) 

print()
print("SEGUNDO MÉTODO CON TRES IF")
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')
    

print()
print("TERCER MÉTODO CON UN SOLO IF")
if   año % 4 == 0 and  (not año % 100 == 0 or  año % 400 == 0):
    print("El", año, "es bisiesto")
else:
    print("El",año, "no es bisiesto")    