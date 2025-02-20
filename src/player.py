# src/player.py
import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))  # Placeholder rectangle
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071  # 1/sqrt(2)
            dy *= 0.7071  

        # Apply movement
        self.rect.x += dx
        self.rect.y += dy

        # Keep player within screen boundaries
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

