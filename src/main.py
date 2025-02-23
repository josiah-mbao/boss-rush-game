# src/main.py
import pygame
from player import Player
from boss import Boss

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
boss = Boss(WIDTH // 2, HEIGHT // 4)  # Placing boss higher up

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.update_attack(event)  # Handle attack duration timeout

    # Get key states
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.attack(keys)  # Trigger melee attack

    # Check if the player's attack hits the boss
    player.check_attack_collision([boss])

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    player.draw(screen)
    boss.update()
    boss.draw(screen)
    pygame.display.flip()

pygame.quit()

