# `sleep` can pause a program.
from time import sleep
import pygame

# Size of the screen in pixels.
SIZE = 800
# Create some colours in RGB:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 150)

# Create the screen.
screen = pygame.display.set_mode((SIZE, SIZE))

# Fill the screen with white:
screen.fill(WHITE)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program for 1s
sleep(1)

# Fill the screen with BLACK:
screen.fill(BLACK)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program for 1s
sleep(1)

# Fill the screen with red:
screen.fill(RED)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program for 1s
sleep(1)

# Fill the screen with green:
screen.fill(GREEN)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program for 1s
sleep(1)

# Fill the screen with blue:
screen.fill(BLUE)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program.
input()
