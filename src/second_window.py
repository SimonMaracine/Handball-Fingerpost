import pyglet
from main_window import WIDTH, HEIGHT, icon1, icon2, team1, team2, \
    players1, players2, show_round, show_players, show_timers, show_suspended_players, \
    player_panel, close_second_window


def init():
    global background, second_window
    display = pyglet.window.get_platform().get_default_display()
    monitors = display.get_screens()

    second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table (second)", vsync=True, visible=False)
    second_window.set_icon(icon1, icon2)
    if len(monitors) >= 2:
        second_window.set_location(monitors[0].width + monitors[1].width // 2 - second_window.width // 2, 200)
        # second_window.set_fullscreen(True, monitors[1], width=WIDTH, height=HEIGHT)
    second_window.set_visible(True)

    background = pyglet.image.load("gfx\\table2.png")
    pyglet.clock.schedule_interval(update, 1)


def update(dt):
    if close_second_window():
        second_window.close()


init()


@second_window.event
def on_draw():
    second_window.clear()
    background.blit(0, 0)
    team1.render()
    team2.render()
    show_timers()
    show_round()
    show_players(players1)
    show_players(players2)
    show_suspended_players(players1)
    show_suspended_players(players2)
    if player_panel is not None:
        player_panel.render()
