# ejecutar el inicio de sesion
def inicio_sesion(u,c):
    usuario = input("Usuario:")
    contrasena = input("Contraseña:")
    # recorrer los usuarios
    pos = 0
    for x in u:
        if(x==usuario):
            print("encontro el usuario, pos",pos)
        pos = pos + 1
            
# permite registrar un usuario en la lista
def registro_usuarios(u,c):
    usuario = input("ingrese nombre de usuario:")
    contrasena = input("ingrese contrasena:")
    u.append(usuario)
    c.append(contrasena)

# lista Usuarios y Contraseñas
def listar(u,c):
    for x in u:
        print(f"El Usuario es:{x}")
    for i in c:
        print(f"La Contraseña es:{i}")

# determina que camino seguir dependiendo de la OPCION
def opciones(opcion,u,c):
    if(opcion==1):
        inicio_sesion(u,c)
    if(opcion==2):
        registro_usuarios(u,c)
    if(opcion==3):        
        listar(u,c)

# opciones del menu
def menu():
    opcion = 1
    # tenemos 2 listas, una para almacenar Usuarios y otra Contraseñas
    usuarios = []
    contrasenas = []
    # si la opcion es 4 sale
    while (opcion!=4):
        print("Menu Principal")
        print("--------------")
        print("1) Iniciar Sesion")
        print("2) Registrar Usuario")
        print("3) Listar")
        print("4) Salir")
        try:
            opcion = int(input("Seleccione (1-3):"))
            if(opcion<1 or opcion>4):
                print("selecciono un numero incorrecto")
            else:
                opciones(opcion,usuarios,contrasenas)
        except:
            print("ingreso un dato incorrecto")


# establece el punto de partida de una aplicacion en PYTHON
if __name__ =='__main__':
    menu()
    print("Fin de la Aplicacion")