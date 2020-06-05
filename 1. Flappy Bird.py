#by - Tushar Gupta
#about me:- undergraduate in IT at Indian Institute of information Technology, Allahabad
#classic flappy bir game in python using pygame

#importing the pygame library
import pygame
pygame.init()
from random import randint

#making the window
win = pygame.display.set_mode((900,480))
pygame.display.set_caption("Flappy Bird")

#importing the artwork
bird = [pygame.image.load('data/birdup.png'),pygame.image.load('data/birdup.png'),pygame.image.load('data/birdown.png'),pygame.image.load('data/birdown.png')]
pipe = [pygame.image.load('data/pipeup.png'),pygame.image.load('data/pipedown.png')]
gameover = [pygame.image.load('data/gameover.jpg')]
bk = [pygame.image.load('data/flappybk.png')]
boomer = [pygame.image.load('data/boomer.png')]
clock = pygame.time.Clock()

#loading the sound
boom = pygame.mixer.Sound('data/boom.wav')
music = pygame.mixer.music.load('data/bkmusic.mp3')
pygame.mixer.music.play(-1)

score = 0

#player class
class player(object):
    def __init__ (self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def draw(self,win):
        win.blit(bird[self.direction], (self.x,self.y))

# class for pipes
class pipemove(object):
    def __init__ (self, x, y1, y2):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.vel = 5

    def draw(self,win):
        win.blit(pipe[1], (self.x,self.y1))
        win.blit(pipe[0], (self.x,self.y2))
        
#drawing the window    
def redraw():
    win.blit(bk[0], (0,0))
    for blah in obstacle:
        blah.draw(win)
    khiladi.draw(win)
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (750, 10))
    pygame.display.update()

#printing the over screen
def over():
    win.blit(gameover[0], (205,145))
    fontis = pygame.font.SysFont('comiccsans', 50)
    text = fontis.render('Your Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (330, 70))
    text = fonter.render('Press p to Beat your score and press q to quit',1, (255, 255, 255))
    win.blit(text, (205, 100))
    pygame.display.update()
    wait = True
    while wait:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            run = True
            wait = False
        elif key[pygame.K_q]:
            pygame.quit()


#main loop

#defining variables
pipe0 = pipemove(705, 0, 370)
obstacle = [pipe0]
khiladi = player(200, 240, 0)
font = pygame.font.SysFont('comiccsans', 30, True)
fonter = pygame.font.SysFont('arial', 30)
run = False
jump = False
gravity = True
redraw()

#menu page
while not(run):
    text3 = fonter.render('Made by:- Tushar Gupta',1, (255, 255, 255))
    text = fonter.render('Press p to play and q to quit',1, (255, 255, 255))
    text1 = fonter.render('Use Space bar to fly the bird',1,(255, 255, 255))
    win.blit(text3, (600, 440))
    win.blit(text, (310, 200))
    win.blit(text1, (310, 230))
    pygame.display.update()
    clock.tick(27)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
        run = True
    elif key[pygame.K_q]:
        pygame.quit()
        
j = 0

#game loop
while run:
    clock.tick(30)
    for _ in range(10):
        value = randint(0,2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    i = 5
    #moving pipes
    for blah in obstacle:
        blah.x -= i
        if blah.x ==khiladi.x:
            score +=1
        
        #checking collision of the sprite with the pipes
        if khiladi.x + 50 > blah.x and khiladi.x < blah.x + 82:
            if khiladi.y + 42 > blah.y2 or khiladi.y < blah.y2 - 135:
                boom.play()
                pygame.time.delay(1200)
                win.blit(boomer[0], (khiladi.x, khiladi.y -50))
                pygame.display.update()
                pygame.time.delay(1200)
                jump = False
                over()
                score = 0
                gravity = True
                khiladi.y = 240
                obstacle = []
                pipe0 = pipemove(705, 0, 370)
                obstacle = [pipe0]
            
        if blah.x == 630:
            if value == 1:
                obstacle.append(pipemove(900, 0, 370))
            elif value == 2:
                obstacle.append(pipemove(900, -70, 300))
            else:
                obstacle.append(pipemove(900, -130, 240))

    #getting the input
    keys = pygame.key.get_pressed()

    #defining the jump
    if keys[pygame.K_SPACE]:
        jump = True
        j = 10
        khiladi.direction += 1
        if khiladi.direction == 4:
            khiladi.direction = 0
    
    if jump:
        gravity = False
        khiladi.y -= 5
        j -= 1
        if j == 0:
            jump = False
            gravity = True

    #defining gravity
    if gravity:
        khiladi.y += 6


    #checking the collision with thw boundaries
    if khiladi.y > 440 or khiladi.y < 0:
        boom.play()
        pygame.time.delay(1200)
        win.blit(boomer[0], (khiladi.x, khiladi.y -50))
        pygame.display.update()
        pygame.time.delay(1200)
        over()
        score = 0
        jump = False
        obstacle = []
        pipe0 = pipemove(705, 0, 370)
        obstacle = [pipe0]
        khiladi.y = 240

    #drawing the screen
    redraw()

pygame.quit()
#end
