import pygame
from pygame.locals import *
from valley import *

plant_list = ["apple", "eggplant", "grape", "tomato", "beet", "potato", "melon", "pumpkin"]


class VisualPlant(pygame.sprite.Sprite):
    def __init__(self, type_in):
        super().__init__()
        self.type = type_in
        self.stage = 1
        self.name = plant_list[type_in]
        texture_folder = "tree" if 0 <= type_in <= 3 else "product"
        plant_texture = pygame.image.load("lab1\\assets\\textures\\plants\\" +
                                          texture_folder + "\\" + self.name + "\\" + self.name + "_" +
                                          str(self.stage) + ".png")
        self.image = plant_texture
        self.rect = self.image.get_rect()

    def update_texture(self):
        texture_folder = "tree" if 0 <= self.type <= 3 else "product"
        plant_texture = pygame.image.load("lab1\\assets\\textures\\plants\\" +
                                          texture_folder + "\\" + self.name + "\\" + self.name + "_" +
                                          str(self.stage) + ".png")
        self.image = plant_texture
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class VisualGarden:
    content: list = []

    def initial_import(self, player: GameMaster):
        self.content.clear()
        for current_plant in player.field.plants:
            current_visual_plant = VisualPlant(current_plant.id)
            if 0 <= current_plant.id <= 3:
                current_visual_plant.stage = current_plant.growth_progress
            if 4 <= current_plant.id <= 7:
                current_visual_plant.stage = current_plant.harvest_progress + 1
            current_visual_plant.update_texture()
            self.add_plant(current_visual_plant)

    def add_plant(self, plant):
        self.content.append(plant)

    def display_garden(self, surface):
        for i in range(len(self.content)):
            row = i // 6
            column = i % 6
            if row < 2:
                self.content[i].rect.midbottom = ((column + 1) * 154 - 80 + 10, (row + 1) * 240 + 10 - (row * 100))
                self.content[i].draw(surface)
