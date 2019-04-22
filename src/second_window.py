import pyglet
from pyglet.window import key

from table import Table, table
import config
from config import WIDTH, HEIGHT

second_window = None


def start():
    global second_window
    second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table (second)", vsync=True, visible=False)

    @second_window.event
    def on_draw():
        second_window.clear()
        background.blit(0, 0)
        table.team1.render()
        table.team2.render()
        table.show_timers()
        table.show_round()
        Table.show_players(table.get_players("left"), False)
        Table.show_players(table.get_players("right"), False)
        Table.show_suspended_players(table.get_players("left"))
        Table.show_suspended_players(table.get_players("right"))

    @second_window.event
    def on_key_release(symbol, modifiers):
        global fullscreen
        if symbol == key.F:
            if len(monitors) >= 2:
                if not fullscreen:
                    second_window.set_fullscreen(True, monitors[1], width=WIDTH, height=HEIGHT)
                    fullscreen = True
                else:
                    second_window.set_fullscreen(False, monitors[1], width=WIDTH, height=HEIGHT)
                    fullscreen = False

    @second_window.event
    def on_close():
        config.num_second_windows -= 1

    display = pyglet.window.get_platform().get_default_display()
    monitors = display.get_screens()

    icon1 = pyglet.image.load("..\\gfx\\icon1.png")  # window icons
    icon2 = pyglet.image.load("..\\gfx\\icon2.png")
    second_window.set_icon(icon1, icon2)
    if len(monitors) >= 2:
        second_window.set_location(monitors[0].width + monitors[1].width // 2 - second_window.width // 2, 200)
        # second_window.set_fullscreen(True, monitors[1], width=WIDTH, height=HEIGHT)
    second_window.set_visible(True)

    background = pyglet.image.load("..\\gfx\\table2.png")
    fullscreen = False
    config.num_second_windows += 1
