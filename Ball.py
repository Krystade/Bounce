import pygame

class Ball():
    def __init__(self, x, y, width, spritePath, surface):
        self.x = x
        self.y = y
        #How fast the ball is accelerating
        self.acceleration = 0
        #How fast the ball is going x direction
        self.speed = 0
        #How fast the ball is going y direction
        self.ySpeed = 1.5
        #How fast the ball slows down
        self.drag = .01
        #How high the ball will jump when space is pressed
        self.jumpHeight = 10
        
        
        self.width = width
        self.sprite = pygame.transform.scale(pygame.image.load(spritePath), (width, width))
        self.rotation = 0
        self.surface = surface

        self.angle = 0

    def display(self):
        #Rotate the original image to stop deformation
        self.rotatedSprite = pygame.transform.rotate(self.sprite, self.rotation)
        #Calc rotation based on speed
        self.rotation -= self.speed

        boundingBox = self.rotatedSprite.get_rect()
        boundingBox.center = (self.x + self.width/2, self.y + self.width/2)

        #how much to offset the rotated image to keep the center the same
        #x,y
        offset = (self.x + self.width/2 - boundingBox.width/2, self.y + self.width/2 - boundingBox.height/2)
        #Draw the newly rotated sprite
        self.surface.blit(self.rotatedSprite, offset)
        #Draw the bounding box
        #pygame.draw.rect(self.surface, (255,0,0), boundingBox, 4)
    
    def move(self, screen):
        #How fast the ball will accelerate downward
        gravity = .25
        #Define the edges of the screen
        width, height = screen.get_size()

        #If the ball is moving left slow it down to the right
        if(self.speed < -0.0001):
            self.speed += self.drag
        #If the ball is moving right slow it down to the left
        elif(self.speed > 0.0001):
            self.speed -= self.drag
        else:
            self.speed = 0
        #If the ball is moving up slow it downwards
        if(self.ySpeed < -0.0001):
            self.ySpeed += self.drag
        #If the ball is moving down slow it upwards?
        elif(self.ySpeed > 0.0001):
            self.ySpeed -= self.drag
        else:
            self.ySpeed = 0

            
            
        #Update the speed based on any acceleration
        self.speed += self.acceleration
        #Always accelerate the ball downwards
        self.ySpeed += gravity
        #Check if the ball's new position would stil be on the screen
        newPos = (self.x + self.speed, self.y + self.ySpeed)
        if(newPos[0] < 0 or newPos[0] > width - self.width):
            #If it would put it off the screen, instead flip the speed direction and put it at the edge
            self.speed *= -.75
        if(newPos[1] < 0 or newPos[1] > height - self.width):
            #If it would put it off the screen, instead flip the speed direction and put it at the edge
            self.ySpeed *= -.75
            #Stop the ball from bouncing infinitely
            if self.ySpeed < 1 and self.ySpeed > -1:
                self.ySpeed = 0
            
        #Update the x pos based on the speed
        self.x += self.speed
        self.y += self.ySpeed

        
    def jump(self):
        #Define the edges of the screen
        width, height = self.surface.get_size()
        #Make sure the ball isnt falling or going up
        #Still should make sure the ball is on the ground not just at the apex of the jump
        if(False and self.ySpeed == 0):
            self.ySpeed = self.jumpHeight

        if (self.y >= height - self.width - 15):
            self.ySpeed += self.ySpeed/abs(self.ySpeed) * self.jumpHeight
            print("boing")
            
        
    def update(self, screen):
        self.move(screen)
        self.display()
