import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boss Rush Game")

# Clock for managing frame rate
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    clock.tick(FPS)  # Maintain FPS
    screen.fill(WHITE)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update display

# Quit Pygame
pygame.quit()

