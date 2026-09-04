import sys
import pygame
ancho=800
alto=700
pygame.init()
pantalla=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Space Invaders")
tamaño=2
reloj=pygame.time.Clock()
titulo=pygame.font.SysFont("Arial",50)
estado="menu"
texto_titulo=titulo.render("SPACE INVADERS",True,(255,255,255))
fuente=pygame.font.SysFont("Arial",30)
texto_fuente=fuente.render("Pulsa Space para entrar al juego",True,(255,255,255))
estrellas=[(100,200),(5,5),(400,500),(600,700),(482, 315),(124, 642),(739, 88),(311, 583),(605, 214),(160, 482),(231, 319),(703, 315),(589, 669),(397, 352),(694, 617),(730, 607),(513, 548),(103, 460),(71, 352),(380, 143),(503, 317),(370, 593),(231, 587),(176, 267),(722, 520),(46, 331),(694, 189),(305, 393),(466, 557),(361, 28),(109, 149),(16, 412),(46, 480),(413, 20),(105, 502),(613, 649),(441, 108),(697, 517),(317, 156),(63, 319),(244, 211),(214, 347),(103, 330),(650, 66),(338, 566),(230, 380),(627, 254),(15, 156),(277, 113),(671, 232),(195, 190),(758, 32),(380, 626),(195, 202),(254, 105)]
jugador_x=100
jugador_y=650
cañon_x=750
cañon_y=630
velocidad_y=0
impulso=-20
gravedad=1
en_el_suelo=True
tamaño_cañon=50
puntos=0
vidas=3
obstaculo1_x=200
obstaculo1_y=650
obstaculo2_x=500
obstaculo2_y=650
balas=[]
ultimo_disparo=0
obstaculo1_superado=False
obstaculo2_superado=False
puntos_sumados=False
while True:
    pantalla.fill((0,0,0)) 
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if estado=="menu":
        pantalla.blit(texto_titulo,(200,300))
        pantalla.blit(texto_fuente,(200,500))
        for i in estrellas:
            pygame.draw.circle(pantalla,(255,255,255),i,tamaño,tamaño)
    tecla=pygame.key.get_pressed()
    if tecla[pygame.K_SPACE]:
        estado="jugando"
    if estado=="jugando":
        rect_jugador=pygame.draw.rect(pantalla,(255,0,0),(jugador_x,jugador_y-5,40,100))
        tiempo=pygame.time.get_ticks()
        if tiempo-ultimo_disparo>=3000:
            ultimo_disparo=tiempo
            nueva_bala=pygame.Rect(cañon_x,cañon_y,10,10)
            balas.append(nueva_bala)
        for bala in balas:
            bala.x-=15
            pygame.draw.rect(pantalla,(0,255,0),bala)
            if rect_jugador.colliderect(bala):
                jugador_x=10
                jugador_y=650
                balas.remove(bala)
                vidas-=1
            elif bala.x<0:
                balas.remove(bala)
                puntos+=1
        if vidas==0:
            print("GAME OVER")
            print("Puntos:",puntos) 
            pygame.quit()
            sys.exit()
        puntos_marcador=pygame.font.SysFont("Arial",30)
        texto_puntos=puntos_marcador.render(f"Puntos:{puntos}",True,(255,255,255))
        vidas_marcador=pygame.font.SysFont("Arial",30)
        texto_vidas=vidas_marcador.render(f"Vidas:{vidas}",True,(255,255,255))
        pantalla.blit(texto_puntos,(10,10))
        pantalla.blit(texto_vidas,(10,50))             
            
        if tecla[pygame.K_LEFT] and jugador_x>0:
            jugador_x-=10
        if tecla[pygame.K_RIGHT] and jugador_x<750:
            jugador_x+=10
        if tecla[pygame.K_SPACE] and en_el_suelo:
            velocidad_y=impulso
            en_el_suelo=False
        velocidad_y+=gravedad
        jugador_y+=velocidad_y 
        if jugador_y>=650:
            jugador_y=650
            en_el_suelo=True
            velocidad_y=0  
        rect_cañon=pygame.draw.rect(pantalla,(0,255,0),(cañon_x,cañon_y,60,10000))
        rect_obstaculo1=pygame.Rect(obstaculo1_x,obstaculo1_y,50,300)
        rect_obstaculo2=pygame.Rect(obstaculo2_x,obstaculo2_y,50,300)
        if jugador_x+40>=obstaculo1_x and jugador_x<=obstaculo1_x+40 and rect_jugador.colliderect(rect_obstaculo1):
            jugador_y=obstaculo1_y-100
            en_el_suelo=True
            velocidad_y=0
        if jugador_x>250 and not puntos_sumados:
            puntos+=2
            obstaculo1_superado=True
            puntos_sumados=True
        if jugador_x>550 and not puntos_sumados:
            puntos+=2
            obstaculo2_superado=True
            puntos_sumados=True
        if jugador_x+40>=obstaculo2_x and jugador_x<=obstaculo2_x+40 and rect_jugador.colliderect(rect_obstaculo2):
            jugador_y=obstaculo2_y-100
            en_el_suelo=True
            velocidad_y=0
        if rect_jugador.colliderect(rect_cañon):
            jugador_x-=3
            jugador_x=740    
        pygame.draw.rect(pantalla,(255,165,0),rect_obstaculo1)
        pygame.draw.rect(pantalla,(0,0,255),rect_obstaculo2)          
    pygame.display.flip()
    reloj.tick(60)  
                        
        
    
    
               


        
            
           
    
    
                    
                                  