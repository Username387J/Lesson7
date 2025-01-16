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



def draw():
    screen.fill("black")
    flower.draw()
    bee.draw()
    background.draw()

pgzrun.go()
