inversion=float(input("Introduzca la cantidad que desea invertir: "))
procentaje_interes_anual=float(input("Introduzca el procentaje de interes anual: "))
años_de_inversion=int(input("Durante cuantos años desea invertir? "))

calcular_interes=inversion*(procentaje_interes_anual/100+1)**años_de_inversion


print("{:.2f}".format(calcular_interes))