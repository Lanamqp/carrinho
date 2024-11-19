import pygame
import random

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, image, largura, altura):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largura, altura))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - largura)  # Posição inicial aleatória em X
        self.rect.y = -altura  # Começa fora da tela, no topo
        self.velocidade = 5  # Velocidade fixa para todos os obstáculos

    def update(self):
        # Movimento do obstáculo: ele cai para baixo (todos se movendo com a mesma velocidade)
        self.rect.y += self.velocidade
        
        # Se o obstáculo sair da tela (fora da parte inferior), ele deve ser removido
        if self.rect.top > 600:
            self.kill()  # Remove o obstáculo do grupo de sprites
