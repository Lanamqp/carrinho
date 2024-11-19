import pygame
import random
import sys
from carro import Carro
from obstaculo import Obstaculo

# Inicializando o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo de Carro')

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Função para exibir a pontuação
def mostrar_pontuacao(pontos):
    fonte = pygame.font.SysFont("arial", 30)
    texto = fonte.render(f'Pontuação: {pontos}', True, BRANCO)
    tela.blit(texto, (10, 10))

# Função principal para o loop do jogo
def iniciar_jogo():
    # Criando o carro e os obstáculos
    jogador = Carro('assets/carro.png', 64, 64, 5)
    obstaculos = pygame.sprite.Group()
    todos_sprites = pygame.sprite.Group(jogador)

    clock = pygame.time.Clock()
    pontos = 0
    game_over = False

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentos do jogador
        teclas = pygame.key.get_pressed()  # Captura todas as teclas pressionadas
        jogador.update(teclas[pygame.K_LEFT], teclas[pygame.K_RIGHT], LARGURA)

        # Criação e movimentação dos obstáculos
        if random.randint(1, 20) == 1:
            obstaculo = Obstaculo('assets/obstaculo.png', 64, 64)
            obstaculos.add(obstaculo)
            todos_sprites.add(obstaculo)

        # Atualizando os obstáculos
        obstaculos.update()

        # Verificando colisões
        if pygame.sprite.spritecollide(jogador, obstaculos, False):
            game_over = True

        # Atualizando a pontuação
        pontos += 1

        # Desenhando a tela
        tela.fill(PRETO)
        todos_sprites.draw(tela)
        mostrar_pontuacao(pontos)

        pygame.display.update()
        clock.tick(60)

    mostrar_game_over(pontos)

# Função para exibir a tela de Game Over
def mostrar_game_over(pontos):
    fonte = pygame.font.SysFont("arial", 50)
    texto_game_over = fonte.render(f"Game Over! Pontuação: {pontos}", True, BRANCO)
    texto_game_over_rect = texto_game_over.get_rect(center=(LARGURA//2, ALTURA//2))

    while True:
        tela.fill(PRETO)
        tela.blit(texto_game_over, texto_game_over_rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
