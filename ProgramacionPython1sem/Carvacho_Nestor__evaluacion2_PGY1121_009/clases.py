class vuelos:
    pasajes=0
    numero_vuelo = 0
    codigo_avion = ""
    ciudad_origen = ""
    ciudad_destino =""
    valor_vuelo = 0
    numero_pasajeros=0
    tipo_de_avion = ""
    registro_pasajeros =[]
        
    def __init__(self):
        self.numero_vuelo = 1
        self.codigo_avion = ""
        self.ciudad_origen = "NN"
        self.ciudad_destino ="NN"
        self.valor_vuelo = 4000
        self.numero_pasajeros=1
        self.tipo_de_avion = ""
        self.registro_pasajeros = []
    
    def setCodigoAvion(self,cod_avi):
        if len(cod_avi)==6:
            if (cod_avi[0:2].isalpha() and cod_avi[2:4].isdigit() and cod_avi[4:6].isalpha()) or (cod_avi[0:2].isdigit() and cod_avi[2:4].isalpha() and cod_avi[4:6].isdigit()):
                return True
            else:
                print("Formato Incorrecto")
                return False
        else:
            print("Largo Codigo Incorrecto")
            return False
    
    def setNumeroVuelo(self,num_vuelo):
        #if num_vuelo.isdigit():
        if ((num_vuelo)>=1 and (num_vuelo)<=5000):
                #self.setNumeroVuelo==num_vuelo
            return True
        else:
            print("Vuelo Incorrecto, Ingrese un valor entre 1 y 5000")
            return False
        #else:
            #print("Ingrese un valor entre 1 y 5000")
            #return False

    def setNumeroPasajeros(self,num_pasa):
        #if num_pasa.isdigit():
        if ((num_pasa)>=1 and (num_pasa)<=70):
                #self.setNumeroVuelo==num_pasa)
            return True
        else:
            print("Cantidad Incorrecta, Ingrese un valor entre 1 y 70")
            return False
        #else:
            #print("Ingrese un valor entre 1 y 70")
            #return False


    def setTipoAvion(self,tp_avion):
        if (tp_avion=="airbus 319" or tp_avion=="airbus 330" or tp_avion=="BOEING 737"or tp_avion=="BOEING 777"):
            #self.setNumeroVuelo==num_pasa)
            return True
        else:
            print("Avion Incorrecto, Ingrese AIRBUS 319//AIRBUS 330//BOEING 737//BOEING 777")
            return False
    
    def setValorVuelo(self,vlr_vuelo):
        if len(vlr_vuelo)==7 and len(vlr_vuelo)<7:
            return True
        else:
            print("Valor No Puede Superar las 7 cifras")
    
    
    def addDatosPasajeros(self):
        nomb_pasa=input("Ingrese Nombre de pasajeros")
        asie_pasa=int(input("ingrese Asiento Pasajero"))
        for i in self:
            if i<=self.numero_pasajeros:
                self.registro_pasajeros.append(nomb_pasa)
                self.registro_pasajeros.append(asie_pasa)
                print=("¿Desea Agregar otro Pasajero?")
                op2=int("1)SI  // 2)NO")
                if op2==1:
                    pasajes=pasajes+1
                    return False
                if op2==2:
                    return True

