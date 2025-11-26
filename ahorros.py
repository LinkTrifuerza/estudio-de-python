saldo=float(input("Cuanto dinero desea depositar?"))
años=int(input("Cuantos años desea ahorrar?"))
i = 1
print("Con un inversion inicial de $", "{:.2f}".format(saldo),"pesos")
while i<=años:
 interes_anual=float(saldo*0.04)
 saldo+=interes_anual
 print("El saldo en su año", i, "seria de: $", "{:.2f}".format(saldo), "pesos")
 i += 1