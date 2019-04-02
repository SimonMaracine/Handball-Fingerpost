import pyglet


class Timer:
    def __init__(self, x, y, size, time=1200):
        self.x = x
        self.y = y
        self.size = size
        self.time = time
        self.countdown = self.time
        self.running = False  # for 'starting' the timer only once
        self.finished = False

    @staticmethod
    def show(countdown) -> str:
        minutes = countdown // 60
        seconds = countdown % 60
        time = "{:02d}:{:02d}".format(minutes, seconds)
        return time

    def render(self):
        timer = pyglet.text.Label(__class__.show(self.countdown),
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
            pyglet.clock.schedule_interval(self.update, 0.5)
            self.running = True

    def set_time(self, time=1200):
        self.countdown = time
        self.finished = False
        self.running = False
        pyglet.clock.unschedule(self.update)

    def interrupt(self):
        pyglet.clock.unschedule(self.update)
        self.running = False
