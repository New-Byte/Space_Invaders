#Import important libraries

import random

import pygame

from pygame import mixer

#Initialize a pygame

pygame.init()

#Create a game window
screen = pygame.display.set_mode((800,600))

#Background image

background = pygame.image.load('bg2.png')

#Background sound

mixer.music.load('bg.wav')
mixer.music.play(-1)

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('ufo.png')
X = 370
Y = 480
X_change = 0
Y_change = 0

#Enemy

#Multiple enemies
enemyImg = []
e_X = []
e_Y = []
e_X_change = []
e_Y_change = []

#number of enemies

n = random.randint(1,10)

#For loop to append all enemies

for i in range(n):
    enemyImg.append(pygame.image.load('alien.png'))
    e_X.append(random.randint(0,736))
    e_Y.append(random.randint(50,200))
    e_X_change.append(5)
    e_Y_change.append(25)

#Bullet
bulletImg = pygame.image.load('bullet.png')
b_X = 0
b_Y = 480
b_X_change = 0
b_Y_change = 12
b_state = "ready"

#score

score = 0

font = pygame.font.Font('freesansbold.ttf',32)

t_X = 10

t_Y = 10

#Functionality for score

def show_score(x,y):
    s = font.render("Score : " + str(score),True, (255, 255, 255))
    screen.blit(s,(x,y))

#Functionality for player

def player(x,y):
    screen.blit(playerImg,(x,y))

#Functionality for Enemy

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
#Functionality for bullet
    
def fire_bullet(x,y):
    global b_state
    b_state = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))
    
#Functionality for game over
def game_over():
    gofont = pygame.font.Font('freesansbold.ttf',(70,70,70))
    go = gofont.render("GAME OVER",True, (200, 200, 200))
    screen.blit(go,(200,250))
    
#Functionality for collision
    
def collision(e_X,e_Y,b_X,b_Y) :
    d = ((e_X - b_X)**2  + (e_Y - b_Y)**2)**0.5
    if d <=20 :
        return True
    
    else:
        return False
    

#To hold the game window create infinite loop(Virus to hang screen). To deal with virus create an event to quit.

#Important variables

running = True

#Game loop 

while running:
    
    #Fill background colour RGB
    
    screen.fill((0, 0, 0))
    
    #Display background
    
    screen.blit(background,(0, 0))
    
    for event in pygame.event.get():
        
        #Quit functionality
        
        if (event.type == pygame.QUIT):
            pygame.display.quit()
            pygame.quit()
            runnung = False
            
        #Check if Keystroke is being pressed
        
        if (event.type == pygame.KEYDOWN) :
            
            #Check which key is being pressed
            
            #Horizontle movements
            if (event.key == pygame.K_LEFT) :
                X_change = -5
                
            if (event.key == pygame.K_RIGHT) :
                X_change = 5
            
            #Bullet movements
                
            if (event.key == pygame.K_SPACE) :
                if b_state == "ready" :
                    b_sound = mixer.Sound('lsr.wav')
                    b_sound.play()
                    b_X = X
                    fire_bullet(b_X,b_Y)
        
        #Check if keystroke is released
                
        if (event.type == pygame.KEYUP) :
            
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) :
                
                X_change = 0
    
            #Change the co-ordinates of player and enemy
    
    X += X_change
    
   #Set horizontle movement restrictions for player
    
    if X <= 0 :
        X = 0
        
    elif X >=736 :
        X = 736
        
    #Set movement restrictions for enemy
    
    for i in range(n):
        
        #Game over
        if e_Y[i] >=440 :
            for j in range(n):
                e_Y[j] = 2000
                
            game_over()
            break
        
        e_X[i] += e_X_change[i]
        if e_X[i] <= 0 :
            e_X_change[i] = 5
            e_Y[i] += e_Y_change[i]
            
        elif e_X[i] >=736 :
            e_X_change[i] = -5
            e_Y[i] += e_Y_change[i]
                  
        #Check for hit
        
        check = collision(e_X[i],e_Y[i],b_X,b_Y)
        if check :
            
            c_sound = mixer.Sound('exp.wav')
            c_sound.play()
            b_Y= 480
            b_state = "ready"
            score += 2
            e_X[i] = random.randint(0,736)
            e_Y[i] = random.randint(50,200)
        
        #Call the enemy
    
        enemy(e_X[i],e_Y[i],i)
    
    
    #Shoot multiple bullets
    
    if b_Y <= 0 :
        b_Y = 480
        b_state = "ready"
        
    #Make bullet persistant
        
    if b_state == "fire" :
        fire_bullet(b_X,b_Y)
        b_Y -= b_Y_change
       
    #Call the player
    
    player(X,Y)
    
    #Display the score
    
    show_score(t_X,t_Y)
    
    #Update the changes
    
    pygame.display.update()
