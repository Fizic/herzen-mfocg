import pygame


class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("sprites/person.png")
        self.rect = self.image.get_rect()
        self.rect.right
        self.speed = self.settings.player_speed
        self.airborne = True
        self.y_force = 0
        self.h_mov = None
        self.ground = None

    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.h_mov = "right"
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.h_mov = "left"
        if keys[pygame.K_UP] and not self.airborne:
            self.airborne = True
            self.y_force = -self.settings.jump_height
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.airborne:
            self.rect.y += self.y_force
            self.y_force += 1
        else:
            self.y_force = 0
        if self.ground:
            if self.rect.right < self.ground.left or self.rect.left > self.ground.right:
                self.airborne = True

        self._check_border()



    def render(self):
        """Рисует персонажа в текущей позиции"""

        self.screen.blit(self.image, self.rect)

    def _check_border(self):
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.airborne = False
            self.ground = self.screen.get_rect()
        if self.rect.top < 0:
            self.rect.top = 0

