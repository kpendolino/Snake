import sys, pygame
pygame.init()

gameOver = False
size = width, height = 720, 480
vel = 1
speed = [vel, 0]
sp_up = [0,-vel]
sp_dn = [0,vel]
sp_lf = [-vel,0]
sp_rg = [vel,0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

head = pygame.image.load("Snake.png")
head_up = head
head_dn = pygame.transform.rotate(head,180)
head_lf = pygame.transform.rotate(head,90)
head_rg = pygame.transform.rotate(head,-90)

body_lin = pygame.image.load("Snake-Body.png")
body_h = pygame.transform.rotate(body_lin,90)
body_v = body_lin
body_ell = pygame.image.load("Snake-Body-L.png")
body_rg_dn = pygame.transform.rotate(body_lin,-90)
body_dn_lf = pygame.transform.rotate(body_lin,180)
body_lf_up = pygame.transform.rotate(body_lin,90)
body_up_rg = body_ell

tail = pygame.image.load("Snake-Tail.png")
tail_up = tail
tail_dn = pygame.transform.rotate(tail,180)
tail_lf = pygame.transform.rotate(tail,90)
tail_rg = pygame.transform.rotate(tail,-90)

class Snake:
    def __init__(self,snake,speed):
         self.b = snake
         self.s = speed
         self.gameOver = False
    def move(self):
        new = self.b[-1].move(self.s)
        if new.left < 0 or new.right > width or new.top < 0 or new.bottom > height:
            self.gameOver=True
        self.b.pop(0)
        self.b.append(new)
    def draw(self):
        screen.fill(black)
        for i in range(len(self.b)):
            if i==0: # tail
                #get orientation
                if self.b[i].x==self.b[i+1].x: #vertical
                    if self.b[i].y>self.b[i+1].y: #down
                        tail=tail_dn
                    elif self.b[i].y<self.b[i+1].y: #up
                        tail=tail_up
                elif self.b[i].y==self.b[i+1].y: #horizontal
                    if self.b[i].x<self.b[i+1].x: #right
                        tail=tail_rg
                    elif self.b[i].x>self.b[i+1].x: #left
                        tail=tail_lf
                screen.blit(tail,self.b[i])
            elif i==len(self.b)-1: # head
                #get orientation
                if self.b[i].x==self.b[i-1].x and self.b[i].y<self.b[i-1].y:
                    head=head_dn
                elif self.b[i].x==self.b[i-1].x and self.b[i].y>self.b[i-1].y:
                    head=head_up
                elif self.b[i].y==self.b[i-1].y and self.b[i].x<self.b[i-1].x:
                    head=head_lf
                elif self.b[i].y==self.b[i-1].y and self.b[i].x>self.b[i-1].x:
                    head=head_rg
                else: print("  ->  ".join([str(r) for r in self.b]))
                screen.blit(head,self.b[i])
            else: #body
                #get orientation
                if self.b[i].x==self.b[i-1].x and self.b[i].x==self.b[i+1].x: #vertical
                    body=body_v
                elif self.b[i].y==self.b[i-1].y and self.b[i].y==self.b[i+1].y: #horizontal
                    body=body_h
                elif self.b[i].x==self.b[i-1].x and self.b[i].y<self.b[i-1].y: # in going up
                    if   self.b[i].x<self.b[i+1].x: # out going right
                        body=body_up_rg
                    elif self.b[i].x>self.b[i+1].x: # out going left
                        body=body_rg_dn
                elif self.b[i].x==self.b[i-1].x and self.b[i].y>self.b[i-1].y: # in going down
                    if   self.b[i].x<self.b[i+1].x: # out going right
                        body=body_lf_up
                    elif self.b[i].x>self.b[i+1].x: # out going left
                         body=body_dn_lf 
                elif self.b[i].y==self.b[i-1].y and self.b[i].x<self.b[i-1].x: # in going left
                    if   self.b[i].y<self.b[i+1].y: # out going up
                        body=body_lf_up
                    elif self.b[i].y>self.b[i+1].y: # out going down
                        body=body_up_rg
                elif self.b[i].y==self.b[i-1].y and self.b[i].x>self.b[i-1].x: # in going right
                    if   self.b[i].y<self.b[i+1].y: # out going up
                         body=body_dn_lf
                    elif self.b[i].y>self.b[i+1].y: # out going down
                         body=body_rg_dn
                screen.blit(body,self.b[i])
        pygame.display.flip()
    
length = 3
snake = [pygame.Rect(0,240,25,25),pygame.Rect(25,240,25,25),pygame.Rect(50,240,25,25)]
snek = Snake(snake,speed)

while snek.gameOver==False:
    pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if snek.s==sp_dn: continue
                elif snek.s!=sp_up:
                    snek.s=sp_up
            elif event.key==pygame.K_DOWN:
                if snek.s==sp_up: continue
                elif snek.s!=sp_dn:
                    snek.s=sp_dn
            elif event.key==pygame.K_RIGHT:
                if snek.s==sp_lf: continue
                elif snek.s!=sp_rg:
                    snek.s=sp_rg
            elif event.key==pygame.K_LEFT:
                if snek.s==sp_rg: continue
                elif snek.s!=sp_lf:
                    snek.s=sp_lf
            
    snek.move()        
    snek.draw()    
   




