import pyglet
from text_entry import TextWidget

WIDTH = 800  # these may remain
HEIGHT = 600
window0 = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table (first)", vsync=True)


def create_labels():
    pyglet.text.Label("Team 1", x=10, y=HEIGHT-110, anchor_y="bottom",
                      color=(0, 0, 0, 255), batch=batch)
    for i in range(16):
        pyglet.text.Label("Player {}".format(i + 1), x=10, y=HEIGHT-140-30*i, anchor_y="bottom",
                          color=(0, 0, 0, 255), batch=batch)
    pyglet.text.Label("Team 2", x=WIDTH//2 - 100, y=HEIGHT-110,
                      anchor_y="bottom", color=(0, 0, 0, 255), batch=batch)
    for i in range(16):
        pyglet.text.Label("Player {}".format(i + 1), x=WIDTH//2-100, y=HEIGHT-140-30*i, anchor_y="bottom",
                          color=(0, 0, 0, 255), batch=batch)
    pyglet.text.Label("Main timer", x=WIDTH//2+190, y=HEIGHT-110, anchor_y="bottom",
                      color=(0, 0, 0, 255), batch=batch)


def create_widgets() -> tuple:
    widgets_ = []
    widgets_.append(TextWidget('', 90, HEIGHT - 110, 150, batch))
    for i in range(16):
        widgets_.append(TextWidget('', 90, HEIGHT - 140 - 30 * i, 150, batch))

    widgets_.append(TextWidget('', WIDTH // 2 - 20, HEIGHT - 110, 150, batch))
    for i in range(16):
        widgets_.append(TextWidget('', WIDTH // 2 - 20, HEIGHT - 140 - 30 * i, 150, batch))

    widgets_.append(TextWidget("20", WIDTH // 2 + 290, HEIGHT - 110, 90, batch))
    return tuple(widgets_)


def update(dt):
    pass


@window0.event
def on_draw():
    pyglet.gl.glClearColor(1, 1, 1, 1)
    window0.clear()
    for widget in widgets:
        widget.render()
    batch.draw()


@window0.event
def on_mouse_motion(x, y, dx, dy):
    for widget in widgets:
        if widget.hit_test(x, y):
            window0.set_mouse_cursor(text_cursor)
            break
    else:
        window0.set_mouse_cursor(None)


@window0.event
def on_mouse_press(x, y, button, modifiers):
    for widget in widgets:
        if widget.hit_test(x, y):
            set_focus(widget)
            break
    else:
        set_focus(None)

    if focus:
        focus.caret.on_mouse_press(x, y, button, modifiers)


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
def on_key_press(symbol, modifiers):
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
        start_table()  # open the actual table interface thingy... what am I saying
        window0.close()
    elif symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()


@window0.event
def on_close():
    pyglet.app.exit()


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


def get_text(widget: int):
    text = widgets[widget].document.text
    return text


def start_table():
    import table
    table.prepare_table(int(get_text(34)),
                        [get_text(i) for i in range(1, 16) if get_text(i)],
                        [get_text(i) for i in range(18, 32) if get_text(i)],
                        get_text(0),
                        get_text(17))
    import main_window
    import second_window
    main_window.main_window.activate()


batch = pyglet.graphics.Batch()
create_labels()
widgets = create_widgets()
text_cursor = window0.get_system_mouse_cursor('text')
focus = None
set_focus(widgets[0])
