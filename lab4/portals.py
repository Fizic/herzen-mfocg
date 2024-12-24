import pygame
from pygame.sprite import Sprite


class Portals(Sprite):
    portals_colors = {
        1: (255, 0, 0),
        -1: (0, 0, 255)
    }
    portals = {}
    next_portal = -1

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen

    def update(self):
        for portal in self.portals:
            pygame.draw.rect(self.screen,
                             self.portals_colors[portal],
                             self.portals[portal])
        self._check_collide()

    def set_portal(self, mouse_pos):
        portal = pygame.Rect(0, 0, 50, 50)
        portal.center = mouse_pos

        self.portals[self.next_portal] = portal
        self.next_portal *= -1


    def _check_collide(self):
        portal_collided = 0
        collision = False
        for portal in self.portals:
            collision = self.portals[portal].colliderect(self.game.player.rect)
            if collision and portal_collided == 0:
                print(f"collide with {portal}")
                collision = self.portals[portal].colliderect(self.game.player.rect)
                portal_collided = portal
                break

        if collision:
            x = (-self.game.player.rect.center[0] + self.portals[portal_collided].center[0]) + self.portals[-portal_collided].center[0]
            y = (-self.game.player.rect.center[1] + self.portals[portal_collided].center[1]) + self.portals[-portal_collided].center[1]

            self.game.player.rect.center = (x, y)

            portal = self.portals[-portal_collided]
            top = self.game.player.rect.bottom - portal.top
            bottom = -self.game.player.rect.top + portal.bottom
            left = self.game.player.rect.right - portal.left
            right = -self.game.player.rect.left + portal.right
            if top < bottom and top < left and top < right:
                self.game.player.rect.bottom = self.portals[-portal_collided].top
            elif bottom < left and bottom < right:
                self.game.player.rect.top = self.portals[-portal_collided].bottom
            elif left < right:
                self.game.player.rect.right = self.portals[-portal_collided].left
            else:
                self.game.player.rect.left = self.portals[-portal_collided].right



