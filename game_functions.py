import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_events(settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event,settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,settings,screen,ship,bullets)

def update_screen(settings,screen,ship,aliens,bullets):
    screen.fill(settings.bg_color) 
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_keydown_events(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        ship.tu_default_posityon()
    elif event.key == pygame.K_SPACE:
        if len(bullets)< settings.bullets_allowed:    
            new_bullet1 = Bullet(settings,screen,ship)
            bullets.add(new_bullet1)

            new_bullet2 = Bullet(settings,screen,ship,centerx_factor=-15)
            bullets.add(new_bullet2)

def check_keyup_events(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def create_fleet(settings,screen,aliens):
    alien=Alien(settings,screen)
    alien_width=alien.rect.width
    available_aliens_x=settings.screen_width - 2 *alien_width
    number_aliens_x=int(available_aliens_x/(2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien=Alien(settings,screen)
        alien_x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien_x
        aliens.add(alien)