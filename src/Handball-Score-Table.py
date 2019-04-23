import pyglet
import window0
import log

VERSION = "v0.0"

if __name__ == "__main__":
    print("Handball Score Table " + VERSION)
    window0.switch_scene(window0.menu_scene, True)
    pyglet.app.run()
