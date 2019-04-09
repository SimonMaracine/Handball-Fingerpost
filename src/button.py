import pyglet
import draw


class Button:
    def __init__(self, x, y, text, size, color=(255, 255, 255, 255), bold=False, bigger=False, secondary_color=(0, 0, 0, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.color = color
        self.bold = bold
        self.bigger = bigger
        self.secondary_color = secondary_color
        self.width = len(self.text) * (self.size // 2) + (24 if self.bigger else 0)
        self.height = self.size + (5 if self.bigger else 0)
        self.button_text = pyglet.text.Label(self.text, font_name="Calibri", font_size=self.size,
                                             x=self.x, y=self.y, color=self.color, bold=self.bold)
        self.highlight = False

    def render(self, text: bool=True):
        # some image or something graphical here todo implement this
        if self.highlight:
            draw.rect(self.x, self.y - 3, self.width, self.height, self.secondary_color)
        else:
            pass
        if text:
            self.show_text()

    def show_text(self):
        self.button_text.draw()

    def pressed(self, x, y) -> bool:
        if self.x + self.width >= x >= self.x:
            if self.y + self.height - (5 if self.bigger else 0) >= y >= self.y - (5 if self.bigger else 0):
                self.highlight = True
                return True
        self.highlight = False
        return False
