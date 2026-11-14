import sys
import pygame

pygame.init()

WIDTH,HEIGHT = 600,800

pygame.display.set_caption('NewGame')
        
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.flip()

from object1 import *

class new():

    def main():
        
        running = True

        object1.wq.tj.n=1
        
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    new.main()
