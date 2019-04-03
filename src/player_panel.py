from button import Button


class PlayerPanel:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.suspend_button = Button(x + 15, y + 30, "Suspend player", 16, (255, 16, 16, 255), True)
        self.release_button = Button(x + 15, y + 30 - 25, "Release player", 16, (255, 16, 16, 255), True)

    def render(self):
        self.suspend_button.render()
        self.release_button.render()

    def update(self, x, y):
        if self.suspend_button.pressed(x, y):
            self.player.suspended = True
        elif self.release_button.pressed(x, y):
            self.player.suspended = False
