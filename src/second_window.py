import pyglet
from main_window import WIDTH, HEIGHT, icon1, icon2, \
    team1, team2, players1, players2, show_round, show_players, show_timers

second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Fingerpost (second)", vsync=False, visible=False)
second_window.set_icon(icon1, icon2)
second_window.set_visible(True)
background = pyglet.image.load("gfx\\table2.png")

# FOR MANAGING THE SECOND MONITOR
# display = window.get_platform().get_default_display()
# screens = display.get_screens()
# windows = []
# for screen in screens:
#     windows.append(window.Window(fullscreen=True, screen=screen))


@second_window.event
def on_draw():
    second_window.clear()
    background.blit(0, 0)
    team1.render()
    team2.render()
    show_timers()
    show_round()
    show_players(players1, "first")
    show_players(players2, "second")
