import pyglet


class Timer:
    def __init__(self, x, y, size, time=20):
        self.x = x
        self.y = y
        self.size = size
        self.time = time
        self.countdown = self.time

    def render(self):
        timer = pyglet.text.Label("{}:00".format(self.countdown),
                                  font_name="Calibri",
                                  font_size=self.size,
                                  x=self.x, y=self.y)
        timer.draw()

    def update(self, dt):
        if self.countdown > 0:
            self.countdown -= 1
        else:
            print("Time's up.")

    def start(self):
        pyglet.clock.schedule_interval(self.update, 1)
