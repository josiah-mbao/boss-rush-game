import pygame

class Boss:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 60)  # Placeholder enemy size
        self.color = (255, 0, 0)  # Red for visibility
        self.health = 100
        self.hit_timer = 0  # Timer to show hit effect

    def take_damage(self, amount):
        self.health -= amount
        self.hit_timer = 10  # Flash white for a few frames
        print(f"Boss took {amount} damage! Health: {self.health}")
        if self.health <= 0:
            print("Boss defeated!")

    def update(self):
        # Reduce hit effect timer
        if self.hit_timer > 0:
            self.hit_timer -= 1

    def draw(self, screen):
        # Flash white if recently hit
        color = (255, 255, 255) if self.hit_timer > 0 else self.color
        pygame.draw.rect(screen, color, self.rect)

