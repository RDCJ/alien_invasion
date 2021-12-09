import sys
import pygame
import random
from bullet import Bullet
from alien import Alien

def fire(bullets, settings, ship):
    if settings.bullet_limit > 0:
        new_bullet = Bullet(settings, ship)
        bullets.add(new_bullet)
        settings.bullet_limit -= 1

def deal_keyup(event, ship, bullets):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.move_right = False
        elif event.key == pygame.K_LEFT:
            ship.move_left = False
        elif event.key == pygame.K_UP:
            ship.move_up = False
        elif event.key == pygame.K_DOWN:
            ship.move_down = False

def deal_keydown(event, ship, bullets, settings):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.move_right = True
        elif event.key == pygame.K_LEFT:
            ship.move_left = True
        elif event.key == pygame.K_UP:
            ship.move_up = True
        elif event.key == pygame.K_DOWN:
            ship.move_down = True
        elif event.key == pygame.K_SPACE:
            fire(bullets, settings, ship)
        elif event.key == pygame.K_q:
            sys.exit()

def deal_event(ship, bullets, aliens, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        deal_keydown(event, ship, bullets, settings)
        deal_keyup(event, ship, bullets)

def creat_new_alien(aliens, screen, settings):
    k1 = random.randint(1, 1000)
    if k1 > 997:
        new_alien = Alien(screen)
        new_alien.rect.centerx = random.randint(30, settings.width-30)
        aliens.add(new_alien)

def update_bullets(bullets, aliens, gamestats, settings):
    for bullet in bullets:
        bullet.update_position(settings)
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        gamestats.score += 1

def update_aliens(aliens, ship, settings):
    for alien in aliens:
        alien.update_position(settings)
    for alien in aliens.copy():
        if alien.rect.top > settings.height:
            aliens.remove(alien)
            ship.hp -= 1
    if pygame.sprite.spritecollide(ship, aliens, True):
        ship.hp -= 10
        if ship.hp < 1:
            ship.hp = 0

def update_screen(screen, settings, ship, bullets, alien, HP_record, SCORE_record):
    screen.fill(settings.color)
    ship.draw(screen)
    for bullet in bullets:
        bullet.draw(screen, settings)
    alien.draw(screen)
    HP_record.draw(screen)
    SCORE_record.draw(screen)
    pygame.display.flip()