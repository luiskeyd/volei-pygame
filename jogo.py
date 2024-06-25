import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
#from pygame.locals import *
#from sys import exit

# Inicializando o Pygame
class Jogo:
    def __init__(self):
        #criando a tela do jogo
        pygame.init() 
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.Titulo_Jogo)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
    
    def novo_jogo(self):
        #inicializacao das sprites
        self.todas_as_sprites= pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()
    
    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #caso o player feche o jogo
                if self.jogando:
                    self.jogando=False
                self.esta_rodando=False
    
    def atualizar_sprites(self):
        #atualiza sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        #desenha as sprites
        self.tela.fill(constantes.PRETO) # limpa a tela
        self.todas_as_sprites.draw(self.tela) #faz oq a função fala
        pygame.display.flip() # atuliza a tela a cada frame

    def mostrar_tela_inicial(self):
        pass
    def mostrar_tela_final(self):
        pass


        




# Fonte para usar nos textos
#fonte_maior = pygame.font.Font(None, 74)
#fonte_menor = pygame.font.Font(None, 36)

# como o jogo se comporta
#placar_jogador1 = 0
#placar_jogador2 = 0
#mensagem_ganhador = None
#ativaçao_jogo = True
#tempo_tela_mensagem = 0
#pergunta_final = False 
'''
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/jogador_1andando.png'))
        self.sprites.append(pygame.image.load('imagens/jogador_1andando.1.png'))
        self.sprites.append(pygame.image.load('imagens/jogador_1andando.2.png'))
        self.atual=0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(32*4,32*4))

        self.rect=self.image.get_rect()
        self.rect.topleft = 100, 400

        self.animar=False

    def update(self):
        if self.animar==True:
            self.atual = self.atual + 0.2
            if self.atual>= len(self.sprites):
                self.atual = 0
                self.animar=False
            self.image= self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(32*4,32*4))
    
    def andar(self):
        self.animar=True



#jogador1 = Jogador()
#self.todas_as_sprites.add(jogador1)
'''


volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
    
    #for event in pygame.event.get():
        #if event.type == QUIT:
            #pygame.quit()
            #exit()
        #if event.type==KEYDOWN:
            #jogador1.andar()


    
    #self.todas_as_sprites.draw(tela)
    #self.todas_as_sprites.update()

        
    #pygame.display.flip()        