import sys
import time

import pygame
from pygame.locals import *
from valley import *
from stored_plants import StoredPlant, VisualWarehouse
from visual_garden import VisualPlant, VisualGarden

pygame.init()

DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 1200
FPS = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Stardew Valley на минималках")
pygame.display.set_icon(pygame.image.load("lab1\\assets\\textures\\hoe.png"))


def draw_interface():
    pygame.draw.rect(DISPLAYSURF, BLACK, (10, 10, 935 - 10, 490 - 10), 5)  # основной экран фермы
    pygame.draw.rect(DISPLAYSURF, BLACK, (950, 10, 1190 - 950, 490 - 10), 5)  # экран высадки растений

    pygame.draw.line(DISPLAYSURF, BLACK, (1070, 10), (1070, 485), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (950, 130), (1185, 130), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (950, 250), (1185, 250), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (950, 370), (1185, 370), 5)  # ячейки высадки растений

    tiles = pygame.image.load("lab1\\assets\\textures\\tiles.png")
    tiles = pygame.transform.scale(tiles, (915, 470))
    tiles_box = tiles.get_rect()
    tiles_box.topleft = (15, 15)
    DISPLAYSURF.blit(tiles, tiles_box)

    plus_sign = pygame.image.load("lab1\\assets\\textures\\plus.png")
    plus_sign = pygame.transform.scale(plus_sign, (30, 25))
    plant_list = [["apple", "eggplant", "grape", "tomato"], ["beet", "potato", "melon", "pumpkin"]]
    for i in range(2):  # весь код ниже это таблица для кнопок высадки растений
        for j in range(4):
            draw_plus = plus_sign.get_rect()
            draw_plus.midleft = (950 + i * 120 + 10, 10 + j * 120 + 60)
            DISPLAYSURF.blit(plus_sign, draw_plus)
            texture_folder = "tree" if i == 0 else "product"
            plant_texture = pygame.image.load("lab1\\assets\\textures\\plants\\" + texture_folder + "\\" + plant_list[i][j] + "\\" + plant_list[i][j] + "_plod.png")
            plant_rect = plant_texture.get_rect()
            plant_rect.midright = (1070 + i * 120 - 25, 10 + j * 120 + 60)
            DISPLAYSURF.blit(plant_texture, plant_rect)

    pygame.draw.rect(DISPLAYSURF, BLACK, (10, 505, 935 - 10, 800 - 500 - 15), 5)
    for i in range(7):
        pygame.draw.line(DISPLAYSURF, BLACK, (10 + (i + 1) * 115.625, 505), (10 + (i + 1) * 115.625, 785), 10)

    for i in range(3):
        pygame.draw.rect(DISPLAYSURF, BLACK, (950, 505 + 97.5 * i, 1190 - 950, 90), 5)

    watering_texture = pygame.image.load("lab1\\assets\\textures\\watering.png")
    weeding_texture = pygame.image.load("lab1\\assets\\textures\\weeding.png")
    skip_texture = pygame.image.load("lab1\\assets\\textures\\skip.png")
    watering_rect = watering_texture.get_rect()
    watering_rect.midright = (1190 - 30, 505 + 45)
    weeding_rect = weeding_texture.get_rect()
    weeding_rect.midright = (1190 - 30, 505 + 97.5 + 45)
    skip_rect = skip_texture.get_rect()
    skip_rect.midright = (1190 - 40, 505 + 195 + 47)

    DISPLAYSURF.blit(weeding_texture, weeding_rect)
    DISPLAYSURF.blit(watering_texture, watering_rect)
    DISPLAYSURF.blit(skip_texture, skip_rect)

    hardwood_texture = pygame.transform.scale(pygame.image.load("lab1\\assets\\textures\\hardwood.png"), (111.25, 275))
    for i in range(8):
        draw_floor = hardwood_texture.get_rect()
        draw_floor.topleft = (15 + i * 115, 510)
        DISPLAYSURF.blit(hardwood_texture, draw_floor)

def next_turn():
    player.age_all()
    Events.start_disasters(player)
    visual_warehouse.initial_import(player)
    visual_garden.initial_import(player)


def button_control():
    button_pressed = False

    pressed_keys = pygame.key.get_pressed()
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    mouse_pressed = pygame.mouse.get_pressed()[0]

    if 950 <= mouse_x <= 1190 and 505 + 195 <= mouse_y <= 505 + 195 + 90 and mouse_pressed:
        next_turn()
        pygame.draw.rect(DISPLAYSURF, GREEN, (950, 505 + 97.5 * 2, 1190 - 950, 90), 5)
        button_pressed = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            next_turn()
            pygame.draw.rect(DISPLAYSURF, GREEN, (950, 505 + 97.5 * 2, 1190 - 950, 90), 5)
            button_pressed = True
        if event.key == pygame.K_1:
            player.add_plant_based_on_id(0)
            next_turn()
        if event.key == pygame.K_2:
            player.add_plant_based_on_id(1)
            next_turn()
        if event.key == pygame.K_3:
            player.add_plant_based_on_id(2)
            next_turn()
        if event.key == pygame.K_4:
            player.add_plant_based_on_id(3)
            next_turn()
        if event.key == pygame.K_5:
            player.add_plant_based_on_id(4)
            next_turn()
        if event.key == pygame.K_6:
            player.add_plant_based_on_id(5)
            next_turn()
        if event.key == pygame.K_7:
            player.add_plant_based_on_id(6)
            next_turn()
        if event.key == pygame.K_8:
            player.add_plant_based_on_id(7)
            next_turn()
    return button_pressed


def gameloop():
    DISPLAYSURF.fill(WHITE)
    draw_interface()

    button_pressed = button_control()

    visual_warehouse.display_warehouse(DISPLAYSURF)
    visual_garden.display_garden(DISPLAYSURF)
    pygame.display.update()
    if button_pressed:
        time.sleep(0.05)
    FPS.tick(60)


player = GameMaster()
visual_warehouse = VisualWarehouse()
visual_garden = VisualGarden()

player.import_plants()
player.storage.import_warehouse()
visual_warehouse.initial_import(player)
visual_garden.initial_import(player)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            gameloop()
