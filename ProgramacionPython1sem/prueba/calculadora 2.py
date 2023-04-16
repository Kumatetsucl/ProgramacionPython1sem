menu = print("--main menu--  \n1- suma \n2- resta \n3- multiplicacion \n4- division \n5- salir")
opcion = int(input ("ingrese su opcion: "))
opcion == 0
while opcion < 5 or opcion > 0:
        if opcion == 1:
                A = input("ingrese primer numero: ")
                B = input("ingrese segundo numero: ")
                print("respuesta: la suma de", str(int(A)), "+", str(int(B)), "es: ", str(int(A)+int(B)))
        elif opcion == 2:
                A = input("ingrese primer numero: ")
                B = input("ingrese segundo numero: ")
                print("respuesta: la resta de", str(int(A)), "-", str(int(B)), "es: ", str(int(A)-int(B)))
        elif opcion == 3:
                A = input("ingrese primer numero: ")
                B = input("ingrese segundo numero: ")
                print("respuesta: la multiplicacion de", str(int(A)), "*", str(int(B)), "es: ", str(int(A)*int(B)))
        elif opcion == 4:
                A = input("ingrese primer numero: ")
                B = input("ingrese segundo numero: ")
                print("respuesta: la division de", str(int(A)), "/", str(int(B)), "es: ", str(int(A)/int(B)))
        elif opcion == 4:
                A = input("ingrese primer numero: ")
                B = input("ingrese segundo numero: ")
                print("respuesta: la division de", str(int(A)), "/", str(int(B)), "es: ", str(int(A)/int(B)))
        elif opcion == 5:
                print("gracias por usar el sistema: ")
        else :
                print(menu)
        break