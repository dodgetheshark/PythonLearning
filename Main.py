import pygame
from pygame.locals import *
from Characters import NPC, Player, Bullet


pygame.init()
pygame.font.init()

background = pygame.image.load('images/starsbackground.jpg')

clock = pygame.time.Clock()
screen = pygame.display.set_mode((540, 450))

spawn_num = 0
player = Player()
aliens = []
bullets = []
score = 0

while 1:
    clock.tick(10)
    if spawn_num == 0:
        for i in range(0, 5):
            aliens.append(NPC(75 + (i * 70), 10))
        spawn_num = 30

    spawn_num -= 1

    screen.blit(background, (0, 0))
    screen.blit(player.image, (player.x, player.y))

    for alien in aliens:
        alien.move_down()
        if alien.y >= 350:
            exit(0)
        screen.blit(alien.image, (alien.x, alien.y))

    for bullet in bullets:
        bullet.move()
        screen.blit(bullet.image, (bullet.x, bullet.y))

    for alien in aliens:
        alien_as_rect = Rect((alien.x, alien.y), (50, 29))
        for bullet in bullets:
            if alien_as_rect.collidepoint((bullet.x, bullet.y)):
                aliens.remove(alien)
                bullets.remove(bullet)
                score += 1

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move(True)
            elif event.key == K_RIGHT:
                player.move(False)
            elif event.key == K_SPACE:
                bullets.append(Bullet(player.x, player.y))

    pygame.display.set_caption('Python Space invaders - Score = %i' % score)
    pygame.display.flip()