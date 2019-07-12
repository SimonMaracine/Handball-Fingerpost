from os.path import join
import configparser

import pyglet

from src.text_entry import TextWidget
from src.button import Button
from src.config import WIDTH, HEIGHT, icon1, icon2

window0 = None


def save_configuration(configfile=join("data", "_last_config.ini")):
    config = configparser.ConfigParser()
    config["Team1"] = {}
    config["Team2"] = {}
    config["Timer"] = {}

    config["Team1"]["team_name"] = get_text(0)
    for i in range(1, 17):
        config["Team1"]["player{}_name".format(i)] = get_text(i)
    for i in range(34, 50):
        config["Team1"]["player{}_number".format(i - 33)] = get_text(i)

    config["Team2"]["team_name"] = get_text(17)
    for i in range(18, 34):
        config["Team2"]["player{}_name".format(i - 17)] = get_text(i)
    for i in range(50, 66):
        config["Team2"]["player{}_number".format(i - 49)] = get_text(i)

    config["Timer"]["main_timer"] = get_text(66)

    with open(configfile, "w") as file:
        config.write(file)


def load_configuration(configuration=join("data", "_last_config.ini")):
    config = configparser.ConfigParser()
    config.read(configuration)

    try:
        with open(configuration) as _:
            pass
    except FileNotFoundError:
        print("No such configuration file found.")
        return

    try:
        widgets[0].document.text = config["Team1"]["team_name"]
        for i in range(1, 17):
            widgets[i].document.text = config["Team1"]["player{}_name".format(i)]
        for i in range(34, 50):
            widgets[i].document.text = config["Team1"]["player{}_number".format(i - 33)]

        widgets[17].document.text = config["Team2"]["team_name"]
        for i in range(18, 34):
            widgets[i].document.text = config["Team2"]["player{}_name".format(i - 17)]
        for i in range(50, 66):
            widgets[i].document.text = config["Team2"]["player{}_number".format(i - 49)]

        widgets[66].document.text = config["Timer"]["main_timer"]
    except (configparser.MissingSectionHeaderError, KeyError):  # todo might exist more exceptions
        print("Configuration file might be corrupted.")
    finally:
        for widget in widgets:
            widget.caret.visible = False


def create_labels():
    pyglet.text.Label("Team 1", x=10, y=HEIGHT - 110, anchor_y="bottom",
                      color=(0, 0, 0, 255), batch=batch)
    for i in range(16):
        pyglet.text.Label("{}".format(i + 1), x=10, y=HEIGHT - 140 - 30 * i, anchor_y="bottom",
                          color=(0, 0, 0, 255), batch=batch)
    pyglet.text.Label("Team 2", x=WIDTH // 2 - 100, y=HEIGHT - 110,
                      anchor_y="bottom", color=(0, 0, 0, 255), batch=batch)
    for i in range(16):
        pyglet.text.Label("{}".format(i + 1), x=WIDTH // 2 - 100, y=HEIGHT - 140 - 30 * i, anchor_y="bottom",
                          color=(0, 0, 0, 255), batch=batch)
    pyglet.text.Label("Main timer", x=WIDTH // 2 + 190, y=HEIGHT - 110, anchor_y="bottom",
                      color=(0, 0, 0, 255), batch=batch)


