import pygame
import constantes  # pasta onde estarão as variáveis
import sprites  # imagens do jogo
import os

# Inicializando o Pygame
class Jogo:

    def __init__(self):
        # Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_DO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        # Inicialização das sprites
        self.todas_as_sprites = pygame.sprite.Group()
        self.jogador1 = Jogador(1)
        self.jogador2 = Jogador(2)
        self.bola = Bola()
        self.todas_as_sprites.add(self.bola)
        self.todas_as_sprites.add(self.jogador1)
        self.todas_as_sprites.add(self.jogador2)
        self.rodar()

    def rodar(self):
        # Loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        # Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Caso o player feche o jogo
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False
                

    def atualizar_sprites(self):
        # Atualiza as sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        # Desenha as sprites
        self.tela.fill(constantes.PRETO)  # Limpa a tela
        self.imagem_de_game_play()  # Desenha a tela de fundo da gameplay
        self.rede()  # Desenha a rede
        self.todas_as_sprites.draw(self.tela)  # Desenha as sprites
        pygame.display.flip()  # Atualiza a tela a cada frame

    def carregar_arquivos(self):
        # Carrega os arquivos de áudio e imagem
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
        # Exibe imagem de fundo
        self.imagem_de_fundo(constantes.LARGURA // 2, constantes.ALTURA // 2)
        # Exibe o texto da tela inicial
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

    def imagem_de_fundo(self,x,y):
        self.imagem_inicial = pygame.image.load('imagens/imagem_de_fundo.png')
        self.imagem_inicial = pygame.transform.scale(self.imagem_inicial, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_inicial.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_inicial, self.rect)

    def rede(self):
        pygame.draw.rect(self.tela, constantes.AZUL, [constantes.LARGURA // 2, 320, 10, constantes.TAMANHO_REDE], 0)

    def imagem_de_game_play(self):
        self.imagem_gameplay = pygame.image.load('imagens/imagem_de_gameplay.png')
        self.imagem_gameplay = pygame.transform.scale(self.imagem_gameplay, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_gameplay.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_gameplay, self.rect)

    def mostrar_tela_final(self):
        pass


class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogador_id):
        super().__init__()
        if jogador_id == 1:
            self.sprites = [pygame.image.load(f'imagens/jogador1_andando.{i}.png') for i in range(1, 5)]
            self.rect_topleft = (constantes.X_JOGADOR1, constantes.Y_JOGADOR1)
        else:
            self.sprites = [pygame.image.load(f'imagens/jogador2_andando.{i} (1).png') for i in range(1, 5)]
            self.rect_topleft = (620, 430)

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 4, 32 * 4))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.rect_topleft
        self.animar = False

    def update(self):
        if self.animar:
            self.atual += 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (32 * 4, 32 * 4))

    def andar(self):
        self.animar = True


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagens/bola mikasa (1).png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.midtop = (constantes.LARGURA // 2, 250)


volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
