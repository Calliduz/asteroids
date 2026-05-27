import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    

    while running:
        #logging
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
