import pyglet


class Button:
    def __init__(self, x, y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.width = len(self.text) * (self.size // 2)
        self.button_text = pyglet.text.Label(self.text, font_name="Calibri", font_size=self.size,
                                             x=self.x, y=self.y)

    def render(self):
        # some image or something graphical here
        self.show_text()

    def show_text(self):
        self.button_text.draw()

    def pressed(self, x, y) -> bool:
        if self.x + self.width >= x >= self.x:
            if self.y + self.size >= y >= self.y:
                return True
        return False
