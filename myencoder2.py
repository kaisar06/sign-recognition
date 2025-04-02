"""
 WE  CAN DO IT
"""



import pygame 
import math
pygame.init()

SCREEN_HEIGHT ,SCREEN_WIDTH = 600,600
WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()

robot_size = (50,20)
x,y = 100,400     # position x , y 
theta = 0           # curent angle
delta = 0           # changing angle
r = 0.03               # radius of wheel
t = 0
d_w = 0.3           # distance beetwen wheels
w_l = 0             # right wheel angel velocity
w_r = 0             # left wheel  angel velocity

              



in_robot = pygame.Surface(robot_size,pygame.SRCALPHA)
in_robot.fill(WHITE)
    
    



add = 0.2
runing = True


while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                w_l += add
            elif event.key == pygame.K_LEFT:
                w_r += add
            elif event.key == pygame.K_UP:
                add = 0.2
            elif event.key == pygame.K_DOWN:
                add = -0.2
    
    # calculation
    v_l = w_l * r
    v_r = w_r * r 
    v = ( v_r + v_l ) / 2
    v_x = v * math.cos( theta + delta / 2 )
    v_y =  v * math.sin( theta + delta / 2 )
    delta = (v_r - v_l ) / d_w
    theta -= delta
    t = pygame.time.get_ticks() - t
    x += v_x * t / 100.0 
    y -= v_y * t / 100.0
    print(x,y)
    

    if x > SCREEN_WIDTH:
        x -= SCREEN_WIDTH
    elif x < 0:
        x += SCREEN_WIDTH
    if y > SCREEN_HEIGHT:
        y -= SCREEN_HEIGHT
    elif y < 0:
        y += SCREEN_HEIGHT
    

   
    screen.fill(BLACK)
    robot = pygame.transform.rotate(in_robot,math.degrees(theta))
    new_cor = robot.get_rect()
    new_cor.center = x , y
    screen.blit( robot , new_cor )
    
    pygame.display.flip()
    clock.tick(FPS)
    





pygame.quit()
