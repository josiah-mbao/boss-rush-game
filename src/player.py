# src/player.py
import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)  # Placeholder rectangle
        self.color = (0, 255, 0)  # Green color for visibility
        self.speed = 5
        self.dash_speed = 12
        self.is_dashing = False
        self.dash_timer = 0
        self.max_dash_time = 10  # Frames (e.g., 10 frames at 60 FPS = ~0.16s)
        self.dash_cooldown = 30  # Frames before dashing again
        self.dash_cooldown_timer = 0
    def move(self, keys):
        dx, dy = 0, 0
        
        # Normal movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
        
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.71  # Approximate 1/sqrt(2) to keep speed consistent
            dy *= 0.71
        # Dashing Logic
        if keys[pygame.K_LSHIFT] and self.dash_cooldown_timer == 0:
            self.is_dashing = True
            self.dash_timer = self.max_dash_time
        if self.is_dashing:
            speed = self.dash_speed
            self.dash_timer -= 1
            if self.dash_timer <= 0:
                self.is_dashing = False
                self.dash_cooldown_timer = self.dash_cooldown
        else:
            speed = self.speed
            if self.dash_cooldown_timer > 0:
                self.dash_cooldown_timer -= 1
        # Apply movement
        self.rect.x += int(dx * speed)
        self.rect.y += int(dy * speed)

        # Keep player within screen boundaries
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
