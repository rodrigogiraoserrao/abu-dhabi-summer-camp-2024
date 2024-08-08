import pygame
import sys  # We can use this to stop our program.

# Size of the screen in pixels.
SIZE = 400
# Create some colours in RGB:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen.
screen = pygame.display.set_mode((SIZE, SIZE))

# Fill the screen with white:
screen.fill(WHITE)
# Show the updates on the screen:
pygame.display.flip()

# Run the program forever.
while True:
    # Ask pygame for the clicks:
    for event in pygame.event.get():
        # If the user tried to leave...
        if event.type == pygame.QUIT:
            # ... stop the program.
            pygame.quit()
            sys.exit()
        # Did the user press a key?
        elif event.type == pygame.KEYDOWN:
            print("Key press!")
            # Did the user press the up arrow?
            if event.dict["key"] == pygame.K_UP:
                # Fill the screen with red.
                screen.fill(RED)
                pygame.display.flip()
            # Did the user press the down arrow?
            elif event.dict["key"] == pygame.K_DOWN:
                # Fill the screen with blue.
                screen.fill(BLUE)
                pygame.display.flip()
            # If you press any other key:
            else:
                screen.fill(WHITE)
                pygame.display.flip()
