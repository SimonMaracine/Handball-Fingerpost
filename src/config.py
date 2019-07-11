"""
Module's main purpose is to store some values.
It is shared to all modules.

"""
from os.path import join
from pyglet import image
from pyglet import media
from pyglet import font

VERSION = "v0.1"
WIDTH = 800
HEIGHT = 600
num_second_windows = 0

icon1 = image.load(join("gfx", "icon1.png"))
icon2 = image.load(join("gfx", "icon2.png"))
background = image.load(join("gfx", "table2.png"))
img1 = image.load(join("gfx", "start_stop_button.png"))
img2 = image.load(join("gfx", "restart_button.png"))
img3 = image.load(join("gfx", "time_out_button.png"))
img4 = image.load(join("gfx", "arrow_button.png"))
img5 = image.load(join("gfx", "arrow_button2.png"))

ring_sound = media.load(join("sounds", "sound.wav"), streaming=False)
font.add_file(join("fonts", "open-sans", "OpenSans-Regular.ttf"))
