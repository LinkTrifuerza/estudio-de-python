pan=float(3.49)
descuento=float(0.60)
cantidad=int(input("cuantos panes desea llevar?"))
total_panes=cantidad*pan
total_descuento=total_panes*descuento
total=total_panes-total_descuento
print("El precio total por sus", cantidad, "piezas de panes es de", "{:.2f}".format(total), "con un descuento aplicado del 60%, " \
"Gracias por su compra")