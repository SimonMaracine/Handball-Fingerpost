import pyglet


class Timer:
    def __init__(self, x, y, size, time=20):
        self.x = x
        self.y = y
        self.size = size
        self.time = time
        self.countdown = self.time
        self.running = False  # for 'starting' the timer only once
        self.finished = False

    def render(self):
        timer = pyglet.text.Label("00:{:02d}".format(self.countdown),
                                  font_name="Calibri",
                                  font_size=self.size,
                                  x=self.x, y=self.y)
        timer.draw()

    def update(self, dt):
        if self.countdown > 0:
            self.countdown -= 1
        else:
            self.finished = True
            pyglet.clock.unschedule(self.update)
            print("Time's up!")

    def start(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.update, 1)
            self.running = True

    def set_time(self, time=20):
        self.countdown = time
        self.finished = False
        self.running = False
        pyglet.clock.unschedule(self.update)

    def interrupt(self):
        pyglet.clock.unschedule(self.update)
        self.running = False
