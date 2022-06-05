import pygame, time
import random

speedX = 1
speedY = 1

pygame.init()

timeRemaining = 5
timeSurvived = 0
timer = 0

vbuxSpeed = [speedX, speedY]

width, height = 1200, 800
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))

vbux = pygame.image.load("assets/target.png")
vbuxRect = vbux.get_rect()

while True:
    screen.fill(backgroundColor)

    screen.blit(vbux, vbuxRect)
    vbuxRect = vbuxRect.move(vbuxSpeed)

    eve = pygame.event.get()

    for event in eve:

        if event.type == pygame.MOUSEBUTTONUP:
            if vbuxRect.collidepoint(pygame.mouse.get_pos()):
                timeRemaining = timeRemaining + 1
                vbuxSpeed = [speedX + random.randint(1,19), speedY + random.randint(1,19)]
            else:
                timeRemaining = timeRemaining - 1

    if vbuxRect.left < 0 or vbuxRect.right > width:
        vbuxSpeed[0] = -vbuxSpeed[0]
    if vbuxRect.top < 0 or vbuxRect.bottom > height:
        vbuxSpeed[1] = -vbuxSpeed[1]

    timer = timer + 1

    if timer == 100:
        
        timeRemaining = timeRemaining - 1
        timeSurvived = timeSurvived + 1
        
        if timeRemaining <= 0:
            print(timeSurvived, "seconds survived!")
            break
        
        print(timeRemaining, "seconds left")
        timer = 0

    pygame.display.flip()
    time.sleep(10 / 1000)
