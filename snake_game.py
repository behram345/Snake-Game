import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake block size
BLOCK_SIZE = 20

# Clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, GREEN)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLUE, [block[0], block[1], block_size, block_size])

def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [WIDTH // 6, HEIGHT // 3])

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()

# Run the game
game_loop()
