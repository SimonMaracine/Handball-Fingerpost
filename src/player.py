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

    def render(self, x, y):
        self.update(x, y)
        self.player.draw()

    def update(self, x, y):
        self.player.x = x
        self.player.y = y

    def suspend(self):
        self.suspended = True

    def pressed(self):
        pass

    def update_button(self, x, y):
        self.button = Button(x, y, "{}[{}]".format(self.name, self.id), 20)

    def get_button(self):
        return self.button