def create_widgets() -> tuple:
    widgets_ = []

    # Team 1
    widgets_.append(TextWidget("Home", 85, HEIGHT - 110, 170, batch))
    for i in range(16):
        widgets_.append(TextWidget("", 40, HEIGHT - 140 - 30 * i, 130, batch))

    # Team 2
    widgets_.append(TextWidget("Guest", WIDTH // 2 - 25, HEIGHT - 110, 170, batch))
    for i in range(16):
        widgets_.append(TextWidget("", WIDTH // 2 - 70, HEIGHT - 140 - 30 * i, 130, batch))

    # Team 1 numbers
    for i in range(16):
        widgets_.append(TextWidget("", 190, HEIGHT - 140 - 30 * i, 40, batch))

    # Team 2 numbers
    for i in range(16):
        widgets_.append(TextWidget("", 480, HEIGHT - 140 - 30 * i, 40, batch))

    # Main timer
    widgets_.append(TextWidget("20", WIDTH // 2 + 290, HEIGHT - 110, 70, batch))

    # Those two configuration buttons
    widgets_.append(TextWidget("", 570, HEIGHT - 65, 180, batch))
    widgets_.append(TextWidget("", 570, HEIGHT - 35, 180, batch))

    return tuple(widgets_)


def set_focus(focus_):
    global focus
    if focus:
        focus.caret.visible = False
        focus.caret.mark = focus.caret.position = 0

    focus = focus_
    if focus:
        focus.caret.visible = True
        focus.caret.mark = 0
        focus.caret.position = len(focus.document.text)


def get_text(widget: int) -> str:
    text = widgets[widget].document.text
    return text


def start_table() -> bool:
    try:
        time = int(get_text(66))
    except ValueError:
        print("Main timer has to be an integer.")
        return False

    players_introduced = [get_text(i) for i in list(range(1, 17)) + list(range(18, 34)) if get_text(i)]
    if len(list(filter(lambda text: len(text) <= 11, players_introduced))) < len(players_introduced):
        print("Players' names cannot exceed 11 characters.")
        return False

    if len(get_text(0)) > 22 or len(get_text(17)) > 22:
        print("Teams' names cannot exceed 22 characters.")
        return False

    import src.table as table
    table.prepare_table(
        time,
        [get_text(i) for i in range(1, 17) if get_text(i)],
        [get_text(i) for i in range(18, 34) if get_text(i)],
        get_text(0),
        get_text(17),
        [get_text(i) for i in range(34, 50) if get_text(i)],
        [get_text(i) for i in range(50, 66) if get_text(i)]
    )
    import src.main_window as main_window
    import src.second_window as second_window
    main_window.start()
    second_window.start()
    main_window.main_window.activate()
    return True


def start():
    global window0, widgets, batch, focus

    window0 = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table", vsync=True)
    window0.set_icon(icon1, icon2)

    button1 = Button(15, HEIGHT - 35, "Load last configuration", 16, (0, 0, 0, 255), secondary_color=(200, 200, 200, 255))
    button2 = Button(295, HEIGHT - 65, "Load custom configuration", 16, (0, 0, 0, 255), secondary_color=(200, 200, 200, 255))
    button3 = Button(295, HEIGHT - 35, "Save custom configuration", 16, (0, 0, 0, 255), secondary_color=(200, 200, 200, 255))
    button4 = Button(570, HEIGHT - 335, "Start match", 26, (0, 0, 0, 255), secondary_color=(200, 200, 200, 255))
    buttons = (button1, button2, button3, button4)

    @window0.event
    def on_draw():
        pyglet.gl.glClearColor(0.98, 0.98, 0.98, 1)
        window0.clear()
        for widget in widgets:
            widget.render()
        batch.draw()
        for button in buttons:
            button.render()

    @window0.event
    def on_mouse_motion(x, y, dx, dy):
        for widget in widgets:
            if widget.hit_test(x, y):
                window0.set_mouse_cursor(text_cursor)
                break
        else:
            window0.set_mouse_cursor(None)
        for button in buttons:
            button.pressed(x, y)

    @window0.event
    def on_mouse_release(x, y, button, modifiers):
        for widget in widgets:
            if widget.hit_test(x, y):
                set_focus(widget)
                break
        else:
            set_focus(None)

        if focus:
            focus.caret.on_mouse_press(x, y, button, modifiers)
        if button1.pressed(x, y):
            load_configuration()
        elif button2.pressed(x, y):
            load_configuration(join("data", "custom_configs", "{}.ini".format(get_text(67))))
        elif button3.pressed(x, y):
            save_configuration(join("data", "custom_configs", "{}.ini".format(get_text(68))))
        elif button4.pressed(x, y):
            if start_table():  # open the actual table interface thingy what am I saying
                save_configuration()
                window0.close()

    @window0.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if focus:
            focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    @window0.event
    def on_text(text):
        if focus:
            focus.caret.on_text(text)

    @window0.event
    def on_text_motion(motion):
        if focus:
            focus.caret.on_text_motion(motion)

    @window0.event
    def on_text_motion_select(motion):
        if focus:
            focus.caret.on_text_motion_select(motion)

    @window0.event
    def on_key_release(symbol, modifiers):
        if symbol == pyglet.window.key.TAB:
            if modifiers & pyglet.window.key.MOD_SHIFT:
                direction = -1
            else:
                direction = 1

            if focus in widgets:
                i = widgets.index(focus)
            else:
                i = 0
                direction = 0

            set_focus(widgets[(i + direction) % len(widgets)])
        elif symbol == pyglet.window.key.ENTER:
            if start_table():  # open the actual table interface thingy... what am I saying
                save_configuration()
                window0.close()
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()

    @window0.event
    def on_close():
        pyglet.app.exit()

    batch = pyglet.graphics.Batch()
    create_labels()
    widgets = create_widgets()
    text_cursor = window0.get_system_mouse_cursor('text')
    focus = None
    set_focus(widgets[0])
