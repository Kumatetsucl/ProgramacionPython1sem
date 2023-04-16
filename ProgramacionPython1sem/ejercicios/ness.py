import os
from re import U


    
def inicio_sesion(U,C):
    print("\n \t INICIO SESION")
    usu=input("Usuario: ")
    contra=input("Contraseña: ")
    pos=0
    for x in U:
        if(x==usu):
            if(C[pos]==contra):
                print("\n \tinicio se sesion exitoso")
            pos=pos+1
    menu2(U,C)
                       
def registro_usuario(U,C):
    print("\n \t REGISTRO USUARIO")
    usuario=input("ingrese usuario: ")
    contrasenia=input("ingrese contraseña: ")
    U.append(usuario)
    C.append(contrasenia)


def listar(U, C):
    for x in U:
        print(f"usuario",x)
    for i in C:
        print(f"contraseña",i)
        
def menu2(U,C):
    subciclo=True
    while subciclo:
        print("\n\tMenu Usuario\n1.- Realizar llamada\n2.- Enviar Correo\n3.- Salir")
        try:
            op2=int(input("\n Seleccione (1-3): "))
            if(op2<1 or op2>3):
                print("seleccionó numero incorrecto")
            else:
                if op2==3:
                    subciclo=False
                    menu1()
                if op2==2:
                    correo=input("correo: ")
                    for letra in correo:
                        existe=False
                        if letra=="@":
                            existe==True
                            esc_correo=input("\nEscriba su correo: ")
                            print ("Desea enviar ", esc_correo,)
                            op3=int(input("1)SI\n2)NO\n"))
                            if(op3>1):
                                print("\nborrando correo....")
                            else:
                                print("\nenviando correo ....")
                        else:
                            existe=False
                if op2==1:
                    numero=input("ingrese numero: ")
                    if numero.isdigit():
                        if numero[0]=="9":
                            if len(numero)==9:
                                print("\nLlamando a Nasa...")
                            else:
                                print("formato incorrecto")                         
                        else:
                            print("numero incorrecto")
                    else:
                        print("\nNumero Incorrecto")
        except:
            print("opcion incorrecta")
def menu1():
    usuarios=[]
    contrasenias=[]
    ciclo=True
    sw=False
    subciclo=False
    while ciclo:
        print("\n\tmenu principal\n1.- Iniciar sesion\n2.- Registrar Usuario \n3.- Salir")
        try:
            op=int(input("seleccione (1-3): "))
            if(op<1 or op>4):
                print("seleccionó numero incorrecto")
            else:   
                if op==3:
                    ciclo=False
                if op==2:
                    sw=True
                    registro_usuario(usuarios, contrasenias)
                if op==1:
                    sw=True
                    inicio_sesion(usuarios, contrasenias)
                if op==4:
                    listar(usuarios, contrasenias)
        except:
            print("ingresó un valor que no corresponde")



if __name__ == "__main__":
    os.system("cls")
    menu1()
    os.system("cls")
    print("Gracias por usar el sistema")