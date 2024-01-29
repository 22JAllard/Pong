import pygame #import pygame
import sys #imports system

#set variables
width = 1000
height = 500
fps=60
white = (255, 255, 255)
black = (0, 0, 0)

#create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

#the bats
bat_size = 50
y1 = 150
y2 = 150
bat1 = pygame.Rect(50, y1, bat_size //2, bat_size *3)
bat2 = pygame.Rect(925, y2, bat_size //2, bat_size *3)
bat1.y
bat2.y
bat1.y = 150
bat2.y = 150

#background
run = True
while run:
    screen.fill(black)
    pygame.draw.rect(screen, white, bat1)
    pygame.draw.rect(screen, white, bat2)
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
            bat1.y -= 1
    if key[pygame.K_s]:
        if bat1.y >= 350:
            bat1.y = 350
        else:
            bat1.y += 1
        pygame.draw.rect(screen, white, bat1)

    #right bat
    if key[pygame.K_UP]:
        if bat2.y <= 0:
            bat2.y = 0
        else:
            bat2.y -= 1
    if key[pygame.K_DOWN]:
        if bat2.y >= 350:
            bat2.y = 350
        else:
            bat2.y += 1
        pygame.draw.rect(screen, white, bat2)
        
#important stuff for quitting
pygame.quit()
sys.exit()