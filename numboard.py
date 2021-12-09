import pygame.font

class Numboard():
    def __init__(self, text, num, position, settings, screen):
        self.text = text
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("微软雅黑", 30)
        self.update_num(num, settings)
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_rect().left+position
        self.rect.top = 10

    def update_num(self, num, settings):
        self.num = num
        self.score_str = self.text + str(self.num)
        self.image = self.font.render(self.score_str, True, self.text_color, settings.color)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
