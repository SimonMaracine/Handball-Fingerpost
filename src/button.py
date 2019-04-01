import pyglet


class Button:
    def __init__(self, x, y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.width = len(self.text) * (self.size//2)

    def render(self):
        pass

    def show_text(self):
        text = pyglet.text.Label(self.text, font_name="Calibri", font_size=self.size,
                                 x=self.x, y=self.y)
        text.draw()

    def pressed(self, x, y) -> bool:
        if self.x + self.width >= x >= self.x:
            if self.y + self.size >= y >= self.y:
                return True
        return False
