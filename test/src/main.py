import pygame
import sys
from pygame.locals import *
from const import *

pygame.init()
pygame.display.set_caption('植物大战僵尸')

DS = pygame.display.set_mode(GAME_SIZE)
# image = pygame.image.load('pz/pic/other/back.png')
import image
import zombiebase
import peabullet
img = image.Image(PATH_BACK, 0, (0,0), GAME_SIZE, 0)
# img1 = image.Image('pz/pic/zombie/0/%d.png', 0, (1080, 200), (100,128), 15)
zom = zombiebase.ZombieBase('pz/pic/zombie/0/%d.png', 0, (1080, 200), (100,128), 15)
pea = peabullet.PeaBullet('pz/pic/other/peabullet.png', 0, (0, 200), (24, 24), 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
            # R红  G绿  B蓝
    DS.fill((255, 255, 255))
    # DS.blit(image, image.get_rect())
    img.draw(DS)
    zom.update()
    zom.draw(DS)
    pea.update()
    pea.draw(DS)
    pygame.display.update()