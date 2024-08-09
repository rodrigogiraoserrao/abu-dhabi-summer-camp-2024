import pygame
import sys  # We can use this to stop our program.

# Size of the screen in pixels.
SIZE = 400
BLOCK_SIZE = 30
# Create some colours in RGB:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen.
screen = pygame.display.set_mode((SIZE, SIZE))

# Fill the screen with white:
screen.fill(WHITE)
# Show the updates on the screen:
pygame.display.flip()

# Run the program forever.
block_x = 50
block_y = 60
# Run the program until the block leaves the screen.
while block_x < SIZE + BLOCK_SIZE:
    # Deal with the pygame events.
    for event in pygame.event.get():
        # If the user tried to leave...
        if event.type == pygame.QUIT:
            # ... stop the program.
            pygame.quit()
            sys.exit()

    # Fill screen with white to clear previous drawings.
    screen.fill(WHITE)
    # Move the block.
    block_x += 0.1
    # Draw the block in the new position.
    pygame.draw.rect(screen, BLACK, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
    # Update the screen.
    pygame.display.flip()
