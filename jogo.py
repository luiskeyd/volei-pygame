import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
from pygame.locals import *
from sys import exit

# Inicializando o Pygame
pygame.init() 

# Configurações da Tela
largura = 840
altura = 580
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Vôlei ')
pygame.display.set_caption('Sprites')

# Configurações do Relógio
relogio = pygame.time.Clock()
FPS = (60)

#Cores
PRETO=(0,0,0)
BRANCO=(255,255,255)
AZUL = (0,0,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
CINZA = (200,200,200)

# Física do Jogo
GRAVIDADE = 0.2
ALTURA_DO_SALTO = -9
FORCA_DE_ATAQUE = -6
VELOCIDADE_BOLA = 6
VELOCIDADE_ATAQUE = 8

# Fonte para usar nos textos
fonte_maior = pygame.font.Font(None, 74)
fonte_menor = pygame.font.Font(None, 36)

# como o jogo se comporta
placar_jogador1 = 0
placar_jogador2 = 0
mensagem_ganhador = None
ativaçao_jogo = True
tempo_tela_mensagem = 0
pergunta_final = False 

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/New Piskel.png'))
        self.sprites.append(pygame.image.load('imagens/New Piskel (1).png'))
        self.sprites.append(pygame.image.load('imagens/New Piskel (2).png'))
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


todas_as_sprites= pygame.sprite.Group()
jogador1 = Jogador()
todas_as_sprites.add(jogador1)





while True:
    relogio.tick(40)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            jogador1.andar()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

        
    pygame.display.flip()        