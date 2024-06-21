import pygame
import sys
from pygame.locals import *
from const import *

pygame.init()
pygame.display.set_caption('植物大战僵尸')

DS = pygame.display.set_mode(GAME_SIZE)

import image
import zombiebase
import peabullet
img = image.Image(PATH_BACK, 0, (0,0), GAME_SIZE, 0)
pea = peabullet.PeaBullet( 0, (0, 200))
zom = zombiebase.ZombieBase( 1, (1080, 200))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
            # R红  G绿  B蓝
    DS.fill((255, 255, 255))
    img.draw(DS)
    zom.update()
    zom.draw(DS)
    pea.update()
    pea.draw(DS)
    pygame.display.update()