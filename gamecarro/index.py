import pygame
import random

pygame.init()
x = 400
y = 400
v = 10
y1 = 0
v1 = -20
fundo = pygame.image.load('img/estrada.png')
pista1 = pygame.image.load('img/estrada.png')
pista2 = pygame.image.load('img/asfalto.png')
carro = pygame.image.load('img/f1.png')
carro = pygame.transform.scale(carro, (100, 150))

carro_1 = pygame.image.load('img/carro1.png')
largura_carro1 = 50  # Largura desejada para o carro_1
altura_carro1 = 100  # Altura desejada para o carro_1
carro_1 = pygame.transform.scale(carro_1, (largura_carro1, altura_carro1))
carro_1_x = 150  # Posição inicial no eixo x
carro_1_y = random.randint(-altura_carro1, -100)  # Posição inicial aleatória no eixo y

carro_2 = pygame.image.load('img/carro2.png')
largura_carro2 = 50  # Largura desejada para o carro_2
altura_carro2 = 100  # Altura desejada para o carro_2
carro_2 = pygame.transform.scale(carro_2, (largura_carro2, altura_carro2))
carro_2_x = 400  # Posição inicial no eixo x
carro_2_y = random.randint(-altura_carro2, -100)  # Posição inicial aleatória no eixo y

carro_3 = pygame.image.load('img/carro3.png')
largura_carro_3 = 50  # Largura desejada para o carro_3
altura_carro_3 = 100  # Altura desejada para o carro_3
carro_3 = pygame.transform.scale(carro_3, (largura_carro_3, altura_carro_3))
carro_3_x = 600 # Posição inicial no eixo x
carro_3_y = random.randint(-altura_carro_3, -100)  # Posição inicial aleatória no eixo y
carro_3_speed = 20  # Velocidade do carro 3

pixel_font = pygame.font.Font('font/pixel-font.ttf', 80)  # Adicionando fonte pixel
fonte_botao = pygame.font.SysFont('font/pixel-font.ttf', 40)

janela = pygame.display.set_mode((1050, 650))
pygame.display.set_caption('jogo parte 1')

distance_element = pygame.font.SysFont('Arial', 30).render('Distância: 0m', True, (255, 255, 255))
distance_rect = distance_element.get_rect(center=(janela.get_width() // 2, 50))
# Cria um botão para iniciar o jogo
texto_botao = pixel_font.render('Start', True, (255, 255, 255))
retangulo_botao = texto_botao.get_rect(center=(1050 // 2, 650 // 2))

game_over_font = pygame.font.SysFont('Arial', 80)
game_over_text = pixel_font.render('Game Over', True, (255, 255, 255))
game_over_rect = game_over_text.get_rect(center=(janela.get_width() // 2, janela.get_height() // 2))

restart_text = pixel_font.render('Restart', True, (0, 0, 255))
restart_rect = restart_text.get_rect(center=(1050 // 2, 650 // 2 + 100))

distance = 0
speed = 40
increase_rate = 110  # Taxa de aumento de velocidade de descida do fundo

# Estados do jogo
tela_inicial = True
jogando = False
game_over = False

while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if tela_inicial:
        janela.fill((0, 0, 0))
        janela.blit(texto_botao, retangulo_botao)

    if pygame.mouse.get_pressed()[0]:
        posicao_mouse = pygame.mouse.get_pos()
        if retangulo_botao.collidepoint(posicao_mouse) and not jogando:
            tela_inicial = False
            jogando = True
            game_over = False
            distance = 0
            speed = 40
            carro_1_y = random.randint(-altura_carro1, -100)
            carro_2_y = random.randint(-altura_carro2, -100)
            carro_3_y = random.randint(-altura_carro_3, -100)

    if jogando:
        pygame.time.delay(50)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP] and y > 10:  # Verifica se a posição y é maior que 10
            y -= speed
        if comandos[pygame.K_DOWN] and y < 500:  # Verifica se a posição y é menor que 500
            y += speed
        if comandos[pygame.K_RIGHT] and x < 850:  # Verifica se a posição x é menor que o limite
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

        carro_1_speed = 50
        carro_2_speed = 20

        jogador_rect = pygame.Rect(x, y, carro.get_width(), carro.get_height())

        # Verifica a colisão com carro_1
        carro_1_rect = pygame.Rect(carro_1_x, carro_1_y, largura_carro1, altura_carro1)
        if carro_1_rect.colliderect(jogador_rect):
            game_over = True
            speed = 0  # Para o movimento do jogador
           
            carro_1_speed = 0
            carro_2_speed = 0
            carro_3_speed = 0

        # Verifica a colisão com carro_2
        carro_2_rect = pygame.Rect(carro_2_x, carro_2_y, largura_carro2, altura_carro2)
        if carro_2_rect.colliderect(jogador_rect):
            game_over = True
            speed = 0  # Para o movimento do jogador
            carro_1_speed = 0
            carro_2_speed = 0
            carro_3_speed = 0

        # Verifica a colisão com carro_3
        carro_3_rect = pygame.Rect(carro_3_x, carro_3_y, largura_carro_3, altura_carro_3)
        if carro_3_rect.colliderect(jogador_rect):
            game_over = True
            speed = 0  # Para o movimento do jogador
            carro_1_speed = 0
            carro_2_speed = 0
            carro_3_speed = 0

        carro_1_y += carro_1_speed
        if carro_1_y > janela.get_height():
            carro_1_y = random.randint(-altura_carro1, -100)

        carro_2_y += carro_2_speed
        if carro_2_y > janela.get_height():
            carro_2_y = random.randint(-altura_carro2, -100)

        carro_3_y += carro_3_speed
        if carro_3_y > janela.get_height():
            carro_3_y = random.randint(-altura_carro_3, -100)

        janela.blit(fundo, (0, y1))
        janela.blit(distance_element, distance_rect)
        janela.blit(carro, (x, y))
        janela.blit(carro_1, (carro_1_x, carro_1_y))
        janela.blit(carro_2, (carro_2_x, carro_2_y))
        janela.blit(carro_3, (carro_3_x, carro_3_y))

        if game_over:
            game_over_bg_rect = pygame.Rect(janela.get_width() // 2 - 200, janela.get_height() // 2 - 50, 400, 100)
            pygame.draw.rect(janela, (255, 0, 0), game_over_bg_rect, border_radius=10)
            janela.blit(game_over_text, game_over_rect)
            janela.blit(restart_text, restart_rect)

        if game_over and pygame.mouse.get_pressed()[0]:
            posicao_mouse = pygame.mouse.get_pos()
            if restart_rect.collidepoint(posicao_mouse):
                game_over = False
                distance = 0
                speed = 40
                carro_1_y = random.randint(-altura_carro1, -100)
                carro_2_y = random.randint(-altura_carro2, -100)
                carro_3_y = random.randint(-altura_carro_3, -100)

    pygame.display.update()
