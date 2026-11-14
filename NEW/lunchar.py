try:
    import pygame
except ModuleNotFoundError:
    os.system('pip3 install pygame')
except:
    print('缺少对应模块,无法运行爽文修真!')
    input()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('爽文修真')
screen.fill((255,255,255))
font_fangsong = pygame.font.match_font('fangsong')
font = pygame.font.Font(font_fangsong,20)

font_1 = font.render('加 载 中 . . .',True,'black')

screen.blit(font_1,(352.5,170))

pygame.display.flip()

from object1 import *
from set_object import *
import os
import json
import random
import time
import sys

class swxz():
    screen_type = 'root'

    def set_root():
        font_big = pygame.font.Font(font_fangsong,60)
        font_mid = pygame.font.Font(font_fangsong,40)
        screen.fill((255,255,255))
        swxz.screen_type = 'root'
        font0 = font_mid.render('主 页',True,'black')
        font1 = font.render('   单 人 游 戏   ',True,'white',(150,150,150))
        font2 = font.render('   多 人 游 戏   ',True,'white',(150,150,150))
        font3 = font.render(' 墓 地 ',True,'white',(150,150,150))
        font4 = font.render(' 设 置 ',True,'white',(150,150,150))
        font5 = font.render('   退 出 游 戏   ',True,'white',(150,150,150))
        font6 = font_big.render('爽 文 修 真',True,'black')
        
        screen.blit(font0,(352.5,170))
        screen.blit(font1,(315,230))
        screen.blit(font2,(315,270))
        screen.blit(font3,(315,310))
        screen.blit(font4,(410,310))
        screen.blit(font5,(315,350))
        screen.blit(font6,(240,80))

        pygame.display.flip()
    
    def main():
        swxz.set_root()
        while True:
            for event in pygame.event.get():
                if swxz.screen_type == 'root':
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = event.pos
                        if 315<=pos[0]<=485 and 350<=pos[1]<=370:
                            pygame.quit()
                            sys.exit()

if __name__ == '__main__':
    swxz.main()
