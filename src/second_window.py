import pyglet
from table import Table, table, WIDTH, HEIGHT

display = pyglet.window.get_platform().get_default_display()
monitors = display.get_screens()

second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table (second)", vsync=True, visible=False)
icon1 = pyglet.image.load("..\\gfx\\icon1.png")  # window icons
icon2 = pyglet.image.load("..\\gfx\\icon2.png")
second_window.set_icon(icon1, icon2)
if len(monitors) >= 2:
    second_window.set_location(monitors[0].width + monitors[1].width // 2 - second_window.width // 2, 200)
    # second_window.set_fullscreen(True, monitors[1], width=WIDTH, height=HEIGHT)
second_window.set_visible(True)

background = pyglet.image.load("..\\gfx\\table2.png")


@second_window.event
def on_draw():
    second_window.clear()
    background.blit(0, 0)
    table.team1.render()
    table.team2.render()
    table.show_timers()
    table.show_round()
    Table.show_players(table.get_players("left"))
    Table.show_players(table.get_players("right"))
    Table.show_suspended_players(table.get_players("left"))
    Table.show_suspended_players(table.get_players("right"))
