import pygame
import constantes
import sprites
import os
import sist_players



class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = (pygame.image.load(sprites.BOLA))
        self.image = self.sprite
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect= self.image.get_rect()
        self.rect.midtop = (constantes.LARGURA//2, 250)
    
    def movimento_bola(self):
        oi_tudo_bem = 8