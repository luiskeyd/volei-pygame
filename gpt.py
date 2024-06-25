import pygame
import sys
import time

# Inicializando o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo de Vôlei')

# Cores
BRANCO = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Configurações do relógio
clock = pygame.time.Clock()
FPS = 60

# Variáveis de física
GRAVITY = 0.2
JUMP_STRENGTH = -9
ATTACK_STRENGTH = -6
BALL_SPEED = 6
ATTACK_SPEED = 8

# Fonte
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Variáveis de estado do jogo
score_player1 = 0
score_player2 = 0
winner_message = None
game_active = True
display_winner_time = 0
display_question = False

class Ball:
    def __init__(self, x, y, radius, color):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = BALL_SPEED
        self.dy = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.dy += GRAVITY
        self.x += self.dx
        self.y += self.dy

        # Colisão com as bordas da tela
        if self.x - self.radius < 0:
            self.x = self.radius
            self.dx = -self.dx
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.dx = -self.dx

        if self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.dy = -self.dy
            if self.x < SCREEN_WIDTH // 2:
                score_point('player2')
            else:
                score_point('player1')

        # Colisão com a rede
        if net.x < self.x < net.x + net.width:
            if self.y + self.radius > SCREEN_HEIGHT - net.height:
                if self.y - self.radius < SCREEN_HEIGHT - net.height:
                    self.dy = -abs(self.dy)
                else:
                    self.dx = -self.dx

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = BALL_SPEED
        self.dy = 0

    def reset_position_to(self, direction):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = BALL_SPEED if direction == 'right' else -BALL_SPEED
        self.dy = 0

    def check_collision_with_player(self, player):
        if (self.x + self.radius > player.x and self.x - self.radius < player.x + player.width and
            self.y + self.radius > player.y and self.y - self.radius < player.y + player.height):
            
            # Ajustar a posição da bola para não entrar no jogador
            if abs(self.x - player.x) < self.radius:
                self.dx = -abs(self.dx)
            elif abs(self.x - (player.x + player.width)) < self.radius:
                self.dx = abs(self.dx)
            
            if abs(self.y - player.y) < self.radius:
                self.dy = -abs(self.dy)
            elif abs(self.y - (player.y + player.height)) < self.radius:
                self.dy = abs(self.dy)

class Player:
    def __init__(self, x, y, width, height, color):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.dx = 0
        self.dy = 0
        self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.dy += GRAVITY
        self.x += self.dx
        self.y += self.dy

        # Colisão com as bordas da tela
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.dy = 0
            self.on_ground = True

        # Colisão com a rede
        if self.x < net.x + net.width and self.x + self.width > net.x:
            if self.x < SCREEN_WIDTH // 2:
                self.x = net.x - self.width
            else:
                self.x = net.x + net.width

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = 0
        self.dy = 0

    def jump(self):
        if self.on_ground:
            self.dy = JUMP_STRENGTH
            self.on_ground = False

    def move_down(self):
        if self.y + self.height < SCREEN_HEIGHT:
            self.y += 5

    def attack(self, direction):
        if (self.x - self.width < ball.x < self.x + self.width and
                self.y - self.height < ball.y < self.y + self.height):
            if direction == 'right':
                ball.dx = ATTACK_SPEED
            elif direction == 'left':
                ball.dx = -ATTACK_SPEED
            ball.dy = ATTACK_STRENGTH

class Net:
    def __init__(self, x, width, height, color):
        self.x = x
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, SCREEN_HEIGHT - self.height, self.width, self.height))

def score_point(player):
    global score_player1, score_player2, winner_message, game_active, display_winner_time

    if player == 'player1':
        score_player1 += 1
    else:
        score_player2 += 1

    if score_player1 >= 12 and score_player1 - score_player2 >= 2:
        winner_message = "Jogador Azul ganhou!"
        game_active = False
        display_winner_time = time.time()
    elif score_player2 >= 12 and score_player2 - score_player1 >= 2:
        winner_message = "Jogador Preto ganhou!"
        game_active = False
        display_winner_time = time.time()
    else:
        pygame.time.delay(2000)
        player1.reset_position()
        player2.reset_position()
        ball.reset_position_to('right' if player == 'player1' else 'left')

def reset_game():
    global score_player1, score_player2, winner_message, game_active, display_question

    score_player1 = 0
    score_player2 = 0
    winner_message = None
    game_active = True
    display_question = False

    player1.reset_position()
    player2.reset_position()
    ball.reset_position()

def draw_button(text, position, size):
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = small_font.render(text, True, BLACK)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    return button_rect

# Criar a bola
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, RED)

# Criar a rede
net = Net(SCREEN_WIDTH // 2 - 5, 10, 150, BLACK)

# Criar jogadores
player1 = Player(100, SCREEN_HEIGHT - 70, 50, 70, BLUE)
player2 = Player(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70, 50, 70, BLACK)

# Loop principal do jogo
while True:
    screen.fill(BRANCO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_a:
                    player1.dx = -5
                elif event.key == pygame.K_d:
                    player1.dx = 5
                elif event.key == pygame.K_w:
                    player1.jump()
                elif event.key == pygame.K_s:
                    player1.move_down()
                elif event.key == pygame.K_f:
                    player1.attack('right')
                elif event.key == pygame.K_LEFT:
                    player2.dx = -5
                elif event.key == pygame.K_RIGHT:
                    player2.dx = 5
                elif event.key == pygame.K_UP:
                    player2.jump()
                elif event.key == pygame.K_DOWN:
                    player2.move_down()
                elif event.key == pygame.K_k:
                    player2.attack('left')
            else:
                if display_winner_time and time.time() - display_winner_time >= 3:
                    if event.key == pygame.K_y:
                        reset_game()
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player1.dx = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player2.dx = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if not game_active and display_winner_time and time.time() - display_winner_time >= 3:
                if yes_button.collidepoint(mouse_pos):
                    reset_game()
                elif no_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    if game_active:
        # Movimento e desenho da bola
        ball.move()
        ball.check_collision_with_player(player1)
        ball.check_collision_with_player(player2)
        ball.draw(screen)

        # Desenhar a rede
        net.draw(screen)

        # Movimento e desenho dos jogadores
        player1.move()
        player1.draw(screen)
        player2.move()
        player2.draw(screen)

        # Exibir pontuação
        score_text = font.render(f"{score_player1} - {score_player2}", True, BLACK)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(score_text, score_rect)
    else:
        if display_winner_time and time.time() - display_winner_time < 3:
            # Exibir mensagem de vitória
            winner_text = font.render(winner_message, True, BLUE if "Azul" in winner_message else BLACK)
            winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            screen.blit(winner_text, winner_rect)
        else:
            display_question = True
            # Exibir mensagem "Outro jogo?"
            question_text = font.render("Outro jogo?", True, BLACK)
            question_rect = question_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
            screen.blit(question_text, question_rect)

            # Exibir botões "Sim" e "Não"
            yes_button = draw_button("Sim", (SCREEN_WIDTH / 2 - 75, SCREEN_HEIGHT / 2), (50, 30))
            no_button = draw_button("Não", (SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT / 2), (50, 30))

    pygame.display.flip()
    screen.fill(BRANCO)
    clock.tick(FPS)
