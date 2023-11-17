import pygame
import random

WSIZE = (720, 480)
img = pygame.image.load('images/asd.png')
pygame.display.set_icon(img)
screen = pygame.display.set_mode(WSIZE)
pygame.display.set_caption('Snake game by Volodya')
TSIZE = 30
MSIZE = WSIZE[0] // TSIZE, WSIZE[1] // TSIZE

start_pos = MSIZE[0] // 2, MSIZE[1] //2
snake = [start_pos]
alive = True

direction = 0
directions =[(1, 0), (0, 1), (-1, 0), (0, -1)]

apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])
fps = 5
clock = pygame.time.Clock()

pygame.font.init()
font_score = pygame.font.SysFont('Arial', 20)
font_gameover = pygame.font.SysFont('Arial', 40)
font_help = pygame.font.SysFont('Arial', 18)

running = True
while running:
    clock.tick(fps)
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_RIGHT and direction != 2:
                    direction = 0
                if event.key == pygame.K_DOWN and direction != 3:
                    direction = 1
                if event.key == pygame.K_LEFT and direction != 0:
                    direction = 2
                if event.key == pygame.K_UP and direction != 1:
                    direction = 3
            else:
                if event.key == pygame.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])
                    fps = 5
    [pygame.draw.rect(screen, 'green', (x * TSIZE, y * TSIZE, TSIZE - 1, TSIZE - 1))for x, y in snake]
    pygame.draw.rect(screen, 'red', (apple[0] * TSIZE, apple[1] * TSIZE, TSIZE - 1, TSIZE - 1))


    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < MSIZE[0] and 0 <= new_pos[1] < MSIZE[1]) or \
                new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                fps += 1
                apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])
            else:
                snake.pop(-1)
    else:
        screen.fill('blue')
        text = font_gameover.render(f'GAME OVER', True, 'white')
        screen.blit(text, (WSIZE[0] // 2 - text.get_width()//2, WSIZE[1] // 2 - 50))
        text = font_gameover.render(f'Press SPACE for restart', True, 'white')
        screen.blit(text, (WSIZE[0] // 2 - text.get_width() // 2, WSIZE[1] // 2 + 50))
    screen.blit(font_score.render(f'Score: {len(snake)- 1}', True, 'yellow'), (5, 5))
    pygame.display.flip()