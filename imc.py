peso=(float(input("introduzca su peso en kg:")))
altura=(float(input("introduzca su altura en cm:")))
imc=peso/altura**2
print("Tu indice de masa corporal es de: " + "{:.2f}".format(imc))
