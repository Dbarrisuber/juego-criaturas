import pygame
import sys
import random
pygame.init()
ancho=900
alto=800
jugador_x=500
jugador_y=750
frutas=[ (102, 392),(435, 206),(270, 14),(106, 553),(71, 460),(700, 690),(20, 574),(614, 240),(121, 563),(466, 95),(214, 484),(330, 406),(458, 230),(87, 654), (372, 170)]

tamaño_fruta=30
tamaño=50
gravedad=1
fuente=pygame.font.SysFont("Arial",30)
puntos=0


en_el_suelo=True
impulso=-20
velocidad=0
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego de frutas del bosque")
reloj=pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    teclas=pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x>0:
        jugador_x-=10  
    if teclas[pygame.K_RIGHT] and jugador_x<ancho-tamaño:
        jugador_x+=10
    if teclas[pygame.K_SPACE] and en_el_suelo:
        en_el_suelo=False
        velocidad=impulso
    velocidad+=gravedad
    jugador_y+=velocidad
    if jugador_y>=750:
        jugador_y=750
        en_el_suelo=True
    rect_jugador=pygame.Rect(jugador_x,jugador_y,tamaño,tamaño)
    ventana.fill((6, 64, 43))
    for x,y in frutas:
        rect_fruta=pygame.Rect(x,y,tamaño,tamaño)
        pygame.draw.rect(ventana,(0,255,0),rect_fruta)
        if rect_jugador.colliderect(rect_fruta):
            puntos+=1
            frutas.remove((x,y))
            break
    marcador=fuente.render(f"Puntos:{puntos}",True,(255,255,255))
            
    pygame.draw.rect(ventana,(255,255,255),rect_jugador)
    ventana.blit(marcador,(10,10))
    pygame.display.flip()
    reloj.tick(60)    
    
    
    
        
            
          
                      