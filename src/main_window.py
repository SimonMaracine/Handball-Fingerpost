import os
import pyglet
from pyglet.window import key, mouse

import countdown
import team
from player import Player
from button import Button
from player_panel import PlayerPanel
import window0

WIDTH = 800
HEIGHT = 600
closed = False


def init(*args):
    global main_window, fps, timer, time_out_timer, game_round, round_text, player_panel, \
        players1, players2, team1, team2, buttons, background, icon1, icon2
    print(window0.get_text(0))
    main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table", vsync=True, visible=False)
    fps = pyglet.clock.ClockDisplay()
    os.chdir("..")

    icon1 = pyglet.image.load("gfx\\icon1.png")  # window icons
    icon2 = pyglet.image.load("gfx\\icon2.png")
    main_window.set_icon(icon1, icon2)
    main_window.set_visible(True)

    timer = countdown.Timer(WIDTH // 2 - 92, HEIGHT // 2 + 180, 60, 60 * 20)  # main timer
    time_out_timer = None  # time-out timer
    game_round = 1
    round_text = pyglet.text.Label(str(game_round), font_name="Calibri", font_size=90, x=334, y=304)
    player_panel = None

    players1 = [Player("Simon", 1, "left"), Player("Teodor", 2, "left"), Player("player3", 3, "left")]
    players2 = [Player("player1", 4, "right"), Player("player2", 5, "right"), Player("player3", 6, "right"),
                Player("player4", 7, "right")]
    team1 = team.Team("Home", players1, 30, HEIGHT - 130, 110, 362)
    team2 = team.Team("Guest", players2, 565, HEIGHT - 130, 590, 362)

    button1 = Button(360, 60, "first button", 14)
    buttons = ()

    background = pyglet.image.load("gfx\\table2.png")

    pyglet.clock.set_fps_limit(48)
    pyglet.clock.schedule_interval(update, 1 / 48)


def update(dt):
    global time_out_timer
    if time_out_timer is not None and time_out_timer.finished:
        time_out_timer = None
        timer.start()
        update_players_timers("start", get_players())
    if timer.finished:
        update_players_timers("release", get_players())
    team1.update()
    team2.update()


init()


@main_window.event
def on_draw():
    main_window.clear()
    background.blit(0, 0)
    team1.render()
    team2.render()
    show_timers()
    show_round()
    show_players(get_players("left"))
    show_players(get_players("right"))
    show_suspended_players(get_players("left"))
    show_suspended_players(get_players("right"))
    show_buttons()
    if player_panel is not None:
        player_panel.render()
    fps.draw()


@main_window.event
def on_key_press(symbol, modifiers):
    global game_round, time_out_timer
    if symbol == key.SPACE and time_out_timer is None:
        if not timer.running:
            timer.start()
            update_players_timers("start", get_players())
        else:
            timer.pause()
            update_players_timers("pause", get_players())
    elif symbol == key.LEFT:
        team1.set_name(input("Type first team's name: "))
    elif symbol == key.RIGHT:
        team2.set_name(input("Type second team's name: "))
    elif symbol == key.UP:
        timer.set_time(int(input("Time: ")))
    elif symbol == key.A:
        game_round += 1
    elif symbol == key.Z:
        if game_round > 1:
            game_round -= 1
    elif symbol == key.ENTER and timer.finished:
        game_round += 1
        timer.restart()
    elif symbol == key.T:
        team1.request_time_out()
        if timer.running:
            time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
            timer.pause()
            update_players_timers("pause", get_players())
        if time_out_timer is not None:
            if not time_out_timer.running:
                time_out_timer.start()
            else:
                time_out_timer.pause()
    elif symbol == key.Y:
        team2.request_time_out()
        if timer.running:
            time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
            timer.pause()
            update_players_timers("pause", get_players())
        if time_out_timer is not None:
            if not time_out_timer.running:
                time_out_timer.start()
            else:
                time_out_timer.pause()
    elif symbol == key.R:
        timer.restart()
        time_out_timer = None
        update_players_timers("release", get_players())


@main_window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        # print('The left mouse button was pressed at ({}, {}).'.format(x, y))
        update_player_functionality(x, y)


@main_window.event
def on_mouse_motion(x, y, dx, dy):  # to update buttons' visuals
    for button in map(lambda player: player.get_button(), get_players("remained")):
        button.pressed(x, y)
    if player_panel is not None:
        for button in player_panel.get_buttons():
            button.pressed(x, y)


@main_window.event
def on_close():
    pyglet.app.exit()


def show_round():
    round_text.text = str(game_round)
    round_text.draw()


def show_players(players):
    for i, player in enumerate(players):
        player.render((-i + 13) * 23)


def show_suspended_players(players):
    suspended_players = list(filter(lambda player: player.suspended, players))
    for i, player in enumerate(suspended_players):
        player.render_suspended((-len(suspended_players) + i + 12) * 23)


def show_buttons():
    for button in buttons:
        button.render()


def show_timers():
    if time_out_timer is None:
        timer.render()
    if time_out_timer is not None:
        time_out_timer.render()


def get_players(mode="all") -> list:  # Returns all players.
    if mode == "all":
        players = players1 + players2
    elif mode == "left":
        players = players1
    elif mode == "right":
        players = players2
    else:
        players = list(filter(lambda player: not player.disqualified, players1 + players2))
    return players


def update_player_functionality(x, y):
    global player_panel
    players = get_players("remained")
    player_buttons = list(map(lambda player: player.get_button(), players))

    if player_panel is not None:
        if player_panel.update(x, y, timer):
            return  # to not check for other buttons bellow the panel

    for i, btn in enumerate(player_buttons):
        if btn.pressed(x, y):
            # print("player {}".format(i + 1))
            if players[i].select() == "selected":  # select the clicked player
                player_panel = PlayerPanel(x, y, players[i], (team1, team2))
                if len(list(filter(lambda player: player.selected, players))) == 2:
                    Player.de_select(players, i)  # de-select previous clicked player
            else:
                player_panel = None
            break
    else:
        Player.de_select(players)
        player_panel = None


def init_player_buttons():
    for i, player in enumerate(get_players("left")):
        player.update_button(32, (-i + 13) * 23)
    for i, player in enumerate(get_players("right")):
        player.update_button(WIDTH - 238, (-i + 13) * 23)


init_player_buttons()


def update_players_timers(func: str, players):
    suspended_players = filter(lambda player: player.suspended, players)
    if func == "start":
        for player_timer in map(lambda player: player.suspend_timer, suspended_players):
            player_timer.start()
    elif func == "pause":
        for player_timer in map(lambda player: player.suspend_timer, suspended_players):
            player_timer.pause()
    else:
        for player in suspended_players:
            player.release()
