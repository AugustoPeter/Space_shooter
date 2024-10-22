import pygame
from os.path import join
from random import  randint

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGH = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption('Starship Game')
running = True

player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGH / 2))
player_direction = 1

star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGH))  for i in range(20)]

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGH / 2))

laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
lase_rect = laser_surface.get_frect(bottomleft = (20, WINDOW_HEIGH - 20))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('indianred4')

    for position in star_position:
        display_surface.blit(star_surface, position)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, lase_rect)

    #player moviment
    player_rect.x += player_direction * 0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1

    display_surface.blit(player_surface, player_rect)


    pygame.display.update()


pygame.quit()