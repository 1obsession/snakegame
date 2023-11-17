
import random
import pygame

pygame.init()
pygame.mouse.set_visible(False)
apple_img = pygame.image.load('images/13.png')
apple_img = pygame.transform.scale(apple_img, (30, 30))
img = pygame.image.load('images/asd.png')
chess_img = pygame.image.load('images/chess.png')
chess_img = pygame.transform.scale(chess_img, (600, 400))
pygame.display.set_icon(img)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Volodyan')

clock = pygame.time.Clock()

snake_block = 15
snake_speed = 15

font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsansms', 35)
def Your_score(score):
    value = score_font.render('Your Score: ' + str(score), True, yellow)
    dis.blit(value, [0, 0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Lenght_of_snake = 1


    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message('You lost! Press Q=Quit or C=Play Again', red)
            Your_score(Lenght_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = False
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        apple_rect = apple_img.get_rect(top=foody, left=foodx)
        dis.blit(apple_img, apple_rect)
        # pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Lenght_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        # Your_score(Lenght_of_snake - 1)

        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10.0
            Lenght_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()