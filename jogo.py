import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
from pygame.locals import *
from sys import exit

pygame.init() 

largura = 840
altura = 680

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Vôlei ')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #pygame.draw.rect(tela, (255,0,0), (200,300,40,50))  
    #pygame.draw.circle(tela, (0,255,0), (300,250), 40)  
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)    
    pygame.display.update()        