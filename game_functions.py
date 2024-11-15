import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(settings,stats,screen,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(settings,screen,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets)

        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event,settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(settings,screen,stats,ship,aliens,bullets,play_button):
    screen.fill(settings.bg_color) 
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(settings,screen,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(settings,screen,ship,aliens,bullets)

def check_bullet_alien_collision(settings,screen,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        settings.incraese_speed()
        create_fleet(settings,screen,ship,aliens)

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

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def create_fleet(settings,screen,ship,aliens):
    alien=Alien(settings,screen,name='first')

    number_aliens_x=get_number_aliens_x(settings,alien.rect.width)
    number_rows=get_number_rows(settings,ship.rect.height,alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(settings,alien_width):
    available_aliens_x=settings.screen_width - 2 *alien_width
    number_aliens_x=int(available_aliens_x/(2 * alien_width))
    return number_aliens_x-1

def create_alien(settings,screen,aliens,alien_number,row_number):
    alien=Alien(settings,screen,name=str(row_number)+"-"+str(alien_number))
    alien.rect.x=alien.rect.width+2*alien.rect.width*alien_number
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(settings,ship_height,alien_height):
    available_spase_y=(settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_spase_y/(2*alien_height))
    
    return 3 if number_rows > 3 else number_rows
    
def update_aliens(settings,stats,screen,ship,aliens,bullets):
    check_aliens_bottom(settings,stats,screen,ship,aliens,bullets)
    
    check_fleet_edges(settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!!")
        
def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_diriction(settings,aliens)
            break
    
def change_fleet_diriction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def ship_hit(settings,stats,screen,ship,aliens,bullets):
    if stats.ship_left > 0:
        stats.ship_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(False)

def check_aliens_bottom(settings,stats,screen,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,stats,screen,ship,aliens,bullets)
            break

def check_play_button(settings,screen,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settngs()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        aliens.empty()
        bullets.empty()

        create_fleet(settings,screen,ship,aliens)
        ship.center_ship()