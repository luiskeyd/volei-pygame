import pygame
import constantes # pasta onde estarão as variáveis
import sprites # imagens do jogo 
import os

# Inicializando o Pygame
class Jogo:

    def __init__(self):
        # criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_DO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        # inicialização das sprites
        self.todas_as_sprites = pygame.sprite.Group()
        self.jogador1 = Jogador(1)
        self.jogador2 = Jogador(2)
        self.todas_as_sprites.add(self.jogador1)
        self.todas_as_sprites.add(self.jogador2)
        self.rodar()

    def rodar(self):
        # loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        # define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # caso o player feche o jogo
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        # atualiza sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        # desenha as sprites
        self.tela.blit(self.imagem_inicial, self.rect)  # desenha a imagem de fundo
        self.todas_as_sprites.draw(self.tela)  # desenha as sprites na tela
        pygame.display.flip()  # atualiza a tela a cada frame

    def carregar_arquivos(self):
        # Carregar os arquivos de áudio e imagem
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.jogo_python = os.path.join(diretorio_imagens, 'imagem_de_fundo.png')

    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        # Exibe um texto na tela
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, False, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x, y)
        self.tela.blit(mensagem, mensagem_rect)

    def mostrar_tela_inicial(self):
        # exibe imagem de fundo
        self.imagem_de_fundo()

        # exibe o texto da tela inicial
        self.mostrar_texto('Pressione espaço para jogar', 32, constantes.BRANCO, constantes.LARGURA // 2, constantes.ALTURA // 2)

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

    def imagem_de_fundo(self):
        self.imagem_inicial = pygame.image.load(self.jogo_python)
        self.imagem_inicial = pygame.transform.scale(self.imagem_inicial, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_inicial.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_inicial, self.rect)

    def mostrar_tela_final(self):
        pass

class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogador_id):
        pygame.sprite.Sprite.__init__(self)
        if jogador_id == 1:
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/jogador1_andando.1.png'))
            self.sprites.append(pygame.image.load('imagens/jogador1_andando.2.png'))
            self.sprites.append(pygame.image.load('imagens/jogador1_andando.3.png'))
            self.sprites.append(pygame.image.load('imagens/jogador1_andando.4.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (32*4, 32*4))
            self.rect = self.image.get_rect()
            self.rect.topleft = 100, 400
            self.animar = False
        else:
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/jogador2_andando.1 (1).png'))
            self.sprites.append(pygame.image.load('imagens/jogador2_andando.2 (1).png'))
            self.sprites.append(pygame.image.load('imagens/jogador2_andando.3 (1).png'))
            self.sprites.append(pygame.image.load('imagens/jogador2_andando.4 (1).png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (32*4, 32*4))
            self.rect = self.image.get_rect()
            self.rect.topleft = 600, 400
            self.animar = False

    def update(self):
        if self.animar:
            self.atual = self.atual + 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (32*4, 32*4))

    def andar(self):
        self.animar = True

volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
