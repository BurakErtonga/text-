import pygame
import sys
import random

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

snake_block = 10
snake_speed = 15
snake = [[width / 2, height / 2]]
snake_direction = 'RIGHT'

food = [random.randrange(1, (width//snake_block)) * snake_block,
        random.randrange(1, (height//snake_block)) * snake_block]

score = 0

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(window, white, [block[0], block[1], snake_block, snake_block])

def draw_food(food):
    pygame.draw.rect(window, red, [food[0], food[1], snake_block, snake_block])

def display_score(score):
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    for i in range(len(snake) - 1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]

    if snake_direction == 'UP':
        snake[0][1] -= snake_block
    elif snake_direction == 'DOWN':
        snake[0][1] += snake_block
    elif snake_direction == 'LEFT':
        snake[0][0] -= snake_block
    elif snake_direction == 'RIGHT':
        snake[0][0] += snake_block

    if snake[0][0] < 0 or snake[0][0] >= width or snake[0][1] < 0 or snake[0][1] >= height:
        pygame.quit()
        sys.exit()

    for block in snake[1:]:
        if snake[0][0] == block[0] and snake[0][1] == block[1]:
            pygame.quit()
            sys.exit()

    # Check if the snake has eaten the food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = [random.randrange(1, (width//snake_block)) * snake_block,
                random.randrange(1, (height//snake_block)) * snake_block]

        snake.append([snake[-1][0], snake[-1][1]])

        score += 1


    window.fill(black)
    draw_snake(snake)
    draw_food(food)
    display_score(score)
    pygame.display.update()

    pygame.time.Clock().tick(snake_speed)



def print_hi(name):
   
    print(f'Hi, {name}')  



if __name__ == '__main__':
    print_hi('PyCharm')


