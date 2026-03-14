import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    __clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    version = pygame.version.ver
    game_started = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

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

        pygame.display.flip()

        dt = __clock.tick(60) / 1000
        print(dt)
        

        

if __name__ == "__main__":
    main()
