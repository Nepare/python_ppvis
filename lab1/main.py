import os
import sys
import numpy as np
import json

from valley import *


if __name__ == '__main__':

    command = ''
    with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\settings.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())
        f.close()
    autoprint = settings["autoprint"]
    if len(sys.argv) != 1:
        command = str(sys.argv[1])

    player = GameMaster()

    if command == 'new':
        player.storage.nullify_warehouse()
        player.nullify_field()
        player.export_plants()
    else:
        player.import_plants()
        player.storage.import_warehouse()
        if command == 'help':
            print("\n--- HELP MENU ---\n")
            print("print - prints the garden")
            print("autoprint on/off - toggles autoprint with every move")
            print("move - makes a singular move without actions")
            print("plant (argumenents) - lets you plant something in your garden. \nIf done with parameters, you will "
                  "plant something specific")
            print("weed (argumenents) - lets you weed something in your garden. \nWeeding gets rid of weeds in your"
                  "garden. \nIf done with parameters, you will weed some specific plant")
            print("water (argumenents) - lets you water your plants. \nThe water cancels drought effect. \nWhen done "
                  "with parameters, you will water a specific plant")
            print("new - starts a new game")
            print("help - print this menu")

        if command == 'print':
            os.system('cls' if os.name == 'nt' else 'clear')
            player.update_screen()
        if command == 'autoprint':
            if len(sys.argv) > 2:
                if str(sys.argv[2]) == 'on':
                    new_settings: dict = {}
                    new_settings["autoprint"] = True
                    with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\settings.json', 'w', encoding='utf-8') as f:
                        json.dump(new_settings, f, ensure_ascii=False, indent=2)
                        f.close()
                if str(sys.argv[2]) == 'off':
                    new_settings: dict = {}
                    new_settings["autoprint"] = False
                    with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\settings.json', 'w', encoding='utf-8') as f:
                        json.dump(new_settings, f, ensure_ascii=False, indent=2)
                        f.close()
        if command == 'move':
            Events.start_disasters(player)
            player.age_all()
            if autoprint:
                os.system('cls' if os.name == 'nt' else 'clear')
                player.update_screen()
            Events.start_disasters(player)
        if command == 'plant':
            if len(sys.argv) <= 2:
                player.planting()
            else:
                plant_id = sys.argv[2]
                try:
                    number = int(plant_id) - 1
                except:
                    pass
                if number > 7 or number < 0:
                    pass
                else:
                    player.add_plant_based_on_id(number)
            player.age_all()
            if autoprint:
                os.system('cls' if os.name == 'nt' else 'clear')
                player.update_screen()
            Events.start_disasters(player)
        if command == 'weed':
            if len(sys.argv) <= 2:
                player.weeding()
            else:
                plant_id = sys.argv[2]
                try:
                    number = int(plant_id) - 1
                except:
                    pass
                if number > len(player.field.plants) or number < 0:
                    pass
                else:
                    player.field.plants[number].weeded = False
                    player.field.plants[number].mods += 0.2
                    player.field.plants[number].mods = np.around(player.field.plants[number].mods, 3)
                    if player.field.plants[number].mods >= 1.0:
                        player.field.plants[number].mods = 1.0
            player.age_all()
            if autoprint:
                os.system('cls' if os.name == 'nt' else 'clear')
                player.update_screen()
            Events.start_disasters(player)
        if command == 'water':
            if autoprint:
                os.system('cls' if os.name == 'nt' else 'clear')
                player.update_screen()
            if len(sys.argv) <= 2:
                player.watering()
            else:
                plant_id = sys.argv[2]
                try:
                    number = int(plant_id) - 1
                except:
                    pass
                if number > len(player.field.plants) or number < 0:
                    pass
                else:
                    if player.field.plants[number].is_droughted:
                        player.field.plants[number].is_droughted = False
                        player.field.plants[number].mods += 0.5
                        player.field.plants[number].mods = np.around(player.field.plants[number].mods, 3)
                    if player.field.plants[number].mods > 1.0:
                        player.field.plants[number].mods = 1.0
            if autoprint:
                os.system('cls' if os.name == 'nt' else 'clear')
                player.update_screen()
            Events.start_disasters(player)