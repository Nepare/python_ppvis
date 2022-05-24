import random
import pygame
from valley import *
from pygame.locals import *

plant_list = ["apple", "eggplant", "grape", "tomato", "beet", "potato", "melon", "pumpkin"]


class StoredPlant(pygame.sprite.Sprite):
    def __init__(self, type_in):
        super().__init__()
        self.plant_type = type_in
        self.name = plant_list[self.plant_type]
        texture_folder = "tree" if 0 <= type_in <= 3 else "product"
        plant_texture = pygame.image.load("lab1\\assets\\textures\\plants\\" +
                                          texture_folder + "\\" + self.name + "\\" + self.name + "_plod.png")
        self.image = plant_texture
        self.rect = self.image.get_rect()
        random_x = random.randint(0, 45)
        random_y = random.randint(0, 200)
        self.rect.center = (40 + (self.plant_type * 115.625) + random_x, 545 + random_y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class VisualWarehouse:
    content: list = []

    def initial_import(self, player: GameMaster):
        self.content.clear()
        for x in range(player.storage.house["Яблоки"]):
            self.add_plant(StoredPlant(0))
        for x in range(player.storage.house["Груши"]):
            self.add_plant(StoredPlant(1))
        for x in range(player.storage.house["Вишни"]):
            self.add_plant(StoredPlant(2))
        for x in range(player.storage.house["Сливы"]):
            self.add_plant(StoredPlant(3))
        for x in range(player.storage.house["Картофель"]):
            self.add_plant(StoredPlant(4))
        for x in range(player.storage.house["Морковь"]):
            self.add_plant(StoredPlant(5))
        for x in range(player.storage.house["Капуста"]):
            self.add_plant(StoredPlant(6))
        for x in range(player.storage.house["Перец"]):
            self.add_plant(StoredPlant(7))

    def add_plant(self, plant):
        self.content.append(plant)

    def display_warehouse(self, surface):
        for x in self.content:
            x.draw(surface)

