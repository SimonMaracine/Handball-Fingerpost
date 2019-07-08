import pyglet


class Timer:
    def __init__(self, x, y, size, time=1200, sound=None):
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
        self.sound = sound

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
            if self.countdown == 10 and self.sound is not None:
                self.sound.play()
            self.countdown -= 1
        else:
            if self.sound is not None:
                self.sound.play()
            self.finished = True
            self.running = False
            pyglet.clock.unschedule(self.update)
            # print("Time's up!")

    def start(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.update, 1)
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
