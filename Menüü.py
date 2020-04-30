import pygame, sys

pygame.init();
win = pygame.display.set_mode((1280,720));
pygame.display.set_caption("MENÜÜ");
taust = pygame.image.load('menüüü.png')
menüü = True;
win.blit(taust, [0, 0])
pygame.display.update()


pygame.display.flip();

def alusta():
    win.fill((0,0,0));
    pygame.display.flip();
    import game.py;

def juhised():
    win.fill((0,0,0));
    pygame.display.flip();
    import Juhised.py;

while menüü:
    for event in pygame.event.get():
        print(event);
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if pygame.mouse.get_pos()[0] >= 360 and pygame.mouse.get_pos()[1] >= 270:
                if pygame.mouse.get_pos()[0] <= 930 and pygame.mouse.get_pos()[1] <= 320:
                        alusta()
                        
            if pygame.mouse.get_pos()[0] >= 450 and pygame.mouse.get_pos()[1] >= 430:
                if pygame.mouse.get_pos()[0] <= 820 and pygame.mouse.get_pos()[1] <= 480:
                        juhised()
            
        
            
        
