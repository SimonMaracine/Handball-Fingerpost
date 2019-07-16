import pyglet


class Timer:

    player = pyglet.media.Player()

    def __init__(self, x: int, y: int, size: int, time: int = 1200, sound=None):
        self.x = x
        self.y = y
        self.size = size
        self.time = time
        self.sound = sound
        self.countdown = self.time
        self.running = False  # for 'starting' the timer only once
        self.finished = False
        self.timer = pyglet.text.Label(Timer.show(self.countdown),
                                       font_name="Open Sans",
                                       font_size=self.size,
                                       x=self.x, y=self.y)

    @staticmethod
    def show(countdown: int) -> str:
        minutes = countdown // 60
        seconds = countdown % 60
        time = "{:02d}:{:02d}".format(minutes, seconds)
        return time

    def render(self):
        self.timer.draw()

    def update(self, dt):
        self.timer.text = Timer.show(self.countdown)
        self.timer.y = self.y

        if self.countdown > 0:
            if self.countdown == 10 and self.sound is not None:
                Timer.player.queue(self.sound)
                Timer.player.play()
            self.countdown -= 1
        else:
            if self.sound is not None:
                Timer.player.queue(self.sound)
                Timer.player.play()
            self.finished = True
            # self.running = False
            pyglet.clock.unschedule(self.update)
            # print("Time's up!")

    def start(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.update, 0.999)
            self.running = True

    def set_time(self, time: int = 1200):
        self.countdown = time
        self.timer.text = Timer.show(self.countdown)
        self.finished = False
        self.pause()

    def pause(self):
        pyglet.clock.unschedule(self.update)
        self.running = False

    def restart(self):
        self.countdown = self.time
        self.timer.text = Timer.show(self.countdown)
        self.finished = False
        self.pause()
        if self.sound is not None:
            Timer.player.delete()
