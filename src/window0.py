import pyglet
from text_entry import TextWidget

WIDTH = 640  # these may remain
HEIGHT = 480


def init(*args):
    global window0, batch, widgets, text_cursor, focus
    window0 = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table (first)", vsync=True)
    batch = pyglet.graphics.Batch()
    pyglet.text.Label('Name', x=10, y=HEIGHT-120, anchor_y='bottom',
                      color=(0, 0, 0, 255), batch=batch),
    pyglet.text.Label('Species', x=10, y=HEIGHT-155, anchor_y='bottom',
                      color=(0, 0, 0, 255), batch=batch),
    pyglet.text.Label('Special abilities', x=10, y=HEIGHT-190,
                      anchor_y='bottom', color=(0, 0, 0, 255), batch=batch)
    widgets = (
        TextWidget('', 200, HEIGHT - 120, WIDTH - 210, batch),
        TextWidget('', 200, HEIGHT - 155, WIDTH - 210, batch),
        TextWidget('', 200, HEIGHT - 190, WIDTH - 210, batch)
    )
    text_cursor = window0.get_system_mouse_cursor('text')
    focus = None


def update(dt):
    pass


init()


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
        # todo hmm
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


set_focus(widgets[0])


def get_text(widget: int):
    text = widgets[widget].document.text
    return text
