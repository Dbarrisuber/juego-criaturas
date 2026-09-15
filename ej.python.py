class Jugador:
    def __init__(self,nombre,posicion,goles):
        self.nombre=nombre
        self.posicion=posicion
        self.goles=goles
    def marcarGol(self):
        self.goles+=1
class Plantilla:
    def __init__(self):
        self.portero=[]
        self.defensa=[]
        self.centrocampista=[]
        self.delantero=[]
    def fichar(self,Jugador):
        if Jugador.posicion=="portero":
            self.portero.append(Jugador)
        elif Jugador.posicion=="defensa":
            self.defensa.append(Jugador)
        elif Jugador.posicion=="centrocampista":
            self.centrocampista.append(Jugador)
        elif Jugador.posicion=="delantero":
            self.delantero.append(Jugador)
    def mostrar_plantilla(self):
        for i in self.portero:
            print(f"Nombre:{i.nombre}| Posicion: {i.posicion} | Goles:{i.goles}")
        for i in self.defensa:
            print(f"Nombre:{i.nombre} | Posicion: {i.posicion} | Goles: {i.goles}")
        for i in self.centrocampista:
            print(f"Nombre:{i.nombre} | Posicion: {i.posicion} | Goles: {i.goles}")
        for i in self.delantero:
            print(f"Nombre:{i.nombre} | Posicion: {i.posicion} | Goles: {i.goles}")
    def vender(self,Jugador):
        if Jugador.posicion=="portero":
            self.portero.remove(Jugador)
        elif Jugador.posicion=="defensa":
            self.defensa.remove(Jugador)
        elif Jugador.posicion=="centrocampista":
            self.centrocampista.remove(Jugador)
        elif Jugador.posicion=="delantero":
            self.delantero.remove(Jugador) 
mi_Jugador=Jugador("Courtois","portero",0) 
mi_Jugador2=Jugador("Neuer","portero",0)
mi_Jugador3=Jugador("Sergio Ramos","defensa",5)
mi_Jugador4=Jugador("Beckenbauer","defensa",10) 
mi_Jugador5=Jugador("Modric","centrocampista",15)
mi_Jugador6=Jugador("Cruyff","centrocampista",20)
mi_Jugador7=Jugador("Cristiano Ronaldo","delantero",50)
mi_Jugador8=Jugador("Messi","delantero",60)
mi_plantilla=Plantilla()
mercado=[]
mercado.append(mi_Jugador)
mercado.append(mi_Jugador2)
mercado.append(mi_Jugador3)
mercado.append(mi_Jugador4)
mercado.append(mi_Jugador5)
mercado.append(mi_Jugador6)
mercado.append(mi_Jugador7)
mercado.append(mi_Jugador8)
while True:
    eleccion=int(input("Escoge 1 para ver la plantilla\nEscoge 2 para fichar\nEscoge 3 para vender\nEscoge 4 para ver estadísticas\nEscoge 5 para salir:"))
    if eleccion==1:
       mi_plantilla.mostrar_plantilla()
    elif eleccion==2:  
        for indice,Jugador in enumerate(mercado):
            print(f"[{indice}] {Jugador.nombre} {Jugador.posicion} | Goles:{Jugador.goles}")    
            eleccion_mercado=int(input("Escribe el numero de la posicion del mercado del jugador que desea fichar:"))-1 
            Jugador_elegido=mercado[eleccion_mercado]
            mi_plantilla.fichar(Jugador_elegido)
            mercado.remove(Jugador_elegido)
    if eleccion==3: 
        posicion=str(input("Elige que posición desea vender:"))
        if posicion=="portero":
            indice=int(input("Elige con un numero que portero desea vender:"))
            mi_plantilla.portero.remove(indice)
            mercado.append(indice)
        elif posicion=="defensa":
            indice=int(input("Elige con un numero que defensa desea vender:"))
            mi_plantilla.defensa.remove(indice)
            mercado.append(indice)
        elif posicion=="centrocampista":
                indice=int(input("Elige con un numero que centrocampista desea vender:"))
                mi_plantilla.centrocampista.remove(indice) 
                mercado.append(indice)
        elif posicion=="delantero":
            indice=int(input("Elige con un numero que delantero desea vender:"))
            mi_plantilla.delantero.remove(indice)
            mercado.append(indice)
    if eleccion==4:
        goles_totales=0
        for i in mi_plantilla.portero:
            goles_totales+=i.goles
        for i in mi_plantilla.defensa:
            goles_totales+=i.goles
        for i in mi_plantilla.centrocampista:
            goles_totales+=i.goles
        for i in mi_plantilla.delantero:
            goles_totales+=i.goles
        print(f"El total de goles de la plantilla es:{goles_totales}")
    if eleccion==5:
        break        
                   
               
        
    
    
      
    
    
    
        


    

    
    


             
                    
                        
                        
                
      
                  
            
    

    


