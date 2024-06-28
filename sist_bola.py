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
        self.gravidade = constantes.Y_GRAVIDADE
        self.dx = # tu deve saber oq fazer
        self.dy = # //
    
    def movimento_bola(self):
        # Aplicando a gravidade
        self.rect.y += self.gravidade
        # Atualizando a posição
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Aplicando a colisão nas bordas da tela
        if self.rect.left <= 0 or self.rect.right >= constantes.LARGURA:  # se o lado direito ou o lado esquerdo da bola chegar na borda
            self.dx = -self.dx # a bola vai voltar
        if self.rect.top <= 0: #mesma coisa com o topo
            self.dy = -self.dy
        if self.rect.bottom <= constantes.ALTURA:
            self.dy = -self.dy * 0.9 # isso vai reduzir a velocidade quando a bola quicar         
            self.rect.bottom = constantes.ALTURA # isso é pra bola não sair da tela


    def verificar_colisao(self, jogador):
        # isso é pra ver de qual lado a bola ta acertando o jogador
        if self.rect.right >= jogador.rect.left and self.rect.left < jogador.rect.left:
            self.dx = -abs(self.dx)
        elif self.rect.left <= jogador.rect.right and self.rect.right > jogador.rect.right:
            self.dx = abs(self.dx)
        if self.rect.bottom >= jogador.rect.top and self.rect.top < jogador.rect.top:
            self.dy = -abs(self.dy)
        elif self.rect.top <= jogador.rect.bottom and self.rect.bottom > jogador.rect.bottom:
            self.dy = abs(self.dy)

        # isso é pra não deixar a bola prender no jogador
        if self.rect.right > jogador.rect.left and self.rect.left < jogador.rect.left:
            self.rect.right = jogador.rect.left  
        elif self.rect.left < jogador.rect.right and self.rect.right > jogador.rect.right:
            self.rect.left = jogador.rect.right
        if self.rect.bottom > jogador.rect.top and self.rect.top < jogador.rect.top:
            self.rect.bottom = jogador.rect.top
        elif self.rect.top < jogador.rect.bottom and self.rect.bottom > jogador.rect.bottom:
            self.rect.top = jogador.rect.bottom                                              