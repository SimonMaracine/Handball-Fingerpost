import pyglet
from main_window import WIDTH, HEIGHT, \
    team1, team2, players1, players2, show_round, show_players, show_timers

second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Fingerpost (second)", vsync=False)
background = pyglet.image.load("gfx\\Table.png")


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
