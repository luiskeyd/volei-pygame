import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
import sist_players
import sist_bola
import sist_rede





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
        #self.carregar_arquivos()
    

    def novo_jogo(self):
        #inicializacao das sprites
        self.todas_as_sprites = pygame.sprite.Group() # carrega todas as sprites
        self.rede_sprite = pygame.sprite.Group()
        self.jogador1 = sist_players.Jogador(1) # sprites do jogador 1
        self.jogador2 = sist_players.Jogador(2) # sprites do jogador 2
        self.bola = sist_bola.Bola() # sprite da bola
        self.rede = sist_rede.Rede(constantes.AZUL,10, constantes.TAMANHO_REDE, (constantes.LARGURA//2, 320) )
        self.rede_sprite.add(self.rede)
        #self.todas_as_sprites.add(self.rede)
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
            #caso o player feche o jogo
            if event.type == pygame.QUIT: 
                    self.jogando = False 
                    self.esta_rodando = False
            
            

    def atualizar_sprites(self):
        #atualiza sprites
        self.todas_as_sprites.update()
        # sistema de colisao
        self.jogador1.colide(self.rede_sprite)
        self.jogador2.colide(self.rede_sprite)


    def desenhar_sprites(self):
        #desenha as sprites
        self.tela.fill(constantes.PRETO) # limpa a tela
        self.imagem_de_game_play()# desenha a tela de funda da game play
        #self.rede() # desenha a rede
        self.todas_as_sprites.draw(self.tela) #faz oq a função fala
        self.rede_sprite.draw(self.tela)
        pygame.display.flip() # atualiza a tela a cada frame

    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        #definicao do texto na tela
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

    def imagem_de_game_play(self):
        self.imagem_gameplay = pygame.image.load(sprites.TELA_DE_GAMEPLAY )
        self.imagem_gameplay = pygame.transform.scale(self.imagem_gameplay, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_gameplay.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_gameplay, self.rect)


    def mostrar_tela_final(self):
        pass


 

volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
