import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('image\\ufo.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.top = screen.get_rect().top
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, settings):
        self.y += settings.alien_speed
        self.rect.top = self.y