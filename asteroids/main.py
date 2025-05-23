import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init

    #initialization code/boilerplate
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containters = (drawable, updatable)
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #add player after group containment
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    asteroid_field = AsteroidField()

    #game loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user closes the window
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        for a in asteroids:
            if player.collisions(a) == True:
                print("Game over!")
                return

        pygame.display.flip()
        

        clock.tick(60)
        dt = clock.get_time()/1000

if __name__ == "__main__":
    main()