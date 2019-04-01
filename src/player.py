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
        self.button = Button(x, y, self.name, 20)

    def suspend(self):
        self.suspended = True

    def pressed(self):
        pass
