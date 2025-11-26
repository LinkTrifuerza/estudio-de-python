payaso= 112
muñeca=75

cantidad_p=int(input("Cuantos payasos lleva este pedido?"))
cantidad_m=int(input("Cuantas muñecas lleva este pedido?"))

total_p=cantidad_p*payaso
total_m=cantidad_m*muñeca

total_pedido=total_p+total_m

print("El peso todal del pedido es de: ", total_pedido, "kg")