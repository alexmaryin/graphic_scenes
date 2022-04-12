import pygame


SX = 1360
SY = 760


def process_graphics():
    pass


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SX, SY))
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        process_graphics()
        pygame.display.flip()
        clock.tick()
        pygame.display.set_caption(f'FPS: {round(clock.get_fps())}')

    pygame.quit()
