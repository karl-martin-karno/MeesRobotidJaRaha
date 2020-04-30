import pygame, sys

pygame.init();
win = pygame.display.set_mode((1280,720));
pygame.display.set_caption("JUHISED");
menüü = True;
taust = pygame.image.load('juhised.png')
win.blit(taust, [0, 0])

pygame.display.update()

pygame.display.flip();

def alusta():
    win.fill((0,0,0));
    pygame.display.flip();
    import game.py;

while menüü:
    for event in pygame.event.get():
        print(event);
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if pygame.mouse.get_pos()[0] >= 410 and pygame.mouse.get_pos()[1] >= 440:
                if pygame.mouse.get_pos()[0] <= 890 and pygame.mouse.get_pos()[1] <= 490:
                        alusta()