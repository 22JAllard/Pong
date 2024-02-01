import pygame #import pygame
import sys #imports system
import random #imports random
pygame.init()

#set variables
width = 1000
height = 500
fps=69
white = (255, 255, 255)
black = (0, 0, 0)

#create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
left_score = 0
right_score = 0
font = pygame.font.SysFont('Ariel', 60)

#the bats
bat_size = 25
y1 = 150
y2 = 150
bat1 = pygame.Rect(50, y1, bat_size //2, bat_size *3)
bat2 = pygame.Rect(925, y2, bat_size //2, bat_size *3)
bat1.y
bat2.y
bat1.y = 150
bat2.y = 150
ball_speedx = 5
ball_speedy = 5

#ball draw
ballradius=8
ball = pygame.Rect(width // 2, height // 2, ballradius, ballradius)

#background
run = True
while run:
    screen.fill(black)
    pygame.draw.rect(screen, white, bat1)
    pygame.draw.rect(screen, white, bat2)
    pygame.draw.circle(screen, (white), (ball.x, ball.y), ballradius, ballradius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #bat movement
    key = pygame.key.get_pressed()

    #left bat
    if key[pygame.K_w]:
        if bat1.y <= 0:
            bat1.y = 0
        else:
            bat1.y -= 5
    if key[pygame.K_s]:
        if bat1.y >= height - bat_size *3:
            bat1.y = height - bat_size *3
        else:
            bat1.y += 5
        pygame.draw.rect(screen, white, bat1)

    #right bat
    if key[pygame.K_UP]:
        if bat2.y <= 0:
            bat2.y = 0
        else:
            bat2.y -= 5
    if key[pygame.K_DOWN]:
        if bat2.y >= height - bat_size *3:
            bat2.y = height - bat_size *3
        else:
            bat2.y += 5
        pygame.draw.rect(screen, white, bat2)
        
    #ball moving?
    ball.x += ball_speedx 
    ball.y += ball_speedy 

    #wall collision
    if ball.x >= 1000 or ball.x <= 0:
        ball_speedx = -ball_speedx

    if ball.y >= 500 or ball.y <= 0:
        ball_speedy = -ball_speedy

    #bat collision
    if ball.colliderect(bat1) or ball.colliderect(bat2):
        ball_speedx = -ball_speedx

    #scoring
    #left
    if ball.x == 0:
        right_score += 1
        ball.x = 500
        ball.y = 250

    #right
    if ball.x == 1000:
        left_score += 1
        ball.x = 500
        ball.y = 250
        
    if left_score == 11 or right_score == 11:
        pygame.quit()
        sys.exit()    

    #display scores
    left_score_text = font.render("Score: " + str(left_score), True, white)
    right_score_text = font.render("Score: " + str(right_score), True, white)

    screen.blit(left_score_text, (10, 10))
    screen.blit(right_score_text, ((width - right_score_text.get_width()) - 10, 10))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

#important stuff for quitting
pygame.quit()
sys.exit()