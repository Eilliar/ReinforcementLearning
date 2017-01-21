"""
Game to be used for RL studies

Author: Bruno G. Eilliar

Notes:
    - 
"""

import pygame, sys
from pygame.locals import *
from robot import Robot

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Pygame Initialization
pygame.init()

# Screen size and name
world_size = (700, 500)
WORLD = pygame.display.set_mode(world_size)
pygame.display.set_caption('Hell no World!')

# Robot
Jarvis = Robot("Jarvis", WORLD, (200, 50))

# Main game loop
while True:
    # Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Game logic
    # Screen Clearing
    WORLD.fill(WHITE)
    # Draw code
    Jarvis.draw()
    # Update
    pygame.display.update()
