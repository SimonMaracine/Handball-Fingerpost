import pyglet
from button import Button


class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.suspended = False
        self.button = None
        self.player = pyglet.text.Label("{}[{}]".format(self.name, self.id),
                                        font_name="Calibri",
                                        font_size=20)
        self.selected = False

    def render(self, x, y):
        self.update(x, y)
        self.player.draw()

    def update(self, x, y):
        self.player.x = x
        self.player.y = y

    def suspend(self):
        self.suspended = True

    def select(self, x, y) -> str:
        if not self.selected:
            self.player.color = (140, 16, 140, 255)
            self.selected = True
            return "selected"
        else:
            self.player.color = (255, 255, 255, 255)
            self.selected = False
            return "released"

    def update_button(self, x, y):
        self.button = Button(x, y, "{}[{}]".format(self.name, self.id), 20)

    def get_button(self):
        return self.button
