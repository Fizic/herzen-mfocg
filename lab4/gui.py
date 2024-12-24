import pygame

class GUI:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.width, self.height = 200, 50
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 20)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen.get_rect().topright

    def render(self):
        self.msg_image = self.font.render(f"coins: {self.game.coins}", True, self.text_color, (255, 255, 255))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)
