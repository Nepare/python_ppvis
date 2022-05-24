import pygame
from pygame.locals import *
from valley import *

event_list = ["disease", "drought", "rain", "colorado", "weed"]


class VisualEffect(pygame.sprite.Sprite):
    def __init__(self, type_in):
        super().__init__()
        self.type = type_in
        self.name = event_list[self.type]
        self.texture = pygame.image.load("lab1\\assets\\textures\\events\\" + self.name + ".png")
        self.texture = pygame.transform.scale(self.texture, (50, 50))
        self.rect = self.texture.get_rect()

    def draw(self, surface):
        surface.blit(self.texture, self.rect)


class VisualStatusBar:
    effect_list: list = []

    def add_effect(self, effect):
        self.effect_list.append(effect)

    def remove_effect(self, effect):
        self.effect_list.remove(effect)

    def display_status_bar(self, surface):
        start_pos_y = 485
        start_pos_x = 15

        for x in self.effect_list:
            x.rect.bottomleft = (start_pos_x, start_pos_y)
            start_pos_x += 50
            x.draw(surface)

    def import_effects(self, player: GameMaster):
        self.effect_list.clear()
        if Events.illness:
            self.add_effect(VisualEffect(0))
        if Events.drought:
            self.add_effect(VisualEffect(1))
        if Events.rainy:
            self.add_effect(VisualEffect(2))
        if Events.colorado_attack:
            self.add_effect(VisualEffect(3))
        for x in player.field.plants:
            if x.weeded:
                self.add_effect(VisualEffect(4))
                break
