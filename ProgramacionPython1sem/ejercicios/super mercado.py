cantidad = 0
acumular = 0
precio = 0
opcion = 0
vuelto = 0
efectivo = 0
while opcion != 9:
    print("listado supermercado")
    print("1) Agua          ->  600")
    print("2) Azucar        -> 1200")
    print("3) Aceite        -> 2300")
    print("4) Arroz         -> 1250")
    print("5) Fideos        ->  790")
    print("6) Bebida        -> 1780")
    print("7) Chocolate     -> 2500")
    print("8) Pan de Molde  -> 1340")
    print("9) Salir")
    print("Seleccione (1-9):")
    opcion = int(input("seleccione:"))
    if (opcion>= 1 and opcion<=8):
        if (opcion==1):
            precio=600
        if (opcion==2):
            precio=1200
        if (opcion==3):
            precio=2300
        print("Cantidad del producto")
        cantidad = int(input("ingrese:"))
        acumular = acumular + (precio*cantidad)

print("Gracias por su compra")
print(f" Total a Pagar: {acumular}")
print("¿ Es Cliente Preferencial ? (Si=1,No=0)")
opcion = int(input("Ingrese:"))
if (opcion==1):
    acumular = int( acumular - (acumular*0.25) )
    print(f" Su nuevo total es: {acumular}")
print("Ingrese efectivo")
efectivo= int(input("ingrese:"))
if (efectivo>=acumular):
    vuelto = efectivo - acumular
    if(vuelto>0):
        print(f" su vuelto es:{vuelto}")
    else:
        print("pago justo")
else:
    print("falta dinero, guardias !!")