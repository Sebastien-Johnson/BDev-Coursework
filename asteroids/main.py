import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()

    print("Starting Asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    #add player after group containment

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    
    dt = 0

    #game loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user closes the window
                return
            
        dt = clock.tick(60) / 1000

        for obj in updatable:
            obj.update(dt)

        
        for a in asteroids:
            if a.collisions(player):
                print("Game over!")
                return
            
        for a in asteroids:
            for s in shots:
                if a.collisions(s):
                    s.kill()
                    a.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()