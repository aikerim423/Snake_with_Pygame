import pygame


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.snake_color = (0, 255, 0)
        self.x = 10
        self.y = 20
        self.size = 20
        self.snake = []
        self.len = 1
        self.head = []

    def update_position(self):
        new_head = (self.x, self.y)
        self.snake.insert(0, new_head)
        if len(self.snake) > self.len:
            self.snake.pop()

    def snake_position(self):
        for blok in self.snake:
            pygame.draw.rect(self.screen, self.snake_color, [blok[0], blok[1], self.size, self.size])
