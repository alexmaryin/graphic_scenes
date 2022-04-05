import pygame


SX = 800
SY = 800


def process_graphics():
    pass


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SX, SY))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        process_graphics()
        pygame.display.flip()

    pygame.quit()
