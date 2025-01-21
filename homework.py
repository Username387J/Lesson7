from random import randint
import pgzrun

WIDTH=400
LENGTH=400

Player=Actor("Player")
Player.pos=100,300

def draw():
    screen.fill("black")