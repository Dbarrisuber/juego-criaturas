import random
print("Juego de Criaturas y combate")
class Jugador:
    vida=100
    daño=60
    cura=10
    def atacar(self,objetivo):
        objetivo.vida-=self.daño
        objetivo.vida=max(0,objetivo.vida)
        print(f"La  vida del enemigo es de {objetivo.vida}")
    def curacion(self):
        self.vida+=self.cura
        print(f"Tu vida es de {self.vida}")
class Zombie:
    vida=200
    daño=50
    def atacar(self,objetivo):
        objetivo.vida-=self.daño
        objetivo.vida=max(0,objetivo.vida)
        print(f"La vida del Zombie es de {objetivo.vida}")
class Payaso:
    vida=300
    daño=40
    def atacar(self,objetivo):
        objetivo.vida-=self.daño
        objetivo.vida=max(0,objetivo.vida)
        print(f"La vida del Payaso es de {objetivo.vida}")
class Dragon:
    vida=400
    daño=30
    def atacar(self,objetivo):
        objetivo.vida-=self.daño
        objetivo.vida=max(0,objetivo.vida)
        print(f"La vida del Dragon es de {objetivo.vida}")
class Ogro:
    vida=500
    daño=20
    def atacar(self,objetivo):
        objetivo.vida-=self.daño
        objetivo.vida=max(0,objetivo.vida)
        print(f"La vida del Ogro es de {objetivo.vida}")
while True:        
    eleccion=int(input("Escoge 1 para mostrar equipo y estadísticas\nEscoge 2 para crear enemigo aleatorio y luchar contra él\nEscoge 3 para salir:"))
    mi_Jugador=Jugador()
    mi_Zombie=Zombie()
    mi_Payaso=Payaso()
    mi_Dragon=Dragon()
    mi_Ogro=Ogro()
    criaturas=[mi_Jugador,mi_Zombie,mi_Payaso,mi_Dragon,mi_Ogro] 
    if eleccion==1:
        for i in criaturas:
            print(f"Nombre:{i.__class__.__name__}")
            print(f"Vida:{i.vida}")
            print(f"Daño:{i.daño}")
    if eleccion==2:
        criaturas_seleccion=random.randint(0,3)
        if criaturas_seleccion==0:
            print("Que comience el combate contra el Zombie")
            while mi_Jugador.vida>0 and mi_Zombie.vida>0:
                mi_Jugador.atacar(mi_Zombie)
                mi_Zombie.atacar(mi_Jugador)
                mi_Jugador.curacion()
                if mi_Zombie.vida<=0:
                    print("Ganaste el combate")
                elif mi_Jugador.vida<=0:
                    print("Perdiste el combate")
        elif criaturas_seleccion==1:
            print("Que comience el combate contra el Payaso")
            while mi_Jugador.vida>0 and mi_Payaso.vida>0:
                mi_Jugador.atacar(mi_Payaso)
                mi_Payaso.atacar(mi_Jugador)
                mi_Jugador.curacion()
                if mi_Payaso.vida<=0:
                    print("Ganaste el combate")
                elif mi_Jugador.vida<=0:
                    print("Perdiste el combate") 
        elif criaturas_seleccion==2:
            print("Que comience el combate contra el Dragon")
            while mi_Jugador.vida>0 and mi_Dragon.vida>0:
                mi_Jugador.atacar(mi_Dragon) 
                mi_Dragon.atacar(mi_Jugador)
                mi_Jugador.curacion()
                if mi_Dragon.vida<=0:
                    print("Ganaste el combate")
                elif mi_Jugador.vida<=0:
                    print("Perdiste el combate")
        elif criaturas_seleccion==3:
            print("Que comience el combate contra el Ogro")
            while mi_Jugador.vida>0 and mi_Ogro.vida>0:
                mi_Jugador.atacar(mi_Ogro) 
                mi_Ogro.atacar(mi_Jugador)
                mi_Jugador.curacion()
                if mi_Ogro.vida<=0:
                    print("Ganaste el combate")
                elif mi_Jugador.vida<=0:
                    print("Perdiste el combate")
    if eleccion==3:
        break
    if eleccion>3 or eleccion<1:
        print("Error la opción que escogiste no existe")            
                                     
            
                
            
            
    
        
    
    

                    
    
    