import random
import pygame


SX = 1440
SY = 900
num_stars = 200
speed = 0.4
radius_delta = 0.005


def new_star():
    return [random.randint(0, SX) - SX // 2, random.randint(0, SY) - SY // 2, 256, 0, 2]


def off_screen(x, y, z):
    return z <= 0 or x <= -SX//2 or x >= SX//2 or y <= -SY//2 or y >= SY//2


stars = [new_star() for _ in range(0, num_stars)]


def process_graphics(screen):
    screen.fill((0, 0, 0))
    x = y = 0
    for i in range(0, num_stars):
        s = stars[i]
        x = s[0] * 256 / s[2]
        y = s[1] * 256 / s[2]
        s[2] -= speed
        s[4] += radius_delta
        if off_screen(x, y, s[2]):
            s = new_star()
        if s[3] < 256:
            s[3] += 0.15
        if s[3] >= 256:
            s[3] = 255
        stars[i] = s
        x = round(s[0] * 256 / s[2]) + SX//2
        y = round(s[1] * 256 / s[2]) + SY//2
        pygame.draw.circle(screen, (s[3], s[3], s[3]), (x, y), s[4])


if __name__ == '__main__':
    pygame.init()
    _screen = pygame.display.set_mode((SX, SY))
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        process_graphics(_screen)
        pygame.display.flip()
        clock.tick()
        pygame.display.set_caption(f'FPS: {round(clock.get_fps())}')


    pygame.quit()
