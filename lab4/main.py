import pygame
import sys
from settings import Settings
from player import Player
from platforms import Platform
from gui import GUI
import coins
from portals import Portals

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("LR4")
        self.portals = Portals(self)
        self.portals.set_portal((200, 200))
        self.portals.set_portal((300, 300))
        self.coins = 0
        self.coins_sprites = pygame.sprite.Group()
        self.gui = GUI(self)
        self.platforms = pygame.sprite.Group()
        for i in range(5):
            self.platforms.add(Platform(self, 50 + 250*i, self.screen.get_height() - 50 - 100*i, 200 + 250*i, - 50 + self.screen.get_height() - 100 - 100*i))
        self.enemies = pygame.sprite.Group()

        self.player = Player(self)

    def run_game(self):
        while True:
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self._check_events()
            self._check_platform_collide()
            self._check_coin_collide()
            self.portals.update()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._spawn_coin(mouse_pos)

    
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.player.render()
        self.platforms.update()
        self.enemies.update()
        self.coins_sprites.draw(self.screen)
        self.portals.update()
        self.gui.render()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_1:
            mouse_pos = pygame.mouse.get_pos()
            self.portals.set_portal(mouse_pos)

    def _check_platform_collide(self):
        collisions = pygame.sprite.spritecollideany(self.player, self.platforms)
        if collisions:

            top = self.player.rect.bottom - collisions.rect.top - self.player.y_force
            bottom = -self.player.rect.top + collisions.rect.bottom
            left = self.player.rect.right - collisions.rect.left
            right = -self.player.rect.left + collisions.rect.right

            if bottom < left and bottom < right and bottom < top:
                self.player.rect.top = collisions.rect.bottom
                self.player.y_force = 0
            elif left < right and left < top:
                self.player.rect.right = collisions.rect.left
            elif right < top:
                self.player.rect.left = collisions.rect.right
            else:
                self.player.rect.bottom = collisions.rect.top
                self.player.airborne = False
                self.player.ground = collisions.rect

    def _check_coin_collide(self):
        collision = pygame.sprite.spritecollideany(self.player, self.coins_sprites)
        if collision:
            self.coins +=1
            self.coins_sprites.remove(collision)

    def _spawn_coin(self, mouse_pos):
        coin = coins.Coins(self)
        coin.rect.center = mouse_pos
        self.coins_sprites.add(coin)




if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()