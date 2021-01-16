import pygame
import random
from pygame import mixer

count=0
fail=0
overbutton="off"
#from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,700))
icon=pygame.image.load('coconut.png')
pygame.display.set_icon(icon)


#game-name
pygame.display.set_caption("FRUIT IN BOX")



#player
box=pygame.image.load('box.png')
box=pygame.transform.scale(box,(200,100))
boxx=400
boxy=600
bx=0
  
   
#background
sg=pygame.image.load('startmenu_fruit.jpg')
sg=pygame.transform.scale(sg,(800,700))

bg=pygame.image.load('fruitbox.png')
bg=pygame.transform.scale(bg,(800,700))
go=pygame.image.load('gameover.jpg')
go=pygame.transform.scale(go,(800,700))

#fruits
fruitpic=[]
frx=[]
fry=[]
fs=[]

for i in range(6):
    
    fruitpic.append(pygame.image.load('banana.png'))
    fruitpic.append(pygame.image.load('bengan.png'))
    fruitpic.append(pygame.image.load('redgrape.png'))
    fruitpic.append(pygame.image.load('tomato.png'))
    fruitpic.append(pygame.image.load('capcicum.png'))
    fruitpic.append(pygame.image.load('coconut.png'))

    
    fruitpic[i]=pygame.transform.scale(fruitpic[i],(50,50))
    frx.append(random.randint(2,700))
    r=random.randint(-1000,0)
    fry.append(r-(i*200))

    fs.append(4)

heart=[]
hx=[]
hy=50
hp=0
hrx=random.randint(10,700)
hry=-200
for i in range(5):
    heart.append(pygame.image.load('Heart_Shape.png'))   
    heart[i]=pygame.transform.scale(heart[i],(30,30))
    hx.append(750-i*(40))

heartbig=pygame.image.load('Heart_Shape.png')  
heartbig=pygame.transform.scale(heartbig,(60,60))


fonts1=pygame.font.Font('freesansbold.ttf',40)
fonts2=pygame.font.Font('freesansbold.ttf',35)
fonts3=pygame.font.Font('freesansbold.ttf',50)

def countboard():
    scount=fonts2.render("COUNT : "+str(count),True,(255, 13, 0))
    screen.blit(scount,(0,0))

def livewrite():
    slive=fonts1.render("LIVE : "+str(5-fail),True,(45, 3, 255))
    screen.blit(slive,(590,0))
    

def fruitfall(x,y,i):
    screen.blit(fruitpic[i],(x,y))  

def boxcollector(x,y):
    screen.blit(box,(x,y))

def distancing(x1,y1,x2,y2):
    d=(((x1-x2)**2)+((y1-y2)**2))**(.5)
    if(d<100):
        return True
    else:
        return False

def liveheart(x,y,i):
    screen.blit(heart[i],(x,y))  

def heartfall(x,y):
    screen.blit(heartbig,(x,y))  



    
fontg=pygame.font.Font('freesansbold.ttf',80)
def gameover():
    g2=fonts3.render("YOUR SCORE: "+str(count),True,(235, 238, 242))
    gom=mixer.Sound('Pacman_Introduction_Music-KP-826387403.wav')
    gom.play()
    screen.blit(g2,(200,550))

def text_objects(text, font):
    textSurfac = font.render(text, True, (255,255,255))
    return textSurfac, textSurfac.get_rect()
 
def button(text,x,y,w,h,c1,c2,ask):
    mice=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()


    if((x+w>mice[0]>x) and (y+h>mice[1]>y)):
        pygame.draw.rect(screen,c2,(x,y,w,h))
        if click[0]==1:
            clm=mixer.Sound('laser.wav')
            clm.play()
            return ask
    else:pygame.draw.rect(screen,c1,(x,y,w,h))
    buttontext=pygame.font.Font('freesansbold.ttf',40)
    textsurf,textRect=text_objects(text,buttontext)
    textRect.center=( (x+(w/2)), (y+(h/2)) )
    screen.blit(textsurf,textRect)
playmusic=True
if playmusic:
    mixer.music.load('Pim Poy.wav ')
    mixer.music.play(-1) 


running=False
intro = True
screen.fill((66, 236, 245))
screen.blit(sg,(0,0))
while intro:
    screen.fill((66, 236, 245))
    screen.blit(sg,(0,0))
   
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.quit()
        
        action= button("PLAY",300,450,200,60,(75, 97, 70),(45, 224, 0),"start")       
        if (action=="start"):
            running=True
            intro=False
        pygame.display.update()
while running:
    
        screen.fill((66, 236, 245))
        
    
        
        if(fail<6):screen.blit(bg,(0,0))  
        
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                running=False
                pygame.quit()
            if (event.type==pygame.KEYDOWN):
                  if(event.key==pygame.K_RIGHT):
                      bx= 8
                  elif(event.key==pygame.K_LEFT):
                      bx= -10
            if (event.type==pygame.KEYUP):
                  if(event.key==pygame.K_RIGHT) or (event.key==pygame.K_LEFT) :
                      bx=0
        playmusic=True
        if(boxx>=630):
             boxx=630
        if(boxx<=-30):
            boxx=-30         
        for i in range(6):
             fry[i]+=2
             fruitfall(frx[i],fry[i],i)
             
             collisioncatch=distancing(frx[i],fry[i],boxx,boxy+50)
             collisiongroundf=distancing(5,fry[i],5,750)
             collisionheart=distancing(hrx,hry,boxx,boxy+50)
             collisiongroundh=distancing(5,hry,5,750)
    
             if collisioncatch :
                 
                ex=mixer.Sound('Jump-SoundBible.com-1007297584.wav')
                ex.play()
                count=count+1
                frx[i]=random.randint(2,700)
                fry[i]=random.randint(-1000,0)
                
             if collisiongroundf:
                 fcm=mixer.Sound('Dry Fire Gun-SoundBible.com-2053652037.wav')
                 fcm.play()
                 fail=fail+1
                 frx[i]=random.randint(2,700)
                 fry[i]=random.randint(-1000,0)
             for i2 in range(fail,5):
               liveheart(hx[i2],hy,i2)  
                  
                 
                 
             if((count%15==0) and (0<fail<6)):
                 hp=.5
             if collisionheart:
                 hcm=mixer.Sound('Power_Up_Ray-Mike_Koenig-800933783.wav')
                 hcm.play()
                 fail=0
                 hp=0
                 hrx=random.randint(2,700)
                 hry=-200
             
             if collisiongroundh:
                 hdcm=mixer.Sound('Dry Fire Gun-SoundBible.com-2053652037.wav')
                 hdcm.play()
                 hp=0

                 hry=-200
             if(overbutton=="off"):
                 hry+=hp
                 heartfall(hrx,hry)
                    
       
              
               
               
               
        if(fail<6):
            
            playmusic=True
            countboard()
            livewrite()            
            boxx+=bx
            boxcollector(boxx,boxy)
        else:
            playmusic=False
            overbutton="on"
            for j in range(6):
                frx[j]=2000;fry[j]=2000
            screen.blit(go,(0,0))      
            gameover()
        
        pygame.display.update()
 
  
    