import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing single alien in fleet."""

    def __init__(self, ai_settings, screen, stats):
        """Alien initialization. """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = self.check_image(stats)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Displays alien in its current position."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if alien is near to the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Motion of aliens."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_image(self, stats):
        if stats.game_difficulty == "normal":
            return pygame.image.load('images/polak.png')
        elif stats.game_difficulty == "hard":
            return pygame.image.load('images/polak-small.png')
        elif stats.game_difficulty == "easy":
            return pygame.image.load('images/polak-big.png')

