import os
import pyglet
from pyglet.window import key, mouse

import countdown
import team

WIDTH = 800
HEIGHT = 600
main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Fingerpost")
fps = pyglet.clock.ClockDisplay()
timer = countdown.Timer(WIDTH//2 - 92, HEIGHT//2 + 180, 60, 60 * 20)  # main timer
time_out = None  # time-out timer
game_round = 1
team1 = team.Team("Home", None)
team2 = team.Team("Guest", None)
cwd = os.getcwd()
os.chdir(cwd[:len(cwd) - 3])  # todo this isn't quite right
background = pyglet.image.load("gfx\\Table.png")


def show_round():
    round = pyglet.text.Label(str(game_round), font_name="Calibri", font_size=90, x=340, y=276)
    round.draw()


@main_window.event
def on_key_press(symbol, modifiers):
    global game_round, time_out
    if symbol == key.SPACE and time_out is None:
        timer.start()
    elif symbol == key.LEFT:
        team1.set_name(input("Type first team's name: "))
    elif symbol == key.RIGHT:
        team2.set_name(input("Type second team's name: "))
    elif symbol == key.UP:
        timer.set_time(int(input("Time: ")))
    elif symbol == key.A:
        team1.score_up()
    elif symbol == key.D:
        team2.score_up()
    elif symbol == key.Z:
        team1.score_down()
    elif symbol == key.C:
        team2.score_down()
    elif symbol == key.ENTER and timer.finished:
        game_round += 1
        timer.set_time()
    elif symbol == key.T and time_out is None and timer.running:
        time_out = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
        timer.interrupt()
        time_out.start()


@main_window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed at ({}, {}).'.format(x, y))


# def init():
#     pass


def update(dt):
    global time_out
    if time_out is not None and time_out.finished:
        time_out = None
        timer.start()


@main_window.event
def on_draw():
    main_window.clear()
    background.blit(0, 0)
    if time_out is None:
        timer.render()
    if time_out is not None:
        time_out.render()
    team1.render(30, HEIGHT - 130, 110, 350)
    team2.render(565, HEIGHT - 130, 590, 350)
    show_round()
    fps.draw()


pyglet.clock.schedule_interval(update, 1/60)
