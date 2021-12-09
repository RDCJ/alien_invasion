import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, ship):
        super().__init__()
        self.rect = pygame.Rect(ship.rect.centerx-settings.bullet_width/2, ship.rect.top, settings.bullet_width, settings.bullet_height)
        self.y = float(self.rect.top)

    def draw(self, screen, settings):
        pygame.draw.rect(screen, settings.bullet_color, self.rect)

    def update_position(self, settings):
        self.y -= settings.bullet_speed
        self.rect.top = self.y