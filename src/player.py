import pyglet
from button import Button
import countdown
import draw


class Player:
    def __init__(self, name, id, team):
        self.name = name
        self.id = id
        self.team = team
        self.suspended = False
        self.yellow_cards = 0
        self.red_cards = 0
        self.button = None
        self.player_text = pyglet.text.Label("{}[{}]".format(self.name, self.id),
                                             font_name="Calibri",
                                             font_size=18)
        self.suspend_text = pyglet.text.Label("[{}]".format(self.id),
                                              font_name="Calibri",
                                              font_size=18)
        self.suspend_timer = None  # player timer
        self.selected = False

    def render(self, y):
        self.update(y)
        self.player_text.draw()
        for i in range(self.yellow_cards):
            draw.rect((190 if self.team == "left" else 800 - 80) + i * 14, y, 8, 15, (255, 255, 0, 255))

    def render_suspended(self, y):
        self.suspend_text.x = 276 if self.team == "left" else 426
        self.suspend_text.y = y

        if self.suspended:
            self.suspend_text.draw()
            if self.suspend_timer is not None:
                self.suspend_timer.render()

        if self.suspend_timer is not None:
            self.suspend_timer.y = y
            if self.suspend_timer.finished:
                self.release()

    def update(self, y):
        self.player_text.x = 32 if self.team == "left" else 800 - 238  # todo the WIDTH!
        self.player_text.y = y

    def suspend(self, timer: countdown.Timer):
        if not self.suspended:
            self.suspended = True
            self.suspend_timer = countdown.Timer(314 if self.team == "left" else 464, -100, 20, 60 * 2)  # todo not that good
            if timer.running:
                self.suspend_timer.start()

    def release(self):
        if self.suspended:
            self.suspended = False
            self.suspend_timer.restart()
            self.suspend_timer = None

    def select(self) -> str:
        if not self.selected:
            self.player_text.color = (140, 16, 140, 255)
            self.selected = True
            return "selected"
        else:
            self.player_text.color = (255, 255, 255, 255)
            self.selected = False
            return "released"

    def update_button(self, x, y):
        self.button = Button(x, y, "{}[{}]".format(self.name, self.id), 20)

    def get_button(self):
        return self.button

    @staticmethod
    def de_select(players, j):
        for i in range(len(players)):
            if j == i:
                continue
            if players[i].selected:
                players[i].select()

    def give_card(self, type: str):
        if type == "yellow":
            self.yellow_cards += 1
        elif type == "red":
            self.red_cards += 1

    def take_away_card(self, type: str):
        if type == "yellow":
            self.yellow_cards -= 1
        elif type == "red":
            self.red_cards -= 1

    def disqualify(self):
        del self
