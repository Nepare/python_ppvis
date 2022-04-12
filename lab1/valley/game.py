from .warehouse import Warehouse
from .gardenbed import GardenBed
import numpy as np
import random
import json
import os


class GameMaster(Warehouse, GardenBed):
    field = GardenBed()
    storage = Warehouse()

    def watering(self, number):
        if int(number) > len(self.field.plants) or int(number) < 0:
            return
        number = int(number) - 1
        if self.field.plants[number].is_droughted:
            self.field.plants[number].is_droughted = False
            self.field.plants[number].mods += 0.5
            self.field.plants[number].mods = np.around(self.field.plants[number].mods, 3)
        if self.field.plants[number].mods > 1.0:
            self.field.plants[number].mods = 1.0


    def age_all(self):  # Увеличивается процесс урожая ход
        for x in self.field.plants:
            x.age(self)
        self.export_plants()

    def add_plant(self, plant_name):
        self.field.plants.append(plant_name)

    def add_plant_based_on_id(self, id_name):
        if id_name == 0:
            self.add_plant(Apple())
        if id_name == 1:
            self.add_plant(Pear())
        if id_name == 2:
            self.add_plant(Cherry())
        if id_name == 3:
            self.add_plant(Plum())
        if id_name == 4:
            self.add_plant(Potato())
        if id_name == 5:
            self.add_plant(Carrot())
        if id_name == 6:
            self.add_plant(Cabbage())
        if id_name == 7:
            self.add_plant(Pepper())

    def display_garden(self):
        for i in self.field.plants:
            i.show_plant_status(self)

    def weeding(self, number):
        if number > len(self.field.plants) or number < 0:
            return
        number = int(number) - 1
        self.field.plants[number].weeded = False
        self.field.plants[number].mods += 0.2
        self.field.plants[number].mods = np.around(self.field.plants[number].mods, 3)
        if self.field.plants[number].mods >= 1.0:
            self.field.plants[number].mods = 1.0

    def update_screen(self):
        print("ГРЯДКИ")
        self.display_garden()
        print("\n\nСКЛАД")
        self.storage.display_warehouse()
        print()

    def import_plants(self):
        house1 = {}
        try:
            working_directory = os.getcwd()
            file_path = working_directory + '/field.json'

            with open(file_path, 'r', encoding='utf-8') as f:
                house1 = json.loads(f.read())
                f.close()
        except OSError:
            print("Не удалось открыть файл!")
            return
        self.field.plants.clear()
        for i in range(0, len(house1)):
            current_plant: dict = house1.get(str(i))
            self.add_plant_based_on_id(current_plant.get("id"))
            self.field.plants[i].mods = current_plant.get("mods")
            self.field.plants[i].harvest_progress = current_plant.get("harvest_progress")
            self.field.plants[i].growth_progress = current_plant.get("growth_progress")
            self.field.plants[i].id = current_plant.get("id")
            self.field.plants[i].is_droughted = current_plant.get("is_droughted")
            self.field.plants[i].weeded = current_plant.get("weeded")
            self.field.plants[i].diseases = current_plant.get("diseases")
            self.field.plants[i].has_colorado_beatle = current_plant.get("has_colorado_beatle")

    def export_plants(self):
        gamefield = dict()
        for i in range(0, len(self.field.plants)):
            current_plant = dict()
            current_plant["id"] = self.field.plants[i].id
            current_plant["mods"] = self.field.plants[i].mods
            current_plant["harvest_progress"] = self.field.plants[i].harvest_progress
            current_plant["growth_progress"] = self.field.plants[i].growth_progress
            current_plant["is_droughted"] = self.field.plants[i].is_droughted
            current_plant["weeded"] = self.field.plants[i].weeded
            current_plant["diseases"] = self.field.plants[i].diseases
            current_plant["has_colorado_beatle"] = self.field.plants[i].has_colorado_beatle
            gamefield[str(i)] = current_plant
        working_directory = os.getcwd()
        file_path = working_directory + '/field.json'

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(gamefield, f, ensure_ascii=False, indent=2)
            f.close()

    def nullify_field(self):
        self.field.plants.clear()


class Plant:  # Базовый класс
    harvest_progress: int = 0
    harvest_max: int = 0
    growth_progress = 0
    growth_max = 0
    name: 'Plant'
    mods:  float = 1.0  # Шанс на то, что растение даст урожай
    is_droughted:  bool = False
    has_colorado_beatle: bool = False
    diseases: bool = False
    weeded: bool = False
    id: None
    plods: str = 'Plods'


class Tree(Plant, GameMaster):  # Класс дерева
    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ", sep='', end='')

        self.mods = np.around(self.mods, 3)
        if self.growth_progress < self.growth_max:
            print(self.name, ". Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max), sep='',
                  end='')
        else:
            print(self.name, ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
                  str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.growth_progress < self.growth_max:
            self.growth_progress += 1
        else:
            if self.growth_progress < self.growth_max:
                self.growth_progress += 1
            else:
                if self.harvest_progress < self.harvest_max:
                    self.harvest_progress += 1
                if self.harvest_progress == self.harvest_max:
                    if random.random() < self.mods:
                        working_directory = os.getcwd()
                        file_path = working_directory + '/warehouse.json'
                        with open('file_path', 'r', encoding='utf-8') as f:
                            house = json.loads(f.read())
                        self.harvest_progress = 0
                        self.storage.house[self.plods] += 1
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(self.house, f, ensure_ascii=False, indent=2)



class Vegetable(Plant, GameMaster):  # Класс овощей
    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ", sep='', end='')
        print(self.name, ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
              str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.harvest_progress < self.harvest_max:
            self.harvest_progress += 1
        if self.harvest_progress == self.harvest_max:
            self.harvest_progress = 0
            if random.random() < self.mods:
                    working_directory = os.getcwd()
                    file_path = working_directory + '/warehouse.json'
                    with open('file_path', 'r', encoding='utf-8') as f:
                        house = json.loads(f.read())
                    self.harvest_progress = 0
                    self.storage.house[self.plods] += 1
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(self.house, f, ensure_ascii=False, indent=2)


# FRUIT TREES


class Apple(Tree):
    harvest_max = 3
    growth_max = 5
    name = 'Яблоня'
    plods = "Яблоки"
    id = 0


class Pear(Tree):
    harvest_max = 3
    growth_max = 6
    name = 'Груша'
    plods = 'Груши'
    id = 1


class Cherry(Tree):
    harvest_max = 2
    growth_max = 6
    name = 'Вишня'
    plods = 'Вишни'
    id = 2


class Plum(Tree):
    harvest_max = 2
    growth_max = 5
    name = 'Слива'
    plods = 'Сливы'
    id = 3


# VEGETABLES


class Potato(Vegetable):
    harvest_max = 2
    name = 'Картофель'
    plods = 'Картофель'
    id = 4


class Carrot(Vegetable):
    harvest_max = 3
    name = 'Морковь'
    plods = 'Морковь'
    id = 5


class Cabbage(Vegetable):
    harvest_max = 2
    name = 'Капуста'
    plods = 'Капуста'
    id = 6


class Pepper(Vegetable):
    harvest_max = 3
    name = 'Перец'
    plods = 'Перец'
    id = 7
