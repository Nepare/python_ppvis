import pygame
from pygame.locals import *
from valley import *

plant_list = ["apple", "eggplant", "grape", "tomato", "beet", "potato", "melon", "pumpkin"]


class VisualPlant(pygame.sprite.Sprite):
    def __init__(self, type_in):
        super().__init__()
        self.type = type_in
        self.stage = 1
        self.illness = False
        self.dry = False
        self.weeded = False
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

        if self.illness:
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.weeded:
            grass_texture = pygame.image.load("lab1\\assets\\textures\\events\\grass.png")
            for x in range(-2, 3):
                grass_box = grass_texture.get_rect()
                grass_box.midbottom = (self.rect.midbottom[0] + (x * grass_box.width / 2.5), self.rect.midbottom[1] + 20)
                surface.blit(grass_texture, grass_box)
        if self.dry:
            dry_texture = pygame.image.load("lab1\\assets\\textures\\events\\heatwave.png")
            dry_texture = pygame.transform.scale(dry_texture, (60, 100))
            dry_box = dry_texture.get_rect()
            dry_box.midbottom = self.rect.midbottom
            surface.blit(dry_texture, dry_box)


class VisualGarden:
    content: list = []

    def initial_import(self, player: GameMaster):
        self.content.clear()
        for current_plant in player.field.plants:
            current_visual_plant = VisualPlant(current_plant.id)
            current_visual_plant.illness = False
            current_visual_plant.weeded = False
            current_visual_plant.dry = False
            if 0 <= current_plant.id <= 3:
                current_visual_plant.stage = current_plant.growth_progress
            if 4 <= current_plant.id <= 7:
                current_visual_plant.stage = current_plant.harvest_progress + 1
            if Events.idDisease == current_plant.id:
                current_visual_plant.illness = True
            if current_plant.weeded:
                current_visual_plant.weeded = True
            if current_plant.is_droughted:
                current_visual_plant.dry = True
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
