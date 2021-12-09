import pygame
import sys

class Ship():
    def __init__(self, settings, screen):
        self.image = pygame.image.load('image\space ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.hp = settings.ship_hp

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, settings, screen):
        if self.move_left and self.x > 20:
            self.x -= settings.ship_speed
        if self.move_right and self.x < screen.get_rect().right-20:
            self.x += settings.ship_speed
        if self.move_up and self.y > 80:
            self.y -= settings.ship_speed
        if self.move_down and self.y < screen.get_rect().bottom:
            self.y += settings.ship_speed
        self.rect.centerx = self.x
        self.rect.bottom = self.y
        if self.hp < 1:
            sys.exit()