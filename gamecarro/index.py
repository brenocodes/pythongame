import pygame
import pygame.locals
import random
import pygame.font

pygame.init()
x = 400
y = 400
v = 10
y1 = 0
v1 = -20
fundo = pygame.image.load('gamecarro/img/Estrada.png')
pista1 = pygame.image.load('gamecarro/img/estrada.jpg')
carro = pygame.image.load('gamecarro/img/f1.png')
carro = pygame.transform.scale(carro, (100,150))

carro_1 = pygame.image.load('gamecarro/img/carro1.png')
largura_carro1 = 50  # Largura desejada para o carro_1
altura_carro1 = 100  # Altura desejada para o carro_1
carro_1 = pygame.transform.scale(carro_1, (largura_carro1, altura_carro1))
carro_1_x = 150  # Posição inicial no eixo x
carro_1_y = random.randint(-altura_carro1, -100)  # Posição inicial aleatória no eixo y

carro_2 = pygame.image.load('gamecarro/img/carro2.png')
largura_carro2 = 50  # Largura desejada para o carro_2
altura_carro2 = 100  # Altura desejada para o carro_2
carro_2 = pygame.transform.scale(carro_2, (largura_carro2, altura_carro2))
carro_2_x = 400  # Posição inicial no eixo x
carro_2_y = random.randint(-altura_carro2, -100)  # Posição inicial aleatória no eixo y

pixel_font = pygame.font.Font('gamecarro/font/pixel-font.ttf',80) # Adicionando fonte pixel

janela = pygame.display.set_mode((1050, 650))
pygame.display.set_caption('jogo parte 1')

# Cria um novo elemento HTML para exibir a distância percorrida
distance_element = pygame.font.SysFont('Arial', 30).render('Distância: 0m', True, (255, 255, 255))
distance_rect = distance_element.get_rect(center=(janela.get_width() // 2, 50))

game_over_font = pygame.font.SysFont('Arial', 80)
game_over_text = pixel_font.render('Game Over', True, (255, 255, 255))
game_over_rect = game_over_text.get_rect(center=(janela.get_width() // 2, janela.get_height() // 2))

distance = 0  
speed = 20
increase_rate = 800  # Taxa de aumento de velocidade de descida do fundo

janela_aberta = True
game_over = False

while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y > 10:  # Verifica se a posição y é maior que 10
        y -= speed
    if comandos[pygame.K_DOWN] and y < 500:  # Verifica se a posição y é menor que 500
        y += speed
    if comandos[pygame.K_RIGHT] and x < 700:  # Verifica se a posição x é menor que o limite
        x += speed
    if comandos[pygame.K_LEFT] and x > 100:  # Verifica se a posição x é maior que 100
        x -= speed
    
    y1 += speed  
    if y1 >= 0:  
        y1 = -700

    distance += speed * 10 
    if distance < 1000000000000000000000000000000000000000000:  
        speed += distance // 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    else:  
        speed += speed * increase_rate
        y1 += speed
    if y1 >= 0:
        y1 = -700
    distance_element = pygame.font.SysFont('Arial', 30).render(f'Distância: {int(distance)}m', True, (255, 255, 255))

    carro_1_speed = 100
    carro_2_speed = 130

 # Verifica a colisão com carro_1
    carro_1_rect = pygame.Rect(carro_1_x, carro_1_y, largura_carro1, altura_carro1)
    jogador_rect = pygame.Rect(x, y, carro.get_width(), carro.get_height())
    if carro_1_rect.colliderect(jogador_rect):
        game_over = True
        speed = 0  # Para o movimento do jogador
        carro_1_speed = 0
        carro_2_speed = 0

    # Verifica a colisão com carro_2
    carro_2_rect = pygame.Rect(carro_2_x, carro_2_y, largura_carro2, altura_carro2)
    if carro_2_rect.colliderect(jogador_rect):
        game_over = True
        speed = 0  # Para o movimento do jogador
        carro_2_speed = 0
        carro_1_speed = 0
    carro_1_y += carro_1_speed
    if carro_1_y > janela.get_height():
        carro_1_y = random.randint(-altura_carro1, -100)

    carro_2_y += carro_2_speed
    if carro_2_y > janela.get_height():
        carro_2_y = random.randint(-altura_carro2, -100)

   

    janela.blit(fundo, (0, y1))  
    janela.blit(distance_element, distance_rect)
    janela.blit(carro, (x+500, y))
    janela.blit(carro_1, (carro_1_x, carro_1_y))
    janela.blit(carro_2, (carro_2_x, carro_2_y))

    if game_over:
        # Define as dimensões do retângulo de fundo
        game_over_bg_rect = pygame.Rect(janela.get_width() // 2 - 200, janela.get_height() // 2 - 50, 400, 100)
        # Preenche o retângulo de fundo com a cor vermelha
        pygame.draw.rect(janela, (255, 0, 0), game_over_bg_rect, border_radius=10)
        # Centraliza o texto "Game Over" dentro do retângulo de fundo
        game_over_rect.center = game_over_bg_rect.center
        # Desenha o texto "Game Over" no centro do retângulo de fundo
        janela.blit(game_over_text, game_over_rect)

        janela.blit(game_over_text, game_over_rect)

        

    pygame.display.update()