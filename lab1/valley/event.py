from .game import GameMaster
import random
import numpy as np


class Events:  # случайное событие, не зависящее от игрока
    drought = False
    colorado_attack = False
    illness = False
    rainy = False
    idDisease = -1
    num_disease = 0

    @staticmethod
    def drought_start(target: GameMaster):  # бьёт по всем
        print("Начало засухи!")
        Events.drought = True
        for x in target.field.plants:
            if x.mods > 0.5:
                x.mods -= 0.5
                x.mods = np.around(x.mods, 2)
                x.is_droughted = True
            else:
                x.mods = 0.0

    @staticmethod
    def drought_end(target: GameMaster):  # бьёт по всем
        Events.drought = False
        print("Конец засухи!")
        for x in target.field.plants:
            if x.is_droughted:
                x.mods += 0.5
                x.mods = np.around(x.mods, 3)
                x.is_droughted = False

    @staticmethod
    def colorado_beatle_start(target: GameMaster):  # бьёт по картошке
        Events.colorado_attack = True
        print("Тревога! Атака колорадских жуков!")
        for x in target.field.plants:
            if x.id == 4 and x.mods > 0.3 and not x.has_colorado_beatle:
                x.mods -= 0.3
                x.mods = np.around(x.mods, 2)
                x.has_colorado_beatle = True
            elif x.id == 4 and x.mods <= 0.3 and not x.has_colorado_beatle:
                x.mods = 0.0
                x.has_colorado_beatle = True

    @staticmethod
    def colorado_beatle_end(target: GameMaster):
        Events.colorado_attack = False
        print("Колорадские жуки отступают")
        for x in target.field.plants:
            if x.id == 4 and x.has_colorado_beatle:
                x.mods += 0.3
                x.mods = np.around(x.mods, 3)
                x.has_colorado_beatle = False
                if x.mods > 1.0:
                    x.mods = 1.0

    @staticmethod
    def rain_start(target: GameMaster):
        print("Пошёл дождь.")
        Events.rainy = True
        for x in target.field.plants:
            x.mods += 0.05
            x.mods = np.around(x.mods, 3)

    @staticmethod
    def rain_end(target: GameMaster):
        print("Конец дождя.")
        Events.rainy = False
        for x in target.field.plants:
            x.mods -= 0.05
            x.mods = np.around(x.mods, 3)

    @staticmethod
    def disease_start(target: GameMaster):
        print("\n")
        Events.illness = True
        print("\nНашествие болезни на определённый вид растения")
        disease = random.randint(0, 7)
        Events.idDisease = disease
        print("Болезнь пришла по " + target.storage.namelist[Events.idDisease])
        for x in target.field.plants:
            if x.id == disease:
                x.mods -= 0.15
                Events.num_disease = disease
                x.mods = np.around(x.mods, 3)
                x.diseases = True

    @staticmethod
    def disease_end(target: GameMaster):
        print("\n")
        print("\n Нет болезни")
        print("Болезнь вида " + target.storage.namelist[Events.idDisease] + " закончилась")
        Events.illness = False
        for x in target.field.plants:
            if x.id == Events.idDisease and x.diseases and Events.num_disease == Events.idDisease:
                x.mods += 0.15
                x.mods = np.around(x.mods, 3)
                x.diseases = False
            elif x.id == Events.idDisease and not x.diseases and Events.num_disease != Events.idDisease:
                    pass

    @staticmethod
    def weed_infestation(target: GameMaster):
        weed_place = random.randint(0, len(target.field.plants) - 1)
        if target.field.plants[weed_place].weeded:
            return
        target.field.plants[weed_place].weeded = True
        print(target.field.plants[weed_place].name + " под номером " + str(weed_place + 1) +
              " подвергается атаке сорняков")
        if target.field.plants[weed_place].mods >= 0.2:
            target.field.plants[weed_place].mods -= 0.2
            target.field.plants[weed_place].mods = np.around(target.field.plants[weed_place].mods, 3)
        else:
            target.field.plants[weed_place].mods = 0.0

    @staticmethod
    def start_disasters(target: GameMaster):
        if len(target.field.plants) == 0:
            return
        if random.random() < 0.15 and not Events.drought and not Events.rainy:
            Events.drought_start(target)
        elif random.random() < 0.05 and Events.drought:
            Events.drought_end(target)
        if random.random() < 0.30 and not Events.rainy:
            Events.rain_start(target)
            if Events.drought:
                Events.drought_end(target)
        elif random.random() < 0.30 and Events.rainy:
            Events.rain_end(target)
        if random.random() < 0.25 and not Events.colorado_attack:
            Events.colorado_beatle_start(target)
        elif random.random() < 0.20 and Events.colorado_attack:
            Events.colorado_beatle_end(target)
        if random.random() < 0.15 and not Events.illness:
            Events.disease_start(target)
        elif random.random() < 0.15 and Events.illness:
            Events.disease_end(target)
        chance = random.random()
        if (chance < 0.35 and not Events.rainy) or (chance < 0.55 and Events.rainy):
            Events.weed_infestation(target)