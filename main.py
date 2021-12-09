import setting
from ship import Ship
from game_function import *
from pygame.sprite import Group
from numboard import Numboard
from game_stat import GameStats

def run_game():
    pygame.init()
    settings = setting.Setting()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Alien Invasion")
    gamestats = GameStats(settings)
    shipA = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    HP_record = Numboard("HP:", shipA.hp, 10, settings, screen)
    SCORE_record = Numboard("SCORE:", 0, 100, settings, screen)

    while True:
        creat_new_alien(aliens, screen, settings)
        deal_event(shipA, bullets, aliens, settings)
        shipA.update_position(settings, screen)
        update_bullets(bullets, aliens, gamestats, settings)
        update_aliens(aliens, shipA, settings)
        HP_record.update_num(shipA.hp, settings)
        SCORE_record.update_num(gamestats.score, settings)
        update_screen(screen, settings, shipA, bullets, aliens, HP_record, SCORE_record)

run_game()