import pyglet


class Team:
    def __init__(self, name, players, name_x, name_y, score_x, score_y):
        self.name = name
        self.players = players
        self.score = 0
        self.time_out_requests = 0
        self.name_x = name_x
        self.name_y = name_y
        self.team_name = pyglet.text.Label(self.name,
                                           font_name="Calibri",
                                           font_size=40,
                                           x=name_x, y=name_y)
        if self.team_name.content_width > 200:
            self.team_name.font_size = (195 * 40) // self.team_name.content_width
            self.name_x = name_x + 4
        self.score_x = score_x
        self.team_score = pyglet.text.Label(str(self.score),
                                            font_name="Calibri",
                                            font_size=54,
                                            x=score_x, y=score_y)

    def render(self):
        self.team_name.draw()
        self.team_score.draw()

    def update(self):
        self.team_score.text = str(self.score)
        self.team_name.x = self.name_x - 1 + (202 - self.team_name.content_width) // 2
        self.team_name.y = self.name_y + 6 + (100 - self.team_name.content_height) // 2
        self.team_score.x = self.score_x - 1 + (100 - self.team_score.content_width) // 2

    def score_up(self):
        self.score += 1

    def score_down(self):
        if self.score > 0:
            self.score -= 1

    def request_time_out(self):
        self.time_out_requests += 1
