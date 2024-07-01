import pygame
import constantes #pasta onde estarão as variaveis
import sprites #imagens do jogo 
import os # arquivos
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
        self.fonte = pygame.font.match_font(constantes.FONTE)
    

    def novo_jogo(self):
        #inicializacao das sprites
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.load('audio/happy_adveture.mp3')
        pygame.mixer_music.play(-1)
        self.todas_as_sprites = pygame.sprite.Group() # carrega todas as sprites
        self.rede_sprite = pygame.sprite.Group()
        self.bola_sprite = pygame.sprite.Group()
        self.jogador1 = sist_players.Jogador(1) # sprites do jogador 1
        self.jogador2 = sist_players.Jogador(2) # sprites do jogador 2
        self.bola = sist_bola.Bola() # sprite da bola
        self.rede = sist_rede.Rede(constantes.AZUL,10, constantes.TAMANHO_REDE, (constantes.LARGURA//2, 320))
        self.rede_sprite.add(self.rede)
        self.bola_sprite.add(self.bola)
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
            self.bola.movimento_bola()
            self.jogador1.pular(1)
            self.jogador2.pular(2)


            self.jogador1.ataque(self.bola, 1)
            self.jogador2.ataque(self.bola, 2)

            self.jogador1.colide(self.rede_sprite, self.bola_sprite)
            self.jogador2.colide(self.rede_sprite, self.bola_sprite)
            self.bola.verificar_colisao_jogador(self.jogador1)
            self.bola.verificar_colisao_jogador(self.jogador2)
            self.bola.verificar_colisao_rede(self.rede)
            self.atualizar_sprites()
            self.desenhar_sprites()
            self.verificador_win()
            





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


    def desenhar_sprites(self):
        #desenha as sprites
        self.tela.fill(constantes.PRETO) # limpa a tela
        self.imagem_de_game_play()# desenha a tela de funda da game play
        self.BARRIO() # desenha um 'BARRRRRIIIIIIIIIO'
        self.Placar(self.bola)
        self.bola_sprite.draw(self.tela)
        self.rede_sprite.draw(self.tela) # desenha a rede
        self.todas_as_sprites.draw(self.tela) #faz oq a função fala
        pygame.display.flip() # atualiza a tela a cada frame


    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        #definicao do texto na tela
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, False, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x,y)
        self.tela.blit(mensagem, mensagem_rect)


    def mostrar_tela_inicial(self):
       #exibe imagem de fundo
       self.imagem_de_fundo()
       #exibe o texto da tela inicial
       self.mostrar_texto('Pressione espaço para jogar', 32,constantes.BRANCO, constantes.LARGURA//2, constantes.ALTURA//2)
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
        self.imagem_gameplay = pygame.image.load(sprites.TELA_DE_GAMEPLAY )
        self.imagem_gameplay = pygame.transform.scale(self.imagem_gameplay, (constantes.LARGURA, constantes.ALTURA))
        self.rect = self.imagem_gameplay.get_rect()
        self.rect.topleft = (0, 0)
        self.tela.blit(self.imagem_gameplay, self.rect)
       
    

    def BARRIO(self):
        self.barrio = pygame.image.load(sprites.BARRIO)
        self.barrio = pygame.transform.scale(self.barrio, (70,70))
        self.rect = self.barrio.get_rect()
        self.rect.midtop = (50,460)
        self.tela.blit(self.barrio, self.rect)


    def Placar(self, bola):

        self.placar_exterior = pygame.draw.rect(self.tela,(constantes.PRETO), [233,50,400,100], 5)
        self.placar_interior = pygame.draw.rect(self.tela,(constantes.CINZA), [238,54,391,91], 0)
        self.mostrar_texto('PLACAR',30,constantes.PRETO, 435,60 )
        self.mostrar_texto(f'{constantes.PLACAR_JOGADOR1}',45, constantes.VERMELHO,320, 95)
        self.mostrar_texto(f'{constantes.PLACAR_JOGADOR2}',45, constantes.VERMELHO,550, 95)
        POSICAO = self.bola.atualizar_posicao()
        
        if POSICAO[1] >= 547 and (POSICAO[0] > constantes.LARGURA /2):
            constantes.PLACAR_JOGADOR1 += 1
            self.resetar_posicao(1)

        elif POSICAO[1] >= 547 and (POSICAO[0] < constantes.LARGURA /2):
            constantes.PLACAR_JOGADOR2 += 1
            self.resetar_posicao(2)
        


    def verificador_win(self):
        vencedor = False
        if constantes.PLACAR_JOGADOR1 >= 12 and (constantes.PLACAR_JOGADOR1 - constantes.PLACAR_JOGADOR2 >= 2):
            constantes. PLACAR_JOGADOR1 = 0
            constantes. PLACAR_JOGADOR2 = 0
            constantes.eita = 1
            vencedor = True
        
        if constantes.PLACAR_JOGADOR2 >= 12 and (constantes.PLACAR_JOGADOR2 - constantes.PLACAR_JOGADOR1 >= 2):
            constantes. PLACAR_JOGADOR1 = 0
            constantes. PLACAR_JOGADOR2 = 0
            constantes.eita = 2
            vencedor = True

        if vencedor:
            self.mostrar_tela_final()
            self.jogando = False


    def resetar_posicao(self, bola):
        pontuou = True
        if pontuou:
            self.jogador1.resetar_posicao_player(1)
            self.jogador2.resetar_posicao_player(2)
            if bola == 1:
                self.bola.resetar_posicao_bola1() 
            if bola == 2:
                self.bola.resetar_posicao_bola2()     
            pontuou = False


    def mostrar_tela_final(self):
        self.tela.fill(constantes.BRANCO)
        if constantes.eita == 1:
                self.mostrar_texto('JOGADOR 1 GANHOU', 34, constantes.VERMELHO, 415, 230)
                self.mostrar_texto('pressione espaço para reiniciar', 25, constantes.PRETO, 415, 270)
        else:
                self.mostrar_texto('JOGADOR 2 GANHOU', 34, constantes.AZUL, 415, 230)
                self.mostrar_texto('pressione espaço para reiniciar', 25, constantes.PRETO, 415, 270)
        pygame.display.flip()
        self.esperar_resposta()






volei = Jogo()
volei.mostrar_tela_inicial()

while volei.esta_rodando:
    volei.novo_jogo()
    #volei.mostrar_tela_final()
