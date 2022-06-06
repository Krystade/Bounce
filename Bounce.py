import pygame
from Ball import Ball
from pygame.locals import *

pygame.init()

def main():
    screen = pygame.display.set_mode([500, 500])
    width, height = pygame.display.get_surface().get_size()
    # Set the background and adjust its size
    #background = pygame.image.load('background.png')
    #background = pygame.transform.scale(background, (w, h))
    ball = Ball(100, 100, 40, "ball.png", screen)

    clock = pygame.time.Clock()
    pygame.display.set_caption("Rolling")

    running = True
    while(running):
        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                #If esc is pressed exit the game
                if event.key == K_ESCAPE:
                    pygame.quit()
                #Jump with space
                if event.key == pygame.K_SPACE:
                    ball.jump()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        #Check which keys are held down
        keys = pygame.key.get_pressed()
        #If a left or right arrow key is pressed, roll that way
        if keys[pygame.K_LEFT]:
            #Accelerate to the left
            ball.acceleration = -.05
            
        elif keys[pygame.K_RIGHT]:
            #Accelerate to the right
            ball.acceleration = .05
        else:
            ball.acceleration = 0


        #Fill the background
        screen.fill((55,155,155))
        #Update the ball

        ball.update(screen)

        #next frame
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    #GLOBAL VARIABLES
    fps = 60
    
    main()
    pygame.quit()
