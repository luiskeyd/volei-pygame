import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
import os # arquivos



# Inicializando o Pygame
class Jogo:

    def __init__(self):
        #criando a tela do jogo
        pygame.init() # iniciando o jogo
        pygame.mixer.init() # musica pro jogo
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_DO_JOGO)
        self.relogio = pygame.time.Clock() # fps do jogo
        self.esta_rodando = True # jogo aberto
        self.fonte=pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()
    

    def novo_jogo(self):
        #inicializacao das sprites
        self.todas_as_sprites = pygame.sprite.Group() # carrega todas as sprites
        self.jogador1 = Jogador(1) # sprites do jogador 1
        self.jogador2 = Jogador(2) # sprites do jogador 2
        self.bola = Bola() # sprite da bola
        self.todas_as_sprites.add(self.bola)
        self.todas_as_sprites.add(self.jogador1)
        self.todas_as_sprites.add(self.jogador2) # add de todas as sprites na lista
        self.rodar()


    def rodar(self):
        #loop do jogo
        self.jogando = True 
        while self.jogando: #inicializa o loop
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.jogador1.movimento(1)
            self.jogador2.movimento(2)
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #caso o player feche o jogo
                if self.jogando:
                    self.jogando = False 
                self.esta_rodando = False
            
            

    def atualizar_sprites(self):
        #atualiza sprites
        self.todas_as_sprites.update()


    def desenhar_sprites(self):
        #desenha as sprites
        self.tela.fill(constantes.PRETO) # limpa a tela
        self.imagem_de_game_play()# desenha a tela de funda da game play
        self.rede() # desenha a rede
        self.todas_as_sprites.draw(self.tela) #faz oq a função fala
        pygame.display.flip() # atualiza a tela a cada frame


    def carregar_arquivos(self):
        #Carregar os arquivos de audio e imagem
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.jogo_python = os.path.join(diretorio_imagens,'imagem_de_fundo.png' )


    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        #Exibe um texto na tela
        fonte=pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, False, cor)
        mensagem_rect=mensagem.get_rect()
        mensagem_rect.midtop=(x,y)
        self.tela.blit(mensagem, mensagem_rect)


    def mostrar_tela_inicial(self):
       #exibe imagem de fundo
       self.imagem_de_fundo(constantes.LARGURA//2, constantes.ALTURA//2)

       #exibe o texto da tela inicial
       self.mostrar_texto('Pressione espaço para jogar', 32,constantes.BRANCO, constantes.LARGURA//2, constantes.ALTURA//2)

       pygame.display.flip()
       self.esperar_resposta()
    

    def esperar_resposta(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esperando = False

    def imagem_de_fundo(self,x, y):
        self.imagem_inicial = pygame.image.load(sprites.TELA_INICIAL)
        self.imagem_inicial = pygame.transform.scale(self.imagem_inicial, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_inicial.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_inicial, self.rect)

    def rede(self):
        pygame.draw.rect(self.tela, constantes.AZUL, [constantes.LARGURA//2 ,320  , 10, constantes.TAMANHO_REDE], 0 )

    def imagem_de_game_play(self):
        self.imagem_gameplay = pygame.image.load(sprites.TELA_DE_GAMEPLAY )
        self.imagem_gameplay = pygame.transform.scale(self.imagem_gameplay, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_gameplay.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_gameplay, self.rect)



    def mostrar_tela_final(self):
        pass

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
            self.image = pygame.transform.scale(self.image,(32*4,32*4))
            self.rect= self.image.get_rect()
            self.rect.topleft = constantes.X_JOGADOR1, constantes.Y_JOGADOR1           
            self.animar=False
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
            self.image = pygame.transform.scale(self.image,(32*4, 32*4))
            self.rect = self.image.get_rect()
            self.rect.topleft = 620, 430
            self.animar = False
            self.posicao_x2 = constantes.X_JOGADOR2
            self.rect.x = self.posicao_x2
            
    def movimento(self, player):
        teclas_pressionadas = pygame.key.get_pressed()
        if player == 1:
            if teclas_pressionadas[pygame.K_d]:
                self.rect.x +=5
                self.andar(1)
            if teclas_pressionadas[pygame.K_a]:
                self.rect.x -=5
                self.andar(1)
        else:
            if teclas_pressionadas[pygame.K_RIGHT]:
                self.rect.x +=5
                self.andar(2)
            if teclas_pressionadas[pygame.K_LEFT]:
                self.rect.x -=5
                self.andar(2)




        
    def update(self):
            if self.animar==True:
                self.atual= self.atual+ 0.2
                if self.atual>= len(self.sprites):
                    self.atual = 0
                    self.animar=False
                self.image= self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image,(32*4,32*4))

    
    def andar(self, player):
        if player == 1 or player == 2:
            self.animar=True
    

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = (pygame.image.load(sprites.BOLA))
        self.image = self.sprite
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect= self.image.get_rect()
        self.rect.midtop = (constantes.LARGURA//2, 250)


volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
