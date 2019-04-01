import pyglet


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0
        self.team_name = None
        self.team_score = None

    def render(self, name_x, name_y, score_x, score_y):
        self.team_name = pyglet.text.Label(self.name,
                                           font_name="Calibri",
                                           font_size=40,
                                           x=name_x, y=name_y)
        self.team_score = pyglet.text.Label(str(self.score),
                                            font_name="Calibri",
                                            font_size=50,
                                            x=score_x, y=score_y)
        self.team_name.draw()
        self.team_score.draw()

    def set_name(self, name):
        self.name = name

    def score_up(self):
        self.score += 1

    def score_down(self):
        if self.score > 0:
            self.score -= 1
