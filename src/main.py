# src/main.py
import pygame
from player import Player

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boss Rush Game")

# Load assets
player = Player(WIDTH // 2, HEIGHT // 2)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key states
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    player.draw(screen)
    pygame.display.flip()

pygame.quit()

