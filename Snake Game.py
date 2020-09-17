import pygame
import random
import time
pygame.init()
clock=pygame.time.Clock()
orange=(255,123,7)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(50,153,213)
display_width=800
display_height=600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake Game")
snake_block=10
snake_speed=15
snake_list=[]
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(gamedisplay,orange,[x[0],x[1],snake_block,snake_block])
def snakegame():
    game_over=False
    game_end=False
    x1=display_width/2
    y1=display_height/2
    x1_change=0
    y1_change=0
    snake_list=[]
    length_of_snake=1
    foodx=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,display_height-snake_block)/10.0)*10.0
    while not game_over:
        while game_end==True:
            gamedisplay.fill(blue)
            font_style=pygame.font.SysFont("comicsansms",25)
            msg=font_style.render("You Lost ! Want to play again? Press Space Bar",True,red)
            gamedisplay.blit(msg,[display_width/6,display_height/2])
            score=(length_of_snake-1)*5
            score_font=pygame.font.SysFont("comicsansms",35)
            value=score_font.render("Your Score : "+str(score),True,green)
            gamedisplay.blit(value,[display_width/3,display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        snakegame()
                if event.type==pygame.QUIT:
                    game_over=True
                    game_end=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=+snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=+snake_block
        if x1>=display_width or x1<0 or y1>=display_height or y1<0:
            game_end=True
        x1+=x1_change
        y1+=y1_change 
        gamedisplay.fill(black)
        pygame.draw.rect(gamedisplay,green,[foodx,foody,snake_block,snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_Head:
                game_end=True
        snake(snake_block,snake_list)
        pygame.display.update()
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,display_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,display_height-snake_block)/10.0)*10.0
            length_of_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snakegame()