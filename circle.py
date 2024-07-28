from math import sin, cos, pi
import pygame


SIZE = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_pixel(screen, x, y, colour):
    x, y = int(x), int(y)
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            screen.set_at((x + dx, y + dy), colour)


def circle(percentage):
    return (
        SIZE // 2 + SIZE // 3 * cos(2 * pi * percentage),
        SIZE // 2 + SIZE // 3 * sin(2 * pi * percentage),
    )


screen = pygame.display.set_mode((SIZE, SIZE))
screen.fill(WHITE)

STEPS = 1000
step = 0
while step <= STEPS:
    percentage = step / STEPS
    x, y = circle(percentage)
    draw_pixel(screen, x, y, BLACK)
    step += 1
    pygame.display.flip()

input()
