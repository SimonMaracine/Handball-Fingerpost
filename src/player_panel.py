from button import Button
import draw


class PlayerPanel:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.suspend_button = Button(x + 20, y + 30, "Suspend", 16, (255, 16, 16, 255), True)
        self.release_button = Button(x + 20, y + 30 - 25, "Release", 16, (255, 16, 16, 255), True)
        self.yellow_card_button = Button(x + 20, y + 30 - 50, "Give yellow card", 16, (255, 16, 16, 255), True)
        self.red_card_button = Button(x + 20, y + 30 - 75, "Give red card", 16, (255, 16, 16, 255), True)
        self.disqualify_button = Button(x + 20, y + 30 - 100, "Disqualify", 16, (255, 16, 16, 255), True)
        self.buttons = [
            self.suspend_button, self.release_button,
            self.yellow_card_button, self.red_card_button,
            self.disqualify_button
        ]
        self.width = 180
        self.height = 25 * len(self.buttons)

    def render(self):
        draw.rect(self.x + 14, self.y - 15 * len(self.buttons), self.width, self.height, (255, 255, 255, 255))
        for button in self.buttons:
            button.render()

    def update(self, x, y, timer) -> bool:  # returns bool to not check for other buttons bellow the panel
        if self.buttons[0].pressed(x, y):
            self.player.suspend(timer)
            return True
        elif self.buttons[1].pressed(x, y):
            self.player.release()
            return True
        elif self.buttons[2].pressed(x, y):
            self.player.give_card("yellow")
            return True
        elif self.buttons[3].pressed(x, y):
            self.player.give_card("red")
            return True
        elif self.buttons[4].pressed(x, y):
            self.player.disqualify()
            return True
        return False
