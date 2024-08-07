import pygame

# Size of the screen in pixels.
SIZE = 800
# Create some colours in RGB:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen.
screen = pygame.display.set_mode((SIZE, SIZE))

# Fill the screen with white:
screen.fill(WHITE)
# Draw a black circle on the screen:
pygame.draw.circle(screen, BLACK, (150, 350), 100, 3)
# Show the updates on the screen:
pygame.display.flip()

# Pause the program.
input()
