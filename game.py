import pygame, random, sys , time
pygame.init()

win = pygame.display.set_mode((1280, 720))


pygame.display.set_caption("Mees,robotid ja raha")

tegelane = pygame.image.load('male2.png')
taust = pygame.image.load('taust3.jpg')
asi = pygame.image.load("robot1.png")
münt = pygame.image.load("raha.png")
asukoht = [160,485,810,1135]
kell = pygame.time.Clock()
punktid = 0
katki1 = False
katki2 = False
katki3 = False
katki4 = False



class mängija():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 30
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x+40, self.y+60, 115,200)

    def joonista(self, win):
        
        win.blit(tegelane, (self.x,self.y))
        self.hitbox = (self.x+40, self.y+60, 115,200)
        
        
    
        

class objekt():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitbox = (self.x+50 , self.y+120, 100,130)
       

    def joonista(self,win):
        win.blit(asi,  (self.x,self.y))
        self.hitbox = (self.x+50 , self.y+120, 100,130)
        
        
    def katki(self,win):
        asi=pygame.image.load("robot2.png")
        win.blit(asi,  (self.x,self.y))
        
        
        
        


class kukkuja():
    def __init__(self, y, width, height, end):
        self.x = random.choice(asukoht)
        self.y = y
        self.width = width
        self.height = height
        self.rada = [y, end] 
        self.vel = 18
        self.hitbox = (self.x , self.y, 59,450)
        
    def joonista(self, win):
        self.move()
       
        win.blit(münt, (self.x,self.y))
        self.hitbox = (self.x , self.y, 60,59)
        
        
    def move(self):
        
        if self.y < self.rada[1] + self.vel:
             self.y += self.vel
        
        else:
            self.y = -100
            self.x = random.choice(asukoht)
            
    def löök(self):
        self.x = -100
        self.y = random.choice(asukoht)
        
        
      
def tausta_joonistus():
    
    win.blit(taust, (0,0))
    jutt = kirjake.render("Punktid: " + str(punktid), 1,(0,0,0))
    win.blit(jutt, (900,50))
    
    
    
    ese.joonista(win)
    if katki1 is True:
        robot.katki(win)
    else:
        robot.joonista(win)
        
    if katki2 is True:
        robot2.katki(win)
    else:
        robot2.joonista(win)
        
    if katki3 is True:
        robot3.katki(win)
    else:
        robot3.joonista(win)
        
    if katki4 is True:
        robot4.katki(win)
    else:
        robot4.joonista(win)
   
        
    mees.joonista(win)
    
    

    pygame.display.update()


kirjake = pygame.font.SysFont("comicsans",70, True)
mees= mängija(200, 410, 192,256)
robot = objekt(100,410)
robot2 = objekt(425,410)
robot3 = objekt(750,410)
robot4 = objekt(1075,410)
ese = kukkuja(-100, 60,59,450)
run = True

while run:
    
    
    kell.tick(30)
    
    
    if punktid == 20:
        
        font= pygame.font.SysFont("comicsans",100, True)
        tekst = font.render("VÕITSID!",1,(255,0,0))
        win.blit(tekst,(600-(tekst.get_width()/2),200))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    if punktid <=-20:
        
        font= pygame.font.SysFont("comicsans",100, True)
        tekst = font.render("KAOTASID!",1,(255,0,0))
        win.blit(tekst,(600-(tekst.get_width()/2),200))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
    if katki1 is True and katki2 is True and katki3 is True and katki4 is True:
        font= pygame.font.SysFont("comicsans",100, True)
        tekst = font.render("KAOTASID!",1,(255,0,0))
        win.blit(tekst,(600-(tekst.get_width()/2),200))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
       
            
    if robot.hitbox[1] < ese.hitbox[1] + ese.hitbox[3] and robot.hitbox[1] + robot.hitbox[3] > ese.hitbox[1]:
        if robot.hitbox[0] + robot.hitbox[2] > ese.hitbox[0] and robot.hitbox[0] < ese.hitbox[0] + ese.hitbox[2]:
            katki1 = True
            punktid -=2
                       
    if robot2.hitbox[1] < ese.hitbox[1] + ese.hitbox[3] and robot2.hitbox[1] + robot2.hitbox[3] > ese.hitbox[1]:
        if robot2.hitbox[0] + robot2.hitbox[2] > ese.hitbox[0] and robot2.hitbox[0] < ese.hitbox[0] + ese.hitbox[2]:
            katki2 = True
            punktid -=2
             
    if robot3.hitbox[1] < ese.hitbox[1] + ese.hitbox[3] and robot3.hitbox[1] + robot3.hitbox[3] > ese.hitbox[1]:
        if robot3.hitbox[0] + robot3.hitbox[2] > ese.hitbox[0] and robot3.hitbox[0] < ese.hitbox[0] + ese.hitbox[2]:
            katki3 = True
            punktid -=2
            
    if robot4.hitbox[1] < ese.hitbox[1] + ese.hitbox[3] and robot4.hitbox[1] + robot4.hitbox[3] > ese.hitbox[1]:
        if robot4.hitbox[0] + robot4.hitbox[2] > ese.hitbox[0] and robot4.hitbox[0] < ese.hitbox[0] + ese.hitbox[2]:
            katki4 = True
            punktid -=2
    
    if ese.hitbox[1] < mees.hitbox[1] + mees.hitbox[3] and ese.hitbox[1] + ese.hitbox[3] > mees.hitbox[1]:
        if ese.hitbox[0] + ese.hitbox[2] > mees.hitbox[0] and ese.hitbox[0] < mees.hitbox[0] + mees.hitbox[2]:
            ese.löök()
            punktid +=1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and mees.x > mees.vel:
        mees.x -= mees.vel
        mees.left = True
        mees.right = False
    elif keys[pygame.K_RIGHT] and mees.x < 1280 - mees.width - mees.vel:
        mees.x += mees.vel
        mees.right = True
        mees.left = False
    else:
        mees.right = False
        mees.left = False
        mees.walkCount = 0
        
        
    tausta_joonistus()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        

pygame.quit()