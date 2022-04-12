import os
import sys
import numpy as np
import json
import click
from valley import *

@click.command()
@click.option('--new',is_flag=True, help='Start New Game')
@click.option('--move',is_flag=True, help='Next step')
@click.option('--print',is_flag=True, help="Print field and warehouse")
@click.option('--plant', default='', help="plant garden")
@click.option('--weed', default='', help="weed plant")
@click.option('--water', default='', help="water plant")

def main(new, move, print, plant, weed, water):
    player = GameMaster()
    if new:
        player.storage.nullify_warehouse()
        player.nullify_field()
        player.export_plants()
    else:
        player.import_plants()
        player.storage.display_warehouse()
        if print:
            os.system('cls' if os.name == 'nt' else 'clear')
            player.update_screen()
        if move:
            Events.start_disasters(player)
            player.age_all()
        if plant:
            if int(plant) <= 7 and int(plant) > 0:
                player.add_plant_based_on_id(int(plant))
            player.age_all()
        if weed:
            if int(weed) <= 7 and int(weed) > 0:
                player.weeding(int(weed))
            player.age_all()
            Events.start_disasters(player)
        if water:
            if int(water) <= 7 and int(water) > 0:
                player.watering(water)
            Events.start_disasters(player)

if __name__ == '__main__':
    main()
