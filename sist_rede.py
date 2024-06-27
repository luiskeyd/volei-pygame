import pygame
import sist_bola
import sist_players
import sprites
import constantes



class Rede(pygame.sprite.Sprite):

    def __init__(self, cor, largura, altura, posicao):
       super().__init__()
       self.image = pygame.Surface([largura, altura])
       self.image.fill(cor)
       self.rect = self.image.get_rect()
       self.rect.x, self.rect.y = posicao