import pygame
import constantes # Variáveis do jogo (como largura, altura, cores, etc.)
import sprites # Imagens do jogo
import sist_players # Sistema dos jogadores
import sist_bola # Sistema da bola

# Inicializando o Pygame
class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_DO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)

    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rede_sprite = pygame.sprite.Group()
        self.jogador1 = Jogador(1)
        self.jogador2 = Jogador(2)
        self.bola = Bola()
        self.rede = Rede(constantes.AZUL, 10, constantes.TAMANHO_REDE, (constantes.LARGURA // 2, 320))
        self.rede_sprite.add(self.rede)
        self.todas_as_sprites.add(self.bola)
        self.todas_as_sprites.add(self.jogador1)
        self.todas_as_sprites.add(self.jogador2)
        self.rodar()

    def rodar(self):
        self.jogando = True 
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.jogador1.movimento(1)
            self.jogador2.movimento(2)
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False 
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()
        self.jogador1.colide(self.rede_sprite)
        self.jogador2.colide(self.rede_sprite)

    def desenhar_sprites(self):
        self.tela.fill(constantes.PRETO)
        self.imagem_de_game_play()
        self.todas_as_sprites.draw(self.tela)
        self.rede_sprite.draw(self.tela)
        pygame.display.flip()

    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, False, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x, y)
        self.tela.blit(mensagem, mensagem_rect)

    def mostrar_tela_inicial(self):
        self.imagem_de_fundo(constantes.LARGURA // 2, constantes.ALTURA // 2)
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

    def imagem_de_fundo(self, x, y):
        self.imagem_inicial = pygame.image.load(sprites.TELA_INICIAL)
        self.imagem_inicial = pygame.transform.scale(self.imagem_inicial, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_inicial.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_inicial, self.rect)

    def imagem_de_game_play(self):
        self.imagem_gameplay = pygame.image.load(sprites.TELA_DE_GAMEPLAY)
        self.imagem_gameplay = pygame.transform.scale(self.imagem_gameplay, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_gameplay.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_gameplay, self.rect)

    def mostrar_tela_final(self):
        pass

class Rede(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, posicao):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posicao

class Jogador(pygame.sprite.Sprite):
    def __init__(self, player_id):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(constantes.BRANCO)
        self.rect = pygame.Rect(0, 0, 30, 50)  # Define um retângulo menor que a imagem
        self.rect.x = constantes.LARGURA // 4 if player_id == 1 else 3 * constantes.LARGURA // 4
        self.rect.y = constantes.ALTURA - 60

    def movimento(self, player_id):
        keys = pygame.key.get_pressed()
        if player_id == 1:
            if keys[pygame.K_a]:
                self.rect.x -= 5
            if keys[pygame.K_d]:
                self.rect.x += 5
        else:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5

    def colide(self, rede):
        colisao = pygame.sprite.spritecollide(self, rede, False)
        for i in colisao:
            if self.rect.colliderect(i):
                if self.rect.centerx < constantes.LARGURA // 2:
                    self.rect.right = i.rect.left
                else:
                    self.rect.left = i.rect.right

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(constantes.VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = constantes.LARGURA // 2
        self.rect.y = constantes.ALTURA // 2

volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    volei.mostrar_tela_final()
