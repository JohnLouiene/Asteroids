import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    __clock = pygame.time.Clock()
    dt = 0
    time_elapsed = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    version = pygame.version.ver
    game_started = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    #Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #Asteroid field object
    asteroid_field = AsteroidField()

    while game_started == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #Object rendering
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Score: {time_elapsed:.2f} seconds")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                
        pygame.display.flip()

        dt = __clock.tick(60) / 1000
        time_elapsed += dt
        
if __name__ == "__main__":
    main()
