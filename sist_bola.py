import pygame
#import random
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
        self.rect.x, self.rect.y = (280, 260)
        self.rect.inflate_ip(-10, -10)
        self.posicao_inicial_bola_x = self.rect.x 
        self.posicao_inicial_bola_y = self.rect.y
        self.gravidade = constantes.Y_GRAVIDADE
        self.vel_x = 6
        self.vel_y = 6
        self.colidiu = False

    def gravidade_ativada(self):
        self.colidiu = True

    def movimento_bola(self):
        # Aplicando a gravidade
        if self.colidiu == True:
            self.vel_y += self.gravidade
        # Atualizando a posição
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

        # Aplicando a colisão nas bordas da tela
        if self.rect.left <= 0:   # se o lado direito ou o lado esquerdo da bola chegar na borda
            self.rect.left = 5
            self.vel_x = abs(self.vel_x)
        if self.rect.right >= constantes.LARGURA:
            self.rect.right = constantes.LARGURA
            self.vel_x = -abs(self.vel_x)
         # a bola vai voltar

        if self.rect.top <= 0: #mesma coisa com o topo
            self.vel_y = -self.vel_y

        elif self.rect.bottom >= constantes.ALTURA:
            self.vel_y = -self.vel_y * 0.85 # isso vai reduzir a velocidade quando a bola quicar         
            self.rect.bottom = constantes.ALTURA # isso é pra bola não sair da tela

# buguei todinho nesse codigo
    
    def verificar_colisao_rede(self, rede):
            #isso é pra ver de qual lado a bola ta acertando a rede
            if self.rect.colliderect(rede.rect):
                if self.rect.right >= rede.rect.left and self.rect.left < rede.rect.left:
                     self.vel_x = -abs(self.vel_x)
                elif self.rect.left <= rede.rect.right and self.rect.right > rede.rect.right:
                     self.vel_x = abs(self.vel_x)
                if self.rect.bottom >= rede.rect.top and self.rect.top < rede.rect.top:
                     self.vel_y = -abs(self.vel_y)
                elif self.rect.top <= rede.rect.bottom and self.rect.bottom > rede.rect.bottom:
                    self.vel_y = abs(self.vel_y)

                if self.rect.right > rede.rect.left and self.rect.left < rede.rect.left:
                     self.rect.right = rede.rect.left  
                elif self.rect.left < rede.rect.right and self.rect.right > rede.rect.right:
                     self.rect.left = rede.rect.right
                if self.rect.bottom > rede.rect.top and self.rect.top < rede.rect.top:
                     self.rect.bottom = rede.rect.top
                elif self.rect.top < rede.rect.bottom and self.rect.bottom > rede.rect.bottom:
                     self.rect.top = rede.rect.bottom 


    def verificar_colisao_jogador(self, player):
        # isso é pra ver de qual lado a bola ta acertando o jogador
        
        if self.rect.colliderect(player.rect):
            self.gravidade_ativada()
            if self.rect.right >= player.rect.left and self.rect.left < player.rect.left:
                self.vel_x = -abs(self.vel_x)
            elif self.rect.left <= player.rect.right and self.rect.right > player.rect.right:
                self.vel_x = abs(self.vel_x)
            if self.rect.bottom >= player.rect.top and self.rect.top < player.rect.top:
                self.vel_y = -abs(self.vel_y) 
            elif self.rect.top <= player.rect.bottom and self.rect.bottom > player.rect.bottom:
                self.vel_y = abs(self.vel_y)

            # isso é pra não deixar a bola prender no jogador
            if self.rect.right > player.rect.left and self.rect.left < player.rect.left:
                self.rect.right = player.rect.left  
            elif self.rect.left < player.rect.right and self.rect.right > player.rect.right:
                self.rect.left = player.rect.right
            if self.rect.bottom > player.rect.top and self.rect.top < player.rect.top:
                self.rect.bottom = player.rect.top
            elif self.rect.top < player.rect.bottom and self.rect.bottom > player.rect.bottom:
                self.rect.top = player.rect.bottom                                              


    def atualizar_posicao(self):
        return (self.rect.x, self.rect.y)  
        
    
    def resetar_posicao_bola1(self):
        self.rect.x = self.posicao_inicial_bola_x
        self.rect.y = self.posicao_inicial_bola_y
        self.vel_x = 5
        self.vel_y = 5
        self.colidiu = False

    def resetar_posicao_bola2(self):
        self.rect.x = 530
        self.rect.y = 260
        self.vel_x = 5
        self.vel_y = 5
        self.colidiu = False