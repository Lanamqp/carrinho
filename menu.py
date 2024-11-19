import pygame
import sys
import jogo  # Importa o arquivo game.py para iniciar o jogo

# Configurações da tela e cores
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Menu do Jogo')
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Função para exibir o menu
def mostrar_menu():
    fonte = pygame.font.SysFont("arial", 50)
    texto_menu = fonte.render("Pressione ENTER para Iniciar", True, BRANCO)
    texto_rect = texto_menu.get_rect(center=(LARGURA//2, ALTURA//2))

    # Loop do menu
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Fechar o jogo corretamente

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Inicia o jogo quando pressionar ENTER
                    jogo.iniciar_jogo()  # Chama a função para iniciar o jogo
                    return  # Retorna para sair do menu

        # Preencher a tela com fundo preto e mostrar o menu
        tela.fill(PRETO)
        tela.blit(texto_menu, texto_rect)
        pygame.display.update()  # Atualiza a tela a cada iteração do lo
