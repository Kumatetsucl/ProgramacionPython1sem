import random as rn
from re import S

#Mostrar datos del vehiculo
def mostrar(matriz_auto):
    for f in range (40):
        fila=""
        for c in range(7):
            fila=fila+"|"+str(matriz_auto[f][c])
    print(matriz_auto)

#Guardar datos del vehiculo
def guardar_vehiculo(matriz_auto,indice):
    tipo_auto=input("ingrese tipo vehiculo: ")
    patente_auto=valida_patente()
    marca_auto=input("ingrese marca vehiculo: ")
    precio_auto=valida_precio()
    multa_auto=input("ingrese Valor de Multa: ")
    registro_auto=input("Ingrese Fecha del registro del Vehiculo: ")
    dueno_auto=input("ingrese Nombre del dueno del vehiculo: ")
    matriz_auto[indice][0]=tipo_auto
    matriz_auto[indice][1]=patente_auto
    matriz_auto[indice][2]=marca_auto
    matriz_auto[indice][3]=precio_auto
    matriz_auto[indice][4]=multa_auto
    matriz_auto[indice][5]=registro_auto
    matriz_auto[indice][6]=dueno_auto

#buscar datos del vehiculo
def buscar_vehiculo(matriz_auto,vehiculo):
    switch=False
    for f in range (40):
        if matriz_auto[f][1]==vehiculo:
            switch=True
            print("tipo de vehiculo: ",matriz_auto[f][0])
            print("patente vehiculo: ",matriz_auto[f][1])
            print("marca vehiculo: ",matriz_auto[f][2])
            print("precio vehiculo: ",matriz_auto[f][3])
            print("multa vehiculo: ",matriz_auto[f][4])
            print("fecha registro vehiculo: ",matriz_auto[f][5])
            print("dueno vehiculo: ",matriz_auto[f][6])
    if switch==False:
        print("no se encontró vehiculo")

#impresion de Certificados
def certificado_contamiante(matriz_auto,emision_contaminante):
    nro_certificado=rn.randint(1500,3500)
    switch=False
    for f in range (40):
        if matriz_auto[f][1]==emision_contaminante:
            switch=True
            fila=""
            fila=fila+"|"+str(matriz_auto[f][0])
            fila=fila+"|"+str(matriz_auto[f][1])
            fila=fila+"|"+str(matriz_auto[f][2])
            fila=fila+"|"+str(matriz_auto[f][3])
            fila=fila+"|"+str(matriz_auto[f][4])
            fila=fila+"|"+str(matriz_auto[f][5])
            fila=fila+"|"+str(matriz_auto[f][6])
            print(fila)
    if switch==False:
        print("no se encontro vehiculo")
    else:
        print("Certificado Contaminante : $",nro_certificado)

def certificado_anotaciones(matriz_auto,anotaciones):
    nro_certificado=rn.randint(1500,3500)
    switch=False
    for f in range (40):
        if matriz_auto[f][1]==anotaciones:
            switch=True
            fila=""
            fila=fila+"|"+str(matriz_auto[f][0])
            fila=fila+"|"+str(matriz_auto[f][1])
            fila=fila+"|"+str(matriz_auto[f][2])
            fila=fila+"|"+str(matriz_auto[f][3])
            fila=fila+"|"+str(matriz_auto[f][4])
            fila=fila+"|"+str(matriz_auto[f][5])
            fila=fila+"|"+str(matriz_auto[f][6])
            print(fila)
    if switch==False:
        print("no se encontro vehiculo")
    else:
        print("Certificado anotaciones : $",nro_certificado)

def certificado_multa(matriz_auto,multa):
    nro_certificado=rn.randint(1500,3500)
    switch=False
    for f in range (40):
        if matriz_auto[f][1]==multa:
            switch=True
            fila=""
            fila=fila+"|"+str(matriz_auto[f][0])
            fila=fila+"|"+str(matriz_auto[f][1])
            fila=fila+"|"+str(matriz_auto[f][2])
            fila=fila+"|"+str(matriz_auto[f][3])
            fila=fila+"|"+str(matriz_auto[f][4])
            fila=fila+"|"+str(matriz_auto[f][5])
            fila=fila+"|"+str(matriz_auto[f][6])
            print(fila)
    if switch==False:
        print("no se encontro vehiculo")
    else:
        print("Certificado multas : $",nro_certificado)

#validaciones
def valida_patente():
    flag=True
    while(flag):
        ppu=input("ingrese Patente: ")
        if len(ppu)==6:
            if (ppu[0:2].isdigit()) and (ppu[2:6].isalpha()):
                return ppu
            if (ppu[0:4].isalpha()) and (ppu[4:6].isdigit()):
                return ppu
        else:
            print("formato Patente invalido")

def valida_precio():
    flag=True
    while(flag):
        try:
            precio=int(input("ingrese precio del Vehiculo: "))
            if precio>=(5000000):
                return precio
            else:
                print("Precio debe ser mayor o igual a $5.000.000")
        except:
            print("ingrese Valor Numerico")
