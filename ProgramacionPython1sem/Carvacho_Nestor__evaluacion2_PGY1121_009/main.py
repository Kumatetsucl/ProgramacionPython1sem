from clases import vuelos
import os
lista=[]

def show(lista):
    ciclo=False
    print("\tConsultar Vuelo")
    fnd_numVuelo=int(input("Ingrese Numero de Vuelo: "))
    for x in lista:
        if x.numero_vuelo==fnd_numVuelo:
            print("")
            print("Numero Vuelo: ",x.numero_vuelo)
            print("Cantidad de Pasajes: ",x.pasajes)
            print("Codigo Avion: ",x.codigo_avion)
            print("Ciudad de Origen: ",x.ciudad_origen)
            print("Ciudad de Destino: ",x.ciudad_destino)
            print("Valor Vuelo: ",x.valor_vuelo)
            print("Cantidad de pasajeros: ",x.numero_pasajeros)
            print("Tipo de AVion: ",x.tipo_de_avion)
            print("Lista de Pasajeros: ",x.registro_pasajeros)

def modificar(lista):
    #ciclo=False
    print("\tIngreso de Pasajeros")
    fnd_numVuelo=input("Ingrese Numero de Vuelo: ")
    for x in lista:
        if x.numero_vuelo==fnd_numVuelo:
            x.addDatosPasajeros()
    print("Pasajero Agregado\n")

            

def create():
    ciclo=False
    print("\tIngresar Vuelo")
    avion=vuelos()
    while ciclo==False:
        cod_avi=input("Ingrese Codigo de Avion: ")
        ciclo=avion.setCodigoAvion(cod_avi)
        print("Codigo de Avion Agregado\n")
    ciclo=False
    while ciclo==False:
        num_vuelo=int(input("Ingrese Numero de Vuelo: "))
        ciclo=avion.setNumeroVuelo(num_vuelo)
        print("Numero de Vuelo Agregado\n")
    ciclo=False
    while ciclo==False:
        num_pasa=int(input("ingrese Numero de Pasajeros: "))
        ciclo=avion.setNumeroPasajeros(num_pasa)
        print("Cantidad de pasajeros Agregada\n")
    ciclo=False
    while ciclo==False:
        tp_avion=input("Ingrese Tipo de Avion (use minusculas): ")
        ciclo=avion.setTipoAvion(tp_avion)
        print("Tipo de Avion Agregada\n")
    ciclo=False
    while ciclo==False:
        vlr_vuelo=input("Ingrese Valor del Vuelo: ")
        ciclo=avion.setValorVuelo(vlr_vuelo)
        print("Valor de Vuelo Agregado\n")
    origen=input("ingrese Cuidad de Origen: ")
    destino=input("ingrese Destino: ")
    avion.codigo_avion=cod_avi
    avion.numero_vuelo=num_vuelo
    avion.numero_pasajeros=num_pasa
    avion.tipo_de_avion=tp_avion
    avion.valor_vuelo=vlr_vuelo
    avion.ciudad_origen=origen
    avion.ciudad_destino=destino
    lista.append(avion)
    print("\tVuelo Agregado Correctamente\n\n")

def menu():
    ciclo=False
    while ciclo==False:
        print("\tMenu Principal\n")
        try:
            print("1)Ingresar Vuelo\n2)Ingreso de Pasajeros\n3)Consultar Vuelo\n4)Salir")
            op=int(input("ingrese opcion: "))
            if op==1:
                create()
            if op==2:
                modificar(lista)
            if op==3:
                show(lista)
            if op==4:
                ciclo=True 
        except BaseException as error:
            print("opcion incorrecta", error)
            ciclo=False

if __name__=="__main__":
    os.system("cls")
    menu()
    print("Gracias por Usar")