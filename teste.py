import pygame
import constantes #pasta onde estarão as variáveis
import sprites #imagens do jogo 
import os # arquivos
import sist_players
import sist_bola
import sist_rede

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
        self.jogando = False

    def novo_jogo(self):
        # Inicialização das sprites
        self.todas_as_sprites = pygame.sprite.Group()
        self.rede_sprite = pygame.sprite.Group()
        self.bola_sprite = pygame.sprite.Group()
        self.jogador1 = sist_players.Jogador(1)
        self.jogador2 = sist_players.Jogador(2)
        self.bola = sist_bola.Bola()
        self.rede = sist_rede.Rede(constantes.AZUL, 10, constantes.TAMANHO_REDE, (constantes.LARGURA // 2, 320))
        self.rede_sprite.add(self.rede)
        self.bola_sprite.add(self.bola)
        self.todas_as_sprites.add(self.jogador1)
        self.todas_as_sprites.add(self.jogador2)
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.load('audio/happy_adveture.mp3')
        pygame.mixer_music.play(-1)
        self.rodar()

    def rodar(self):
        # Loop do jogo
        self.jogando = True
        while self.jogando and self.esta_rodando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.jogador1.movimento(1)
            self.jogador2.movimento(2)
            self.bola.movimento_bola()
            self.jogador1.pular(1)
            self.jogador2.pular(2)
            self.jogador1.colide(self.rede_sprite, self.bola_sprite)
            self.jogador2.colide(self.rede_sprite, self.bola_sprite)
            self.bola.verificar_colisao_jogador(self.jogador1)
            self.bola.verificar_colisao_jogador(self.jogador2)
            self.bola.verificar_colisao_rede(self.rede)
            self.atualizar_sprites()
            self.desenhar_sprites()
            self.verificador_win()

    def eventos(self):
        # Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        # Atualiza sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        # Desenha as sprites
        self.tela.fill(constantes.PRETO)
        self.imagem_de_game_play()
        self.BARRIO()
        self.Placar()
        self.bola_sprite.draw(self.tela)
        self.rede_sprite.draw(self.tela)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        # Definição do texto na tela
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, False, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x, y)
        self.tela.blit(mensagem, mensagem_rect)

    def mostrar_tela_inicial(self):
        # Exibe imagem de fundo
        self.imagem_de_fundo()
        # Exibe o texto da tela inicial
        self.mostrar_texto('Pressione espaço para jogar', 32, constantes.BRANCO, constantes.LARGURA // 2, constantes.ALTURA // 2)
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.load('audio/8bit Bossa.mp3')
        pygame.mixer_music.play()
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
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('audio/Menu Selection Click.wav')
                        pygame.mixer_music.play()

    def imagem_de_fundo(self):
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

    def BARRIO(self):
        self.barrio = pygame.image.load(sprites.BARRIO)
        self.barrio = pygame.transform.scale(self.barrio, (70, 70))
        self.rect = self.barrio.get_rect()
        self.rect.midtop = (50, 460)
        self.tela.blit(self.barrio, self.rect)

    def Placar(self):
        self.placar_exterior = pygame.draw.rect(self.tela, constantes.PRETO, [233, 50, 400, 100], 5)
        self.placar_interior = pygame.draw.rect(self.tela, constantes.CINZA, [238, 54, 391, 91], 0)
        self.mostrar_texto('PLACAR', 30, constantes.PRETO, 435, 60)
        self.mostrar_texto(f'{constantes.PLACAR_JOGADOR1}', 45, constantes.VERMELHO, 320, 95)
        self.mostrar_texto(f'{constantes.PLACAR_JOGADOR2}', 45, constantes.VERMELHO, 550, 95)
        POSICAO = self.bola.atualizar_posicao()

        if POSICAO[1] >= 547 and (POSICAO[0] > constantes.LARGURA // 2):
            constantes.PLACAR_JOGADOR1 += 1
            self.resetar_posicao()
        elif POSICAO[1] >= 547 and (POSICAO[0] < constantes.LARGURA // 2):
            constantes.PLACAR_JOGADOR2 += 1
            self.resetar_posicao()

    def verificador_win(self):
        vencedor = False
        if constantes.PLACAR_JOGADOR1 >= 12 and (constantes.PLACAR_JOGADOR1 - constantes.PLACAR_JOGADOR2 >= 2):
            vencedor = 1
        if constantes.PLACAR_JOGADOR2 >= 12 and (constantes.PLACAR_JOGADOR2 - constantes.PLACAR_JOGADOR1 >= 2):
            vencedor = 2

        if vencedor:
            self.mostrar_tela_final(vencedor)
            self.jogando = False
            constantes.PLACAR_JOGADOR1 = 0
            constantes.PLACAR_JOGADOR2 = 0

    def resetar_posicao(self):
        self.jogador1.resetar_posicao_player(1)
        self.jogador2.resetar_posicao_player(2)
        self.bola.resetar_posicao_bola()

    def mostrar_tela_final(self, vencedor):
        self.tela.fill(constantes.BRANCO)
        if vencedor == 1:
            self.mostrar_texto('JOGADOR 1 GANHOU', 34, constantes.VERMELHO, constantes.LARGURA // 2, constantes.ALTURA // 2)
        else:
            self.mostrar_texto('JOGADOR 2 GANHOU', 34, constantes.AZUL, constantes.LARGURA // 2, constantes.ALTURA // 2)
        pygame.display.flip()
        pygame.time.wait(3000)

volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
