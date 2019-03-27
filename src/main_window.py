import os
import pyglet
from pyglet.window import key, mouse

import countdown
import team

WIDTH = 800
HEIGHT = 600
main_window = pyglet.window.Window(WIDTH, HEIGHT, "Fingerpost")
timer = countdown.Timer(main_window.width//2 - 70, main_window.height//2 + 220, 50)
team1 = team.Team("Home", None)
team2 = team.Team("Guest", None)
cwd = os.getcwd()
os.chdir(cwd[:len(cwd) - 3])
background = pyglet.image.load("gfx\\Table.png")


@main_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        timer.start()
    elif symbol == key.LEFT:
        team1.set_name(input("Type team's 1 name: "))
    elif symbol == key.RIGHT:
        team2.set_name(input("Type team's 2 name: "))


@main_window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed at {}, {}.'.format(x, y))


def init():
    pass


def update(dt):
    timer.update()


@main_window.event
def on_draw():
    main_window.clear()
    background.blit(0, 0)
    timer.render()
    team1.render(30, HEIGHT - 100, 70, HEIGHT - 180)
    team2.render(WIDTH - 160, HEIGHT - 100, WIDTH - 95, HEIGHT - 180)
