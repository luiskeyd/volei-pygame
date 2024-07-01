import pygame
import sprites
import constantes
import sist_bola



class Jogador(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        if player == 1:
            self.sprites = []
            
            self.sprites.append(pygame.image.load(sprites.J1_FRAME_1))
            self.sprites.append(pygame.image.load(sprites.J1_FRAME_2))
            self.sprites.append(pygame.image.load(sprites.J1_FRAME_3))
            self.sprites.append(pygame.image.load(sprites.J1_FRAME_4))

            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image,(120,120))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y= constantes.X_JOGADOR1, constantes.Y_JOGADOR1 
            self.rect.inflate_ip(-30, -5)
            self.posicao_x_inicial_j1 = self.rect.x
            self.posicao_y_inicial_j1 = self.rect.y 

            self.animar = False
            self.pulando = False         
            self.posicao_x1 = constantes.X_JOGADOR1
            self.rect.x = self.posicao_x1            

        else: 
            self.sprites = []
            self.sprites.append(pygame.image.load(sprites.J2_FRAME_1))
            self.sprites.append(pygame.image.load(sprites.J2_FRAME_2))
            self.sprites.append(pygame.image.load(sprites.J2_FRAME_3))
            self.sprites.append(pygame.image.load(sprites.J2_FRAME_4))

            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image,(120, 120))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = constantes.X_JOGADOR2, constantes.Y_JOGADOR2
            self.posicao_x_inicial_j2 = self.rect.x
            self.posicao_y_inicial_j2 = self.rect.y
            self.rect.inflate_ip(10, -5)

            self.animar = False
            self.pulando = False
            self.posicao_x2 = constantes.X_JOGADOR2
            self.rect.x = self.posicao_x2

        self.gravidade = 1
        self.altura_salto = 20
        self.y_velocidade = 20 
        self.som_pulo = pygame.mixer.Sound('audio/SFX_Jump_22.wav')
        self.som_pulo.set_volume(0.3) 

            
    def movimento(self, player):
        teclas_pressionadas = pygame.key.get_pressed()
        if player == 1:
            if teclas_pressionadas[pygame.K_d]:
                self.rect.x +=5
                self.andar(1)

            if teclas_pressionadas[pygame.K_a]:
                self.rect.x -=5
                self.andar(1)

            if self.rect.x <= -25: # caso o jogador1 encoste na borda da tela
                self.rect.x = -25
        else:
            if teclas_pressionadas[pygame.K_RIGHT]:
                self.rect.x +=5
                self.andar(2)
            if teclas_pressionadas[pygame.K_LEFT]:
                self.rect.x -=5
                self.andar(2)
            if self.rect.x >= constantes.LARGURA - 95: # caso o jogador2 encoste na borda da tela
                self.rect.x = constantes.LARGURA - 95



        
    def update(self):
            #if self.pular == True:
                #self.rect.y -= 20
            # atualiza as sprites caso os jogadores se movam            
            if self.animar == True:
                self.atual = self.atual + 0.2
                if self.atual>= len(self.sprites):
                    self.atual = 0
                    self.animar=False
                self.image= self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image,(120,120))
            #self.pular(1)
                

    
    def andar(self, player):
        if player == 1 or player == 2:
            self.animar=True
    

    def colide(self, rede, bola):
        colisao_rede = pygame.sprite.spritecollide(self, rede, False)
        colisao_bola = pygame.sprite.spritecollide(self, bola, False)
        for i in colisao_rede:
                if self.rect.colliderect(i):
                    self.rect.x -= 5
                if self.rect.colliderect(i):
                    self.rect.x +=10

        


    def pular(self, player):
        pressionado = pygame.key.get_pressed()
        if player == 1:
            if pressionado[pygame.K_w] and self.pulando == False:
                self.pulando = True
                #pygame.mixer.Sound.set_volume(0.2)

                self.som_pulo.play()         
            if self.pulando:
                              
                self.rect.y -= self.y_velocidade
                self.y_velocidade -= self.gravidade
                
                if self.y_velocidade < -self.altura_salto:
                    self.pulando = False
                    
                    self.y_velocidade = self.altura_salto
                    
            
            
           
        else:                
            if pressionado[pygame.K_UP] and self.pulando == False:
                self.pulando = True
                #pygame.mixer.Sound.set_volume(0.2)
                self.som_pulo.play()              
            if self.pulando:               
                self.rect.y -= self.y_velocidade
                self.y_velocidade -= self.gravidade
                if self.y_velocidade < -self.altura_salto:
                    self.pulando = False
                    self.y_velocidade = self.altura_salto 

                   

    def resetar_posicao_player(self, player):
        if player == 1:
            self.rect.x = self.posicao_x_inicial_j1
            self.rect.y = self.posicao_y_inicial_j1


        else:
            self.rect.x = self.posicao_x_inicial_j2
            self.rect.y = self.posicao_y_inicial_j2

        self.y_velocidade = self.altura_salto
        self.pulando = False


    def ataque(self, bola, player):
        pressionado = pygame.key.get_pressed()
        if player == 1:   
            if pressionado[pygame.K_f]:
                if self.rect.topright > bola.rect.bottomleft and bola.rect.bottomleft > self.rect.midbottom: 
                      bola.vel_x = 6
                      self.rect.topright = bola.rect.bottomleft
        if player == 2:
            if pressionado[pygame.K_k]:
                if self.rect.topleft < bola.rect.bottomright and bola.rect.bottomright < self.rect.midleft:
                    bola.vel_x = -6
                    self.rect.topleft = bola.rect.bottomright
        