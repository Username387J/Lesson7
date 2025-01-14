from random import randint
import pgzrun

WIDTH=400
HEIGHT=400
TITLE="BEE GAME"

flower=Actor("flower")
flower.pos=200,200

def draw():
    screen.fill("black")
    flower.draw()

pgzrun.go()
    