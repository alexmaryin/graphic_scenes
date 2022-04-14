import math
import random

import pygame

SX = 1360
SY = 760

CIRCLE_COUNT = 100
STEP_RADIUS = 10
STEP_COLOR = (255 - 10) / CIRCLE_COUNT
DOTS_IN_CIRCLE = 100


def draw_circle(circle: list[int, int, int, int]):
    alpha = 0
    step = math.pi * 2 / DOTS_IN_CIRCLE
    while alpha < math.pi * 2:
        s_x = round(circle[0] + math.sin(alpha) * circle[2])
        s_y = round(circle[1] + math.cos(alpha) * circle[2] / 1.5)
        color = round(circle[3])
        if 0 < s_x < SX and 0 < s_y < SY:
            pygame.draw.circle(screen, (color, color, color), (s_x, s_y), 2)
        alpha += step


dist = 0.05
circles = [[SX // 2, SY // 2, 100, 10] for _ in range(CIRCLE_COUNT)]
make_rib = random.randint(0, 10)


def process_graphics():
    screen.fill((0, 0, 0))

    for i in range(len(circles) - 2, -1, -1):
        c = circles[i]
        c[2] += STEP_RADIUS
        c[3] += STEP_COLOR
        circles[i + 1] = c
        draw_circle(c)

    global dist, make_rib

    sx = SX // 2 + math.sin(dist) * 50.0 + (random.randint(-5, 5) if make_rib == 0 else 0)
    sy = SY // 2 + math.sin(dist) * 35.0 + (random.randint(-5, 5) if make_rib == 0 else 0)

    circles[0] = [sx, sy, 100, 10]
    dist += 0.05
    make_rib -= 1
    if make_rib == -1:
        make_rib = random.randint(0, 10)


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
