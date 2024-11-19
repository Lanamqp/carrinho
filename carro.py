import pygame

class Carro(pygame.sprite.Sprite):
    def __init__(self, image, largura, altura, velocidade):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largura, altura))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)  # Posição inicial do carro
        self.velocidade = velocidade

    def update(self, tecla_esquerda, tecla_direita, largura_tela):
        # Movimentos do carro com base nas teclas pressionadas
        if tecla_esquerda:
            self.rect.x -= self.velocidade
        if tecla_direita:
            self.rect.x += self.velocidade

        # Impedindo o carro de sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > largura_tela:
            self.rect.right = largura_tela
