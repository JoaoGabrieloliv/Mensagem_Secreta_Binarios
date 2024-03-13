import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Configurações da janela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missão Binária")

# Fontes
FONT = pygame.font.Font(None, 24)
SMALL_FONT = pygame.font.Font(None, 18)
BIG_FONT = pygame.font.Font(None, 36)

# Mensagem binária
binary_message = "01010011 01101111 01100011 01101111 01110010 01110010 01101111 00100000"

# Valores decimais correspondentes aos bits
decimal_values = [64, 32, 16, 8, 4, 2, 1]

# Lista para armazenar os valores decimais selecionados
selected_values = []

# Variável para controlar se a mensagem foi revelada
message_revealed = False

# Mensagem secreta
secret_message = ""

# Texto de regras
rules_text1 = "Para decifrar a mensagem, some os valores decimais dos bits selecionados."
rules_text2 = "Os valores decimais correspondem a potências de 2: 64, 32, 16, 8, 4, 2, 1."

# Função para desenhar a interface
def draw_interface():
    SCREEN.fill(WHITE)
    draw_story()
    draw_message()
    draw_decimal_buttons()
    draw_reveal_button()
    draw_rules()

# Função para desenhar a história
def draw_story():
    story_text1 = SMALL_FONT.render("Durante a guerra, um mensageiro", True, BLACK)
    story_text2 = SMALL_FONT.render("envia uma mensagem vital ao", True, BLACK)
    story_text3 = SMALL_FONT.render("comandante aliado através de seu cachorro,", True, BLACK)
    story_text4 = SMALL_FONT.render("Rex. A mensagem, escrita em sangue,", True, BLACK)
    story_text5 = SMALL_FONT.render("contém um código binário decimal que,", True, BLACK)
    story_text6 = SMALL_FONT.render("quando decifrado, revela a frase", True, BLACK)
    story_text7 = SMALL_FONT.render("'..........'", True, BLACK)
    x = (WIDTH - max([text.get_width() for text in [story_text1, story_text2, story_text3, story_text4, story_text5, story_text6, story_text7]])) / 2
    y = 50
    for text in [story_text1, story_text2, story_text3, story_text4, story_text5, story_text6, story_text7]:
        SCREEN.blit(text, (x, y))
        y += 20

# Função para desenhar a mensagem binária
def draw_message():
    if not message_revealed:
        x = (WIDTH - 20 * len(binary_message.split())) / 2
        y = 280
        for binary in binary_message.split():
            for i, bit in enumerate(binary):
                bit_text = SMALL_FONT.render("V" if bit == "1" else "F", True, BLACK)
                SCREEN.blit(bit_text, (x + i * 20, y))
            y += 20
    else:
        secret_text = BIG_FONT.render(f"Mensagem secreta: \"{secret_message}\"", True, BLACK)
        x = (WIDTH - secret_text.get_width()) / 2
        y = 280
        SCREEN.blit(secret_text, (x, y))

# Função para desenhar os botões decimais
def draw_decimal_buttons():
    if not message_revealed:
        x = 50
        y = 450
        button_width = 100
        button_height = 50
        for value in decimal_values:
            button_text = SMALL_FONT.render(str(value), True, BLACK)
            pygame.draw.rect(SCREEN, GRAY, (x, y, button_width, button_height))
            SCREEN.blit(button_text, (x + 10, y + 10))
            x += button_width + 10

# Função para desenhar o botão de revelação
def draw_reveal_button():
    if not message_revealed:
        reveal_button_text = SMALL_FONT.render("Revelar Mensagem", True, BLACK)
        pygame.draw.rect(SCREEN, GRAY, (300, 550, 200, 30))
        SCREEN.blit(reveal_button_text, (310, 555))

# Função para desenhar o texto de regras
def draw_rules():
    if not message_revealed:
        rules_text1_surface = SMALL_FONT.render(rules_text1, True, BLACK)
        rules_text2_surface = SMALL_FONT.render(rules_text2, True, BLACK)
        SCREEN.blit(rules_text1_surface, (50, 520))
        SCREEN.blit(rules_text2_surface, (50, 540))

# Função para verificar se o jogador clicou nos botões decimais
def check_button_click(pos):
    if not message_revealed:
        x = 50
        y = 450
        button_width = 100
        button_height = 50
        for value in decimal_values:
            rect = pygame.Rect(x, y, button_width, button_height)
            if rect.collidepoint(pos):
                selected_values.append(value)
                break
            x += button_width + 10

# Função para verificar se o jogador clicou no botão de revelação
def check_reveal_button_click(pos):
    global message_revealed
    if not message_revealed:
        reveal_button_rect = pygame.Rect(300, 550, 200, 30)
        if reveal_button_rect.collidepoint(pos):
            reveal_message()

# Função para revelar a mensagem
def reveal_message():
    global message_revealed, secret_message
    message_revealed = True
    # A mensagem secreta é "socorro"
    secret_message = "socorro"

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                check_button_click(event.pos)
                check_reveal_button_click(event.pos)

    draw_interface()
    pygame.display.flip()

pygame.quit()
sys.exit()