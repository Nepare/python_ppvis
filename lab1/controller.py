import sys
import pygame
from pygame.locals import *
from valley import *
from stored_plants import StoredPlant, VisualWarehouse

pressed_keys = pygame.key.get_pressed()
if pressed_keys[K_SPACE]:
    player.update_screen()
