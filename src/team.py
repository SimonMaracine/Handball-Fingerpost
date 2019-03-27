import pyglet


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0

    def render(self, name_x, name_y, score_x, score_y):
        name = pyglet.text.Label("{}".format(self.name),
                                 font_name="Calibri",
                                 font_size=40,
                                 x=name_x, y=name_y)
        score = pyglet.text.Label("{}".format(self.score),
                                  font_name="Calibri",
                                  font_size=42,
                                  x=score_x, y=score_y)
        name.draw()
        score.draw()

    def set_name(self, name):
        self.name = name
