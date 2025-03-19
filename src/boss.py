import pygame


class Boss:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 60)  # Placeholder size
        self.color = (255, 0, 0)  # Red color for visibility
        self.health = 100
        self.speed = 3
        self.attack_range = 100  # Range within which the boss will attack
        self.attack_cooldown = 1.5  # Time between attacks in seconds
        self.last_attack_time = 0
        self.hit_timer = 0  # Timer to show hit effect
        self.target = None  # Player target

    def take_damage(self, amount):
        self.health -= amount
        self.hit_timer = 10  # Flash white for a few frames
        print(f"Boss took {amount} damage! Health: {self.health}")
        if self.health <= 0:
            print("Boss defeated!")

    def move_towards_player(self):
        """ Moves the boss towards the player if within range """
        if self.target:
            # Calculate direction towards the player
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Avoid div by 0

            # Normalize direction and apply speed
            dx /= distance
            dy /= distance
            self.rect.x += int(dx * self.speed)
            self.rect.y += int(dy * self.speed)

    def attack(self):
        """ Simulate an attack if within range """
        if (self.target and self.rect.colliderect(self.target.rect) and
            (pygame.time.get_ticks() - self.last_attack_time) >
                self.attack_cooldown * 1000):
            self.last_attack_time = pygame.time.get_ticks()
            print("Boss attacked!")

    def update(self):
        """ Update the boss logic """
        # Update hit effect timer
        if self.hit_timer > 0:
            self.hit_timer -= 1

        self.move_towards_player()
        self.attack()

    def draw(self, screen):
        """ Draw the boss on the screen """
        color = (255, 255, 255) if self.hit_timer > 0 else self.color
        pygame.draw.rect(screen, color, self.rect)
