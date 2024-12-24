import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
    def __init__(self, ai_game, x1, y1, x2, y2):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.platform_color

        x2, x1 = max(x1, x2), min(x1, x2)
        y2, y1 = max(y1, y2), min(y1, y2)
        print(x1, x2)
        self.rect = pygame.Rect(x1, y1, x2-x1, y2-y1)

    def update(self) -> None:
        self.render()

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

