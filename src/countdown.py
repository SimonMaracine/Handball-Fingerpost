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
        self.timer = pyglet.text.Label(__class__.show(self.countdown),
                                       font_name="Calibri",
                                       font_size=self.size,
                                       x=self.x, y=self.y)

    @staticmethod
    def show(countdown) -> str:
        minutes = countdown // 60
        seconds = countdown % 60
        time = "{:02d}:{:02d}".format(minutes, seconds)
        return time

    def render(self):
        self.timer.draw()

    def update(self, dt):
        self.timer.text = __class__.show(self.countdown)
        self.timer.y = self.y
        if self.countdown > 0:
            self.countdown -= 1
        else:
            self.finished = True
            self.running = False
            pyglet.clock.unschedule(self.update)
            print("Time's up!")

    def start(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.update, 0.5)
            self.running = True

    def set_time(self, time=1200):
        self.countdown = time
        self.timer.text = __class__.show(self.countdown)
        self.finished = False
        self.pause()

    def pause(self):
        pyglet.clock.unschedule(self.update)
        self.running = False

    def restart(self):
        self.countdown = self.time
        self.timer.text = __class__.show(self.countdown)
        self.finished = False
        self.pause()
