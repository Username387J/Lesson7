from random import randint
import pgzrun

WIDTH=400
HEIGHT=400
TITLE="POKEMON"

jeff=Actor("jeff")
jeff.pos=200,200

ash=Actor("ash")
ash.pos=100,100

bg=Actor("bg")
bg.pos=200,200

timeboost=Actor("timeboost")
timeboost.pos=200,200

scoreboost=Actor("scoreboost")
scoreboost.pos=200,200


score=0
speed=4
z=60.0
game_over=False

def draw():
    screen.fill("blue")
    screen.draw.text("Score: ",+str(score), center=(75,50), fontsize=40, color="black")
    bg.draw()
    jeff.draw()
    ash.draw()
    scoreboost.draw()
    timeboost.draw()
    if game_over:
        screen.fill("white")
        screen.draw.text("Time's Up ! Your Final Score: "+str(score), center=(200,50), fontsize=35, color="black")

def move():
   jeff.x=randint(50,350)
   jeff.y=randint(50,350)

def update():
    global score

    if keyboard.right:
        ash.x=ash.x+speed

    if keyboard.left:
        ash.x=ash.x-speed

    if keyboard.up:
        ash.y=ash.y-speed

    if keyboard.down:
        ash.y=ash.y+speed

    if ash.collidepoint(ash):
        score=score+10
        move()

    if ash.collidepoint(timeboost):
        addtime()
        movetime()

    if ash.collidepoint(scoreboost):
        addscore()
        movescore()
    

def respawn():
    movescore()
    movetime()    


def timeup():
    global game_over
    game_over=True

def addtime():
    z = z+10.0

def addscore():
    score=score+5

def movescore():
    scoreboost.y=randint(0,400)
    scoreboost.x=randint(0,400)

def movetime():
    timeboost.y=randint(0,400)
    timeboost.x=randint(0,400)

def spawn():
    for i in range (12):
        clock.schedule (respawn, 5.00)



clock.schedule(time_up, z)

move()
pgzrun.go()
