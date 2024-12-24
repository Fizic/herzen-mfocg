import pygame
from pygame.sprite import Sprite

class Coins(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load('sprites/coin.png')
        self.rect = self.image.get_rect()


