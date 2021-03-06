import pyglet
import src.draw as draw


class TextWidget:

    def __init__(self, text, x, y, width, batch):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.batch = batch
        self.document = pyglet.text.document.UnformattedDocument(text)

        font = self.document.get_font()
        self.height = font.ascent - font.descent

        self.layout = pyglet.text.layout.IncrementalTextLayout(self.document, self.width, self.height, multiline=False, batch=self.batch)
        self.layout.x = self.x
        self.layout.y = self.y

        self.caret = pyglet.text.caret.Caret(self.layout)

    def hit_test(self, x, y):
        x_hit = 0 < x - self.layout.x < self.layout.width  # todo change this
        y_hit = 0 < y - self.layout.y < self.layout.height
        return x_hit and y_hit

    def render(self):
        draw.rect(self.layout.x - 2, self.layout.y, self.width + 4, self.height, (200, 200, 210, 255))
