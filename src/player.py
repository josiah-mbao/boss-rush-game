# src/player.py
import pygame
import time

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
        
        # Attack properties
        self.is_attacking = False
        self.attack_cooldown = 0.25  # Seconds
        self.last_attack_time = 0
        self.attack_hitbox = None  # Stores the hitbox for an active attack

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

    def attack(self, keys):
        """ Handles melee attack logic """
        if keys[pygame.K_SPACE] and not self.is_attacking and (time.time() - self.last_attack_time > self.attack_cooldown):
            self.is_attacking = True
            self.last_attack_time = time.time()
        
        # Attack hitbox
            hitbox_width = 60
            hitbox_height = 20
            knockback_force = 10  # How far the player is pushed back

            self.attack_hitbox = pygame.Rect(self.rect.right, self.rect.y + 10, hitbox_width, hitbox_height)
            self.rect.x -= knockback_force  # Push player back slightly

            # Prevent knockback from going off-screen
            self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))

            # Simulate attack duration
            pygame.time.set_timer(pygame.USEREVENT, 200)  # Attack lasts 200ms

    def update_attack(self, event):
        """ Ends the attack when the timer expires """
        if event.type == pygame.USEREVENT:
            self.is_attacking = False
            self.attack_hitbox = None

    def check_attack_collision(self, enemies):
        """ Checks if the attack hitbox collides with any enemies """
        if self.attack_hitbox:
            for enemy in enemies:
                if self.attack_hitbox.colliderect(enemy.rect):
                    enemy.take_damage(10)  # Example damage value

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Draw attack hitbox if attacking
        if self.is_attacking and self.attack_hitbox:
            pygame.draw.rect(screen, (255, 0, 0), self.attack_hitbox, 2)  # Red outline for attack hitbox

