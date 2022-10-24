# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:23:40 2022

@author: Admin
"""
import pygame

pygame.init()

#set up game
width = 1000
height = 600
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pong')
white = (255, 255, 255)
black = (0, 0, 0)
my_font = pygame.font.SysFont('MSGothic', 30)


clock = pygame.time.Clock()

#Variable
CountA = 0
CountB = 0
PosA = 300
PosB = 300
BallX = 500
BallY = 200
SpeedBall = 3
SpeedPaddle = 10
DirX = -1
DirY = 1


pygame.font.get_fonts()

GameOver = False

while not GameOver:
   
    #background design
    gameDisplay.fill(black)
    pygame.draw.line(gameDisplay, white, (500,10), (500, 590), 5) #middle line
    pygame.draw.line(gameDisplay, white, (10,10), (10, 590), 10) #left border
    pygame.draw.line(gameDisplay, white, (6,10), (995, 10), 10) #top border
    pygame.draw.line(gameDisplay, white, (990,10), (990, 590), 10) #right border
    pygame.draw.line(gameDisplay, white, (6,590), (995, 590), 10) #bottom border

    #display scores at top of page
    TextA = my_font.render(str(CountA), False, white)
    TextB = my_font.render(str(CountB), False, white)
    gameDisplay.blit(TextA, (250,30))
    gameDisplay.blit(TextB, (750,30))
     
    #set up ball
    pygame.draw.rect(gameDisplay, white, pygame.Rect(BallX, BallY, 10, 10))
    
    #ball movement mechanics
    BallX += SpeedBall * DirX
    BallY += SpeedBall * DirY
    
    #bounce mechanics
    if BallX > 975:
        DirX = -1
        SpeedBall = 3
        BallX = 500 #reset ball
        CountA += 1 #player A has scored
    if BallX < 15:
        DirX = 1
        SpeedBall = 3
        BallX = 500 #reset ball
        CountB += 1 #player B has scored
    if BallY > 575:
        DirY = -1 #bounce off bottom wall
        SpeedBall += 1 #speed up after each bounce
    if BallY < 15:
        DirY = 1 #bounce off top wall
        SpeedBall += 1 #speed up after each bounce
    
    if 78 <= BallX <= 80 and PosA <= BallY <= PosA + 100 and DirX == -1:
        DirX = 1 #player A has saved a goal
    if 927 >= BallX >= 925 and PosB <= BallY <= PosB + 100 and DirX == 1:
        DirX = -1 #player B has saved a goal
    
    #set up paddles
    pygame.draw.rect(gameDisplay, white, pygame.Rect(925, PosB, 30, 100))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(50, PosA, 30, 100))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        #paddle movement
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            # if keys[pygame.K_UP]:
            #     if PosB > (15 + SpeedPaddle):
            #         PosB -= (15 + SpeedPaddle)
            # if keys[pygame.K_DOWN]:
            #             y += speed
            if event.key == pygame.K_UP:
                if PosB > (15 + SpeedPaddle):
                    PosB -= (15 + SpeedPaddle)
            if event.key == pygame.K_DOWN:
                if PosB < 495 - (15 + SpeedPaddle):
                    PosB += (15 + SpeedPaddle)
            if event.key == pygame.K_w:
                if PosA > (15 + SpeedPaddle):
                    PosA -= (15 + SpeedPaddle)
            if event.key == pygame.K_s:
               if PosA < 495 - (15 + SpeedPaddle):
                    PosA += (15 + SpeedPaddle)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
