import numpy as np
#import random as rn
from funciones import *

matriz_auto=np.full((40,7),'                ')
indice=0

ciclo=True
while(ciclo):
    print("\t\t\t MENU PRINCIPAL\n1)Guardar Datos de Vehiculos\n2)Buscar Vehiculo\n3)Mostrar Todos los vehiculos\n4)Certificados\n5)Salir")
    try:
        opcion=int(input("ingrese opcion: "))
        if opcion ==1:
            guardar_vehiculo(matriz_auto,indice)
            indice=indice+1
        if opcion ==2:
            vehiculo=input("Ingrese vehiculo a Buscar")
            buscar_vehiculo(matriz_auto,vehiculo)
        if opcion ==3:
            mostrar(matriz_auto)
        if opcion ==4:
            print("\t\t\t CERTIFICADOS")
            print("1)Certificado de Emision de contaminante\n2)Anotaciones Vigentes\n3)Mulas")
            op=int(input("Ingrese Opcion: "))
            if op==1:
                emision_contaminante=input("ingrese Vehiculo")
                certificado_contamiante(matriz_auto,emision_contaminante)
            if op==2:
                anotaciones=input("Ingrese Vehiculo")
                certificado_anotaciones(matriz_auto,anotaciones)
            if op==3:
                multa=input("Ingrese Vehiculo")
                certificado_multa(matriz_auto,multa)
        if opcion==5:
            print("Gracias por usar el sistema, VER.1.0, by Nestor Carvacho")
            ciclo=False
    except BaseException as error:
        print("error:", error)