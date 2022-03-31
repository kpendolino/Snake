import sys, pygame
pygame.init()

gameOver = False

size = width, height = 720, 480
clock = pygame.time.Clock()
clock.tick(1)
vel = 1
speed = [vel, 0]
sp_up = [0,-vel]
sp_dn = [0,vel]
sp_lf = [-vel,0]
sp_rg = [vel,0]
black = 0, 0, 0
length = 3

screen = pygame.display.set_mode(size)

head = pygame.image.load("Snake.png")
head_up = head
head_dn = pygame.transform.rotate(head,180)
head_lf = pygame.transform.rotate(head,90)
head_rg = pygame.transform.rotate(head,-90)

body = pygame.image.load("Snake-Body.png")
body_h = pygame.transform.rotate(body,90)
body_v = body

tail = pygame.image.load("Snake-Tail.png")
tail_up = tail
tail_dn = pygame.transform.rotate(tail,180)
tail_lf = pygame.transform.rotate(tail,90)
tail_rg = pygame.transform.rotate(tail,-90)


head = head_rg
headrect = head.get_rect()

def turnHead(head,oldsp,newsp):
    if oldsp==newsp: return
    if oldsp==sp_up: 
        if newsp==sp_rg:
            return head_rg
        elif newsp==sp_lf:
            return head_lf
    elif oldsp==sp_dn: 
        if newsp==sp_rg:
            return head_rg
        elif newsp==sp_lf:
            return head_lf
    elif oldsp==sp_rg: 
        if newsp==sp_up:
            return head_up
        elif newsp==sp_dn:
            return head_dn
    elif oldsp==sp_lf: 
        if newsp==sp_up:
            return head_up
        elif newsp==sp_dn:
            return head_dn
    return head

while gameOver==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if speed==sp_dn: continue
                elif speed!=sp_up:
                    head=turnHead(head,speed,sp_up)
                    speed=sp_up
            elif event.key==pygame.K_DOWN:
                if speed==sp_up: continue
                elif speed!=sp_dn:
                    head=turnHead(head,speed,sp_dn)
                    speed=sp_dn
            elif event.key==pygame.K_RIGHT:
                if speed==sp_lf: continue
                elif speed!=sp_rg:
                    head=turnHead(head,speed,sp_rg)
                    speed=sp_rg
            elif event.key==pygame.K_LEFT:
                if speed==sp_rg: continue
                elif speed!=sp_lf:
                    head=turnHead(head,speed,sp_lf)
                    speed=sp_lf
            
        
    
    pygame.time.delay(10)
    
    headrect = headrect.move(speed)
    if headrect.left < 0 or headrect.right > width or headrect.top < 0 or headrect.bottom > height:
        gameOver=True

    screen.fill(black)
    screen.blit(head, headrect)
    pygame.display.flip()
