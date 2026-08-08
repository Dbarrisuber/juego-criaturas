import random
presupuesto=200
criaturas=["Dragón","Fénix","Goblin","Lobo","Golem"]
precios=[100,200,500,300,400]
mis_criaturas=[]
def mostrar_criaturas():
    for i in range(len(criaturas)):
        print(criaturas[i],"cuesta:",precios[i])
def combatir():
    ataque=random.randint(0,1)
    global presupuesto
    if ataque<0.6:
        print("Has ganado y sumas 600 al presupuesto") 
        presupuesto+=600
    else:
        print("Has perdido y pierdes 300 de tu presupuesto")
        presupuesto-=300
def comprar_criatura(indice):
    global presupuesto
    if precios[indice]>presupuesto:
        print("No tienes presupuesto para realizar esta compra")
    else:
        presupuesto-=precios[indice]
        mis_criaturas.append(criaturas[indice])
        criaturas.remove(criaturas[indice])
        print("Fichaje realizado con éxito")
while True:
    opcion=int(input("Escoge 1 para ver criaturas en venta\nEscoge 2 para comprar una criatura\nEscoge 3 para ir a combatir y ganar monedas\nEscoge 4 para ver tus criaturas capturadas\nEscoge 5 para salir:"))
    if opcion==1:
        mostrar_criaturas()
    if opcion==2:
        indice=int(input("Que criatura desea comprar??:")) 
        comprar_criatura(indice) 
    if opcion==3:
        combatir()
    if opcion==4:
        print("Criaturas capturadas:",mis_criaturas)
    if opcion==5:
        break              
              
                       
        
    
    
               


        
            
           
    
    
                    
                                  