registro_paciente = []
diccionario={}
paciente = []
opcion = 0
while (opcion != 4):
    try:
        print("Centro Médico DUOC\n1)Registrar Paciente\n2)Atención Paciente\n3)Consultar Datos Paciente\n4)Salir")
        opcion = int(input("Seleccione (1-4): "))
        if (opcion == 1):

              #ingreso de rut
                digitos = 0
                while (digitos < 7 or digitos > 8):
                    try:
                        rut = int(input("Ingrese Rut (sin dígito verificador ni puntos): "))
                        #Validacion de la cantidad de digitos del rut
                        #len(str()) Convierte la variable en texto, y cuenta la cantidad de caracteres que posee
                        digitos = len(str(rut))
                        if (digitos < 7 or digitos > 8):
                            print("Error: Ingrese un rut válido (Entre 7 y 8 dígitos)")
                    except:
                        print("Error: Ingrese un rut válido (Sin dígito verificador ni puntos")
                paciente.append(rut)
                

                #ingreso de nombres
                nombres = input("Ingrese Nombres: ")
                paciente.append(nombres)

                #ingreso de apellidos
                apellidos = input("Ingrese Apellidos: ")
                paciente.append(apellidos)

                #ingreso de direccion
                direccion = input("Ingrese Dirección: ")
                paciente.append(direccion)

                #ingreso de correo
                # .count cuenta los caracteres señalados de una variable
                correo = '0'
                while (correo.count('@') < 1 or correo.count('@') > 1):
                    correo = input ("Ingrese correo electrónico: ")
                    if (correo.count('@') < 1 or correo.count('@') > 1):
                        print("Error: Ingrese una dirección de correo electrónico válida (con solo 1 '@')")
                paciente.append(correo)

                #ingreso de edad
                edad = 0
                while (edad < 0 or edad > 110):
                    try:
                        edad = int(input("Ingrese Edad (con numeros): "))
                        if (edad < 0 or edad > 110):
                            print("Error: Ingrese una edad válida (Entre 0 y 110)")
                    except:
                        print("Error: Ingrese una edad válida (En dígitos)")
                paciente.append(edad)
                #ingreso de sexo
                sexo = "0"
                while (sexo != "F" and sexo != "M"):
                    sexo = input("Ingrese Sexo (F o M): ")
                    if (sexo != "F" and sexo != "M"):
                        print("Error: Ingrese un sexo válido (F o M)")

                paciente.append(sexo)

                #ingreso de registros
                registros = input("Ingrese Registros: ")
                paciente.append(registros)

                #Ingreso de plan de salud
                ps = "0"
                while (ps != 'Isapre' and ps != 'Fonasa'):
                    ps = input("Ingrese Plan de Salud (Isapre o Fonasa): ")
                    if (ps != 'Isapre' and ps != 'Fonasa'):
                        print("Error: Ingrese un Plan de Salud válido (Isapre o Fonasa)")
                paciente.append(ps)   

                print(paciente)
                print(f"Rut: {paciente[0]}")
                print(f"Nombres: {paciente[1]}")
                print(f"Apellidos: {paciente[2]}")
                print(f"Direccion: {paciente[3]}")
                print(f"Correo: {paciente[4]}")
                print(f"Edad: {paciente[5]}")
                print(f"Sexo: {paciente[6]}")
                print(f"Registros: {paciente[7]}")
                print(f"PS: {paciente[8]}")

        elif (opcion == 2):
            print("atencion")
        elif (opcion == 3):
            print("mostrar datos", paciente)
        elif (opcion == 4):
            print("Ha salido del sistema")
        else:
            print("Error: Ingrese una opción válida (1-4)")      
    except:
        print("Error: Ingrese una opción válida (1-4)")