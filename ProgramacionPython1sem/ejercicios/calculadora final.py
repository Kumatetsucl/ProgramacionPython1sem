import os
import math
def raizcuadrada():
    print("\n\tRaiz Cuadrada")
    num = int(input("\nIngrese Número: "))
    print("\nLa raíz cuadrada de {} es {}".format(num, math.sqrt(num)))

def radianes():
    print("\n\tSENO")
    radianes = float(input("\nIngrese Radianes: "))
    print("\nEl seno de {} es {}". format (radianes, math.sin(radianes)))
              
def multiplicacion():
    print("\n\tMULTIPLICACION")
    a = int(input("ingrese primer numero: "))
    b = int(input("ingrese segundo numero: "))
    print(f"resultado: ", a*b)

def division():
    print("\n\tDIVISION")
    a = int(input("ingrese primer numero: "))
    b = int(input("ingrese segundo numero: "))
    if b==0:
        print("error de sintaxys")
    else:
        print(f"resultado: ", a/b)
        
def resta():
    print("\n\tRESTA")
    a = int(input("ingrese primer numero: "))
    b = int(input("ingrese segundo numero: "))
    print(f"resultado: ", a-b)
    
def suma():
    print("\n\tSUMA")
    a = int(input("ingrese primer numero: "))
    b = int(input("ingrese segundo numero: "))
    print(f"resultado: ", a+b)
    
def menu():
    os.system("cls")
    opcion=1
    while (opcion!=5):
        print("\n\tMENU \n1)suma \n2)resta \n3)division \n4)multiplicacion \n5)Seno \n6)Raiz Cuadrada \n7)salir")
        opcion=int(input("seleccione opcion(1-5): "))
        if(opcion>6) or (opcion<1):
            print("Selecciono una opcion incorrecta")
        else:
            opciones(opcion)
                   
def opciones(opcion):
    if(opcion==1):
        suma()
    if(opcion==2):
        resta()
    if(opcion==3):
        division()
    if(opcion==4):
        multiplicacion()
    if(opcion==5):
        radianes()
    if(opcion==6):
        raizcuadrada()
    if(opcion==7):
        print("salio del sistema")

if __name__ == '__main__':
    menu()
    os.system("cls")
    print("fin de la aplicacion")