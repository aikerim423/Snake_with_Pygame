import time

import pygame
from snake import Snake
from food_for_the_snake import Food


def run():
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake game")

    change_pos_x = 0
    change_pos_y = 0

    start = True
    snake = Snake(screen)
    food = Food(screen)
    clock = pygame.time.Clock()

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_pos_x = -10
                    change_pos_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_pos_x = 10
                    change_pos_y = 0
                elif event.key == pygame.K_UP:
                    change_pos_x = 0
                    change_pos_y = -10
                elif event.key == pygame.K_DOWN:
                    change_pos_x = 0
                    change_pos_y = 10

        if snake.x >= width or snake.x < 0 or snake.y >= width or snake.y < 0:
            pygame.display.set_caption("GAME OVER!!!")
            time.sleep(5)
            start = False

        snake.x += change_pos_x
        snake.y += change_pos_y
        screen.fill((0, 0, 0))
        food.food_position()
        snake.update_position()
        snake.snake_position()
        pygame.display.update()

        if snake.x == food.food_x and snake.y == food.food_y:
            food.new_position()
            snake.len += 1
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    run()
