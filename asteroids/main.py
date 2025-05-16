import pygame
from constants import *
from player import Player


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user closes the window
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.flip()
        

        clock.tick(60)
        dt = clock.get_time()/1000

if __name__ == "__main__":
    main()