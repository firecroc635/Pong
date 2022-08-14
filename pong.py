#general shit
import pygame
from random import *
from pygame.locals import *

#setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen_scroll = [0, 0]
clock = pygame.time.Clock()
bg_width, bg_height = 1280, 720
screen = pygame.display.set_mode([bg_width,bg_height])
running = True
ev = pygame.event.get()
pygame.display.set_caption('pong')


#animation variables
y = 50
momentum = 13
limitedSmol = False
limitedBeg = False
#2nd thing
y2 = 50
limitedSmol2 = False
limitedBeg2 = False

#rects
rectHeight = 150
rectWidth = 10
coll = 175,175,175

#ball
ballX = 640
ballY = 360
addX = 0
addY = 0
disX = 0
disY = 0
ballMove = 12
running = True

#midas
won = 0
start = True

#text
score = 0
score2 = 0
font = pygame.font.SysFont('Brandish Medium',75)
font2 = pygame.font.SysFont('Brandish Medium',120)
font3 = pygame.font.SysFont('Brandish Medium',100)
lobby = 250
ticks = 0
timer = 0
wordX1 = 600
wordX2 = 680

while running:
    #don't worry about these
    ticks += 1
    timer += 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40,40,40))

    #the end
    if ballX <= 0:
        #running = False
        end = True
    elif ballX >= 1300:
        #running = False
        end = True
    else:
        end = False


    if timer < 40:
        coolour = (200,200,200)

    elif timer < 80 and timer > 40:
        coolour = (150,150,150)

    elif timer > 80:
        timer = 0
    else:
        coolour = (150,150,150)


    coolor = (150,150,150)
    if score > score2:
        coolor1 = (175,175,30)
        coolor2 = (150,150,150)
    elif score < score2:
        coolor1 = (150,150,150)
        coolor2 = (175,175,30)
    else:
        coolor1 = (150,150,150)
        coolor2 = (150,150,150)

    if score >= 10:
        wordX1 = 580
    if score2 >= 10:
        wordX2 = 660


    ren = font.render(str(score),1,coolor1)
    screen.blit(ren,(wordX1,20))
    ren1= font.render(':',1,coolor)
    screen.blit(ren1,(640,20))
    ren2 = font.render(str(score2),1,coolor2)
    screen.blit(ren2,(wordX2,20))
    ren3 = font2.render('Press ["S P A C E"]',1,coolour)
    screen.blit(ren3,(300,lobby))

    if start and keys[pygame.K_SPACE] and end == False:
        addY = randint(6, 8)
        addX = randint(6, 8)
        disX = randint(-8, -6)
        disY = randint(-8, -6)
        if randint(0, 1) == 1:
            addX = disX
        else:
            addX = addX
        if randint(0, 1) == 1:
            addY = disY
        else:
            addY = addY

    ballY += addY
    ballX += addX
    print(ballX, ballY)
    if ballY <= 20:
        addY = addY - (addY * 2)
    elif ballY >= 680:
        addY = addY - (addY * 2)

    elif (ballX <= 80 and ballX >= 65)  and (ballY >= y - 8 and ballY <= y + rectHeight + 10):
        score += 1
        addX = addX - (addX * 2)
        won = 0
    elif (ballX >= (1230 - rectWidth - 15) and ballX <= 1235 - rectWidth) and (ballY >= y2 - 8 and ballY <= y2 + rectHeight + 10):
        score2 += 1
        addX = addX - (addX * 2)
        won = 1


    #ball
    pygame.draw.circle(screen,(220,220,220),(ballX,ballY), 14)

    #movement of the 2 players:
    if y <= 20:
        limitedSmol = True
    elif y >= (680 - rectHeight + 5):
        limitedBeg = True
    else:
        limitedSmol = False
        limitedBeg = False

    if y2 <= 20:
        limitedSmol2 = True
    elif y2 >= (680 - rectHeight + 5):
        limitedBeg2 = True
    else:
        limitedSmol2 = False
        limitedBeg2 = False

    pygame.draw.rect(screen,(coll), [(65 - rectWidth),y, rectWidth,rectHeight])
    pygame.draw.rect(screen,(coll), [(55 - rectWidth),y + (50 / 2), rectWidth + 5,rectHeight - 50])
    pygame.draw.rect(screen,(coll), [(1235 - rectWidth),y2, rectWidth,rectHeight])
    pygame.draw.rect(screen,(coll), [(1240 - rectWidth),y2 + (50 / 2), rectWidth + 5,rectHeight - 50])

    if keys[pygame.K_UP] and keys[pygame.K_DOWN] and limitedSmol2 == 0 and end == False:
        y2 += 0
    elif keys[pygame.K_UP] and limitedSmol2 == 0 and end == False:
        y2 -= momentum
        print("yes")
    elif keys[pygame.K_DOWN] and limitedBeg2 == 0 and end == False:
        y2 += momentum
        print('no')

    if keys[pygame.K_w] and keys[pygame.K_s] and limitedSmol == 0 and end == False:
        y += 0
    elif keys[pygame.K_w] and limitedSmol == 0 and end == False:
        y -= momentum
        print("yes")
    elif keys[pygame.K_s] and limitedBeg == 0 and end == False:
        y += momentum
        print('no')
    #end of movement of the 2 players
    if keys[pygame.K_SPACE] and start and end == False:
        lobby = -200
        start = False


    if end:
        screen.fill((50,50,50))
        if won == 0:
            ren4 = font3.render('Player 1 wins',1,coolour)
            screen.blit(ren4,(420,300))
            ren5 = font3.render('Press ["E N T E R"] to play again',1,coolour)
            screen.blit(ren5,(120,100))
            cool = (175,175,30)
            if score <= 10:
                ren6 = font3.render(str(score),1,cool)
                screen.blit(ren6,(620,420))
            else:
                ren6 = font3.render(str(score),1,cool)
                screen.blit(ren6,(600,420))

            if keys[pygame.K_RETURN]:
                end = False
                #start = True
                ballX = 640
                ballY = 360
                score = 0
                score2 = 0
                y = 50
                y2 = 50
        elif won == 1:
            ren4 = font3.render('Player 2 wins',1,coolour)
            screen.blit(ren4,(420,300))
            ren5 = font3.render('Press ["E N T E R"] to play again',1,coolour)
            screen.blit(ren5,(120,100))
            cool = (175,175,30)
            if score2 <= 10:
                ren6 = font3.render(str(score2),1,cool)
                screen.blit(ren6,(620,420))
            else:
                ren6 = font3.render(str(score2),1,cool)
                screen.blit(ren6,(600,420))
            if keys[pygame.K_RETURN]:
                end = False
                #start = True
                ballX = 640
                ballY = 360
                score = 0
                score2 = 0
                y = 50
                y2 = 50
        else:
            ren4 = font3.render('Draw',1,coolour)
            screen.blit(ren4,(560,300))
            ren5 = font3.render('Press ["E N T E R"] to play again',1,coolour)
            screen.blit(ren5,(120,100))
            cool = (175,175,30)
            if score <= 10:
                ren6 = font3.render(str(score),1,cool)
                screen.blit(ren6,(620,420))
            else:
                ren6 = font3.render(str(score),1,cool)
                screen.blit(ren6,(600,420))
            if keys[pygame.K_RETURN]:
                end = False
                #start = True
                ballX = 640
                ballY = 360
                score = 0
                score2 = 0
                y = 50
                y2 = 50
        start = True
    clock.tick(60)
    pygame.display.flip()
