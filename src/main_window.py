import os
import pyglet
from pyglet.window import key, mouse

import countdown
import team
from player import Player
from button import Button

WIDTH = 800
HEIGHT = 600
main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Fingerpost", vsync=False, visible=False)
fps = pyglet.clock.ClockDisplay()
cwd = os.getcwd()
os.chdir(cwd[:len(cwd) - 3])  # todo this isn't quite right

icon2 = pyglet.image.load("gfx\\icon2.png")
main_window.set_icon(icon2)
main_window.set_visible(True)

timer = countdown.Timer(WIDTH//2 - 92, HEIGHT//2 + 180, 60, 60 * 20)  # main timer
time_out_timer = None  # time-out timer
game_round = 1

players1 = [Player("Simon", 1), Player("Teodor", 2), Player("player3", 3)]
players2 = [Player("player1", 4), Player("player2", 5), Player("player3", 6), Player("player4", 7)]
team1 = team.Team("Home", players1, 30, HEIGHT - 130, 110, 350)
team2 = team.Team("Guest", players2, 565, HEIGHT - 130, 590, 350)

button1 = Button(360, 60, "first button", 14)
buttons = (button1,)

background = pyglet.image.load("gfx\\table2.png")


def show_round():
    round = pyglet.text.Label(str(game_round), font_name="Calibri", font_size=90, x=340, y=276)
    round.draw()


def show_players(players, team):
    if team == "first":
        x = 32
    else:
        x = WIDTH - 278
    for i, player in enumerate(players):
        player.render(x, (-i + 8) * 25)


def show_buttons():
    for button in buttons:
        button.render()


def show_timers():
    if time_out_timer is None:
        timer.render()
    if time_out_timer is not None:
        time_out_timer.render()


@main_window.event
def on_key_press(symbol, modifiers):
    global game_round, time_out_timer
    if symbol == key.SPACE and time_out_timer is None:
        if not timer.running:
            timer.start()
        else:
            timer.interrupt()
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
        timer.restart()
    elif symbol == key.T:
        if timer.running:
            time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
            timer.interrupt()
        if time_out_timer is not None:
            if not time_out_timer.running:
                time_out_timer.start()
            else:
                time_out_timer.interrupt()
    elif symbol == key.R:
        timer.restart()
        time_out_timer = None


@main_window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        player_buttons = list(map(lambda player: player.get_button(), players1 + players2))
        print('The left mouse button was pressed at ({}, {}).'.format(x, y))

        for i, button in enumerate(player_buttons):
            if button.pressed(x, y):
                print("player {}".format(i + 1))


def init():
    pass


def update(dt):
    global time_out_timer
    if time_out_timer is not None and time_out_timer.finished:
        time_out_timer = None
        timer.start()
    for i, player in enumerate(players1):
        player.update_button(32, (-i + 8) * 25)
    for i, player in enumerate(players2):
        player.update_button(WIDTH - 278, (-i + 8) * 25)
    team1.update()
    team2.update()


@main_window.event
def on_draw():
    main_window.clear()
    background.blit(0, 0)
    team1.render()
    team2.render()
    show_timers()
    show_round()
    show_players(players1, "first")
    show_players(players2, "second")
    show_buttons()
    fps.draw()


pyglet.clock.schedule_interval(update, 1/60)
pyglet.clock.set_fps_limit(60)
