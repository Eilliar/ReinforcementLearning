# Robot Class
import pygame

ROBOT_COLOR = (0, 0, 255)

class Robot(object):

    def __init__(self, name, world, position):
        self.name = name
        self.world = world
        self.position = position
        self.radius = 20

    def draw(self):
        pygame.draw.circle(self.world, ROBOT_COLOR, self.position, self.radius)
