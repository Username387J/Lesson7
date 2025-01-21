from random import randint
import pgzrun

WIDTH=400
HEIGHT=400
TITLE="BEE GAME"

flower=Actor("flower")
flower.pos=200,200

bee=Actor("bee")
bee.pos=100,300

background=Actor("background")
background.pos=200,200

score=0
game_over=False

def draw():
    screen.fill("black")
    background.draw()
    screen.draw.text("Score:"+str(score), center=(75,50), fontsize=35, color="white")
    flower.draw()
    bee.draw()
    if game_over:
        screen.fill("white")
        screen.draw.text("Time's Up ! Your Final Score: "+str(score), center=(200,50), fontsize=35, color="black")
    
def move():
    flower.x=randint(50,350)
    flower.y=randint(50,350)

def update():
    global score
    
    if keyboard.right:
       bee.x=bee.x+2 
    
    if keyboard.left:
        bee.x=bee.x-2
    
    if keyboard.up:
        bee.y=bee.y-2

    if keyboard.down:
        bee.y=bee.y+2

   
    if bee.colliderect(flower):
        score=score+10
        move()

def time_up():
    global game_over
    game_over=True

clock.schedule(time_up, 60.0)



move()
pgzrun.go()
    