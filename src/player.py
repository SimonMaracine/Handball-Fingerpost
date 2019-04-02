import pyglet
from button import Button


class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.suspended = False
        self.button = None

    def render(self, x, y):
        player = pyglet.text.Label("{}[{}]".format(self.name, self.id),
                                   font_name="Calibri",
                                   font_size=20,
                                   x=x, y=y)
        player.draw()

    def suspend(self):
        self.suspended = True

    def pressed(self):
        pass

    def update_button(self, x, y):
        self.button = Button(x, y, "{}[{}]".format(self.name, self.id), 20)

    def get_button(self):
        return self.button
