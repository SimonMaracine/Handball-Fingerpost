import pyglet
from main_window import WIDTH, HEIGHT, \
    team1, team2, players1, players2, show_round, show_players, show_timers

second_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Fingerpost (second)", vsync=False)
background = pyglet.image.load("gfx\\Table.png")


@second_window.event
def on_draw():
    second_window.clear()
    background.blit(0, 0)
    team1.render(30, HEIGHT - 130, 110, 350)
    team2.render(565, HEIGHT - 130, 590, 350)
    show_timers()
    show_round()
    show_players(players1, "first")
    show_players(players2, "second")
