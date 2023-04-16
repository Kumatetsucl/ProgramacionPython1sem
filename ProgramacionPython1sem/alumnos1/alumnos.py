from alumnos_ent import *

alumnos_list =[]
flag=True
while(flag):
    print("\tINGRESO DE ALUMNOS\n")
    alumn=alumnos()
    alumn.rut=input("ingrese RUT: ")
    alumn.nombre=input("ingrese Nombre: ")
    alumn.apellido=input("ingrese Apellido: ")
    alumn.edad=int(input("ingrese Edad: "))

    alumnos_list.append(alumnos)
    agregar=int(input("\n¿Desea agregar otra Alumno? (1.-SI 2.-NO)"))
    if agregar==2:
        flag=False
    print("\tLISTA ALUMNOS\n")
    for x in alumnos_list:
        print("rut alumno: ", x.rut)
        print("Nombre alumno: ", x.nombre, x.apellido)
        print("Edad Alumno: ", x.edad)
    
    print("\tBUSCAR ALUMNO\n")
    buscar_alumno=input("buscar Alumno: ")
    for x in alumnos_list:
        if x.nombre==buscar_alumno:
            print("rut alumno: ", x.rut)
            print("Nombre alumno: ", x.nombre, x.apellido)
            print("Edad Alumno: ", x.edad)