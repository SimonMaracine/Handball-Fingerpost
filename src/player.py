import pyglet

from src.button import Button
import src.countdown as countdown
import src.draw as draw
from src.config import WIDTH


class Player:

    def __init__(self, name, id, team_side):
        self.name = name
        self.id = id
        self.team_side = team_side
        self.suspended = False
        self.yellow_cards = 0
        self.red_cards = 0
        self.scores = 0
        self.disqualified = False
        self.button = None
        self.player_text = pyglet.text.Label("{}[{}]".format(self.name, self.id),
                                             font_name="Open Sans",
                                             font_size=18)
        self.suspend_text = pyglet.text.Label("[{}]".format(self.id),
                                              font_name="Open Sans",
                                              font_size=18,
                                              color=(255, 190, 255, 255))
        self.scores_text = pyglet.text.Label(str(self.scores),
                                             font_name="Open Sans",
                                             font_size=18,
                                             color=(216, 200, 255, 255))
        self.suspend_timer = None  # player timer
        self.selected = False

    def render(self, y):
        self.update(y)
        self.button.render(False)
        self.player_text.draw()
        self.scores_text.draw()
        for i in range(self.yellow_cards):
            draw.rect((220 if self.team_side == "left" else WIDTH - 50) + i * 14, y, 8, 15, (255, 255, 0, 255))

    def render2(self, y):
        self.update(y)
        self.player_text.draw()
        self.scores_text.draw()
        for i in range(self.yellow_cards):
            draw.rect((220 if self.team_side == "left" else WIDTH - 50) + i * 14, y, 8, 15, (255, 255, 0, 255))

    def render_suspended(self, y):
        self.suspend_text.x = 273 if self.team_side == "left" else 423
        self.suspend_text.y = y + 5

        if self.suspended:
            self.suspend_text.draw()
            if self.suspend_timer is not None:
                self.suspend_timer.render()

        if self.suspend_timer is not None:
            self.suspend_timer.y = self.suspend_text.y - 2
            if self.suspend_timer.finished:
                self.release()

    def update(self, y):
        self.player_text.x = 32 if self.team_side == "left" else WIDTH - 238
        self.player_text.y = y
        self.scores_text.text = str(self.scores)
        self.scores_text.x = 192 if self.team_side == "left" else WIDTH - 80
        self.scores_text.y = y

    def suspend(self, timer: countdown.Timer):
        if not self.suspended:
            self.suspended = True
            self.suspend_timer = countdown.Timer(315 if self.team_side == "left" else 465, -100, 20, 60 * 2)  # todo not that good
            if timer.running:
                self.suspend_timer.start()

    def release(self):
        if self.suspended:
            self.suspended = False
            self.suspend_timer.restart()
            self.suspend_timer = None

    def select(self) -> str:
        if not self.selected:
            if not self.disqualified:
                self.player_text.color = (140, 16, 140, 255)
            else:
                self.player_text.color = (80, 80, 80, 255)
            self.selected = True
            return "selected"
        else:
            if not self.disqualified:
                self.player_text.color = (255, 255, 255, 255)
            else:
                self.player_text.color = (80, 80, 80, 255)
            self.selected = False
            return "released"

    def update_button(self, x, y):
        self.button = Button(x, y - 4, "{}[{}]".format(self.name, self.id), 18, (255, 255, 255, 255), False, False, (140, 140, 140, 255))

    def get_button(self):
        return self.button

    @staticmethod
    def de_select(players, j=None):
        if j is not None:
            for i in range(len(players)):
                if j == i:
                    continue
                if players[i].selected:
                    players[i].select()
                    break
        else:
            for i in range(len(players)):
                if players[i].selected:
                    players[i].select()
                    break

    def give_card(self, type: str):
        if type == "yellow":
            if self.yellow_cards < 2:
                self.yellow_cards += 1
        elif type == "red":
            if self.yellow_cards < 1:
                self.red_cards += 1

    def take_away_card(self, type: str):
        if type == "yellow":
            if self.yellow_cards > 0:
                self.yellow_cards -= 1
        elif type == "red":
            if self.red_cards > 0:
                self.red_cards -= 1

    def disqualify(self):
        self.disqualified = True
        self.player_text.color = (80, 80, 80, 255)

    def team_score(self, up: bool):
        if up is True:
            self.scores += 1
        else:
            if self.scores > 0:
                self.scores -= 1
