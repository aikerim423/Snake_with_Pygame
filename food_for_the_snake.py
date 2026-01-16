import pygame
from random import randrange


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.food_color = (255, 0, 0)
        self.size = 20
        self.food_x = round(randrange(0, 580) / 10.0) * 10.0
        self.food_y = round(randrange(0, 580) / 10.0) * 10.0

    def food_position(self):
        pygame.draw.rect(self.screen, self.food_color,
                         (self.food_x, self.food_y, self.size, self.size))

    def new_position(self):
        self.food_x = round(randrange(0, 580) / 10.0) * 10.0
        self.food_y = round(randrange(0, 580) / 10.0) * 10.0
