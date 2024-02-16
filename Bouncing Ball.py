import pygame
import time
dirty=list()
pygame.init()
screen = pygame.display.set_mode(size = (1366,768), flags = pygame.FULLSCREEN | pygame.NOFRAME | pygame.SCALED, vsync=1)
ball=pygame.image.load("Icon.bmp").convert()
ball.set_colorkey((255,255,255))
pygame.display.set_icon(ball)
pygame.display.set_caption("Bouncing Ball")
background=pygame.image.load("Background.bmp").convert()
dirty.append(screen.blit(background,(0,0)))
running=True
bounce=True
x = 166
y = 660
a=-9.8
u=0
v=0
t0=time.time()
while running:
    dirty.append(screen.blit(ball,(x,int(660-y))))
    pygame.display.update(dirty[0].union(dirty[1]))
    screen.blit(background,(0,0))
    d=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running=False
    if y>=0 and y<=660:
        t1=time.time()
        v=a*(t1-t0)
        y=y+u*(t1-t0)+0.5*v*(t1-t0)
    if y<0:
        t0=time.time()
        u=(-0.45)*(u+v)
        if u>3:
            y=0
        else:
            y=-1        