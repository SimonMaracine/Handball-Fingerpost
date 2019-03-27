import pyglet
from pyglet.window import key, mouse

second_window = pyglet.window.Window(800, 600, "Fingerpost")


@second_window.event
def on_draw():
    pass


@second_window.event
def on_key_press(symbol, modifiers):
    pass


@second_window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed at {}, {}.'.format(x, y))
