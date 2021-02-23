import pygame
import os
import math
import random

pygame.init()
width,height=800,500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Hangman")

# Buttons variable
RADIUS=20
GAP=15
letters=[]
startx=round((width - (RADIUS*2+GAP)*13))/2
starty=400
A=65

for i in range(26):
    x=int(startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)))
    y=int(starty + ((i // 13 ) * (GAP + RADIUS * 2)))
    letters.append([x,y,chr(A+i),True])

#  Font 
LETTERS_FONT=pygame.font.SysFont("comicsans",40)
WORD_FONT=pygame.font.SysFont("comicsans",60)
TITLE_FONT=pygame.font.SysFont("comicsans",70)

# Load Image
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#  

#  Hangman variable
hnagmanstatus=0
words=["SAHIL","KHIRSARIYA","VALLABHBHAI"]
word=random.choice(words)
guessed=[]


#  Colors
WHITE=(255,255,255)
BLACK=(0,0,0)

#  Set Game Loop
FPS=60
clock=pygame.time.Clock()
run=True

def draw():
    win.fill(WHITE)

    # Draw Title
    text=TITLE_FONT.render("HANGMAN GAME",1,BLACK)
    win.blit(text,(int(width/2) - int(text.get_width()/2),20))

    #  Draw Words
    dispaly_word=""
    for letter in word:
        if letter in guessed:
            dispaly_word +=letter + ""
        else :
            dispaly_word += "_ "

    text=WORD_FONT.render(dispaly_word,1,BLACK)
    win.blit(text,(400,200))

    # Draw Buttons
    for letter in letters:
        x,y,ltr,visible=letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTERS_FONT.render(ltr,1,BLACK)
            win.blit(text,(int(x-text.get_width()/2),int(y-text.get_height()/2)))

    win.blit(images[hnagmanstatus],(150,100 ))
    pygame.display.update()

def display_msg(msg):
    pygame.time.delay(2000)
    win.fill(WHITE)
    text=WORD_FONT.render(msg,1,BLACK)
    win.blit(text,(int(width/2) - int(text.get_width()/2),int(height/2) - int(text.get_height()/2)))
    pygame.display.update()
    pygame.time.delay(3000)
    


while run :
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis= math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hnagmanstatus+=1

    draw()

    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break
    
    if won:
        display_msg("YOU WON !")
        break

    if hnagmanstatus==6:
        display_msg("YOU LOST !")
        break
        

     

pygame.quit